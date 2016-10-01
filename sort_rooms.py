debaters = [
  {'name': 'xtina', 'role': 'debate'},
  {'name': 'shannon', 'role': 'debate'},
  {'name': 'grant', 'role': 'debate'},
  {'name': 'august', 'role': 'judge'},
  {'name': 'sam', 'role': 'debate'},
  {'name': 'mom', 'role': 'judge'}
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
  }
}

# loop through data and count and make an array of judges

def judges_count(debaters):
  judges = []
  for debater in debaters:
      if debater['role'] == 'judge':
        judges.append(debater['name'])
  assign_judge_room(judges)
  print('Full list of Judges' + str(judges))

def assign_judge_room(judges):
  if len(judges) >= len(rooms):
    counter = 0;
    for judge in judges:
      sortedRooms[counter]["Judge(s)"].append(judge)
      counter += 1
  print('Sorted Rooms' + str(sortedRooms))

judges_count(debaters)
