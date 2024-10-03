def select_character():
    character = input("Choose a character: Mona or Qi Qi: ")
    if character == "Mona":
        print("Mona's character: a tall girl with long hair.")
        haircolor = input("What hair color will you choose? (red, brown, blue): ")
        if haircolor not in ["red", "brown", "blue"]:
            print("Error: Invalid hair color.")
            return

        clothing = input("Which clothes will you choose? (a dress or pants with a jacket): ")
        if clothing not in ["dress", "pants with a jacket"]:
            print("Error: Invalid clothing option.")
            return

        footwear = input("Which shoes will you choose? (heels or sneakers): ")
        if footwear not in ["heels", "sneakers"]:
            print("Error: Invalid shoe option.")
            return

    elif character == "Qi Qi":
        print("Character Qi Qi: A girl with a model of a small child.")
        clothing = input("What clothes will you choose? (a small dress or pants with a jacket): ")
        if clothing not in ["a small dress or pants with a jacket"]:
            print("Error: Invalid clothing option.")
            return

        footwear = input("Which shoes will you choose? (small heels or sneakers): ")
        if footwear not in ["small heels or sneakers"]:
            print("Error: Invalid shoe variant.")
            return

    else:
        print("error: invalid character.")
        return

select_character()