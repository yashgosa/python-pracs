"""Create the vehicle  class as an abstract class and define an abstract methods namely  fuelAmount(),
capacity(), applybreaks(). Inherit the classes like  Class Car, BUS and Truck  from the base class and
implement the abstract methods differently. Each Subclass should have at least  3 unique data members
and methods in the implementation.

WAP to find reverse of string"""

from abc import ABC, abstractmethod
class Vehical(ABC):
    @abstractmethod
    def fuelAmount(self): pass

    @abstractmethod
    def get_capacity(self): pass

    @abstractmethod
    def applybreaks(self): pass

class Car(Vehical):
    def __init__(self, name, fuel, capacity, top_speed, milage):
        self.name = name
        self.fuel = fuel
        self.capacity = capacity
        self.top_speed = top_speed
        self.milage = milage

    def fuelAmount(self):
        return self.fuel

    def get_capacity(self):
        return self.capacity

    def applybreaks(self):
        print("Car applied brakes.....")

    def get_top_speed(self):
        return self.top_speed

    def get_milage(self):
        return self.milage

class Bus(Vehical):
    def __init__(self, name, fuel, capacity, standing, seating):
        self.name = name
        self.fuel = fuel
        self.capacity = capacity
        self.standing = standing
        self.seating = seating

    def fuelAmount(self):
        return self.fuel

    def get_capacity(self):
        return self.capacity

    def applybreaks(self):
        print("Bus applied brakes.....")

    def get_seating(self):
        return self.seating

    def get_standing(self):
        return self.standing

class Truck(Vehical):
    def __init__(self, name, fuel, capacity, payload, distance):
        self.name = name
        self.fuel = fuel
        self.capacity = capacity
        self.payload = payload
        self.distance = distance

    def fuelAmount(self):
        return self.fuel

    def get_capacity(self):
        return self.capacity

    def applybreaks(self):
        print("Car applied brakes.....")

    def get_distance(self):
        return self.distance

    def get_payload(self):
        return self.payload

if __name__ == '__main__':

    stringx = input("Enter the string")
    print(stringx[::-1])

    # ================================================
    carx = Car( "Maruti", 32, 4, 100, 123)
    print("fuelAmount", carx.fuelAmount())
    print("capacity", carx.get_capacity())
    carx.applybreaks()
    print("top_speed", carx.get_top_speed())
    print("Milage", carx.get_milage())
    print()
    busx = Bus("Nashik", 22, 123, 32, 1232)
    print("fuelAmount", busx.fuelAmount())
    print("capacity", busx.get_capacity())
    busx.applybreaks()
    print("Standing Capacity", busx.get_seating())
    print("Seating Capacity", busx.get_standing())
    print()
    truckx = Truck("Honda", 1, 1342, 5432, 1276)
    print("fuelAmount", truckx.fuelAmount())
    print("capacity", truckx.get_capacity())
    truckx.applybreaks()
    print("Disctance", truckx.get_distance())
    print("Payload", truckx.get_payload())
