from Debaters import DebaterSkill, Status, Debater
from Teams import TeamSkill, Team
from Rooms import Room
from typing import Set
import random
import math


class RoomSorter:

    # TODO: Comments

    def __init__(self, participants: Set(Debater), rooms: Set(Room), vpi_pref: TeamSkill):
        self.participants = participants
        self.rooms = rooms
        self.vpi_pref = vpi_pref
        self.judges = set()
        self.judge_or_debate = set()
        self.sorted_rooms = set()
        self.debaters_nov = set()
        self.debaters_pro = set()
        self.debaters_adv = set()
        self.debaters = [self.debaters_adv, self.debaters_pro, self.debaters_nov]
        self.teams_proam = set()
        self.teams_adv = set()
        self.teams_pro = set()
        self.teams_nov = set()
        self.teams = [self.teams_adv, self.teams_pro, self.teams_proam, self.teams_nov]
        # To be used to set if rooms can run without judges, default not
        self.judgeless_rooms = False
        self.sort_participants()
        self.sort_partners()
        self.make_teams()
        self.make_rooms()

    # Main functions

    def sort_participants(self):
        for participant in self.participants:
            if participant.status == Status.JUDGE:
                self.judges.add(participant)
            elif participant.status == Status.JUDGE_OR_DEBATE:
                self.judge_or_debate.add(participant)
            elif participant.status == Status.DEBATER:
                if participant.status == DebaterSkill.ADVANCED:
                    self.debaters_adv.add(participant)
                elif participant.status == DebaterSkill.PRO:
                    self.debaters_pro.add(participant)
                elif participant.status == DebaterSkill.NOV:
                    self.debaters_nov.add(participant)

    def sort_partners(self):
        partner_found = False
        for group in self.debaters:
            for debater in group:
                partner_pref = debater.partner_pref
                if partner_pref is not None:
                    for g2 in self.debaters:
                        for d2 in g2:
                            if d2.name == partner_pref:
                                self.create_team(debater, group, d2, g2)
                                partner_found = True
                                break
                        if partner_found:
                            break
                    if not partner_found:
                        for d2 in self.judge_or_debate:
                            if d2.name == partner_pref:
                                self.create_team(debater, group, d2, self.judge_or_debate)
                                break

    def make_teams(self):
        if self.vpi_pref == TeamSkill.PROAM:
            self.handle_proam()
        for group in self.debaters:
            while len(group) >= 2:
                self.create_team_random(group, group)
            # Judgment call made here that adv debaters should have priority for a pro partner
            # TODO: Confirm
            if len(self.debaters_adv) == 1 and len(self.debaters_pro) >= 1:
                self.create_team_random(group, self.debaters_pro)
        ironperson = self.handle_extras()
        self.maths(ironperson)

    def handle_extras(self):
        extras = len(self.debaters_nov) + len(self.debaters_pro) + len(self.debaters_adv)
        if extras == 0:
            return None
        elif extras == 1:
            for group in self.debaters:
                if len(group) == 1:
                    ironperson = random.sample(group, 1)
                    group.remove(ironperson)
                    return ironperson
        elif extras == 2:
            if len(self.debaters_adv) == 0:
                self.create_team_random(self.debaters_pro, self.debaters_nov)
            else:
                self.create_team_random(self.debaters_adv, self.debaters_nov)
            return None

    def maths(self, ironperson: Debater):
        number_teams = 0
        number_judges = len(self.judges)
        number_either = len(self.judge_or_debate)
        for team in self.teams:
            number_teams += len(team)
        judges_needed = int(math.ceil(number_teams / 4))
        while judges_needed > number_judges and number_either > 0:
            judge = random.sample(self.judge_or_debate, 1)
            self.judges.add(judge)
            self.judge_or_debate.remove(judge)
            number_judges += 1
            number_either -= 1
        if number_judges < judges_needed:
            self.judges.add(ironperson)
            ironperson = None
        while not self.judgeless_rooms and number_judges < judges_needed:
            to_remove = number_teams % 4
            if to_remove == 0:
                to_remove = 4
            for count in range(to_remove):
                self.remove_team()
                number_teams -= 1
                judges_needed = math.ceil(number_teams / 4)
        while number_either > 0:
            extra_teams = number_teams % 4
            if extra_teams == 0:
                judge = random.sample(self.judge_or_debate, 1)
                self.judges.add(judge)
                self.judge_or_debate.remove(judge)
                number_judges += 1
                number_either -= 1
            if ironperson is not None and number_either >= (7 - extra_teams * 2):
                d2 = random.sample(self.judge_or_debate, 1)
                team = Team(ironperson, d2)
                self.judge_or_debate.remove(d2)
                self.add_team(team)
                number_either -= 1
                number_teams += 1
                for count in range(3 - extra_teams):
                    self.create_team_random(self.judge_or_debate, self.judge_or_debate)
                    number_either -= 2
                    number_teams += 1
            elif number_either >= (8 - extra_teams * 2):
                for count in range(4 - extra_teams):
                    self.create_team_random(self.judge_or_debate, self.judge_or_debate)
                    number_either -= 2
            else:
                for judge in self.judge_or_debate:
                    self.judges.add(judge)
                    self.judge_or_debate.remove(judge)
                    number_judges += 1
                    number_either -= 1
        # Judgement call room with 2 teams better than room with 3
        if number_teams % 2 == 1:
            self.remove_team()
            number_teams -= 1

    def make_rooms(self):
        if self.vpi_pref is not None:
            for team_group in self.teams:
                if random.sample(team_group, 1).skill == self.vpi_pref:
                    while len(team_group) >= 4:
                        self.make_rooms_full(team_group)
        group_number = 0
        for team_group in self.teams:
            while len(team_group) >= 4:
                self.make_rooms_full(team_group)
            if len(team_group) != 0 and group_number < 3:
                for team in team_group:
                    self.teams[group_number + 1].add(team)
                    team_group.remove(team)
            # Judgement call that half rooms should be novs
            elif len(team_group) != 0 and group_number == 3:
                self.make_rooms_half(team_group)
            group_number += 1
        while len(self.judges) > 0:
            judge = random.sample(self.judges, 1)
            room = random.sample(self.sorted_rooms, 1)
            room.judges.add(judge)
            self.judges.remove(judge)

    # Helper functions
    # TODO: break out to 2nd file

    def remove_team(self):
        # Judgement call on order of removal
        if len(self.teams_pro) > 0:
            group = self.teams_pro
        elif len(self.teams_nov) > 0:
            group = self.teams_nov
        elif len(self.teams_proam) > 0:
            group = self.teams_proam
        elif len(self.teams_adv) > 0:
            group = self.teams_adv
        team = random.sample(group, 1)
        group.remove(team)

    def add_team(self, team: Team):
        if team.skill == TeamSkill.WORLDS:
            group = self.teams_adv
        elif team.skill == TeamSkill.PRO:
            group = self.teams_pro
        elif team.skill == TeamSkill.PROAM:
            group = self.teams_proam
        elif team.skill == TeamSkill.NOV:
            group = self.teams_nov
        if team not in group:
            group.add(team)

    def create_team(self, d1: Debater, g1: Set(Debater), d2: Debater, g2: Set(Debater)):
        team = Team(d1, d2)
        g1.remove(d1)
        g2.remove(d2)
        self.add_team(team)

    def create_team_random(self, g1: Set(Debater), g2: Set(Debater)):
        d1 = random.sample(g1, 1)
        g1.remove(d1)
        d2 = random.sample(g2, 1)
        g2.remove(d2)
        team = Team(d1, d2)
        self.add_team(team)

    def handle_proam(self):
        if len(self.debaters_pro) < len(self.debaters_nov):
            length = len(self.debaters_pro)
        else:
            length = len(self.debaters_nov)
        for counter in range(length):
            self.create_team_random(self.debaters_pro, self.debaters_nov)

    def make_rooms_full(self, team_group: Set(Team)):
        while len(team_group) >= 4:
            room = random.sample(self.rooms, 1)
            self.rooms.remove(room)
            room.og = random.sample(team_group, 1)
            team_group.remove(room.og)
            room.oo = random.sample(team_group, 1)
            team_group.remove(room.oo)
            room.cg = random.sample(team_group, 1)
            team_group.remove(room.cg)
            room.co = random.sample(team_group, 1)
            team_group.remove(room.co)
            room.full = True
            judge = random.sample(self.judges)
            self.judges.remove(judge)
            room.judges.add(judge)
            room.calc_status()
            self.sorted_rooms.add(room)

    def make_rooms_half(self, team_group: Set(Team)):
        while len(team_group) >= 2:
            room = random.sample(self.rooms, 1)
            self.rooms.remove(room)
            room.og = random.sample(team_group, 1)
            team_group.remove(room.og)
            room.oo = random.sample(team_group, 1)
            team_group.remove(room.oo)
            room.half = True
            judge = random.sample(self.judges)
            self.judges.remove(judge)
            room.judges.add(judge)
            room.calc_status()
            self.sorted_rooms.add(room)
