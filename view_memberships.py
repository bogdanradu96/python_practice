import csv
from os import strerror

def view_memberships():
    try:
        with open('C:/Users/bogda/Desktop/PythonSkillab/citygym/memberships.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except IOError as e:
        print("I/O error occured:", strerror(e.errno))