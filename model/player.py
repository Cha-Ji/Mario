
class Player:
    def move(self, vrx, vry, swt):
        pass

    def get_changed_color(self, vrx, vry, swt):
        return [ 0 if vrx > 500 else 255, 0 if vry > 500 else 255, 0 if swt > 500 else 255]

    
