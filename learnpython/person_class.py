
class Person:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight    
    def Tinhtranghonnhan(self):
        if self.age < 18:
            print("Chua du tuoi ket hon")
        elif 18 <= self.age <= 40:
            print("Da du tuoi lay vo")
        else :
            print("e vo roi")
                    
Tuan = Person("Tuan",50,60)
print("My name is %s, %d year old, weight is %d kilogram" % (Tuan.name,Tuan.age,Tuan.weight))   
Tuan.Tinhtranghonnhan()
# nico = Person()
# nico.name = "Nico"
# print("%s name is %s" % (Person.name,nico.name))