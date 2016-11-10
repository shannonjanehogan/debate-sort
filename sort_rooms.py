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
  {'name': 'devon', 'role': 'debate'}
]

rooms = ['BUCH B211', 'BUCH B219']

judges = []

debaters = []

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
}

#Checklist
#Done
#more judges than rooms
#equal judges to rooms
#more debaters than spots (go through list, then add extra debaters to judges list)

#Todo
#less judges than rooms (later)
#less debaters than rooms (later)
#handle debate or judge
#import data from csv
#export data to csv

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
  for participant in participants:
      if participant['role'] == 'judge':
        judges.append(participant['name'])
  assign_judge_room(judges)

judges_count(participants)

def assign_debater_room(debaters):
  roomCounter = 0
  i = 0
  positions = ["OG", "OO", "CG", "CO"]
  for debater in debaters:
    if roomCounter == len(list(sortedRooms.keys())):
      judges.append(debater)
      continue
    sortedRooms[roomCounter][positions[i]].append(debater)
    if len(sortedRooms[roomCounter][positions[i]]) == 2:
      i += 1
    if i == len(positions):
      i = 0
      roomCounter += 1
  pp.pprint(sortedRooms)

def debaters_count(participants):
  for participant in participants:
    if participant['role'] == 'debate':
      debaters.append(participant['name'])
  assign_debater_room(debaters)

debaters_count(participants)
