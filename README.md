# Parking_Lot_Challenge
 An Automated Car Parking Management System

# Overview

The Parking Lot Challenge involves creating two classes: a ParkingLot class and a Car class.
# ParkingLot Class:
	The ParkingLot class takes a square footage size as input.
	It creates an array of empty values based on the input square footage size, with the ability to account for different parking spot sizes.
	It calculates the array size based on the square footage and the size of each parking spot (e.g., 8x12 for 96 ft2).
	The class has a method to map vehicles to parked spots and save this mapping as a JSON object, with an optional step to upload the file to an S3 bucket.
# Car Class:
	The Car class takes a 7-digit license plate as input and sets it as a property.
	It has two methods:
	A magic method to output the license plate when converting the class instance to a string.
	A "park" method that takes a parking lot and spot number as input and attempts to park the car in the selected spot.
	If the parking spot is occupied by another car, the "park" method returns a status indicating the car was not parked successfully. If the spot is unoccupied, it returns a status indicating a successful parking.
# Views,Models Method:
	The main method takes an array of cars with random license plates.
	It iteratively has the cars park in a random spot in the parking lot array until either the input array is empty or the parking lot is full.
	If a car attempts to park in an occupied spot, it will try to find an unoccupied spot to park in.
	Output messages are displayed in the terminal, indicating whether a car parked successfully or not.
	The program exits when the parking lot is full.
# AWS S3 Integrated:
	An optional feature includes creating a method in the ParkingLot class that maps vehicles to parked spots in a JSON object.
	This JSON object can be saved as a file and uploaded to an S3 bucket at the end of the program.

