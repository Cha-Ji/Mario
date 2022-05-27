class Field:
    def __init__(self, maps):
        self.maps = maps
        self.cur_index = 0

    def move_front(self, distance):
        self.cur_index = (self.cur_index + distance) % len(self.maps)

    def move_back(self, distance):
        self.cur_index = (self.cur_index - distance + len(self.cur_index) % len(self.maps)



