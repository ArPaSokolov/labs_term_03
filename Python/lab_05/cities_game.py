def game():
    flag = True
    cities = set()
    while flag:
        length_before = len(cities)
        word = input("Enter city: ")
        if word == "END":
            break
        cities.add(word)
        if length_before < len(cities):
            print("OK")
        else:
            print("REPEAT")


print("Game started! To finish the game enter 'END'.")
game()
print("Game finished!")
