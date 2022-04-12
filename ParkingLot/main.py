from ParkingLot import ParkingLot


def start():
    parkingLot = ParkingLot("PR1234", 3, 4)
    parkingLot.init(2, 1, 1)
    parkingLot.displayParkingLot()
    parkingLot.displayFreeCount("CAR")
    parkingLot.displayFreeSlot("CAR")
    parkingLot.OccupiedSlot("CAR")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.ParkVehicle("CAR", "1234", "red")
    parkingLot.displayFreeCount("CAR")
    parkingLot.displayFreeCount("BIKE")
    parkingLot.displayFreeCount("TRUCK")
    parkingLot.unParkVehicle("PR1234_1_1")
    parkingLot.unParkVehicle("PR123_1_1")
    parkingLot.unParkVehicle("PR1231_1")
    parkingLot.displayFreeCount("CAR")
    parkingLot.displayFreeCount("BIKE")
    parkingLot.displayFreeCount("TRUCK")


if __name__ == '__main__':
    start()
