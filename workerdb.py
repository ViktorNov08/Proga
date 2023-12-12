import csv
import matplotlib.pyplot as plt
from worker import Worker


def decorator_sort(func):
    def wrapper(self, field):
        print(f"Sorted successfully by {field}")
        return func(self, field)
    return wrapper


def decorator_search(func):
    def wrapper(self, field):
        print(f"Searched results for field {field}:")
        return func(self, field)
    return wrapper


class WorkerDB:
    def __init__(self, filename="workers.csv"):
        self.workers = []
        self.filename = filename
        self.read_from_csv()

    def add_worker(self, worker):
        self.workers.append(worker)
        self.save_to_csv()

    def del_worker(self, id_to_del):
        for worker in self.workers:
            if worker.get_id() == id_to_del:
                self.workers.remove(worker)
                self.save_to_csv()
                return
        print(f"Worker with ID {id_to_del} not found.")

    def edit_worker(self, id_to_edit, field, value_to_edit):
        for worker in self.workers:
            if worker.get_id() == id_to_edit:
                if hasattr(worker, field):
                    setattr(worker, field, value_to_edit)
                    print(f"Worker with ID {id_to_edit} - Field '{field}' edited.")
                    self.save_to_csv()
                    return
                else:
                    print(f"Invalid field: {field}.")
                    return
        print(f"Worker with ID: {id_to_edit} not found.")

    def read_from_csv(self):
        try:
            with open(self.filename, newline='') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                for row in reader:
                    name = row['name']
                    surname = row['surname']
                    depart = row['depart']
                    salary = row['salary']
                    salary = float(salary)
                    worker = Worker(name, surname, depart, salary)
                    self.add_worker(worker)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new one.")

    def display_workers(self):
        if not self.workers:
            print("List is empty.")
        else:
            for worker in self.workers:
                print(worker)

    @decorator_sort
    def sort_workers(self, field):
        try:
            self.workers.sort(key=lambda item: getattr(item, field))
        except AttributeError as e:
            print(e)

    @decorator_search
    def search_workers(self, field):
        found = []
        for worker in self.workers:
            if field in str(worker):
                found.append(worker)
        if not found:
            print(f"Worker with field {field} not found.")
        else:
            return found

    def plot_departs(self):
        departs = {}
        for worker in self.workers:
            if worker.depart not in departs:
                departs[worker.depart] = 1
            else:
                departs[worker.depart] += 1

        labels = []
        sizes = []
        for keys, values in departs.items():
            labels.append(keys)
            sizes.append(values)

        plt.pie(sizes, labels=labels)
        plt.show()

    def save_to_csv(self):
        with open(self.filename, mode='w', newline='') as csv_file:
            fieldnames = ['name', 'surname', 'depart', 'salary']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for worker in self.workers:
                writer.writerow({
                    'name': worker.name,
                    'surname': worker.surname,
                    'depart': worker.depart,
                    'salary': worker.salary
                })
