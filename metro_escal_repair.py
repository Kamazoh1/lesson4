import csv
from datetime import datetime
 
metro_list = []
today = datetime.now()
with open('metro_stations.csv', 'r', encoding= 'utf8') as my_file:
    reader = csv.DictReader(my_file, delimiter = ';')
    for row in reader:
        if row['RepairOfEscalators'] != '':
            repair_dates = row['RepairOfEscalators']
            # print(date_start)
            date_start = repair_dates[:10]
            # print(date_start)
            date_end = repair_dates[11:]
            # print(date_end)
            date_start = datetime.strptime(date_start, '%d.%m.%Y')
            # print(date_start)
            date_end = datetime.strptime(date_end, '%d.%m.%Y')
            # print(date_end)
            if date_start < today and date_end > today:
                metro_list.append(row['Name'])
        # print(row['RepairOfEscalators'])
print(metro_list)