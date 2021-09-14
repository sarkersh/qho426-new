import matplotlib.pyplot as p
import csv

def read_data():
    data = {
        'survived': [],
        'sex': [],
        'age': [],
        'fare': []
    }
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) # ignore any rows with missing values for survived, sex, age or fare.
        for line in csv_reader:
            survived = line[1].strip() # extract required values using appropriate indexes
            sex = line[-1].strip()
            age = line[4].strip()
            fare = line[8].strip()
            # only add the data to the dictionary if not empty
            if (survived != "" and sex != "" and age != "" and fare != ""):
                data['survived'].append(bool(int(survived)))
                if (int(sex == 0)):
                    data['sex'].append['male']
                else:
                    data['sex'].append['female']

                data['age'].append(float(age))
                data['fare'].append(round(float(fare), 2))

    return data




