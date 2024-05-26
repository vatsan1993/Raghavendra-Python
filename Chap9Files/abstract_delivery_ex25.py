from abc import ABC

class Delivery(ABC):
    def __init__(self, sender, receiver, sender_address, receiver_address, delivery_type):
        self.__sender = sender
        self.__receiver = receiver
        self.__sender_address = sender_address
        self.__receiver_address = receiver_address
        self.__delivery_type = delivery_type

    def get_sender(self):
        return self.__sender

    def set_sender(self, sender):
        self.__sender = sender

    def get_receiver(self):
        return self.__receiver

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def get_sender_address(self):
        return self.__sender_address

    def set_sender_address(self, sender_address):
        self.__sender_address = sender_address

    def get_receiver_address(self):
        return self.__receiver_address

    def set_receiver_address(self, receiver_address):
        self.__receiver_address = receiver_address

    def calculate_price(self):
        pass

    def __str__(self):
        return f"Sender: {self.__sender} Receiver: {self.__receiver} Sender Address: {self.__sender_address}\
 Receiver Address: {self.__receiver_address}"

    def __repr__(self):
        return f" {self.__sender} to{self.__receiver} {self.__sender_address}\
         to {self.__receiver_address}"



class City(Delivery):
    def __init__(self, sender, receiver, sender_address, receiver_address, distance):
        super().__init__(sender, receiver, sender_address, receiver_address, "Local")
        self.__distance = distance

    def calculate_price(self):
        BASE_CHARGE = 5
        return BASE_CHARGE + self.__distance * 0.5

    def get_distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance

    def __str__(self):
        return super().__str__() + f' Distance{self.__distance} Price ${self.calculate_price()}'

    def __repr__(self):
        return super().__repr__()  + f' d {self.__distance} ${self.calculate_price()}'


class National(Delivery):
    def __init__(self, sender, receiver, sender_address, receiver_address, cities):
        super().__init__(sender, receiver, sender_address, receiver_address, "National")
        self.__cities = cities

        # city will be a dictionary that has different city names each will have a string number of hours and minutes.


    def get_distance(self):
        distance = 0
        total_hours = 0
        total_minutes = 0

        for city, time in self.__cities.items():
            hours, minutes = time.split(":")
            hours = int(hours)
            minutes = int(minutes)
            total_hours += hours
            total_minutes += minutes

        total_hours += total_minutes / 60
        total_minutes = total_minutes % 60

        distance = total_hours * 2 + total_minutes * 2/60

        return distance

    def calculate_price(self):
        BASE_CHARGE = 5
        distance = self.get_distance()
        waiting_time = len(self.__cities) * 0.005
        return BASE_CHARGE + distance * 1.5 + waiting_time

    def set_distance(self, distance):
        self.__distance = distance

    def __str__(self):
        cities = ""
        for city in self.__cities:
            cities += city + " "
        return super().__str__() + f' cities:{cities} Price ${self.calculate_price()}'

    def __repr__(self):
        cities = ""
        for city in self.__cities:
            cities += city + " "
        return super().__repr__() + f' cities:{cities} Price ${self.calculate_price()}'

class International(Delivery):

    def __init__(self, sender, receiver, sender_address, receiver_address, flight_charges, road_charges):
        super().__init__(sender, receiver, sender_address, receiver_address, "International")
        self.__cities = cities
        self.__flight_charges = flight_charges
        self.__road_charges = road_charges

    def calculate_price(self):
        BASE_CHARGE = 5
        return BASE_CHARGE + self.__flight_charges + self.__road_charges

    def get_flight_charges(self):
        return self.__flight_charges

    def set_flight_charges(self, flight_charges):
        self.__flight_charges = flight_charges

    def get_road_charges(self):
        return self.__road_charges

    def set_road_charges(self, road_charges):
        self.__road_charges = road_charges


    def __str__(self):
        return super().__str__() + f' Flight Charges: {self.__flight_charges} \
Road Charges: {self.__road_charges} Price ${self.calculate_price()}'

    def __repr__(self):
        return super().__repr__() +f' F {self.__flight_charges} R {self.__road_charges} Price ${self.calculate_price()}'


city = City("Max", "James", "1st Street", "10th Street", 2)

cities = {
    "Nellore": "02:30",
    "Ongole" : "02:00",
    "Tenali" : "01:40",
    "Vijayawada": "00:45"
}
national = National("Max", "James","Tirupati", "Vijayawada",cities)

internation = International("Max", "James","NY", "Tirupati", 50, 10)

print(city)
print(national)
print(internation)

