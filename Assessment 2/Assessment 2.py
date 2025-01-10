import random
import time 
import sys

choices = [
    {'type': '🔥 fire starter', 'price': 10, 'stock': 100},
    {'type': '💦 water starter', 'price': 10, 'stock': 100},
    {'type': '🍃 grass starter', 'price': 10,'stock': 100},
    {'type': '🌈🦄 pseudo-legendary', 'price': 20, 'stock': 100},
    {'type': '🐉 legendary', 'price': 30, 'stock': 100}
]

fire_type= ["Charmander","Cyndaquil","Torchic","Chimchar","Tepig","Fennekin","Litten","Scorbunny","Fuecoco"]
water_type=["Squirte","Tododile","Mudkip","Piplup","Oshawott","Frokie","Popplio","Sobble","Quaxly"]
grass_type=["Bulbasaur","chikorita","treecko","Turtwig","Snivy","Chespin","Rowlet","Grookey","Sprigatito"]
pseudo_legendary=["Dratini","Larvitar","Bagon","Beldum","Gible","Deino","Goomy","Jangmo-o","Dreepy","Frigibax"]
legendaries=["Mewtwo","Lugia","Rayquaza","Giratina","Reshiram","Yvetal","Lunala","Zacian","Miraidon"]

pokemon_data = {
    '🔥 fire starter': fire_type,
    '💦 water starter': water_type,
    '🍃 grass starter': grass_type,
    '🌈🦄 pseudo-legendary': pseudo_legendary,
    '🐉 legendary': legendaries,
}

pity_counts = {}
last_type = None

#Function for user to draw 1 or to draw 10
def draw_10(pokemon_type, price):
    global choices
    while True:
        #stock system for the selected pokemon type
        stock_item = next((item for item in choices if item['type'] == pokemon_type), None)
        if not stock_item or stock_item['stock'] <= 0:
            print(f"Sorry, {pokemon_type.capitalize()} is out of stock!")
            return

        print("If you draw 10, your chance of getting a ✨ Shiny Version ✨ of the plushy would be higher!")
        draw_choice = input("\nWould you like to draw 1 or 10?: ")
        if draw_choice in ['1', '10']:
            draw_count = int(draw_choice)
            #checks if there is enough stock
            if draw_count > stock_item['stock']:
                print(f"Sorry, only {stock_item['stock']} {pokemon_type.capitalize()} Pokémon are left in stock.")
                continue
            
            total_price = price * draw_count
            tokens = int(input(f"Please insert 🪙  {total_price} tokens🪙 : "))

            while tokens < total_price:  
                tokens += int(input("Insufficient tokens. Please insert more tokens: "))

            drawing = "Drawing", " your"," Pokémon", ".", ".", ".\n"
            for i in drawing:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.8)

            time.sleep(1.5)
            print("Congratulations! Here are the Pokemon/s you got.")
            
            for _ in range(draw_count):
                selected_pokemon = random.choice(pokemon_data[pokemon_type])
                shiny_result = shiny_pokemon(selected_pokemon, pokemon_type)
                print(f" {shiny_result} ")
                time.sleep(0.8)

            #deduction of stocks
            time.sleep(1)
            stock_item['stock'] -= draw_count
            print (f"\n Remaining 📦 stock 📦 for {pokemon_type.capitalize()}:  {stock_item['stock']}")
            if tokens >= total_price:  
                print(f"\nHere is your change: {tokens - total_price} tokens.")
            break  

        else:
            print("Invalid input. Please input either 1 or 10.")    

#Function for opening animation

def display_welcome_animation():
    message = "Welcome to the Pokemon Plushy Center!"
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    print("\n") 

#Function for Displaying the menu
def display_pokemon():
    display_welcome_animation()  
    time.sleep(0.3)
    print("Guaranteed ✨ Shiny ✨ after 100 pulls!")
    time.sleep(1)
    print("\nAvailable Pokémon Types and Prices:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice['type'].capitalize()} - 🪙  {choice['price']} tokens (Stock: {choice['stock']})")

#Function for shiny pokemon
def shiny_pokemon(selected_pokemon, current_type):
    global pity_counts, last_type

    if current_type not in pity_counts:
        pity_counts[current_type] = 0  
    if current_type != last_type:
        pity_counts[current_type] = 0  
        last_type = current_type  

    pity_counts[current_type] += 1
    shiny_chance = random.random() <= 0.01

    if shiny_chance or pity_counts[current_type] >= 100:  
        pity_counts[current_type] = 0 
        return f"✨ SHINY {selected_pokemon.upper()}! ✨"
    else:
        return selected_pokemon



#Feature for suggesting purchase
def suggest_pokemon(selected_choice):
    suggestions = { 
        'fire starter': 'water starter',
        'water starter': 'grass starter', 
        'grass starter': 'pseudo-legendary', 
        'pseudo-legendary': 'legendary', 
        'legendary': 'pseudo-legendary'
    }
    suggested_type = suggestions.get(selected_choice, None)
    time.sleep(1)
    if suggested_type:
        print(f"\nYou may also be interested in a {suggested_type.capitalize()}! Would you like to try it?")
    else:
        print("\nWould you like to explore other 🔴⚪ Pokémon types?")

# Main program for vending machine and gacha pity
def main():
    while True:
        display_pokemon()
        try:
            time.sleep(1.5)
            user_choice = int(input("\nEnter the number of your choice: "))
            
            if user_choice < 1 or user_choice > len(choices):
                print("Invalid input. Please select a valid number.")
            else:
                selected_choice = choices[user_choice - 1]
                pokemon_type = selected_choice['type']
                price = selected_choice['price']
                time.sleep(1)
                print(f"\nYou have chosen {pokemon_type.capitalize()}. Here are the Pokémons you might receive:")
                time.sleep(1)
                for i, pokemon in enumerate(pokemon_data[pokemon_type], start=1):
                    print(f"{i}. {pokemon}")
                
                print(f"\nThe price for a {pokemon_type} Pokémon is 🪙  {price} tokens.")

                draw_10(pokemon_type,price)

                suggest_pokemon(pokemon_type)

                if not another_purchase():
                    print("Thank you for buying a Pokémon plushie! Please come again!")
                    break 

        except ValueError:
            print("Invalid input. Please enter a valid number.")

#FUnction for another purchase
def another_purchase():
    while True:  
        time.sleep(1)
        choice = input("Would you like to buy another plushie? (yes/no): ").lower()
        if choice in ['n','no']:
            return False
        elif choice in ['y','yes']:
            return True
        else:
            print("Invalid Input. Please type yes or no.")

main()


