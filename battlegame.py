wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 70

dragon_hp = 300
dragon_damage = 50

while True:
    print("1", wizard)
    print("2", elf)
    print("3", human)
    character = input("Choose your character:")
    if character == "1":
        character = wizard
        apos = "Wizard's"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = elf
        apos = "Elf's"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = human
        apos = "Human's"
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
print("You have chosen the character:", character, "\n Health:", my_hp, "\n Damage:", my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon h1as damaged the", character,)
    print("The", apos, "hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle!")
        break