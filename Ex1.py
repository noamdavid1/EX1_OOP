# from CallForElevator import *
import CallForElevator
import csv
import json
import Elevator
import Building
import argparse
import fileinput


def __init__(self, buillding:Building, call:CallForElevator,  elevators=[]):
    self.buillding = buillding
    self.elevators= elevators.copy()
    self.call= call


# Get console variables:
# argparse library

# An object which handles system arguments from the command line.
parser = argparse.ArgumentParser()

parser.add_argument('building_json')
parser.add_argument('elevator_calls_file_path')
parser.add_argument('output_file_path')

# Parse arguments from the command line:
# args = parser.parse_args()

args = parser.parse_args(['B1.json', 'Calls_a.csv', 'output_file.csv'])
#print(args.elevator_calls_file_path)

with open(args.building_json, 'r') as building:
    # Craetes a json object from an object
    building = json.loads(json.dumps(building.read()))

    elevators = []





with open("C:\\Users\\noamd\PycharmProjects\pythonProject\Calls_a.csv", 'r') as file_object:
    #Read from file
    #for line in file_object.read().split("\n"):
    file= file_object.read().split("\n")




with open(args.output_file_path, 'w') as output:

    # Final actions: After the algorithm has given its outputs:
    """
    for e in updatedCallsOfrElevators:
        output.write(e[0], e[1], e[2], ..., e[k])
    """
    calls = list()

    with open(args.elevator_calls_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
             cfe = CallForElevator("Elevator call, "+str(calls.getTime()) +","+str(calls.getSrc())+","+str(calls.getDest())+","+str(calls.getState())+","+str(calls.getallocateAnElevator())+"\n")
            calls.append(cfe)
            print(cfe)
        with open(args.output_file_path, 'w') as new_file:
            csv_writer = csv.writer(new_file)
            for call in calls:
                csv_writer.writerow(line)
                # new_file.write(line)
                new_file.write(call)




def save_to_file(self, file_name, array_Of_Calls):
    try:
        with open(file_name, 'w', newline="") as file:
            csvwriter = csv.writer(file)
            # csvwriter.writerow(header)
            csvwriter.writerows(array_Of_Calls)
    except IOError as e:
        print(e)



