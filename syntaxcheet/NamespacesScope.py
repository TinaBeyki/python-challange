# how to modify global variable inside a function   --------------------------------------------------------------------
enemies = 1


def increase_enemies():
    global enemies  # solution, if we dont define it as global variable, it creates enemies as local variable
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside the function: {enemies}")
# global and local scope -----------------------------------------------------------------------------------------------

""" 
Global Scope , they are accessable inside and outside of functions (all over the class)-> player_health
Local Scope exists within functions -> potion_strength
"""
player_health = 10

# Global constants
PI = 3.1415
URL = "http://www.apple.com"


def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
        print(player_health)
    drink_potion()


game()
"""
drink_potion() -> we have no accessiblity to this function outside if game func
print(potion_strength) its only accessable inside the function because its local variable
"""
# Unless Java, There is no block scope in python -----------------------------------------------------------------------
game_level = 3
enemies_list = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies_list[0]
print(new_enemy)  # its not local variable


"""
If we create a variable inside a function, its only available inside that function, But if we create it within if block
or while loop or for loop or any thing which has the indentation and colon(:), that is not count as creating a seperate 
local variable
"""