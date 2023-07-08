import pokemon_list
import math
import inquirer
import sys

def hp_calc(base_hp, iv_hp, ev_hp, level):
    hp = math.floor(((2 * base_hp + iv_hp + math.floor(ev_hp / 4)) * level) / 100 + level + 10)
    return f"HP: {hp}"

def atk_calc(base_atk, iv_atk, ev_atk, level, nature):
    if (
        nature == "Lonely"
        or nature == "Brave"
        or nature == "Adamant"
        or nature == "Naughty" 
    ):
        nature_modifier = 1.1
    elif (
        nature == "Bold"
        or nature == "Timid"
        or nature == "Modest"
        or nature == "Calm"
    ):
        nature_modifier = 0.9
    else:
        nature_modifier = 1
    atk = math.floor((math.floor((2 * base_atk + iv_atk + math.floor(ev_atk / 4)) * level / 100) + 5) * nature_modifier)
    return f"Attack: {atk}"

def def_calc(base_def, iv_def, ev_def, level, nature):
    if (
        nature == "Bold"
        or nature == "Relaxed"
        or nature == "Impish"
        or nature == "Lax" 
    ):
        nature_modifier = 1.1
    elif (
        nature == "Lonely"
        or nature == "Hasty"
        or nature == "Mild"
        or nature == "Gentle"
    ):
        nature_modifier = 0.9
    else:
        nature_modifier = 1
    defence = math.floor((math.floor((2 * base_def + iv_def + math.floor(ev_def / 4)) * level / 100) + 5) * nature_modifier)
    return f"Defence: {defence}"

def spec_atk_calc(base_spec_atk, iv_spec_atk, ev_spec_atk, level, nature):
    if (
        nature == "Modest"
        or nature == "Mild"
        or nature == "Quiet"
        or nature == "Rash" 
    ):
        nature_modifier = 1.1
    elif (
        nature == "Adamant"
        or nature == "Impish"
        or nature == "Jolly"
        or nature == "Careful"
    ):
        nature_modifier = 0.9
    else:
        nature_modifier = 1
    spec_atk = math.floor((math.floor((2 * base_spec_atk + iv_spec_atk + math.floor(ev_spec_atk / 4)) * level / 100) + 5) * nature_modifier)
    return f"Special attack: {spec_atk}"

def spec_def_calc(base_spec_def, iv_spec_def, ev_spec_def, level, nature):
    if (
        nature == "Calm"
        or nature == "Gentle"
        or nature == "Sassy"
        or nature == "Careful" 
    ):
        nature_modifier = 1.1
    elif (
        nature == "Naughty"
        or nature == "Lax"
        or nature == "Naive"
        or nature == "Rash"
    ):
        nature_modifier = 0.9
    else:
        nature_modifier = 1
    spec_def = math.floor((math.floor((2 * base_spec_def + iv_spec_def + math.floor(ev_spec_def / 4)) * level / 100) + 5) * nature_modifier)
    return f"Special defence: {spec_def}"

def speed_calc(base_speed, iv_speed, ev_speed, level, nature):
    if (
        nature == "Timid"
        or nature == "Hasty"
        or nature == "Jolly"
        or nature == "Naive" 
    ):
        nature_modifier = 1.1
    elif (
        nature == "Brave"
        or nature == "Relaxed"
        or nature == "Quiet"
        or nature == "Sassy"
    ):
        nature_modifier = 0.9
    else:
        nature_modifier = 1
    speed = math.floor((math.floor((2 * base_speed + iv_speed + math.floor(ev_speed / 4)) * level / 100) + 5) * nature_modifier)
    return f"Speed: {speed}"

def main():
    user_choice = input("Pick a Pokémon: ").lower()
    
    try:
        pokemon = getattr(pokemon_list, user_choice)
    except:
        print("No such Pokémon!")
        sys.exit(1)
    
    level = int(input("Pick the level: ")) # Get pokémon's level
    
    # Get IVs
    iv_hp = int(input(f"What is {user_choice.capitalize()}'s HP IV?: "))
    iv_atk = int(input(f"What is {user_choice.capitalize()}'s Attack IV?: "))
    iv_def = int(input(f"What is {user_choice.capitalize()}'s Defence IV?: "))
    iv_spec_atk = int(input(f"What is {user_choice.capitalize()}'s Special attack IV?: "))
    iv_spec_def = int(input(f"What is {user_choice.capitalize()}'s Special defence IV?: "))
    iv_speed = int(input(f"What is {user_choice.capitalize()}'s Speed IV?: "))

    # Get EVs
    ev_hp = int(input(f"What is {user_choice.capitalize()}'s HP EV?: "))
    ev_atk = int(input(f"What is {user_choice.capitalize()}'s Attack EV?: "))
    ev_def = int(input(f"What is {user_choice.capitalize()}'s Defence EV?: "))
    ev_spec_atk = int(input(f"What is {user_choice.capitalize()}'s Special attack EV?: "))
    ev_spec_def = int(input(f"What is {user_choice.capitalize()}'s Special defence EV?: "))
    ev_speed = int(input(f"What is {user_choice.capitalize()}'s Speed EV?: "))

    # Natures
    nature_choices = [
    inquirer.List('nature',
                  message="What is the Pokémon's nature?",
                  choices=[
                    'Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold',
                    'Docile', 'Relaxed', 'Impish', 'Lax', 'Timid', 'Hasty',
                    'Serious', 'Jolly', 'Naive', 'Modest', 'Mild', 'Quiet',
                    'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky'
                  ],
        ),
    ]

    nature = (inquirer.prompt(nature_choices)["nature"])
    
    print(f"\n{user_choice.capitalize()}, at level {level}:\n\n"
          f"{hp_calc(pokemon[0], iv_hp, ev_hp, level)}\n"
          f"{atk_calc(pokemon[1], iv_atk, ev_atk, level, nature)}\n"
          f"{def_calc(pokemon[2], iv_def, ev_def, level, nature)}\n"
          f"{spec_atk_calc(pokemon[3], iv_spec_atk, ev_spec_atk, level, nature)}\n"
          f"{spec_def_calc(pokemon[4], iv_spec_def, ev_spec_def, level, nature)}\n"
          f"{speed_calc(pokemon[5], iv_speed, ev_speed, level, nature)}\n"
    )

main()
