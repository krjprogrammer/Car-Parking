import random
import json
class PARKINGLOT:
    def __init__(self, footage):
        self.length = 8
        self.width = 12
        self.minimum_area = self.length * self.width
        self.total_parking_spots = footage // self.minimum_area
        self.vacant_parking_spots = list(range(1, self.total_parking_spots + 1))
        self.parked_cars_dict = {}

    def map_cars(self):
        return json.dumps(self.parked_cars_dict,indent=1)

class CAR:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"The license plate of the car is {self.license_plate}"

    def park(self,parking_lot,spot):
        if spot not in parking_lot.vacant_parking_spots:
            return "Spot is currently filled"
        else:
            parking_lot.vacant_parking_spots.remove(spot)
            parking_lot.parked_cars_dict[self.license_plate] = spot
            return f"Car with {self.license_plate} was parked successfully at {spot}"
        

def main():
    footage_area = 2000
    parking_lot = PARKINGLOT(footage_area)
    print(parking_lot.total_parking_spots)
    cars = [random.randint(1000000, 9999999) for _ in range(22)]
    
    for car in cars:
        car_obj = CAR(car)
        if len(parking_lot.vacant_parking_spots) !=0:
            random_spot = random.choice(parking_lot.vacant_parking_spots)
            print(car_obj.park(parking_lot,random_spot))
        else:
            print('parking_lot is currently full')
            break
    
    with open('car_parking.json','w') as file:
        file.write(parking_lot.map_cars())

if __name__ == "__main__":
    main()
