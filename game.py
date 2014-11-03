from rooms import *

class map(object):
    # log of every room in the game, for easier referencing
    def __init__(self):
        # there is no room 0
        for x in range(1, 21):
            exec 'self.room_%s = room_%s()' % (x, x)

class game(object):
    
    def __init__(self):
        self.m = map()
        print "Welcome to Nikki's Awesome Adventure! I hope you enjoy it! If this is your first time playing, type in HELP.\n"
        
    def play(self, room):
        """keeps restarting the game, but stops if the user quits"""
        while True:
            if getattr(self, 'main')(room) == 'N':
                break

    def main(self, room):
        """runs the game"""
        # user input, initialized here to prevent errors
        line = '' 
        # used for checking if the current room is new
        lastRoom = ''
        
        # loops until user quits or dies
        while True: 

            r = getattr(self.m, 'room_%s' % room) # gets the class for a room
            exits = r.exits # list of possible exits
            entry = getattr(r, 'entry')() # returns text for entering a room
            
            if lastRoom != room or len(line) == 0 or line == 'LOOK':
                 # won't constantly repeat the entry text unless wanted
                print '%s%s' % (entry, getattr(self, 'getExits')(exits.keys()))
            lastRoom = room

            r = getattr(r, 'room') # function for sending input to
            line = getattr(self, 'getInput')()

            if line == 'QUIT':
                if raw_input('Really quit this great game? (y/n)\n> ').startswith('y'):
                    print 'Seeya!'
                    return 'N'
            elif line == 'ROOM':
                # DEBUG OUTPUT
                print room

            # if the user entered an exit
            if getattr(self, 'isExit')(line):
                # cuts down the direction to a single letter
                line = line[0] 
                # room leave msg, and returns bool for leaving or death
                result = r(line) 
                if result and line in exits.keys():
                    room = exits[line]
                    # blank line for spacing
                    print ""
                elif not line in exits.keys():
                    print "That isn't an exit from here!"

            else:
                # room interaction, returns death if occurs
                result = r(line)
            if result == 'DEATH':
                return raw_input('Play again? (y/n)\n> ').upper()

    def getInput(self):
        """gets a line from the user and returns it"""
        # loops again if the user enters a special case
        while True:
            line = raw_input('> ').upper()

            if line == 'HELP':
                # player wants help
                getattr(self, 'help')()
            elif 'LOOK' in line and getattr(self, 'isExit')(line[5:]):
                print('Why yes that is a direction!')
            elif 'BUTT' in line:
                # wow what a rude entry
                print('HOW RUDE!!!!')
            else:
                return line

    def isExit(self, userInput):
        return userInput in ['NORTH', 'N', 'EAST', 'E', 'SOUTH', 'S', 'WEST', 'W']

    def getExits(self, exits, order = 'NESW'):
        """returns a properly formatted list of exists, and can take any order"""
        # starts at 1 because len() does so too
        currExit = 1
        if len(exits) == 1:
            text = ' The only exit is to the '
        else:
            text = ' Exits are to the '

        toUse = ''
        for i in order:
            if i in exits: toUse += i

        for i in toUse:
            if i == 'N': text += 'NORTH'
            elif i == 'E': text += 'EAST'
            elif i == 'S': text += 'SOUTH'
            elif i == 'W': text += 'WEST'
            if (currExit + 1) == len(exits): text += ', and '
            elif currExit < len(exits): text += ', '
            else: text += '.'
            currExit += 1
        return text

    def help(self):
        """prints out a guide to help the player understand how to play"""

        print("This game is similar to the classic text adventure ZORK. It doesn't have quite as much gameplay, it's a project to help me practice making games. This game does not feature a wide syntax or many puzzles, but it does have quite a few rooms\nwith objects and characters you can interact with.\n")
        print("You can try go into one of four directions by entering N (NORTH), E (EAST), S (SOUTH), or W (WEST). You can LOOK around current room, which may give you a clue for any special things you can do. You can also type LOOK THING to examine most anything that is printed in UPPERCASE. Doors and such may be OPENed. If you see a person or creature, TALK to them, and they might give you useful advice. You may TAKE, or at least try to TAKE, some items.\n")
        print("Also, you can type your actions in all UPPERCASE, lowercase, or any MiX Of caSeS you want, it doesn't matter.\n")
        print("If you ever want to leave the game, enter QUIT.")

# launchs the game in room 1
g = game().play('1')