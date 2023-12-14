# -*- coding: utf-8 -*-
"""1.8 Rentals """

import pandas as pd

class Car:
    def __init__(self, make: str, model: str, year: int):
        self._make = make 
        self._model = model 
        self._year = year  

    def __str__(self):
        return f"{self._make} {self._model} ({self._year})"

class CarRental:
    def __init__(self, name: str):
        self._name = name
        self._cars = [] 

    def add_car(self, car: Car):
        self._cars.append(car)

    def get_available_cars(self):
        return self._cars

    def rent_car(self, car: Car):
        if car in self._cars:
            self._cars.remove(car)
            return f"You have successfully rented {car}."
        else:
            return f"{car} is not available for rental :( ."

    def save_to_file(self, onepointeight: str):
        car_data = []
        for car in self._cars:
            car_data.append({
                "Make": car._make,
                "Model": car._model,
                "Year": car._year
            })

        df = pd.DataFrame(car_data)
        df.to_csv(onepointeight, index=False)

    def add_cars_interactively(self):
        while True:
            make = input("Enter car company: ")
            if make.lower() == 'exit':
                break

            model = input("Enter car model: ")
            year = int(input("Enter car year: "))

            car = Car(make, model, year)
            self.add_car(car)
            print(f"{car} added to inventory.")

class LuxuryCarRental(CarRental):
    def __init__(self, name: str):
        super().__init__(name)

    def rent_car(self, car: Car):
        if car in self._cars:
            self._cars.remove(car)
            return f"You have uccessfully rented a luxury {car}."
        else:
            return f"{car} is not available for rental :( ."

class SportsCarRental(CarRental):
    def __init__(self, name: str):
        super().__init__(name)

    def rent_car(self, car: Car):
        if car in self._cars:
            self._cars.remove(car)
            return f"you have successfully rented a sportscar {car}."
        else:
            return f"{car} is not available for rental :( ."

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2018)
car3 = Car("BMW", "X5", 2021)
car4 = Car("Tesla", "Model X", 2020)
car5 = Car("Mercedes", "e250", 2018)
car6 = Car("Ford", "Focus", 2015)
car7 = Car("Porche", "Macan", 2021)
car8 = Car("Wuling", "Air EV", 2023)
car9 = Car("Jeep", "Wrangler", 2023)
car10 = Car("Mitsubishi", "Xpander", 2015)


car_rental = CarRental("1.8 Rentals")

car_rental.add_car(car1)
car_rental.add_car(car2)
car_rental.add_car(car3)
car_rental.add_car(car4)
car_rental.add_car(car5)
car_rental.add_car(car6)
car_rental.add_car(car7)
car_rental.add_car(car8)
car_rental.add_car(car9)
car_rental.add_car(car10)

print("Welcome to 1.8 Rentals!")
rental_result = car_rental.rent_car(car1)
print(rental_result)

available_cars = car_rental.get_available_cars()
print("Available cars:")
for car in available_cars:
    print(car)

car_rental.save_to_file("car_data.csv")

luxury_car_rental = LuxuryCarRental("Luxury 1.8 Rentals")

luxury_car_rental.add_car(car3)
luxury_car_rental.add_car(car5)

luxury_rental_result = luxury_car_rental.rent_car(car3)
print(luxury_rental_result)

sports_car_rental = SportsCarRental("Sports 1.8 Rentals")

sports_car_rental.add_car(car2)

sports_rental_result = sports_car_rental.rent_car(car2)
print(sports_rental_result)
