from termcolor import colored

class Pet:
    def __init__(self, name, species, price):
        self.name = name
        self.species = species
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.species}), price: ${self.price}"
   

    def display_ascii_art(self):
        if self.species == "Cat":
            print("""
/\_/\  
( o.o )  
 > ^ < 
            """)

class PetShop:
    def __init__(self):
        self.inventory = []
    
    def add_pet(self, pet):
        self.inventory.append(pet)
    
    def display_inventory(self):
        for pet in self.inventory:
            print(pet)
            pet.display_ascii_art()

    def total_inventory_value(self):
        return sum([pet.price for pet in self.pets])

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.purchased_pets = []

    def purchase_pet(self, pet):
        self.purchased_pets.append(pet)

    def display_purchased_pets(self):
        print(colored(f"{self.name}'s Purchased Pets:", "yellow"))
        for pet in self.purchased_pets:
            print(colored(pet, "green"))

def main_menu(pet_shop, customers):
    while True:
        print("\nPet Shop Management System")
        print(colored("1. Add a pet", "yellow"))
        print(colored("2. Sell a pet", "yellow"))
        print(colored("3. Display pet shop inventory", "yellow"))
        print(colored("4. Display customer information", "yellow"))
        print(colored("5. Add a customer", "yellow"))
        print(colored("6. Quit", "yellow"))
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            price = float(input("Enter pet price: $"))
            pet = Pet(name, species, price)
            pet_shop.add_pet(pet)
        elif choice == 2:
            name = input("Enter customer name: ")
            for customer in customers:
                if customer.name == name:
                    pet_name = input("Enter pet name to sell: ")
                    pet = pet_shop.sell_pet(pet_name)
                    if pet:
                        customer.purchase_pet(pet)
                        print(colored(f"Pet {pet_name} sold to {customer.name}", "green"))
                    else:
                        print(colored("Pet not found", "red"))
            else:
                print(colored("Customer not found", "red"))
        elif choice == 3:
            pet_shop.display_inventory()
        elif choice == 4:
            name = input("Enter customer name: ")
            for customer in customers:
                if customer.name == name:
                    customer.display_purchased_pets()
                    break
            else:
                print(colored("Customer not found", "red"))
        elif choice == 5:
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            customer = Customer(name, address)
            customers.append(customer)
        elif choice == 6:
            break
        else:
            print(colored("Invalid choice, try again", "red"))

if __name__ == "__main__":
    pet_shop = PetShop()
    customers = []
    main_menu(pet_shop, customers)

