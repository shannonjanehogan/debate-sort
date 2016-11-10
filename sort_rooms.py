participants = [
  {'name': 'xtina', 'role': 'debate'},
  {'name': 'shannon', 'role': 'debate'},
  {'name': 'grant', 'role': 'debate'},
  {'name': 'august', 'role': 'judge'},
  {'name': 'sam', 'role': 'debate'},
  {'name': 'rebecca', 'role': 'debate'},
  {'name': 'khurram', 'role': 'debate'},
  {'name': 'sarah', 'role': 'debate'},
  {'name': 'patrick', 'role': 'debate'},
  {'name': 'mom', 'role': 'judge'},
  {'name': 'tanya', 'role': 'judge'}
]

rooms = ['BUCH B211', 'BUCH B219']

#final version of data

sortedRooms = {
  0: {
    "RoomName": "BUCH B211",
    "Judge(s)": [],
    "OG": [],
    "OO": []
  },
  1: {
    "RoomName": "BUCH B219",
    "Judge(s)": [],
    "OG": [],
    "OO": []
  },
}

def assign_judge_room(judges):
  if len(judges) >= len(rooms):
    counter = 0;
    for judge in judges:
      sortedRooms[counter]["Judge(s)"].append(judge)
      if counter < len(rooms) - 1:
        counter += 1
      else:
        counter = 0

def judges_count(participants):
  judges = []
  for participant in participants:
      if participant['role'] == 'judge':
        judges.append(participant['name'])
  assign_judge_room(judges)

judges_count(participants)

# loop through data and count and make an array of debaters

def assign_debater_room(debaters):
  if len(debaters) / len(rooms) == 4:
    roomCounter = 0
    positionCounter = 0
    for debater in debaters:
      if positionCounter <= 1:
        sortedRooms[roomCounter]["OG"].append(debater)
        positionCounter += 1
      elif positionCounter == 2:
        sortedRooms[roomCounter]["OO"].append(debater)
        positionCounter += 1
      else:
        sortedRooms[roomCounter]["OO"].append(debater)
        positionCounter = 0
        if roomCounter < 1:
          roomCounter += 1
  print('Debater sorted Rooms' + str(sortedRooms))

def debaters_count(participants):
  debaters = []
  for participant in participants:
    if participant['role'] == 'debate':
      debaters.append(participant['name'])
  assign_debater_room(debaters)

debaters_count(participants)
