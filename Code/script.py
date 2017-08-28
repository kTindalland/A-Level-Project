from tmtu2_5_0 import *
def gblF_Main():
	Main_screen_ins, Main_clock_ins, Main_info_ary = setup_pygame(size, 'Gravity Game - Main Menu', True)
	# Screen size is (700, 500)

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
		levelDesigner_screen_ins, levelDesigner_clock_ins, levelDesigner_info_ary = setup_pygame((900,550), 'Gravity Game - Level Designer', True)

		levelDesigner_inputs_dic = {
		'Toggle_button' : {
			'Menu' : Toggle_button(levelDesigner_info_ary, [275,0], [150,50], [False, GREEN, RED]),
			},
		}

		levelDesigner_buttonFunctions_dic = {
		'Menu' : gblF_Main,
		}

		while True:
			for event in pygame.event.get():
				for key, value in levelDesigner_inputs_dic['Toggle_button'].items():
					value.detect(event)
				if event.type == pygame.QUIT:
					pygame.quit()

			
			levelDesigner_screen_ins.fill(GREY_1)

			for key, value in levelDesigner_inputs_dic['Toggle_button'].items():
				value.draw(key)
				if value.state == True:
					try:
						levelDesigner_buttonFunctions_dic[key]()
					except:
						pass



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