# Problem Statement: https://leetcode.com/problems/design-parking-system/

class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.vehicle = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 :
            if self.vehicle[0] > 0:
                self.vehicle[0] -= 1
                return True
        elif carType == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1] -= 1
                return True
        elif carType == 3:
            if self.vehicle[2] > 0:
                self.vehicle[2] -= 1
                return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)