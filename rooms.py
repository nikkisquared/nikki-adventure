# TODO: West exit from room 5, South exit from room 6, East exit from room 8, rooms 14-16

# empty room, fill in room_X, exits = {'N':X} etc, ROOM X!
# self.exits is a dict of directions, and rooms they lead too if chosen
class room_(object):

	def __init__(self):
		self.exits = {}

	def entry(self):
		return "EMPTY! ROOM !"

	def room(self, l):

		if l in self.exits: return True

class room_1(object):

	def __init__(self):
		self.exits = {'N':'2', 'E':3, 'S':4, 'W': 'Empty'}

	def entry(self):
		return "You are standing in the middle of a FIELD."

   	def room(self, l):

   		if l == 'W':
   			print "You stumble around in darkness and accidently fall off a cliff. Oops."
   			return 'DEATH'
   		elif l == 'N': print "You start heading NORTH. The rumbling noises get louder. It feels very hot!"
   		elif l == 'E': print "You walk towards the CASTLE to the EAST."
   		elif l == 'S': print "You walk SOUTH and soon find a small entrance to a CAVE. Seeing nothing else around you walk in."
   		if l in self.exits: return True

   		elif l == 'LOOK FIELD': print "There is a signpost here labeled with four signs, NORTH, EAST, SOUTH, and WEST. To the NORTH you can hear distant rumbling. To the EAST looms a giant CASTLE. A putrid stench is coming from the SOUTH. You can't see much to the WEST, just some TREES shrouded in complete darkness."
		elif l == 'LOOK CASTLE': print "The stonework is very impressive. You've always wanted to have your own CASTLE. Maybe you can today!"
		elif l == 'LOOK TREES': print "You don't see anything special about the TREES. In fact you don't see a single thing! It is far too dark. Maybe if you got closer you could find out why."
		elif l == 'LOOK TREE': print "There are hundreds of TREES here, you can't possibly inspect all of them!"

class room_2(object):

	def __init__(self):
		self.exits = {'S':1,'N':'?'}
		self.bridge = False

	def entry(self):
		return "You stand on the edge of a wide MOAT full of dangerous LAVA. It seems you are just outside a VOLCANO. It's boiling in here!"

	def room(self, l):

		if l == 'N' and self.bridge == False:
			print "You can't get across the LAVA MOAT that easily!"
			return False
		elif l == 'S':
			print "You decide to get out of here before you melt, and head back SOUTH."
			return True

		elif l == 'LOOK LAVA': print "On closer in spection, the LAVA seems like it could actually just be very hot CHILI! You feel a sudden urge to SWIM around in it."
		elif 'CHILI' in l: print "Even if this MOAT is full of CHILI, you doubt it would be as good eating as your mom's CHILI. Oh, how great her cooking was! Too bad a bowl of her famous CHILI was cursed by a jealous wizard and it ate her."
		elif l == 'LOOK MOAT': print "The LAVA MOAT stretches on to either end up to a high rock WALL. There is no way around!"
		elif l == 'LOOK WALL': print "A sheer 90 degree angle, straight up at least 500 feet until it reaches ground you could stand on. Even if you had your Deckers Brand Extreme Climbing Equipment, you would feel uneasy about trying to scale such a beast."
		elif l == 'LOOK VOLCANO': print "You can't see the VOLCANO so much as hear and feel it. It must be quite an old VOLCANO for this outer LAVA MOAT to exist. That or somebody built this themselves!"
		elif l == 'LOOK LAVA MOAT': print "A MOAT would be bad enough, but a MOAT filled with LAVA? Even if you could build a bridge over this it would melt!"
		elif 'SWIM' in l:
			print "You try to SWIM to the other side. Whether it's really LAVA or CHILI doesn't matter because it burns you to a crisp."
			return 'DEATH'

