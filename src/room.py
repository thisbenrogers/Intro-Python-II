# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        desc = "\n".join(textwrap.wrap(self.description))
        return f'\n{self.name}\n{desc}'