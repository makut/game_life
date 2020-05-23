class CellToString(type):
    pass


class Cell(metaclass=CellToString):
    @classmethod
    def count_similar(cls, neighbours):
        return neighbours.count(cls)

    @classmethod
    def next_type(cls, neighbours):
        cnt = cls.count_similar(neighbours)
        if cnt >= 4 or cnt < 2:
            return EmptyCell
        return cls

    @classmethod
    def update_empty(cls, neighbours):
        return cls.count_similar(neighbours) == 3


class FishToString(CellToString):
    def __repr__(self):
        return 'F'


class Fish(Cell, metaclass=FishToString):
    pass


class CrayFishToString(CellToString):
    def __repr__(self):
        return 'C'


class CrayFish(Cell, metaclass=CrayFishToString):
    pass


class RockToString(CellToString):
    def __repr__(self):
        return '#'


class Rock(Cell, metaclass=RockToString):
    @staticmethod
    def next_type(neighbours):
        return Rock

    @staticmethod
    def update_empty(neighbours):
        return False


class EmptyCellToString(CellToString):
    def __repr__(self):
        return '.'


class EmptyCell(Cell, metaclass=EmptyCellToString):
    @staticmethod
    def next_type(neighbours):
        for cell_type in PRIORITY:
            if cell_type.update_empty(neighbours):
                return cell_type

    @staticmethod
    def update_empty(neighbours):
        return True


PRIORITY = [Fish, CrayFish, Rock, EmptyCell]
