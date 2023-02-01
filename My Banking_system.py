#Parent Class
class  User():
               #arguments we need for our user 
    def __init__(self, name, age, gender):
        #three different properties/methods assigned to our object
        self.name = name 
        self.age = age
        self.gender = gender 
    # a method which is inside a class which is gonna be converted to an object
    #the function has access to every property and every method that is assigned to this object
    def show_user_details(self):
        print()
        print("Personal Details:")
        print("")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
       

#Child Class#
#transfer all the properties/methods from our use class, mention the user class in our brackets
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount 
        print("Account balance has been updated: $", self.balance)

    def withdraw(self, amount):
        self.amount = amount 
        if self.amount > self.balance:
            print("Insufficient funds | Balance Available: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: $", self.balance)


        



Keyik = Bank('Keyik', 18, 'Female')
Keyik.show_user_details()
print()
Keyik.deposit(200)
Keyik.withdraw(400)
