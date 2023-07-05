
class Computer():
    
    def __init__(self,a,b):
        self.a = a
        
    def getSpecs(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def displaySpecs(self,display):
        self.display = display

class Desktop(Computer):

    def getSpecs(self):
        self.dcpu = "Ryzen 5 4600H"
        self.dram = "8GB 3200Mhz"
        print(self.dcpu,self.dram)

    def displaySpecs(self):
        self.display = "1920x1080 HD Display" 
        self.spcl_desk = "Cooler-master Liquid Cooler"
        print(self.display,self.spcl_desk)

class Laptop(Computer):

    def getSpecs1(self):
        self.lcpu = "i5 10th Gen"
        self.lram = "8GB 3200Mhz"
        print(self.lcpu,self.lram)

# Display and special properties added
    def display1(self):
        self.display = "1920x1080 HD IPS Display"
        self.spcl_lap = "Weight < 2.3Kg"
        print(self.display,self.spcl_lap)

#Desktop Object
print("Desktop Specifications")
print("----------------------")
desk_obj = Desktop('','')
desk_obj.getSpecs()
desk_obj.displaySpecs()
print("\n")

#Laptop Object
print("Laptop Specifications")
print("---------------------")
lap_obj = Laptop('','')
lap_obj.getSpecs1()
lap_obj.display1()
print("\n")

