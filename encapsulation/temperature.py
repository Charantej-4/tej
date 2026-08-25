class Temperature():
    def __init__(self,temperature):
        self.__temperature=temperature
    def get_temperature(self):
        return self.__temperature
    def set_temperature(self,temperature):
        if temperature>=-273.15:
            self.__temperature=temperature
        else:
            print("invalid temperature")
T=Temperature(45)
T.set_temperature(67)
print(T.get_temperature())
T.set_temperature(-600)
print(T.get_temperature())