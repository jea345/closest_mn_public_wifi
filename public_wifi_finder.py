import math, geocoder, sys, csv



class Coord:
	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def distanceTo (self, secondCoord):
		val = (self.x-secondCoord.x)**2 + (self.y-secondCoord.y)**2
		return math.sqrt(val)

def stringToArr(str):
	stripped = str.strip('()')
	return stripped.split(',')


searched = sys.argv[1]
g = geocoder.google(str(searched))
searchedCoord = Coord(g.lat, g.lng)


with open('wifi_locations.csv') as d:
	reader = csv.reader(d)
	next(reader, None)															# skip header row
	closestHotspot = ""
	smallestDistance = 1000														# originally set to arbitrary large num
	
	for row in reader:
		latlng = stringToArr(row[3])
		locationCoord = Coord(float(latlng[0]), float(latlng[1]))
		distance = searchedCoord.distanceTo(locationCoord)

		if distance < smallestDistance:
			smallestDistance = distance
			closestHotspot = row[0]

	print(closestHotspot, locationCoord.x, locationCoord.y)

		
