import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBFvfjJKHSyjobRHph9hIBySCDDkC9kbXE')

# Geocoding an address
geocode_result = gmaps.distance_matrix(
        origins=['7.392130,3.839928'],
        destinations=['7.427063,3.901437','7.404383,3.910375']
    )

print(geocode_result)

