# copyright: 2023 by Sampson

import csv
import math

R = 6378

def distance(lat1, lon1, lat2, lon2):
    return R * math.sqrt(math.cos(lat1) ** 2 * (lon2 - lon1) ** 2 + (lat2 - lat1) ** 2)

def total_distance(points):
    total = 0
    for i in range(len(points) - 1):
        total += distance(
            points[i][0],
            points[i][1],
            points[i + 1][0],
            points[i + 1][1]
        )
    return total

def distance_from_csv(file):
    with open(file) as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        del readCSV[0]
        for i in range(len(readCSV)):
            readCSV[i] = [
                float(readCSV[i][0]) * math.pi / 180,
                float(readCSV[i][1]) * math.pi / 180
            ]
        return total_distance(readCSV)
    
print(distance_from_csv('data.csv'))