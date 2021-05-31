class Category:
    # constructor
    # test for merge conflict
    def __init__(self, category, amount):
        self.category = category 
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited $%.2f in %s budget." %(amount, self.category)

    def balance(self):
        return "This is the current balance: $%.2f." %self.amount

    def check_balance(self, amount):
        if amount > self.amount:
            return False
        
        else:
            return True

    def withdraw(self, amount):

        balance_check = self.check_balance(amount)
        if balance_check:
            self.amount -= amount
            return "You have withdrawn $%.2f from %s budget." %(amount, self.category)

        else:
            return "You do not have enough money in your %s budget to withdraw this amount." %(self.category)

    def transfer(self, category, amount):
        balance_check = self.check_balance(amount)
        if balance_check:
            self.amount -= amount
            category.amount += amount
            return "You have sucessfully transferred $%.2f to %s from %s." %(amount, category.category, self.category)

        else:
            return "You do not have enough money in your %s budget to withdraw this amount." %(self.category)



food_budget = Category("Food", 500)
clothing_budget = Category("Clothing", 200)
car_budget = Category("Car", 300)
travel_budget = Category("Travel", 250)
household_budget = Category("Household", 1200)
recreation_budget = Category("Recreation", 150)

print(food_budget.transfer(clothing_budget,100))
print(food_budget.balance()) 
print(clothing_budget.balance())
