class student():
    def __init__(self,name,branch):
        self.name=name
        self.__branch=branch
    def get_branch(self):
        return self.__branch
s=student("tej","csd")
print(s.name)
print(s.get_branch())