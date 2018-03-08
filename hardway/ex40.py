class Song(object):

	def _init_(self,lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print (line)
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there" ])
				
bulls_on_parads = Song(["Tyey tally around the family",
						"whth pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parads.sing_me_a_song()