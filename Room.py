class Room:

    def __init__(self, name: str):
        self.name = name
        self.og = None
        self.oo = None
        self.cg = None
        self.co = None
        self.half = False
        self.full = False
        self.status = None

    def __eq__(self, other):
        return isinstance(other, Room) and self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.name)