class room_3(object):

	def __init__(self):
		self.exits = {'W':1, 'E':5}
		self.grateOpen = False

	def entry(self):
		return "The GATE of a massive CASTLE stands before you. The GRATE is closed shut, without any way of opening it from here."

	def room(self, l):

		if l == 'E': 
			if self.grateOpen == False:
				print "You bump your head into the closed GRATE. Idiot!"
				return False
			elif self.grateOpen: print "You run past the GRATE! WHAM! It slams shut right behind you! Whew, that was a close one!"
		elif l == 'W': print "You are bored of standing around outside a CASTLE and head WEST."
		if l in self.exits:
			self.grateOpen = False
			return True

		elif self.grateOpen:
			print "BAM! The GRATE slams shut right in front of you. The person holding it up for you must not be very strong. That or they hate you! You should move faster if you want to get past."
			self.grateOpen = False

		elif l == 'LOOK GRATE': print "How could you get this GRATE open? You don't see anybody around who could operate it. Maybe if you yelled somebody would hear you."
		elif l == 'LOOK GREAT': print "Look at GREAT what?"
		elif 'YELL' in l:
			print "You yell towards the GRATE hoping somebody hears you. It slowly moves upwards. Looks like you're in luck!"
			self.grateOpen = True
		elif l == 'OPEN GRATE': print "There is no way to open it from this side!"
		elif l == 'LOOK GATE': print "What an astounding work of art! You hope your own CASTLE could have a GATE as magnificent."
		elif l == 'LOOK CASTLE': print "If you could marry a CASTLE you would do so right now. Except you can't. And the castle doesn't belong to you. You're kind of weird."
		elif l == 'TAKE CASTLE': print "As if!"
		elif l == 'LOOK BAM': print "There is no BAM here, fortunately! You wouldn't be alive still if there was. A horde of BAMS once destroyed your village. Oh god, the BAMS were everywhere!"
		elif 'BAMS' in l: print "No, please! Not the BAMS!"

class room_4(object):

	def __init__(self):
		self.exits = {'N':1, 'W':6}
		self.trollGuarding = True

	def entry(self):
		return "You are inside a dark CAVE. You notice an odd SMELL. A giant TROLL holding a dangerous looking CLUB stands in front of a large oak DOOR on the WEST side of the room."

	def room(self, l):

		if l == 'N': print "CAVES and TROLLS are so overdone! You go back NORTH."
		elif l == 'W':
			if self.trollGuarding:
				print "The TROLL doesn't like your sudden movement and crushes you flat with his CLUB."
				return 'DEATH'
			else: "The TROLL steps aside for you. After a few minutes of effort you manage to push open the heavy DOOR and walk through to the WEST."
		if l in self.exits: return True

		elif l == 'LOOK TROLL': print "The TROLL, despite his massive size, does not look very threatening. His CLUB on the other hand, does. Judging by how the troll is wearing glasses and reading a thick-bound copy of The Most Perplexing Works by Charles Chuck Hats, he is probably more approachable than the average troll."
		elif l == 'TALK TROLL':
			print "The TROLL responds to your greeting. He informs you that he was ordered to guard this door from any intruders. You look too weak to be much of a threat. He moves aside to let you through the door."
			self.trollGuarding = False
		elif l == 'LOOK CAVE': print "CAVES sure are common, but you have never seen one such as this. It seems human-made, or possibly even creature made, considering the TROLL."
		elif l == 'LOOK CAVES': print "There is only one CAVE here!"
		elif l == 'LOOK DOOR': print "The DOOR seems to be made out of a good solid oak. Just from the size of the DOOR you imagine it must weigh a ton. Maybe the TROLL is here to open it for people, rather than guard it."
		elif l == 'LOOK CLUB': print "Yikes! That CLUB looks scary. It's full of huge spikes and sharp nails and annoying thumbtacks."
		elif l == 'TAKE CLUB': print "Not a chance buddy!"
		elif 'SMELL' in l: print "A rank SMELL seems to emenating from the WEST. You're not sure if you want to find the source."

