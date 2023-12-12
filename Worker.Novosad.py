import tkinter as tk
from worker import Worker
from workerdb import WorkerDB


class WorkersMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Worker Database")
        self.workers_db = WorkerDB()

        default_filename = "workers.csv"
        self.filename_label = tk.Label(root, text="Filename:", bg="lightblue")
        self.filename_entry = tk.Entry(root)
        self.filename_entry.insert(index=0, string=default_filename)
        self.filename_label.pack(pady=10)
        self.filename_entry.pack(pady=10)

        self.read_csv_button = tk.Button(root, text="Read from CSV", command=self.read_from_csv, bg="green", fg="white")
        self.read_csv_button.pack(pady=10)

        self.add_worker_button = tk.Button(root, text="Add Worker", command=self.add_worker_window, bg="orange", fg="white")
        self.add_worker_button.pack(pady=10)

        self.edit_workers_button = tk.Button(root, text="Edit Worker", command=self.edit_worker_window, bg="yellow", fg="black")
        self.edit_workers_button.pack(pady=10)

        self.display_workers_button = tk.Button(root, text="Display Workers", command=self.display_workers_window, bg="blue", fg="white")
        self.display_workers_button.pack(pady=10)

        self.sort_button = tk.Button(root, text="Sort Workers", command=self.sort_workers_window, bg="purple", fg="white")
        self.sort_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Workers", command=self.search_workers_window, bg="pink", fg="black")
        self.search_button.pack(pady=10)

        self.plot_departs_button = tk.Button(root, text="Plot Departments", command=self.plot_departs, bg="red", fg="white")
        self.plot_departs_button.pack(pady=10)

    def read_from_csv(self):
        filename = self.filename_entry.get()
        self.workers_db.read_from_csv(filename)

    def add_worker_window(self):
        add_worker_window = tk.Toplevel(self.root)
        add_worker_window.title("Add Worker")
        add_worker_window.geometry("250x200")

        name_label = tk.Label(add_worker_window, text="Name:", bg="lightblue")
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(add_worker_window)
        self.name_entry.pack(pady=5)

        surname_label = tk.Label(add_worker_window, text="Surname:", bg="lightblue")
        surname_label.pack(pady=5)
        self.surname_entry = tk.Entry(add_worker_window)
        self.surname_entry.pack(pady=5)

        depart_label = tk.Label(add_worker_window, text="Department:", bg="lightblue")
        depart_label.pack(pady=5)
        self.depart_entry = tk.Entry(add_worker_window)
        self.depart_entry.pack(pady=5)

        salary_label = tk.Label(add_worker_window, text="Salary:", bg="lightblue")
        salary_label.pack(pady=5)
        self.salary_entry = tk.Entry(add_worker_window)
        self.salary_entry.pack(pady=5)

        add_button = tk.Button(add_worker_window, text="Add", command=self.add_worker, bg="green", fg="white")
        add_button.pack(pady=10)

    def add_worker(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        depart = self.depart_entry.get()

        salary_entry_value = self.salary_entry.get()
        salary = float(salary_entry_value) if salary_entry_value else None

        worker = Worker(name, surname, depart, salary)

        self.workers_db.add_worker(worker)
        self.workers_db.display_workers()

    def edit_worker_window(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Worker")
        edit_window.geometry("250x200")

        edit_id_label = tk.Label(edit_window, text="Enter Worker ID to Edit:", bg="lightblue")
        edit_id_label.pack(pady=5)
        self.edit_id_entry = tk.Entry(edit_window)
        self.edit_id_entry.pack(pady=5)

        field_label = tk.Label(edit_window, text="Field to Edit:", bg="lightblue")
        field_label.pack(pady=5)

        options = ["Name", "Surname", "Department", "Salary"]
        self.edit_var = tk.StringVar(edit_window)
        self.edit_var.set(options[0])
        edit_menu = tk.OptionMenu(edit_window, self.edit_var, *options)
        edit_menu.pack(pady=5)

        edit_value_label = tk.Label(edit_window, text="Enter New Value:", bg="lightblue")
        edit_value_label.pack(pady=5)
        self.edit_value_entry = tk.Entry(edit_window)
        self.edit_value_entry.pack(pady=5)

        edit_button = tk.Button(edit_window, text="Edit", command=self.edit_worker, bg="yellow", fg="black")
        edit_button.pack(pady=10)

    def edit_worker(self):
        worker_id = int(self.edit_id_entry.get())
        field = self.edit_var.get().lower()
        new_value = self.edit_value_entry.get()

        self.workers_db.edit_worker(worker_id, field, new_value)
        self.workers_db.display_workers()

    def display_workers_window(self):
        workers_window = tk.Toplevel(self.root)
        workers_window.title("Workers List")

        workers_text = tk.Text(workers_window, height=10, width=40)
        workers_text.pack()

        for worker in self.workers_db.workers:
            worker_info = (f"ID: {worker.get_id()}\n"
                           f"Name: {worker.name}\n"
                           f"Surname: {worker.surname}\n"
                           f"Department: {worker.depart}\n"
                           f"Salary: {worker.salary}\n\n")
            workers_text.insert(tk.END, worker_info)

    def sort_workers_window(self):
        sort_window = tk.Toplevel(self.root)
        sort_window.title("Sort Workers")
        sort_window.geometry("200x200")

        sort_label = tk.Label(sort_window, text="Sort by:", bg="lightblue")
        sort_label.pack(pady=5)

        options = ["Name", "Surname", "Department", "Salary"]
        self.sort_var = tk.StringVar(sort_window)
        self.sort_var.set(options[0])
        sort_menu = tk.OptionMenu(sort_window, self.sort_var, *options)
        sort_menu.pack(pady=5)

        sort_button = tk.Button(sort_window, text="Sort", command=self.sort_workers, bg="purple", fg="white")
        sort_button.pack(pady=10)

    def sort_workers(self):
        field = self.sort_var.get().lower()
        self.workers_db.sort_workers(field)
        self.workers_db.display_workers()

    def search_workers_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Workers")
        search_window.geometry("200x200")

        search_label = tk.Label(search_window, text="Search by:", bg="lightblue")
        search_label.pack(pady=5)

        self.search_entry = tk.Entry(search_window)
        self.search_entry.pack(pady=5)

        search_button = tk.Button(search_window, text="Search", command=self.search_workers, bg="pink", fg="black")
        search_button.pack(pady=10)

    def search_workers(self):
        search_field = self.search_entry.get()

        found_workers = self.workers_db.search_workers(search_field)

        if found_workers:
            search_result_window = tk.Toplevel(self.root)
            search_result_window.title("Search Results")

            results_text = tk.Text(search_result_window, height=10, width=40)
            results_text.pack()

            for worker in found_workers:
                worker_info = (f"ID: {worker.get_id()}\n"
                               f"Name: {worker.name}\n"
                               f"Surname: {worker.surname}\n"
                               f"Department: {worker.depart}\n"
                               f"Salary: {worker.salary}\n\n")
                results_text.insert(tk.END, worker_info)
        else:
            print("No Results.")

    def plot_departs(self):
        self.workers_db.plot_departs()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x500")
    menu = WorkersMenu(root)
    root.mainloop()
