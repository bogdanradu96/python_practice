import csv
from pathlib import Path
from os import strerror

def view_memberships():
    project_root = Path(__file__).resolve().parent.parent #Gets the root directory two levels up from "scripts"
    #Defines the output directory and file path
    folder_path = project_root / 'citygym'
    file_path = folder_path / 'memberships.csv'
    #Opens and reads the data in the file
    try:
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except IOError as e: #Exception in case the file does not exist
        print("I/O error occurred:", strerror(e.errno))