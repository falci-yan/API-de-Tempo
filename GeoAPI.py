from geopy.geocoders import Nominatim

def get_location(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)

    return location.latitude, location.longitude

print(get_location("Campo Grande, RJ"))