import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            self.process_menu_data(reader)

    def process_menu_data(self, reader):
        for row in reader:
            ...
            # search for row data dish name, price, ingredients, amount
