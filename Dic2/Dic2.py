'''
Homework-2:
* create an empty dictonary of cricket_players
* add following data to dictonary
* "ajinkya" : 1, "virat" : 7 , "jadeja" : 3, "bumrah": 5 , "bhuvaneshvar" : 2
* print all player names only (keys) from dictonary
* print all player numbers only (values) from dictionary
* print both player_name and number from dictonary
* find "bhuvaneshvar" in dictonary (remember to use the syntax dicotnary[key])
'''

Players={}
Players["ajinkya"]= 1
Players["virat"]= 7
Players["jadeja"]= 3
Players["bumrah"]= 5
Players["bhuvaneshvar"]= 2
for names in Players.keys():
  print (names)
for names in Players.values():
  print (names)
for names,number in Players.items():
  print (names+" "+ str(number))
if "bhuvaneshvar" in Players:
  print("bhuvaneshvar found")
