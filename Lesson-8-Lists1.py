from wsgiref.util import application_uri

cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'London']

print(cities)
print(len(cities))

print(cities[0])
print(cities[-2])
print(cities[2].title())
print(cities[2].upper())

cities[2] = 'Saint Petersburg'
print(cities)

cities.append('Toronto')
cities.append('Bangkok')
print(cities)

cities.insert(1, 'Florence')
print(cities)

del  cities[-1]
print(cities)

cities.remove('Toronto')
print(cities)

# removes the last one
deleted_city = cities.pop()
print("Deleted city is : " + deleted_city)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)