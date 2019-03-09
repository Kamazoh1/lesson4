import csv

streets = {}

with open('bus_stops.csv', 'r', encoding = "cp1251") as my_file:
    # headers_dict = my_file.readline()
    # print (headers_dict)
    reader = csv.DictReader(my_file, delimiter = ";")
    for row in reader:
        if row['Street']in streets:
            streets[row['Street']] += 1
        else:
            streets[row['Street']] = 1
    # print(streets)    
    # print(sorted(streets.items(), key = lambda item: item[1], reverse = True))
    streets_top = {}
    i = 0
    
    streets = sorted(streets.items(), key = lambda item: item[1], reverse = True)
    for x, y in streets:
        if i < 2:
            streets_top[x] = y
            i += 1
    print(streets_top)
    # print(streets.values())  