from datetime import datetime
import pickle
import csv

class Persone:

    def __init__(self, filename):
        self.filename = filename
        self.name_ = []
        self.date_ = []

    def write_data_pickle(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def write_data_csv(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def read_data_csv(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.name_.append(row['Name'])
                self.date_.append(row['Date'])

    def read_data_pkl(self):
        with open(self.filename, 'rb') as file:
            data = pickle.load(file)
            self.name_ = [entry["Name"] for entry in data]
            self.date_ = [entry["Date"] for entry in data]

    def do_task(self, other_date):
        for i in range(len(self.date_)):
            birth_datetime = datetime.strptime(self.date_[i], "%d.%m.%Y")
            other_datetime = datetime.strptime(other_date, "%d.%m.%Y")

            delta = other_datetime - birth_datetime

            days_in_year = 365.25

            full_years = int(delta.days / days_in_year) + 1

            print(f'{self.name_[i]} - {full_years}')