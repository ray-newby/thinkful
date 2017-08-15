# Pirate Bartender: Unit 1 / Lesson 3 / Project 2
import random # To choose a random ingredient


def drink_style():
    
    questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
    }
    
    preferences = dict() # Create a new dictionary to store the answers
        
    for key in questions: # Iterate through the questions
        print(questions[key])
        
        try:
            ans = str(input("Yay or Nay?: "))
        except ValueError:
            ans = str(input("I say it again, Yay or Nay?: "))
        
        # Make sure to convert answers to lowercase
        if ans.lower() == "yay" or ans.lower() == "y" or ans.lower() == "yes":
            preferences[key] = True
        elif ans.lower() == "nay" or ans.lower() == "n" or ans.lower() == "no":
            preferences[key] = False
        else:
            preferences[key] = "Unknown" # In case of no yes/no answer
    
    return preferences        


def cocktail(preferences):
    
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }

    ingredients_list = []
    
    for key in preferences:
        if preferences[key] == True:
            ingredients_list.append(random.choice(ingredients[key]))
        else:
            pass
    
    print("Your cocktail is made of: " + str(ingredients_list))


# Main function
if __name__ == '__main__':
    preference_dictionary = drink_style()
    cocktail(preference_dictionary)



#######################

# Extra challenges

# If you found completing the basic requirements fairly straightforward then you should try to extend your app to add the following features:

# Give the cocktails a name
# All good cocktails should have a memorable name. Try to write a function which will name your cocktails. The name should be a random combination of an adjective and a noun (for example your bartender could make a "Fluffy Chinchilla", a "Salty Sea-Dog", or a "Fluffy Sea-Dog").

# Keep 'em coming
# At the moment you can only get one drink at a time from the bartender. A well trained pirate bartender should offer his customer another drink when they've finished their previous one. Try adding a loop in the main function which will ask the customer whether they want another drink, and keep creating new recipes as long as they agree.

# Extension exercises

# If the extra challenges were not a problem and you're running ahead of schedule then you could try to implement one or two of the following features in your app:

# Multiple customers: The bartender could ask for the customer's name before they are served. They could then remember the customer's preferences for when the same customer asks for another drink.
# Stock control: Even pirate bars don't have a limitless supply of ingredients. You could add a stock count for each ingredient which decreases whenever the bartender makes a drink. The bartender could restock the ingredients when supplies are low.

#######################