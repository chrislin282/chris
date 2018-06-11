from tkinter import Tk, Label, Button,messagebox,Entry,StringVar
import pickle


class MyFirstGUI:

	def __init__(self, master):
		self.master = master
		master.title("SYSTEM LOGIN")
		master.geometry('450x300')

		self.label=Label(master,text='User name: ').place(x=50, y= 150)
		self.label=Label(master,text='Password: ').place(x=50, y= 190)
		self.var_usr_name = StringVar()
		self.var_usr_name.set('example@python.com')
		self.entry_usr_name =Entry(master, textvariable=self.var_usr_name)
		self.entry_usr_name.place(x=160, y=150)
		self.var_usr_pwd = StringVar()
		self.entry_usr_pwd =Entry(master, textvariable=self.var_usr_pwd, show='*')
		self.entry_usr_pwd.place(x=160, y=190)
		self.btn_login = Button(master, text='Login', command=self.usr_login)
		self.btn_login.place(x=170, y=230)
		#self.btn_sign_up = Button(master, text='Sign up', command=self.usr_sign_up)
		#self.btn_sign_up.place(x=270, y=230)
	def usr_login(self):
		self.usr_name = self.var_usr_name.get()
		self.usr_pwd = self.var_usr_pwd.get()
		print(self.usr_name)
		print(self.usr_pwd)
		file=open('usrs_info.pickle', 'wb')
		file.close()

	
	
if __name__ == '__main__':
	root =Tk()
	my_gui = MyFirstGUI(root)
	root.mainloop()
	
