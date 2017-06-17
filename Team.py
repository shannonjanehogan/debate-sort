import Debater
import TeamSkill


class Team:

    def __init__(self, debater_one: Debater, debater_two: Debater):
        self.debater_one = debater_one
        debater_one.team = self
        self.debater_two = debater_two
        debater_two.team = self
        self.name = self.debater_one.name + "/" + self.debater_two.name
        self.skill = None

    def __eq__(self, other):
        return isinstance(other, Team) and ((self.debater_one == other.debater_one and
                                             self.debater_two == other.debater_two) or
                                            (self.debater_one == other.debater_two and
                                             self.debater_two == other.debater_one))

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.name)

    #TODO: Skillz