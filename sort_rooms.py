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

rooms = ['BUCH B211', 'BUCH B219']

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
#less judges than rooms (later)
#odd number of debaters than rooms (later)

#Todo
#handle debate or judge
#handle partner preference
#import data from csv
#export data to csv
#need to think through how to do sorted rooms

#stretch
#store the data
#match based on skill (aka do a nov room, pro room, or mixed rooms)
#make simple web page and do forms yourself
#text debaters their room & partner & other debaters

def assign_judge_room(judges):
  if len(judges) >= len(rooms):
    counter = 0;
    for judge in judges:
      sortedRooms[counter]["Judge(s)"].append(judge)
      if counter < len(rooms) - 1:
        counter += 1
      else:
        counter = 0

def enough_judges():
  return len(judges) < len(list(sortedRooms.keys()))

def judges_needed():
  return len(list(sortedRooms.keys())) - len(judges)

def handle_extra_debaters(roomCounter, extraDebaters):
  i = 0
  positions = ["OG", "OO"]
  if len(extraDebaters) - judges_needed() >= 5:
    for debater in extraDebaters:
      if enough_judges:
        sortedRooms[roomCounter][positions[i]].append(debater)
        if len(sortedRooms[roomCounter][positions[i]]) == 2:
          i += 1
        if i == len(positions):
          judges.append(debater)
  else:
    judges.extend(extraDebaters)

def assign_debater_room(debaters):
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
    handle_extra_debaters(roomCounter, extraDebaters)

def debaters_count(participants):
  for participant in participants:
    if participant['role'] == 'debate':
      debaters.append(participant['name'])

def judges_count(participants):
  for participant in participants:
      if participant['role'] == 'judge':
        judges.append(participant['name'])

judges_count(participants)

debaters_count(participants)

assign_debater_room(debaters)

assign_judge_room(judges)

pp.pprint(sortedRooms)
