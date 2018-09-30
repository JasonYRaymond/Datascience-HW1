#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(filename) as f:
        read_val = csv.reader(f, delimiter = ',')
        for row in read_val:
            timeList = row[1].split(':')
            hour = timeList[0]
            try:
                #print(hour)
                if int(hour) <24 and int(hour) >= 0:
                    time[int(hour)] = time[int(hour)] + 1
            except ValueError:
                pass
    return time

def weigh_pokemons(filename, weight):
    result = []
    with open(filename) as f:
        loaded_pokedex = json.loads(f.read())
        for pm in loaded_pokedex['pokemon']:
            if pm['weight'] == str(weight) + " kg":
                result.append(pm['name'])
    return result

def single_type_candy_count(filename):
    result = 0
    with open(filename) as f:
        loaded_pokedex = json.loads(f.read())
        for pm in loaded_pokedex['pokemon']:
            if len(pm['type']) == 1:
                try:
                    result += pm['candy_count']
                except KeyError:
                    pass
    return result

def reflections_and_projections(points):
    arr = np.array(points)
    arr[1] = 2 - arr[1]
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = -1 * temp
    arr[0] = (arr[0] + 3 * arr[1]) / 10
    arr[1] = (3 * arr[0] + 9 * arr[1]) / 10
    return arr

def normalize(image):
    arr = np.array(image)
    arr = 255 * (arr - arr.min()) / (arr.max() - arr.min())
    return arr

def sigmoid_normalize(image, variance):
    arr = np.array(image)
    arr = 255 * ((1 + math.exp(-1 * (variance ** -1) * (arr - 128))) ** -1)

print(normalize([[1, 2, 3], [4, 5, 6]]))
