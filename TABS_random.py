import numpy.random as rd

Faction_list = ["Tribal",
                "Farmer",
                "Medieval",
                "Ancient",
                "Vikings",
                "Dynasty",
                "Renaissance",
                "Pirate",
                "Spooky",
                "Wild West",
                "Good",
                "Evil",
                ]

def choose_random_faction(current_list):
    current_list.append(rd.choice(Faction_list))
    if not Allow_doublons:
        check_doublons(current_list)

def check_doublons(list):
    if list[-1] in list[:-1] :
        list.remove(list[-1])
        choose_random_faction(list)

Number_of_faction = 10
Allow_doublons = False

Player1_list = []
Player2_list = []

loop = 1
while loop <= Number_of_faction:
    choose_random_faction(Player1_list)
    choose_random_faction(Player2_list)
    loop += 1

