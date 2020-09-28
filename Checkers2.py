from scene import *
import numpy as np
import sound

class Board(SpriteNode):
	def __init__(self):
		SpriteNode.__init__(self, 'board.png')
		self.checkers = []
		self.valid_locations = [(144, 176), (336, 176), (528, 176), (720, 176),
								(48, 272), (240, 272), (432, 272), (624, 272),
								(144, 368), (336, 368), (528, 368), (720, 368),
								(48, 464), (240, 464), (432, 464), (624, 464),
								(144, 560), (336, 560), (528, 560), (720, 560),
								(48, 656), (240, 656), (432, 656), (624, 656),
								(144, 752), (336, 752), (528, 752), (720, 752),
								(48, 848), (240, 848), (432, 848), (624, 848)]



		for i in range(len(self.valid_locations)):
			if i > 11 and i < 20:
				continue
			self.checkers.append(Checker(i, self.valid_locations[i]))


class Checker(SpriteNode):
		def __init__(self, number, position):
			self.king = False
			if number < 12:
				SpriteNode.__init__(self, 'red.png')
				self.position = position
			else:
				SpriteNode.__init__(self, 'black.png')
				self.position = position


class Game(Scene):
	def setup(self):
		self.background_color = 'orange'
		self.board = Board()
		self.turn = 0
		self.board.position = self.size/2
		self.selected = -1
		self.add_child(self.board)
		for i in self.board.checkers:
			self.add_child(i)

	def touch_began(self, touch):
		for i in range(len(self.board.checkers)):
			if self.board.checkers[i].frame.contains_point(touch.location):
				self.selected = i
				return None
		x,y= touch.location
		move_action = Action.move_to(x, y, 0.7, TIMING_SINODIAL)
		if self.selected != -1 and ((self.selected < 12 and self.turn == 0) or (self.selected > 11 and self.turn == 1)):
			self.board.checkers[self.selected].run_action(move_action)
			if self.turn == 0:
				self.turn = 1
				sound.play_effect('croissant.mp3')
			else:
				self.turn = 0
				sound.play_effect('carl.mp3')
		print(x,y)

run(Game(), PORTRAIT)
