class car():
    def __init__(self,speed):
        self.__speed=speed
    def get_speed(self):
        return self.__speed
    def set_speed(self,speed):
        if 0<=speed<=200:
            self.__speed=speed
        else:
            print("invalid speed")
    def accelerate(self):
        if self.__speed+10<=200:
            self.__speed+=10
        else:
            print("invalid speed")
    def brake(self):
        if self.__speed-10>=0:
            self.__speed-=10
        else:
            print("speed cannot go below 200")
c=car(100)
print(c.get_speed())
c.accelerate()
print(c.get_speed())
c.brake()
print(c.get_speed())
c.set_speed(250)

