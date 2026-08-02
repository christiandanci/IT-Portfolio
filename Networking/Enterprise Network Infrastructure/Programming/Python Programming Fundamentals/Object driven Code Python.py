class student:
    def __init__(self,Name,ID,Age):
        self.Name=Name
        self.ID=ID
        self.Age=Age
    def updateName(self, NewName):
        self.Name=NewName
    def printID(self):
        print ("Your ID is:", self.ID)
    def printAge(self):
        print ("Your age is:", self.Age)
    def printName(self):
        print("Your name is", self.Name)
    

St1=student("Cristian",12345,44)
St2=student("James",54321,35)

St1.printID()
St1.printName()
St2.printAge()
St2.printName()
St2.updateName("John")
St2.printName()
