from tkinter import Tk, Label, Button,messagebox,Entry,StringVar
import pickle


class MyFirstGUI:

	def __init__(self, master):
		self.master = master
		master.title("SYSTEM LOGIN")
		master.geometry('450x300')
# user information
		self.label=Label(master,text='User name: ').place(x=50, y= 150)
		self.label=Label(master,text='Password: ').place(x=50, y= 190)
		var_usr_name = StringVar()
		var_usr_name.set('example@python.com')
		entry_usr_name =Entry(master, textvariable=var_usr_name)
		entry_usr_name.place(x=160, y=150)
		var_usr_pwd = StringVar()
		entry_usr_pwd =Entry(master, textvariable=var_usr_pwd, show='*')
		entry_usr_pwd.place(x=160, y=190)
	
	
if __name__ == '__main__':
	root = Tk()
	root1 = Tk()
	my_gui = MyFirstGUI(root)
	your_gui=MyFirstGUI(root1)
	root.mainloop()