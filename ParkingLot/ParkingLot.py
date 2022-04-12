from ParkingSlot import ParkingSlot
from ParkingTicket import ParkingTicket


class ParkingLot:
    def __init__(self, parkingLotId, floor, slotPerFloor):
        self.parkingLotId = parkingLotId
        self.floorCount = floor
        self.slotPerFloorCount = slotPerFloor
        self.slotPerFloor = None
        self.parkingTicket = {}

    def init(self, car, truck, bike):
        slotPerFloor = []
        for floor in range(self.floorCount):
            slots = []
            count = 0
            for slot in range(car):
                slot = ParkingSlot("CAR", False,floor, count)
                count+=1
                slots.append(slot)
            for slot in range(bike):
                slot = ParkingSlot("BIKE", False,floor,count)
                count += 1
                slots.append(slot)
            for slot in range(truck):
                slot = ParkingSlot("TRUCK", False,floor, count)
                count += 1
                slots.append(slot)
            slotPerFloor.append(slots)
        self.slotPerFloor = slotPerFloor

    def displayParkingLot(self):
        for floor in range(self.floorCount):
            print("FLOOR: " + str((floor + 1)))
            for slot in range(self.slotPerFloorCount):
                print("SLOT: " + str(slot + 1) + " TYPE: " + self.slotPerFloor[floor][
                    slot].vehicleType + " IS PARKED: " + str(self.slotPerFloor[floor][slot].isParked))
            print()

    def displayFreeCount(self, vehicleType):
        for floor in range(self.floorCount):
            count = 0
            for slot in range(self.slotPerFloorCount):
                if self.slotPerFloor[floor][slot].vehicleType == vehicleType and \
                        self.slotPerFloor[floor][slot].isParked == False:
                    count += 1
            print("No. of free slots for " + vehicleType + " on Floor " + str(floor + 1) + ": " + str(count))

    def displayFreeSlot(self, vehicleType):
        for floor in range(self.floorCount):
            freeSlots = []
            for slot in range(self.slotPerFloorCount):
                if self.slotPerFloor[floor][slot].vehicleType == vehicleType and \
                        self.slotPerFloor[floor][slot].isParked == False:
                    freeSlots.append(slot + 1)
            print("Free slots for " + vehicleType + " on Floor " + str(floor + 1) + ": ", freeSlots)

    def OccupiedSlot(self, vehicleType):
        for floor in range(self.floorCount):
            occupiedSlots = []
            for slot in range(self.slotPerFloorCount):
                if self.slotPerFloor[floor][slot].vehicleType == vehicleType and \
                        self.slotPerFloor[floor][slot].isParked == True:
                    occupiedSlots.append(slot + 1)
            print("Occupied slots for " + vehicleType + " on Floor " + str(floor + 1) + ": ", occupiedSlots)

    def FindFreeSlot(self, vehicleType):
        for floor in range(self.floorCount):
            for slot in range(self.slotPerFloorCount):
                if self.slotPerFloor[floor][slot].vehicleType == vehicleType and \
                        self.slotPerFloor[floor][slot].isParked == False:
                    return self.slotPerFloor[floor][slot]
        return None

    def ParkVehicle(self, vehicleType, regNo, color):
        slot = self.FindFreeSlot(vehicleType)
        if slot is None:
            print("Parking Lot Full")
            return
        ticketId = self.parkingLotId+"_"+str(slot.floor+1)+"_"+str(slot.slot+1)
        parkingTicket = ParkingTicket(vehicleType, regNo, color, slot, ticketId)
        self.parkingTicket[ticketId] = parkingTicket
        slot.isParked = True
        print("Parked vehicle. Ticket ID: "+ticketId)

    def unParkVehicle(self, ticketId):
        if ticketId in self.parkingTicket.keys():
            ticket = self.parkingTicket.get(ticketId)
            slot = ticket.slot
            slot.isParked = False
            print("Unparked vehicle with Registration Number: "+ticket.regNum+" and Color:"+ticket.color)
        else:
            print("Invalid Ticket")

