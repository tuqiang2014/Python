from sys import exit
from random import randint

class Scene(object):
	print ("and enter().")
	exit(1)
		
class Engine(object):
	def _int_(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print ("\n=========")
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene_name(next_scene_name)
			
class Death(Scene):

	quips = [
		"You died1. ",
		"You died2. ",
		"You died3. ",
		"You died4. "
	]
		
	def enter(self):
		print (Dead.quips[randint0, len(self.quips)-1])
		exit(1)

class CenteralCorridor(Scene):
	def enter(self):
		print ("The Gothons of Planet Pecal #25have invaded your ship and deatroyed.")
		
		action = input(">")
		
		if action == "shoot!":
			print ("Quick on the draw you yank out your blaster and fire it at the Gothons")
			return 'death'
		elif action == "dodge!":
			print ("Like a worle class boxs you dodge ,weave silp and slide right")
			return 'death'
		elif action == "tell a joke":
			print ("Lucky for you !!")
			return 'lasser_weapon'
			
		else:
			print ("DOES NOT COMPITE")
			return 'centeral_corrdor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print ("You do a dive roll.")
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = input("[keypad]>")
		guesses = 0
		
		while guess != code and gusses < 10:
			print ("BZZZEDD")
			guesse += 1
			guess = input("[keypad]>")
			
		if guess == code:
			print ("The container clicks open and the seal")
		else:
			print ("The lock buzzes one last time and then you hear a sickening")
			return 'death'
			
class TheBrindge(Scene):
	def enter(self):
		print ("You burst onto the Bridge with the netron destruct bomb")
		
		action = input(">")
		
		if action == "throw the bomb":
			print ("In a panic you throw the bomb at the group of Gothons")
			return 'death'
			
		elif action == "slowly place the bomb":
			print ("You point your blaster at the bomb under you arm")
			return 'escape_pod'
		else:
			print ("DOES NOT COMPUTE")
			return "the_bridge"
			
class EscapePod(Scene):

	def enter(self):
		print ("YOu rush through the ship desperately trying to make it to ")
		
		good_pod = randint(1,5)
		gess = input("[pod #]>")
		
	if int(guess) != good_pod:
		print ("You jump into pod %s") % guess
		return 'death'
		
	else:
		print ("You jump into pod %s and hit hthe eject button ")% guess
		return 'finished'
		
class Map(object):

	scenes = [
		'centeral_corrdor': CenteralCorridor(),
		'lasser_weapon': LaserWeaponArmory(),
		'the_bridge': TheBrindge(),
		'escape_pod': EscapePod(),
		'death': Dead()
	]
	
	def  _int_(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name)
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)