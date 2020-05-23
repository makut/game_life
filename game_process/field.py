from .essences import EmptyCell, Rock, Fish, CrayFish
import copy


class Field:
    SYMBOLS = {'.': EmptyCell, '#': Rock, 'F': Fish, 'C': CrayFish}

    def __init__(self, other):
        '''If other is another Field, then the method works as a copy constructor.
           Otherwise it constructs Field from the table in input format'''
        if type(other) == Field:
            self.data = copy.deepcopy(other.data)
        else:
            self.data = []
            for line in other:
                self.data.append([])
                for c in line:
                    self.data[-1].append(Field.SYMBOLS[c])

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return 0 if self.get_height() == 0 else len(self.data[0])

    def is_valid(self, x, y):
        if x <= -1 or y <= -1:
            return False
        if x >= self.get_height() or y >= self.get_width():
            return False
        return True

    def get_neighbours(self, x, y):
        ans = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx == 0 and dy == 0) or not self.is_valid(x + dx, y + dy):
                    continue
                ans.append(self.data[x + dx][y + dy])
        return ans

    def next_state(self, x, y):
        neighbours = self.get_neighbours(x, y)
        return self.data[x][y].next_type(neighbours)

    def next_generation(self):
        result = [[None] * self.get_width() for i in range(self.get_height())]
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                result[i][j] = self.next_state(i, j)
        self.data = result

    def run(self, iterations):
        for i in range(iterations):
            self.next_generation()

    def __repr__(self):
        lines = [''.join([str(self.data[i][j])
                 for j in range(self.get_width())])
                 for i in range(self.get_height())]
        return '\n'.join(lines)
