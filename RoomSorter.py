import Debater
import Team
import Room
import RoomSkill
import DebaterSkill
import TeamSkill
from typing import Set


class RoomSorter:

    def __init__(self, participants: Set(Debater), rooms: Set(Room), vpi_pref: RoomSkill):
        self.participants = participants
        self.rooms = rooms
        self.vpi_pref = vpi_pref
        self.judges = set()
        self.judge_or_debate = set()
        self.sorted_rooms = set()
        self.debaters = set()
        self.teams = set()

    def sort_participants(self):
        for participant in self.participants:
            if participant.status == 'JUDGE':
                self.judges.add(participant)
            if participant.status == 'JUDGE_OR_DEBATE':
                self.judge_or_debate.add(participant)
            if participant.status == 'DEBATER':
                partner_pref = participant.partner_pref
                if partner_pref is None:
                    self.debaters.add(participant)
                else:
                    for p2 in self.participants:
                        if p2.name == partner_pref and p2.status == ('DEBATE' or 'JUDGE_OR_DEBATE'):
                            team = Team(participant, p2)
                            if team not in self.teams:
                                self.teams.add(team)

    #TODO: ALLZ (i.e. finish sorting debaters with no partner pref)