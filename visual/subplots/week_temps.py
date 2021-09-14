"""Activity 2: CSV and Subplots We can use the module csv to handle CSV files. This module provides us with a CSV
reader that allows us to retrieve a row of data one at a time from the file. Each row is a sequence of data that can
be accessed using an index number (e.g. row[0] for the first value, row[1] for the second value and so on).For
example, if we wish to open a CSV file for reading and display the first column of each row then we can do the
following:

import csv

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        print(row[0])

    If the csv file contains a row with header labels then we can read this before processing the records as shown below.
The function next causes the next record to be fetched from the file i.e. the first row which is the header.

import csv

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    header = next(csv_reader)
    for row in csv_reader:
        print(row[0])

"""
import matplotlib.pyplot as p
import csv

def read_data():
    with open("temps.csv") as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader) # ignore header
        data = {
            'week1' : [], 'week2' : []
        }

        for line in csv_reader:
            data['week1'].append(line[0].strip())
            data['week2'].append(line[1].strip())
    return data


def run():
    data = read_data()
    print(data)

    fig, (ax1, ax2) = p.subplots(1, 2)
    ax1.plot(range(len(data['week1'])), data['week1'])
    ax2.plot(range(len(data['week2'])), data['week2'])
    p.show()

run()