class room_5(object):

	def __init__(self):
		self.exits = {'N':7, 'E':8, 'W':3}
		self.grateOpen = False

	def entry(self):
		return "You take in the CASTLE entrance surrounding you. It looks even better than it does on the OUTSIDE. You notice some TORCHES along the wall."

	def room(self, l):

		if l == 'W' and self.grateOpen == False:
			print "You can't walk through a GRATE, geeze!"
			return False
		elif l == 'N': print "You walk on through the castle down a large HALLWAY."
		elif l == 'E': print "Heading EAST, you find yourself outside a looming VAULT DOOR."
		if l in self.exits: return True

		elif l == 'LOOK CASTLE': print "Just look at that lovely stonework! You can't resist rubbing your hands all over the floor and walls."
		elif l == 'LOOK OUTSIDE': print "Where you used to be. But that's the old you. This is the new you. The you that lives inside a castle. Well, you don't know how you could manage to live here. Maybe your servants can bring you food."
		elif l == 'LOOK TORCHES': print "They're burning nicely. You don't see anybody around, so why not take some while you're here?"
		elif 'TAKE' in l and 'TORCH' in l:
			print "You reach for a torch, but the moment you do it falls out of it's wall socket, and sets fire to your clothes! Within minutes nothing remains but a heap of ash. Your dreams of owning a castle will never be realized."
			return 'DEATH'
		elif l == 'LOOK WHAM': print "You can't look at an onomatopoeia!"
		elif l == 'LOOK GRATE': print "There doesn't seem to be any way of raising the GRATE from here. There must be another room with the lifting mechanism above you."

class room_6(object):

	def __init__(self):
		self.exits = {'E':4}
		self.dragonAttack = True

	def entry(self):
		if self.dragonAttack: return "The moment you enter the room, you feel a great blast of HEAT. You notice a particularly large ROCK. The SMELL in here is awful! Suddenly you see a DRAGON swooping down from the roof at you! Think fast!"
		else: return "The air feels COLD in here. You see a broken ROCK, with a dead DRAGON laying on it. A strong, horrible SMELL is present."

	def room(self, l):

		if self.dragonAttack and 'ROCK' not in l:
			print "Before you can finish your action, the DRAGON opens it mouth and lets loose a torrent of fiery death."
			return 'DEATH'
		elif self.dragonAttack:
			print "You quickly run behind the ROCK for safety. The DRAGON tries to ram you, but ends up smashing head first into the ROCK. It gives out a yell of pain. The room starts to feel COLD."
			self.dragonAttack = False

		if l == 'E': print "With the rotting dragon it smells just awful in here. You head back EAST."
		if l in self.exits: return True

		elif l == 'LOOK ROCK': print "Broken shards of what once used to be a great boulder."
		elif l == 'LOOK DRAGON': print "It was a vicious beast in life, but a stupid one. Did it really think it could fly through the ROCK?"
		elif 'COLD' in l: print "Brrr! The DRAGON must have been heating the place up when it was alive."
		elif 'HEAT' in l: print "It's rather COLD in here now, actually."
		elif 'SMELL' in l: print "Pehew! You don't notice any source of the SMELL in here, besides the newly deceased DRAGON, but a much worse stench is coming from the SOUTH end of the room."

class room_7(object):

	def __init__(self):
		self.exits = {'S':5, 'N':9}

	def entry(self):
		return "This HALLWAY is massive! You can barely make out the doors at either end. Large TAPESTRIES are spread along the walls."

	def room(self, l):

		if l == 'S': print "This HALLWAY is big, confusing, and boring. Maybe something more exciting is in the SOUTH."
		if l == 'N': print "Not one for standing around, you head up NORTH."
		if l in self.exits: return True

		if l == 'LOOK HALLWAY': print "Wow! This place is a lot bigger than you could see on the outside. It'll probably take a while for you to get aquainted with the whole place."
		elif l == 'LOOK TAPESTRY': print "Which one? There are many TAPESTRIES!"
		elif l == 'LOOK TAPESTRIES':
			print "There are so many of these beautiful TAPESTRIES! There must be at least a hundred. You walk up to the one closest to you, a masterpiece weaving depicting a kingly figure, probably a previous owner of the CASTLE. Since you'll be the only king around here soon enough, you decide to get rid of the TAPESTRY to make room for your self portrait later."
			print "Unfortunately it's a lot heavier than it looked! You are trapped under the TAPESTRY! Nobody hears your yells for help, and a few hours later you die of suffocation."
			return 'DEATH'
		elif l == 'LOOK CASTLE': print "You're inside it!"

