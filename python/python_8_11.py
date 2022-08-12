# Interview question
# given a key/value structure, write a function that returns the top three players 
# with the highest score, each being assigned with a medal.
# minimum number of players: 8

players = {
    'Tim': 80,
    'Darcy': 65,
    'Molly': 74,
    'Katie': 82,
    'Conor': 45,
    'Dave': 76,
    'Denise': 82,
    'Marcy': 98
}


# def topPlayers(players: dict) -> dict:
# for competitors in players:
#     topThree = []
#     topThree = sorted(players.values(), reverse = True)
#     topScores = topThree[3::]
#     topScores = topThree.append('gold,silver,bronze')
#     print(topScores)

# print(topPlayers(players))

#Dez's solution
def medalAssignment(players:dict)->list:
    highestScores = sorted(players, key=players.get, reverse=True)

    print(highestScores[0],": Gold")
    print(highestScores[1], ": Silver")
    print(highestScores[2], ": Bronze")
medalAssignment(players)

#Dre's solution
def winners(players:dict)->dict:
    first, second, third = ('',0),('',0),('',0)

    for player in players:
        if players.get(player)>first[1]:
            third=second
            second=first
            first=(player, players.get(player))
        elif players.get(player)<first[1] and players.get(player)>first[1]:
            third=second
            second = (player, players.get(player))
        elif players.get(player)>third[1]:
            third = (player, players.get(player))
    
    return({'Gold':first[0],'Silver':second[0],'Bronze':third[0]})

print(winners(players))


# the thing to remember when deciding between structures to use:
#1. what are you going to be doing to the structure (i.e. are you adding things to it?)
#2. for the objects that exist in the structure, are they unique or is it possible that there are duplicates?
    # if there are duplicates, dicitonaries are really useful