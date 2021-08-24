# Check if coordinates are inside certain area or outside,
# if is outside the program calculate the distance
# Import the necessaries libraries
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim

# Create a Class


class Coordinates():

    # With this method calculate the coordinates
    def calcular_coordenadas(self, address):
        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="example app")
        # Obtain the coordinates of an address
        data1 = geolocator.geocode(address)
        # Format the result that was obtained in the previous line
        test_point = [{'lat': data1.point.latitude,
                       'lng': data1.point.longitude}]
        return test_point

    # With this method calculate the distance of two points
    def haversine(self, cords):
        # In this variable save the coordinates of "Moscow Ring Road"
        center_point = [{'lat': 55.8285286, 'lng': 37.6365949}]
        # Separete in tow in two variables
        latitude_one = center_point[0]['lat']
        longitude_one = center_point[0]['lng']
        # Obtein the coordinates of the address, in two variables
        latitude_two = cords[0]['lat']
        longitude_two = cords[0]['lng']
        # Convert decimal degrees to radians
        longitude_one, latitude_one, longitude_two, latitude_two = map(radians, [longitude_one, latitude_one, longitude_two, latitude_two])
        # Haversine formula that calcule the distance
        dlon = longitude_two - longitude_one
        dlat = latitude_two - latitude_two
        operation_one = sin(dlat/2)**2 + cos(latitude_one) * cos(latitude_two) * sin(dlon)**2
        operation_two = 2 * asin(sqrt(operation_one))
        # Radius of earth in kms
        radius = 6371
        # Return the result of the operation
        return operation_two * radius
