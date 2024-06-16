class emp:
  def __init__(self):
    self.ID = []
  def Register(self,name,age):
    self.name = name
    self.age = age
    self.ID.append(name)
    print("you have successfully updated the dateils")
  def details(self,name,age):
      print("Your name is", self.name,"and age is", self.age)
      print("Your ID is", len(self. ID))


Employee = emp()
while True:
  print("Employee info update")
  print("Select your choice")
  print("1 = Register")
  print("2 = View details")
  print("3 = Exit")
  choice = int(input("Enter your choice 1/2/3:"))
  if choice ==1:
    name = input("Enter you name")
    age  = int (input("Enter your age"))
    Employee.Register(name,age)
  elif(choice==2):
    Employee.details(name,age)
  elif (choice ==3 ):
    print("Thank you")
    break;



   

 



 