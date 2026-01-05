#!/bin/bash/python3


print("""\
⬛⬛⬛⬛⬛⬛⬛⬛        \033[1;33m==== Minecraft ====
⬛⬛⬛⬛⬛⬛⬛⬛          Data  dashboard
⬛🏽🏽🏽🏽🏽🏽⬛
🏽🏽🏽🏽🏽🏽🏽🏽        \033[1;37mMade by gtourdia :-)
🏽⬜🟦🏽🏽🟦⬜🏽
🏽🏽🏽🟫🟫🏽🏽🏽
🏽🏽⬛🏽🏽⬛🏽🏽
🏽🏽⬛⬛⬛⬛🏽🏽\n""")

print("\033[0;31mList demo :\033[0;37m")
# We can create lists...
print("\033[1;33m" + "PythonList joined the game\033[1;37m")
print("\033[1;33m" + "Steve joined the game\033[1;37m")
print("Steve> Another beautiful day is starting :D")
steve_invetory = ['potato', 'sword', 'water_bucket']
print("Steve inventory: ", end="")
# Iterate trough each element...
for item in steve_invetory:
    print(f"{item} ", end="")
# Add or remove items...
steve_invetory.append('fishing_rod')
steve_invetory.remove('sword')
print(f"\nSteve's inventory: {steve_invetory}. He's now a peaceful Steve...")
# Count these items
print(f"Steve has now {len(steve_invetory)} unique items")
# And even store numbers !
steve_coords = [-4242, 255, 344001]
print(f"Steve is now searching Alex at the coords {steve_coords}")
print("\033[1;33m" + "Alex joined the game\033[1;37m")
print("Alex> I said MINUS 344001, right ?")
print("Steve> bro...")
print("\033[1;33m" + "Steve left the game\033[1;37m")
print("\n")

# Now, here are the dictionnary
print("\033[0;31mDictionnary demo :\033[0;37m")
print("\033[1;33m" + "Steve joined the game\033[1;37m")
# We can store all type of data in a dict...
steve_status = {'armored': True, 'health': 20, 'items': ['sword', 'bread']}
print(f"Steve's current state: {steve_status}")
print("Notch cleared steve's invetory")
# We can update these items by changing their values
steve_status.update({'armored': False})
# Or remove them completely
steve_status.pop('items')
print(f"Steve's current state: {steve_status}")
# We can get the dict keys, or values
print(f"Steve status keys: {steve_status.keys()}")
print(f"Steve status values: {steve_status.values()}")
# What is most interesting is list of dictionnaries !
players = []
players.append({'username': 'Steve', 'is_operator': False})
players.append({'username': 'Notch', 'is_operator': True})
print("= List of players: =")
for player in players:
    print(f"{player['username']}, OP = {player['is_operator']}")
print("\n")


print("\033[0;31mSets demo :\033[0;37m")
print("\033[1;33m" + "Steve joined the game\033[1;37m")
# Like lists, but with uniques items only
steve_achievements = {'DIAMONDS!', 'Not today thank you'}
alex_achievements = {'DIAMONDS!', 'Ice bucket challenge'}
print(f"Steve achivements: {steve_achievements}")
print(f"Alex achivements: {alex_achievements}")
print("Common achievements :"
      f"{set.intersection(steve_achievements,alex_achievements)}")
print("Non common achievements : ", set.union(
    set.difference(steve_achievements, alex_achievements),
    set.difference(alex_achievements, steve_achievements)))
# Way less impressing, right ?!
print("\n")

print("\033[0;31mFinally, some bonus demo :\033[0;37m")
players = [
    {
        'name': 'Steve',
        'inventory': [
            {'name': 'sword', 'count': 1},
            {'name': 'dirt_block', 'count': 64}
        ],
        'xp': 5,
        'achievements': {'DIAMONDS!', 'Not today thank you'},
        'category': 'player'
    },
    {
        'name': 'Alex',
        'inventory': [
            {'name': 'snowball', 'count': 16},
            {'name': 'egg', 'count': 16}
        ],
        'xp': 12,
        'achievements': {'DIAMONDS!', 'Ice bucket challenge'},
        'category': 'player'
    }
]


print(f"Total players: {len(players)}")
items = 0
for player in players:
    for item in player['inventory']:
        items += item['count']
print(f"Total items: {items}")
print(f"Average items for each player: {items / len(players)}")
top_player = []
for player in players:
    if top_player == []:
        top_player = player
    if top_player['xp'] < player['xp']:
        top_player = player
print(f"Highest XP player: {top_player['name']} ({top_player['xp']})")
steve_occurence = 0
for player in players:
    if player['name'] == 'Steve':
        steve_occurence += 1
print(f"Steve username occurences: {steve_occurence}")
print("Not shared achievements : ", set.union(
    set.difference(players[0]['achievements'], players[1]['achievements']),
    set.difference(players[1]['achievements'], players[0]['achievements'])))

# uselss things but just in case
print("\n")
unique_players = set()
for player in players:
    unique_players = set.union(unique_players, {player['name']})
print(f"Unique players: {unique_players}")
scores = [4, 486, 456, 11, -5]
for score in scores:
    if (score > 100):
        print(score)
scores.append(7777)
