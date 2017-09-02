from tmtu2_5_0 import *
import sys
from math import sqrt
from random import choice
def gblF_Main():
	Main_screen_ins, Main_clock_ins, Main_info_ary = setup_pygame(size, 'Gravity Game - Main Menu', True)
	# Screen size is (700, 500)

	class MainC_point():
		def __init__(self, info_ary, coords_ary, component_ary, boundaries_2dA=[[0  ,0  ],[700,500]]):
			self.screen_ins,     self.screenSize_ary = info_ary[0],      info_ary[1]
			self.x_flt,          self.y_flt          = coords_ary[0],    coords_ary[1] # x_flt and y_flt are Cartesian coordinates.
			self.xComponent_flt, self.yComponent_flt = component_ary[0], component_ary[1]
			self.boundaries_2dA                      = boundaries_2dA
			self.colour_tup                          = RED

		def draw(self):
			coords = self.convertCoords([self.x_flt, self.y_flt])
			pygame.draw.circle(self.screen_ins, self.colour_tup, [int(coords[0]),int(coords[1])], 5)
			self.move()
			self.checkBoundary()

		def move(self):
			self.x_flt += self.xComponent_flt
			self.y_flt += self.yComponent_flt

		def convertCoords(self, coords_ary):
			return [coords_ary[0], (self.screenSize_ary[1]-coords_ary[1])]

		def checkBoundary(self):
			coords = self.convertCoords([self.x_flt, self.y_flt])
			if coords[0] > self.boundaries_2dA[1][0]:
				self.x_flt = self.convertCoords(self.boundaries_2dA[1])[0]
				self.xComponent_flt *= -1
			elif coords[0] < self.boundaries_2dA[0][0]:
				self.x_flt = self.convertCoords(self.boundaries_2dA[0])[0]
				self.xComponent_flt *= -1
			elif coords[1] < self.boundaries_2dA[0][1]:
				self.y_flt = self.convertCoords(self.boundaries_2dA[0])[1]
				self.yComponent_flt *= -1
			elif coords[1] > self.boundaries_2dA[1][1]:
				self.y_flt = self.convertCoords(self.boundaries_2dA[1])[1]
				self.yComponent_flt *= -1


	def MainF_drawStartMenu():
		# Define inputs
		drawStartMenu_inputs_dic = {
		'Toggle_button'  : {
			'Tutorial'       : Toggle_button(Main_info_ary, [250, 155], [200, 50], [False, GREEN, RED]),
			'Load Level'     : Toggle_button(Main_info_ary, [250, 225], [200, 50], [False, GREEN, RED]),
			'Level Designer' : Toggle_button(Main_info_ary, [250, 295], [200, 50], [False, GREEN, RED]),
			}
		}

		drawStartMenu_buttonFunctions_dic = {
		'Tutorial'       : MainF_tutorial,
		'Load Level'     : MainF_loadLevel,
		'Level Designer' : MainF_levelDesigner,
		}

		

		# Keep looping until break
		while True:
			for event in pygame.event.get():
				for key, value in drawStartMenu_inputs_dic['Toggle_button'].items():
					value.detect(event)

				if event.type == pygame.QUIT:
					pygame.quit()

			Main_screen_ins.fill(GREY_1)
			for key, value in drawStartMenu_inputs_dic['Toggle_button'].items():
					value.draw(key)
					if value.state == True:
						try:
							drawStartMenu_buttonFunctions_dic[key]()
						except:
							pass

			

			flip()
			Main_clock_ins.tick(60)

	def MainF_tutorial():
		tutorial_screen_ins, tutorial_clock_ins, tutorial_info_ary = setup_pygame((900,550), 'Gravity Game - Tutorial Levels', True)

		tutorial_inputs_dic = {
		'Toggle_button' : {
			'<- Back' : Toggle_button(tutorial_info_ary, [0  ,0], [150,50], [False, GREEN, RED]),
			'Menu'    : Toggle_button(tutorial_info_ary, [275,0], [150,50], [False, GREEN, RED]),
			'Next ->' : Toggle_button(tutorial_info_ary, [550,0], [150,50], [False, GREEN, RED]),
			}
		}

		tutorial_buttonFunctions_dic = {
		'Menu' : gblF_Main,
		}


		while True:
			for event in pygame.event.get():
				for pkey, pvalue in tutorial_inputs_dic.items():
					for key, value in pvalue.items():
						value.detect(event)

				if event.type == pygame.QUIT:
					pygame.quit()

			tutorial_screen_ins.fill(GREY_1)
			# Drawing
			pygame.draw.line(tutorial_screen_ins, BLACK, (0, 50),(700, 50),3)
			pygame.draw.line(tutorial_screen_ins, BLACK,(700, 0), (700, 550),3)
			pygame.draw.rect(tutorial_screen_ins, BLACK, (0,0,900,550), 3)

			for key, value in tutorial_inputs_dic['Toggle_button'].items():
				value.draw(key)

			for key, value in tutorial_inputs_dic['Toggle_button'].items():
				value.draw(key)
				if value.state == True:
					try:
						tutorial_buttonFunctions_dic[key]()
					except:
						pass

			MainF_drawText(tutorial_info_ary, [800,50], 'Select Element', True)

			flip()
			tutorial_clock_ins.tick(60)

	def MainF_loadLevel():
		pass

	def MainF_levelDesigner():

		# Items tab
		def levelDesignerF_drawItemsTab():
			for key, value in levelDesigner_inputs_dic['Items'].items():
				value.draw(key)

		# Text tab
		def levelDesignerF_drawTextTab():
			pass

		def levelDesignerF_delFunc():
			for key, value in levelDesigner_inputs_dic['Items'].items():
				value.state = False


		levelDesigner_screen_ins, levelDesigner_clock_ins, levelDesigner_info_ary = setup_pygame((900,550), 'Gravity Game - Level Designer', True)

		levelDesigner_inputs_dic = {
		'Toggle_button' : {
			'Menu'   : Toggle_button(levelDesigner_info_ary, [275,0], [150,50], [False, GREEN, RED]),
			'Delete' : Toggle_button(levelDesigner_info_ary, [0,0],   [150,50], [False, GREEN, RED]),
			'Save'   : Toggle_button(levelDesigner_info_ary, [550,0], [150,50], [False, GREEN, RED]),
			'Items'  : Toggle_button(levelDesigner_info_ary, [725,0], [75 ,50], [True , GREEN, RED]),
			'Text'   : Toggle_button(levelDesigner_info_ary, [800,0], [75 ,50], [False, GREEN, RED]),
			},
		'Items'         : {
			'Spawn Box' : Toggle_button(levelDesigner_info_ary, [725, 75],  [150, 50], [False, GREEN, RED]),
			'Well'      : Toggle_button(levelDesigner_info_ary, [725, 150], [150, 50], [False, GREEN, RED]),
			'Hori Wall' : Toggle_button(levelDesigner_info_ary, [725, 225], [150, 50], [False, GREEN, RED]),
			'Verti Wall': Toggle_button(levelDesigner_info_ary, [725, 300], [150, 50], [False, GREEN, RED]),
			}
		}

		levelDesigner_buttonFunctions_dic = {
		'Menu'  : gblF_Main,
		'Delete': levelDesignerF_delFunc,
		}


		while True:
			for event in pygame.event.get():
				for key, value in levelDesigner_inputs_dic['Toggle_button'].items(): # Detection for constant buttons
					if value.detect(event) and ((key == 'Items') or (key == 'Text')): # If an input is pressed and is either the Items or Text button, run code
						if levelDesigner_inputs_dic['Toggle_button']['Items'].state == levelDesigner_inputs_dic['Toggle_button']['Text'].state: # If both buttons are the same state
							levelDesigner_inputs_dic['Toggle_button']['Items'].state = False # Set both buttons to off
							levelDesigner_inputs_dic['Toggle_button']['Text'].state  = False
							levelDesigner_inputs_dic['Toggle_button'][key].state     = True # Set clicked button to on

				if levelDesigner_inputs_dic['Toggle_button']['Items'].state: # Only detect these buttons while on Items tab
					for key, value in levelDesigner_inputs_dic['Items'].items():
						if value.detect(event):
							for ckey, cvalue in levelDesigner_inputs_dic['Items'].items():
								cvalue.state = False
								levelDesigner_inputs_dic['Toggle_button']['Delete'].state = False
							value.state = True



				if event.type == pygame.QUIT:
					pygame.quit()

			
			levelDesigner_screen_ins.fill(GREY_1)

			# Drawing lines
			pygame.draw.line(levelDesigner_screen_ins, BLACK, (0, 50),(700, 50),3)
			pygame.draw.line(levelDesigner_screen_ins, BLACK,(700, 0), (700, 550),3)
			pygame.draw.rect(levelDesigner_screen_ins, BLACK, (0,0,900,550), 3)

			# Drawing buttons and adding functionality
			for key, value in levelDesigner_inputs_dic['Toggle_button'].items():
				value.draw(key)
				if value.state == True:
					try:
						levelDesigner_buttonFunctions_dic[key]()
					except:
						pass

			if levelDesigner_inputs_dic['Toggle_button']['Items'].state  == True:
				levelDesignerF_drawItemsTab()
			else:
				levelDesignerF_drawTextTab()



			flip()
			levelDesigner_clock_ins.tick(60)

	def MainF_drawText(drawText_info_ary, drawText_coords_ary, drawText_text_str, drawText_isUnderlined_boo=False):
		try:
			if drawText_isUnderlined_boo:
				drawText_info_ary[2].set_underline(1)
			drawText_textRender_ins = drawText_info_ary[2].render(str(drawText_text_str), True, BLACK)
			drawText_info_ary[0].blit(drawText_textRender_ins,[int(drawText_coords_ary[0])-(drawText_textRender_ins.get_width()//2),int(drawText_coords_ary[1])-(drawText_textRender_ins.get_height()//2)])
			drawText_info_ary[2].set_underline(0)
			return []

		except Exception:
			return False


	# Main running code
	MainF_drawStartMenu()


if __name__ == '__main__':
	gblF_Main()