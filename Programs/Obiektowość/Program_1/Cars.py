class Cars():
    def __init__(self):
        print("Cars obj. created")
        self.manufacturer = "Unknown"
        self.prod_year = None
        pass


    def get_parameters(self):
        return (self.manufacturer, self.prod_year)
    


first_car = Cars()
print(f'Object has: {first_car.manufacturer, first_car.prod_year}')
print(f'Attributes as a tuple: {first_car.get_parameters()}')