class room_8(object):

	def __init__(self):
		self.exits = {'W':5}

	def entry(self):
		return "You are inside a thin, but tall VAULT entrance room. Two GUARDS stand on watch."

	def room(self, l):

		if l == 'W': print "Without a way in there's no point in being here. You head on back WEST."
		if l in self.exits: return True

		if l == 'LOOK GUARD': print "Which one? LEFT GUARD or RIGHT GUARD?"
		elif l == 'LOOK GUARDS': print "One GUARD stands to the LEFT side of the VAULT DOOR, another  to the RIGHT side. Neither of them pay any attention to you. Despite this you have no doubt they would be quick to run you through if you got any closer to the VAULT."
		elif 'LOOK' in l and 'LEFT' in l: print "The GUARD to the LEFT seems a lot more composed than his companion. You get the feeling if you want to have a meaningful conversation he's the one you should TALK to."
		elif 'LOOK' in l and 'RIGHT' in l: print "This GUARD unnerves you! He keeps a fierce eye upon you, and occasionally taps his hand on the hilt of his sword. You don't want to draw any more attention from him."
		elif l == 'TALK GUARD' or l == 'TALK GUARDS' : print "Talk to the LEFT GUARD or the RIGHT GUARD?"
		elif 'TALK' in l and 'LEFT' in l: 
			print "\"Why hello there! I didn't notice you come in. You must be the new food boy. Where's my lunch?\""
			print "You quickly say that he is mistaken, you are not working here."
			print "\"You must be a guest of the KING than! The inside of this here VAULT is completely offlimits, by order of the KING. You may go where you please within the rest of the CASTLE however.\""
		elif 'TALK' in l and 'RIGHT' in l:
			print "\"AAAAA I KNEW IT!!! INTRUDER!!! INTRUDER!!!\""
			print "The GUARD pulls out his sword and runs at you screaming. You don't even have time to move before he hacks you apart."
			return 'DEATH'
		elif l == 'LOOK VAULT' or l == 'LOOK VAULT DOOR': print "A massive circle made of steel and gold. Giant latches line the top of it. About two dozen key holes are placed around it, every one a unique shape. You know a bit of lockpicking, but trying to get in here, nevermind the GUARDS, would take months."
		elif l == 'LOOK KING': print "The KING isn't in this room!"
		elif l == 'LOOK CASTLE': print "You forgot you were in one! The VAULT is just so magnificent."

class room_9(object):

	def __init__(self):
		self.exits = {'S':7}
		self.kingIn = True
		self.NExitFound = False

	def entry(self):
		if self.kingIn: return "You stand before a large THRONE. In it sits somebody who must be the KING of the CASTLE. Nobody else is present."
		else: return "You stand before a large THRONE. Nobody but you is present."

	def room(self, l):

		if l == 'S': print "As there doesn't seem to be anything more here, you head back SOUTH."
		elif l == 'N' and self.NExitFound: print "Figuring you might find a way to open the GRATE through here, you go through the secret door to the NORTH. You make sure to close it behind you."
		if l in self.exits: return True

		if l == 'LOOK THRONE' and self.kingIn: print "A mighty throne! Perfect for sitting in while yelling at people. Currently a large KING is filling up the entirety of it."
		elif l == 'LOOK THRONE' and self.kingIn == False and self.NExitFound == False: 
			print "Since the KING isn't around, you decide to take a closer look. You walk up to it to sit in it, but before you do you notice something previously hidden by the massive size of the THRONE. There's a concealed door behind it!"
			self.exits['N'] = 10
			self.NExitFound = True
		elif l == 'LOOK THRONE':
			print 'You pretend to be the KING and take a seat in the THRONE. "Oppress the proletariats! Make me a bigger throne! Bring me a cooked dragon!"'
			print "Suddenly the KING bursts back into the room, with two GUARDS behind him. He must have heard your shouting. Uh oh! The GUARDS knock you out, and you wake up in a cell. The PRISON WARDEN happily tells you that you will be executed at dawn for mocking the KING."
			return 'DEATH'
		elif l == 'LOOK KING' and self.kingIn: print "An impressive figure, the KING is large and looming. He seems ready to send off any annoying visitor to their death. He doesn't seem to have noticed you yet, as he is engrossed in writing something down."
		elif l == 'LOOK KING': print "He isn't in here anymore!"
		elif l == 'TALK KING' and self.kingIn:
			print "You say a greeting to the KING."
			print '"Oh!" The KING puts down the paper he was writing on. "You must be the new knight in training! I\'ll find your teacher and bring him over here, the bloody fool seems to be nowhere around when he\'s actually needed."'
			print "The KING picks up the piece of paper and heads out the door to the SOUTH."
			self.kingIn = False
		elif l == 'LOOK CASTLE': print "If you could figure out how to impersonate the KING, this could all be yours!"

