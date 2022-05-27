class Field:
    def __init__(self, maps = [0, 1, 2, 3]):
        self.maps = maps
        self.cur_index = 0

    def move_front(self, distance):
        self.cur_index = (self.cur_index + distance) % len(self.maps)

    def move_back(self, distance):
        self.cur_index = (self.cur_index - distance + len(self.maps)) % len(self.maps)

    def move(self, distance):
        self.cur_index = (self.cur_index + distance + len(self.maps)) % len(self.maps)



