import pprint
pp = pprint.PrettyPrinter(indent=1)

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
  {'name': 'tanya', 'role': 'judge'},
  {'name': 'kaja', 'role': 'debate'},
  {'name': 'vivian', 'role': 'debate'},
  {'name': 'scottish david', 'role': 'debate'},
  {'name': 'dena', 'role': 'debate'},
  {'name': 'charlotte', 'role': 'debate'},
  {'name': 'moira', 'role': 'debate'},
  {'name': 'brian steele', 'role': 'debate'},
  {'name': 'devon', 'role': 'debate'},
  {'name': 'zeynep', 'role': 'debate'},
  {'name': 'allison', 'role': 'debate'},
  {'name': 'pia', 'role': 'debate or judge'},
  {'name': 'lindsey', 'role': 'debate or judge'},
  {'name': 'charlie', 'role': 'debate or judge'}
]

judges = []

debaters = []

debate_or_judge = []

sortedRooms = {
  0: {
    "RoomName": "BUCH B211",
    "Judge(s)": [],
    "OG": [],
    "OO": [],
    "CG": [],
    "CO": []
  },
  1: {
    "RoomName": "BUCH B219",
    "Judge(s)": [],
    "OG": [],
    "OO": [],
    "CG": [],
    "CO": []
  },
  2: {
    "RoomName": "BUCH B215",
    "Judge(s)": [],
    "OG": [],
    "OO": [],
    "CG": [],
    "CO": []
  },
  3: {
    "RoomName": "BUCH B216",
    "Judge(s)": [],
    "OG": [],
    "OO": [],
    "CG": [],
    "CO": []
  },
}

#Checklist

#Done
#assign debaters to rooms
#more judges than rooms
#equal judges to rooms
#more debaters than spots (go through list, then add extra debaters to judges list)
#handle debate or judge
#less judges than rooms (later)
#odd number of debaters than rooms (later)

#Todo
#handle partner preference
#import data from csv
#export data to csv
#need to think through how to do sorted rooms

def assign_judge_room(extraDebaters):
  judges.extend(extraDebaters)
  counter = 0;
  for judge in judges:
    sortedRooms[counter]["Judge(s)"].append(judge)
    if counter < (rooms_used() - 1):
      counter += 1
    else:
      counter = 0

def enough_judges():
  return len(judges) >= rooms_used()

def judges_needed():
  if enough_judges():
    return 0
  else:
    return rooms_used() - len(judges)

def handle_extra_debaters(extraDebaters, roomCounter):
  i = 0
  positions = ["OG", "OO"]
  if debate_or_judge:
    extraDebaters.extend(debate_or_judge)
  if (len(extraDebaters) - judges_needed() >= 5):
    extraRoom = extraDebaters[:5]
    assign_judge_room(extraDebaters[5:])
    for debater in extraRoom:
      if i == len(positions):
        sortedRooms[roomCounter]["Judge(s)"].append(debater)
      else:
        if len(sortedRooms[roomCounter][positions[i]]) < 2:
          sortedRooms[roomCounter][positions[i]].append(debater)
          if len(sortedRooms[roomCounter][positions[i]]) == 2:
            i += 1
  else:
    assign_judge_room(extraDebaters)

def assign_debater_room():
  roomCounter = 0
  i = 0
  positions = ["OG", "OO", "CG", "CO"]
  splicePosition = len(debaters) - (len(debaters) % 8)
  extraDebaters = debaters[splicePosition:]
  slicedDebaters = debaters[:splicePosition]
  for debater in slicedDebaters:
    sortedRooms[roomCounter][positions[i]].append(debater)
    if len(sortedRooms[roomCounter][positions[i]]) == 2:
      i += 1
    if i == len(positions):
      i = 0
      roomCounter += 1
  if extraDebaters:
    handle_extra_debaters(extraDebaters, roomCounter)

def rooms_used():
  roomsUsed = 0
  for room in sortedRooms:
    if sortedRooms[room]["OG"] != []:
      roomsUsed += 1
    else:
      return roomsUsed

def debaters_count():
  for participant in participants:
    if participant['role'] == 'debate':
      debaters.append(participant['name'])

def judges_count():
  for participant in participants:
    if participant['role'] == 'judge':
      judges.append(participant['name'])

def debate_or_judge_count():
  for participant in participants:
    if participant['role'] == 'debate or judge':
      debate_or_judge.append(participant['name'])

judges_count()

debaters_count()

debate_or_judge_count()

assign_debater_room()

assign_judge_room()

pp.pprint(sortedRooms)