class room_10(object):

	def __init__(self):
		self.exits = {'S':9, 'N':11}

	def entry(self):
		return "You stand within a short, poorly lit CORRIDOR. COBWEBS are around the walls. It doesn't look like people come back here often. You should move on before somebody catches you."

	def room(self, l):

		if l == 'S': print "This place gives you the creeps. You head back SOUTH to a normal room."
		elif l == 'N': print "You don't let the darkness get the better of you. What's the worse that could be in here?"
		if l in self.exits: return True
		else:
			print "Suddenly, the KING bursts through the DOOR to the SOUTH and starts yelling for his GUARDS. You should've left while you had the chance! The KING sentences you to death for intruding his personal quarters or whatever this room is."
			return 'DEATH'

class room_11(object):

	def __init__(self):
		self.exits = {'S':10, 'W':12}

	def entry(self):
		return "You find yourself in an even darker room. You realize why these rooms are so hidden. This must be where the KING interrogates prisoners! Awful TOOLS line the walls. You feel an urge to leave immediately."

	def room(self, l):

		if l == 'S': 
			print "No way. If you're this far into this hidden dungeon, you'd rather find a back exit than risk running into somebody."
			return False
		elif l == 'N': print "You head NORTH, not knowing what to expect."
		if l in self.exits: return True

		elif l == 'LOOK TOOLS': print "I'd rather not."
		elif l == 'LOOK KING': print "He's not in here! Thankfully. You don't know what he would do if he was."

class room_12(object):

	def __init__(self):
		self.exits = {'E':11, 'S':14, 'N':13}

	def entry(self):
		return "You stand in a large corridor, with many CELLS lining the walls. This must be where PRISONERS of the CASTLE are kept!"

	def room(self, l):

		if l == 'E': 
			print "You'd rather not go back into that terrible room."
			return False
		elif l == 'N': print "You head NORTH."
		elif l == 'S': print "Hoping for an exit, you wander SOUTH."
		if l in self.exits: return True

		elif l == 'LOOK BARS': print "Cruel pieces of iron, taunting any PRISONERS with a sight of the outside while stopping them from reaching it."
		elif l == 'LOOK CELLS': print "Made up of pure rock on five sides, and a line of BARS on the last. The standard CELL seems to hold a rough rock bed and a privacy-less toilet."
		elif l == 'LOOK CELL': print "Which one!? There's about twenty in here, and none of them look particularly special."
		elif l == 'LOOK PRISONERS': print "There aren't any PRISONERS in here, currently. If anybody finds you here you will most likely become one."
		elif l == 'LOOK CASTLE': print "You never thought such horrible things would be hidden within this CASTLE. You take back your wish of owning it."

