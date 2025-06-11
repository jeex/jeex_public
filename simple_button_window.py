import dearpygui.dearpygui as dpg

def simple_filter(data, channels):
	# all pixel info in data is arrange in a large list
	# with values red, greed, blue, alpha.
	# Alpha is only if channels == 4, otherwise no alpha, channels == 3
	for i in range(len(data)):
		if i % channels == 0:
			# red color in pixel
			if data[i] >= 0.75:
				# quite red, make more red
				data[i] = 1
			elif data[i] <= 0.25:
				# make less red
				data[i] = 0
		elif i % channels == 1:
			# green color in pixel
			if data[i] >= 0.75:
				data[i] = 1
			elif data[i] <= 0.25:
				data[i] = 0
		elif i % channels == 2:
			# blue color in pixel
			if data[i] >= 0.75:
				data[i] = 1
			elif data[i] <= 0.25:
				data[i] = 0
		else:
			# coulf be alpha value, ignore
			pass

def make_filtered_image_window(sender):
	# this function should make a second window with the same image filtered
	print("btn clicked", sender)
	user_data = dpg.get_item_user_data(sender)
	print(user_data) # these user_data are connect to the button

	#  the image data are from the sender button: user_data
	width = user_data[0]
	height = user_data[1]
	channels = user_data[2]
	data = user_data[3]

	# now filter the data
	simple_filter(data, channels)

	# add image to a new texture
	with dpg.texture_registry():
		texture_id = dpg.add_static_texture(width, height, data)

	# now we could make an extra window with a filtered image
	with dpg.window(label="Filtered Image", pos=(330, 0), width=320, height=320, tag="filtered_image_window"):
		dpg.add_image(texture_id)

	# this type of function cannot return anything


def main_window():
	dpg.create_context()
	dpg.create_viewport(title="Images in DearPyGui", width=840, height=660)
	dpg.setup_dearpygui()

	# make a window in the main window
	window_tag = "my_image_window" # the unique id of this window
	with dpg.window(label="The image", width=320, height=400, tag=window_tag, no_close=True, no_resize=True, no_move=True, no_collapse=True):
		pass
		# you can add stuff to this window later, like an image

	# load image
	imagepath = "chrysi.png"
	width, height, channels, data = dpg.load_image(imagepath)

	# add image to texture (paint it on a canvas)
	with dpg.texture_registry():
		texture_id = dpg.add_static_texture(width, height, data)

	# use the window_tag to put this texture in a specific window
	dpg.add_image(texture_id, parent=window_tag)

	# ADD A BUTTON
	dpg.add_button(
		label="Filter Example",
		tag="filter_button",  # unique identifier of button
		width=140,
		height=30,
		show=True, # show button immediately
		user_data=[width, height, channels, data],  # extra data that can be connected to this button
		callback=make_filtered_image_window,  # the name of the function that is called with this button
		parent=window_tag, # this adds the button to this specific window
	)

	dpg.show_viewport()
	dpg.start_dearpygui()
	# end of window
	dpg.destroy_context()

if __name__ == '__main__':
	main_window()
