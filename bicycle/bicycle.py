# Thinkful Unit1 / Lesson3 / Project4: Bicycle.py

# Bicycle Class:
    # Have a model name
    # Have a weight
    # Have a cost to produce

class Bicycle:
    def __init__(self, name="", weight=0, cost=0):
        self.name = name
        self.weight = weight
        self.cost = cost
        
    def model_name(self):
        return self.name
        
    def bike_weight(self):
        return self.weight
        
    def bike_cost(self):
        return self.cost

    def setParameters(self, type):
        if type == "street racer":
            self.name = "Zippidy Do"
            self.weight = 8
            self.cost = 950
        elif type == "mountain":
            self.name = "Regular Joe"
            self.weight = 11
            self.cost = 250
        elif type == "training":
            self.name = "First Try"
            self.weight = 10
            self.cost = 120
        elif type == "long haul":
            self.name = "Sore Rear"
            self.weight = 9.5
            self.cost = 680
        elif type == "professional":
            self.name = "The Lance"
            self.weight = 9
            self.cost = 5200
        elif type == "off road":
            self.name = "Down & Dirty"
            self.weight = 13
            self.cost = 475
        else:
            self.name = "unknown"
            self.weight = 0
            self.cost = 0
        return Bicycle(self.name, self.weight, self.cost)

# Bike Shops Class:
    # Have a name
    # Have an inventory of different bicycles
    # Sell bicycles with a margin over their cost
    # Can see how much profit they have made from selling bikes




# Customers Class:
    # Have a name
    # Have a fund of money to buy a bike
    # Can buy and own a new bicycle



def main():
    bike = Bicycle()
    bike.setParameters("street racer")

    print(bike.model_name())
    print(bike.bike_weight())
    print(bike.bike_cost())

if __name__ == "__main__":
    main()
