import random as rd



def choose_random_faction(current_list):
    current_list.append(rd.choice(Faction_list))
    if not Allow_doublons:
        check_doublons(current_list)

def check_doublons(list):
    if list[-1] in list[:-1] :
        list.remove(list[-1])
        choose_random_faction(list)

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
Number_of_faction = 2
Points = 3000
Allow_doublons = False

Player1_list = []
Player2_list = []

loop = 1
while loop <= Number_of_faction:
    # Player 1
    choose_random_faction(Player1_list)
    P1_SpecialUnits = rd.choices([True,False],[9,1])[0]

    # Player 2
    choose_random_faction(Player2_list)
    P2_SpecialUnits = rd.choices([True, False], [9, 1])[0]

    loop += 1

print(f"""
Player 1: 
- Points :              {Points}
- Factions choices :    {Player1_list}
- Special units :       {P1_SpecialUnits} {"(+" + str(0.1*Points) +"pts)" if P1_SpecialUnits == False else ""}
 
 Player 2: 
- Points :              {Points}
- Factions choices :    {Player2_list}
- Special units :       {P2_SpecialUnits} {"(+" + str(0.1*Points) +"pts)" if P2_SpecialUnits == False else ""}
""")