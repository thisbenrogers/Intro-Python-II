# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
class Player():
    def __init__(self, current_room, carrying=None):
        self.current_room = current_room
        self.carrying = carrying

        if not self.carrying:
            self.carrying = []

    def __str__(self):
        return f'Player location: {self.current_room}, carrying items: {self.carrying}'