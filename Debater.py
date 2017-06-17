import Status
import DebaterSkill


class Debater:

    def __init__(self, name: str, status: Status, skill: DebaterSkill, partner_pref: str):
        self.name = name
        self.status = status
        self.partner_pref = partner_pref
        self.skill = skill
        self.team = None

    def __eq__(self, other):
        return isinstance(other, Debater) and self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.name)
