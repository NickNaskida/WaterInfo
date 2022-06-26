from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="water_meter")


def get_cords(address):
	data = geolocator.geocode(address)
	return data.point.latitude, data.point.longitude