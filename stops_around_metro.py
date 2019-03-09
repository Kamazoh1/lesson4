import csv

def distance(long1, lat1, long2, lat2):
    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(float(lat1))
    lon1 = radians(float(long1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(long2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    # print("Result:", distance)
    return distance

def metro_reader():
    metro_dict = {}
    with open('metro_stations.csv', 'r', encoding= 'utf8') as metro_file:
        metro_reader = csv.DictReader(metro_file, delimiter = ';')
        for row in metro_reader:
            metro_dict[row['Name']] = (row['Longitude_WGS84'], row['Latitude_WGS84'])
        # print(metro_dict.get('Name', 0))
    return metro_dict

def busstop_reader():
    busstop_dict = {}
    with open('bus_stops.csv', 'r', encoding = "cp1251") as busstop_file:
        busstop_reader = csv.DictReader(busstop_file, delimiter = ";")
        for row in busstop_reader:
            busstop_dict[row['Name']] = (row['Longitude_WGS84'], row['Latitude_WGS84'])
    # print(busstop_dict.get('Name',0))
    del busstop_dict['Name']
    return busstop_dict
    # "Name";"Longitude_WGS84";"Latitude_WGS84"
# Longitude_WGS84;Latitude_WGS84
# metro_stops_dict = {}
metro_stops_dict = {}
metro_dict = metro_reader()
# print(metro_dict)
busstop_dict = busstop_reader()
# print(busstop_dict)
for metro in metro_dict:
    # print(type(metro))    
    # print(metro_dict[metro][0])
    # print(metro_dict[metro][1])
    for busstop in busstop_dict:
    #     print(busstop[][0])
    #     print
        dist = distance(metro_dict[metro][0], metro_dict[metro][1], busstop_dict[busstop][0], busstop_dict[busstop][1])
        if  dist < 0.5:
            metro_name = metro.split(',')
            metro_name = metro_name[0]
            if metro_name in metro_stops_dict:
                counter = metro_stops_dict[metro_name] + 1   
                metro_stops_dict[metro_name] = counter
            else:
                metro_stops_dict[metro_name] = 1
    # print(metro_dict[metro].)
    metro_top_dict = sorted(metro_stops_dict.items(), key = lambda item: item[1], reverse = True)[:10]
    print(metro_top_dict)
print('Итоговый топ: {}'.format(metro_top_dict))
# metro_top = {}    
# metro_stops_dict = sorted(metro_stops_dict.items(), key = lambda item: item[1], reverse = True)
# for x, y in metro_stops_dict:
#     if i <= 10:
#         metro_top[x] = y
#         i += 1
# print(metro_top)