class room_13(object):

	def __init__(self):
		self.exits = {'S':12, 'N':16, 'W':15}
		self.wardenIn = True

	def entry(self):
		if self.wardenIn: return "You are in another part of the PRISON. The CELLS in seem to be for special containment. One CELL to the WEST of you has some FURNITURE in it. Suddenly, you hear a door open to the NORTH! What appears to be the PRISON WARDEN is walking down! He hasn't noticed you yet."
		else: "You are in another part of the PRISON. The CELLS in seem to be for special containment. One CELL right beside you currently has some FURNITURE in it."

	def room(self, l):

		if self.wardenIn:
			if l == 'N': 
				print "You walk up to the PRISON WARDEN. He is so unsuspecting of your presence that you bump into him. The WARDEN explodes into a rage at your intrusion, and knocks you over the head. You wake up within in a CELL, where you live the rest of your miserable life."
				return 'DEATH'
			elif l == 'S' or l == 'TALK WARDEN': 
				print "You run to the SOUTH as silently as you can, but before you reach the door you trip over a piece of stone. The PRISON WARDEN hears the noise and runs over to you. He picks you up and quickly asks what you are doing here. You lie and say that you are the new knight in training, and were just walking around. The WARDEN doesn't believe you and shoves you into a CELL. You spend the rest of your life within the small, crushing walls."
				return 'DEATH'
			elif l == 'W' or 'CELL' in l: 
				print "You walk into the CELL to the WEST and hide underneath the TABLE within it. The PRISON WARDEN walks by a moment later and peers inside. You worry that he can see you, but he turns away, and you give a sigh of relief. It's cut short however as the WARDEN closes and locks the CELL DOOR!"
				print "The PRISON WARDEN mumbles to himself, \"That damn janitor left this CELL open, didn't he? I know he's up to something! If I could have my way he would have been locked up here years ago.\""
				print "It doesn't look like you'll be getting out of here anytime soon!"
				self.wardenIn = False
			else:
				print "You have to move before the PRISON WARDEN sees you!"
				return False
		else:
			if l == 'W': print "You duck back into the CELL, just in case the PRISON WARDEN is making another round."
			elif l == 'N': print "You continue past many CELLS to the NORTH door."
			elif l == 'S': print "Having had enough of prison for one day, you go back SOUTH."
		if l in self.exits: return True

		elif 'LOOK' in l and 'WARDEN' in l: print "The PRISON WARDEN is not in here right now, but if he was you wouldn't be standing around looking right at him."
		elif l == 'LOOK PRISON': print "A horrible collection of CELLS. Who knows how many people who only annoyed the KING have lived the rest of their lives here?"
		elif l == 'LOOK CELLS': print "Not as many CELLS in here as the other section. Most of these CELLS are much larger. Maybe mythical monsters are kept in here."
		elif l == 'LOOK CELL': print "There are many, many CELLS in here!"

class room_14(object):

	def __init__(self):
		self.exits = {'N':12, 'S':17}

	def entry(self):
		return "EMPTY! ROOM 14!"

	def room(self, l):

		if l in self.exits: return True

class room_15(object):

	def __init__(self):
		self.exits = {'E':13}
		self.foundWest = False

	def entry(self):
		return "EMPTY! ROOM 15!"

	def room(self, l):

		if l in self.exits: return True

class room_16(object):

	def __init__(self):
		self.exits = {'S':13, 'N':19}

	def entry(self):
		return "EMPTY! ROOM 16!"

	def room(self, l):

		if l in self.exits: return True

class room_17(object):

	def __init__(self):
		self.exits = {'W':18, 'S':'X', 'N':14}

	def entry(self):
		return "EMPTY! ROOM 17!"

	def room(self, l):

		if l in self.exits: return True

class room_18(object):

	def __init__(self):
		self.exits = {'S':2, 'E':17}

	def entry(self):
		return "EMPTY! ROOM 18!"

	def room(self, l):

		if l in self.exits: return True

class room_19(object):

	def __init__(self):
		self.exits = {'S':16}

	def entry(self):
		return "EMPTY! ROOM 19!"

	def room(self, l):

		if l in self.exits: return True

class room_20(object):

	def __init__(self):
		self.exits = {'E':15}

	def entry(self):
		return "EMPTY! ROOM 20!"

	def room(self, l):

		if l in self.exits: return True