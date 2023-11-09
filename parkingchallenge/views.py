from django.shortcuts import render, redirect
import boto3
from botocore.exceptions import NoCredentialsError
from .models import Car, ParkingLot
import random
import json
from django.http import JsonResponse


def home(request):
    num_spots = 100  # Initialize num_spots as 100 by default
    cars = Car.objects.all()
    parking_lot = ParkingLot.objects.first()

    if not parking_lot:
        parking_lot = ParkingLot.objects.create()  # Create a new ParkingLot if it doesn't exist

    parking_lot.num_spots = parking_lot.square_footage // (parking_lot.spot_size_width * parking_lot.spot_size_length)
    parking_lot.save()

    if not cars:
        return render(request, 'home.html', {'cars': cars, 'parking_lot': parking_lot, 'num_spots': num_spots})

    # Create a list of available spots
    # Create a list of available spots
    available_slots = list(range(1, parking_lot.num_spots + 1))

    for car in cars:
        if car.num_spots is None and available_slots:
            random_slot = random.choice(available_slots)
            car.num_spots = random_slot
            car.save()
            available_slots.remove(random_slot)
        elif car.num_spots is None:
            message = f"Car with license plate {car.license_plate} added, but parking is full (Status: Hold-On)"
            print(message)

    return render(request, 'home.html', {'cars': cars, 'parking_lot': parking_lot, 'num_spots': num_spots})


def add_car(request):
    if request.method == 'POST':
        license_plate = request.POST.get('license_plate')
        if license_plate:
            # Check if the number of cars is less than the specified limit (100)
            if Car.objects.count() < 100:
                car = Car.objects.create(license_plate=license_plate)

                # Randomly allocate a spot to the car
                available_slots = [slot for slot in range(100) if not Car.objects.filter(num_spots=slot).exists()]
                if available_slots:
                    car.num_spots = random.choice(available_slots)
                    car.save()
                    message = f"Car with license plate {car.license_plate} parked successfully in spot {car.num_spots}"
                    print(message)
                else:
                    message = f"Car with license plate {car.license_plate} added, but parking is full (Status: Hold-On)"
                    print(message)
            else:
                message = "Parking is full (Status: Hold-On)"
                print(message)
    return redirect('home')

# Function to read AWS credentials from credentials.json
def read_aws_credentials(filename):
    with open(filename, 'r') as json_file:
        credentials = json.load(json_file)
    return credentials

# Function to export car data to JSON
def export_cars_to_json(filename):
    car_data = [{"license_plate": car.license_plate, "num_spots": car.num_spots, "square_footage": car.square_footage, "spot_size_width":car.spot_size_width, "spot_size_length":car.spot_size_length} for car in Car.objects.all()]
    with open(filename, 'w') as json_file:
        json.dump(car_data, json_file)

# Function to upload a file to S3
def upload_to_s3(filename, bucket_name, s3_key, aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    try:
        s3.upload_file(filename, bucket_name, s3_key)
        return True
    except NoCredentialsError:
        return False

def upload_car_data(request):
    # Read AWS credentials from credentials.json
    credentials = read_aws_credentials('credentials.json')
    aws_access_key_id = credentials['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = credentials['AWS_SECRET_ACCESS_KEY']
    aws_region = credentials['AWS_REGION']
    s3_bucket_name = credentials['S3_BUCKET_NAME']

    # Export car data to a JSON file
    export_cars_to_json('parking_lot_data.json')

    # Upload JSON file to S3
    if upload_to_s3('parking_lot_data.json', s3_bucket_name, 'parking_lot_data.json', aws_access_key_id, aws_secret_access_key):
        message = f"Car data uploaded to S3 bucket: {s3_bucket_name}"
    else:
        message = "Failed to upload car data to S3. AWS credentials are missing or incorrect."

    return render(request, 'upload_success.html', {'message': message})


def free_spot(request):
    if request.method == 'POST':
        spot_number = request.POST.get('spot_number')
        if spot_number:
            try:
                # Find the car with the specified spot number and clear the spot
                car = Car.objects.filter(num_spots=spot_number).first()
                if car:
                    car.num_spots = None
                    car.save()

                # Read the JSON data from the file
                with open('parking_lot_data.json', 'r') as file:
                    data = json.load(file)

                # Check if the spot exists in the JSON data before removing it
                if spot_number in data:
                    del data[spot_number]

                # Save the updated JSON data back to the file
                with open('parking_lot_data.json', 'w') as file:
                    json.dump(data, file)

                success_message = "Spot successfully cleared."
                return render(request, 'freesuccess.html', {'success_message': success_message})

            except Exception as e:
                # Add error handling to log or display the error message
                print(f"Error: {e}")
                error_message = "An error occurred while clearing the spot."
                return JsonResponse({'status': 'error', 'message': error_message})

    return redirect('home')