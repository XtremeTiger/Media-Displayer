from tkinter import *
# Se va a necesitar hacer mas facil la adquisicion de Pillow
# para hacerlo mas user friendly
from PIL import ImageTk,Image

screen_width = 20
screen_height = 20

class MainWindow:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master, width='50c', height=200, borderwidth=10, relief="groove")
		self.frame.pack(fill=BOTH, expand=1)
		self.label = Label(self.frame, text="Hello world")
		self.label.pack(expand=1)
		self.button = Button(self.frame, text="Open media", command = self.open_media)
		self.button.pack(expand=1)
		self.button2 = Button(self.frame, text="Close media", command = self.close_media)
		self.button2.pack(expand=1)
		self.exiter = Button(self.frame, text="Quit", command=master.destroy)
		self.exiter.pack(expand=1)

	def open_media(self):
		self.mediaWindow = Toplevel(self.master)
		self.media = Media(self.mediaWindow)

	def close_media(self):
		self.mediaWindow.destroy()

class Media(Tk):
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master, width=200, height=200)
		self.frame.pack(fill=BOTH, expand=1)
		# Grabbing the size of the screen.
		screenRes = [0, 0]
		screenRes[0] = screen_width
		screenRes[1] = screen_height
		# Select image
		self.selected = Image.open("Fox.jpg")
		print(self.selected.size[1])
		# Comparing the size of the image to the screen resolution.
		if self.selected.size[0] < screenRes[0] or self.selected.size[1] < screenRes[1]:
			# [TO DO]Resize the image to bigger
			pass
		# Fetch the size of the image
		self.actImgRes = list(self.selected.size)
		print(self.actImgRes)
		# Resize the image to smaller
		self.selected.thumbnail(tuple(screenRes))
		self.image = ImageTk.PhotoImage(self.selected)
		# Displaying the image with a black background
		self.label = Label(self.frame, width=screen_width, height=screen_height, image=self.image, bg='black')
		self.label.pack(fill=BOTH, expand=1)


def main(): 
	global screen_width
	global screen_height
	root = Tk()
	app = MainWindow(root)
	# Grabbing the size of the screen and printing it to the terminal.
	screen_width = root.winfo_screenwidth()
	print(screen_width)
	screen_height = root.winfo_screenheight()
	print(screen_height)

	root.mainloop()

if __name__ == '__main__':
	main()