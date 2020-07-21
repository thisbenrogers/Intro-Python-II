# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, current_room, carrying=None):
        if carrying is None:
            carrying = []
        self.current_room = current_room
        

    def __str__(self):
        return f'Player location: {self.current_room}, carrying items: {self.carrying}'