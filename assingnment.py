traffic_light = "Green"
speed_limit = 60

class Vehicle:
    def start_engine(self):
      message = "Engine Started"
      print(message)

vehicle = Vehicle()
vehicle.start_engine()

class Car(Vehicle):
  def __init__(self,car):
    self.car = car

  def Display(self):
    #speed_limit = 60
    local_speed_limit = speed_limit
    print(f"Car make is {self.car}")
    print(speed_limit)

  def start_engine(self):
    message = "Car Engine Started"
    print(message)

car1 = Car("Dodge SRT")
car1.Display()
car1.start_engine()


class Bike(Vehicle):
  def __init__(self,bike):
    self.bike = bike

  def Display(self):
    print(f"Bike type is {self.bike}")

  def start_engine(self):
    local_speed_limit = speed_limit
    message = "Bike Engine Started"
    print(message)
    print(f"Speed limit is {local_speed_limit}")

bike1 = Bike("Cruiser")
bike1.Display()
bike1.start_engine()


print(f"Traffic signal is {traffic_light}")

