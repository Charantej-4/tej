class Father():
    def father(self):
        print("father's property")
class Mother():
    def mother(self):
        print("mother's property")
class Son(Father,Mother):
    def son(self):
        print("son's property")
s=Son()
s.father()
s.mother()
s.son()