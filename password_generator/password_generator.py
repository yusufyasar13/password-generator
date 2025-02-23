# MIT License
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, askyesno, showinfo
import string, random, os.path


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # general features of the app 
        self.title('Password Generator')
        self.iconbitmap('.icons/key.ico')
        self.size(300,200)
        self.main_screen()


    def size(self,window_width,window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2 - 100)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)


    def main_screen(self):
        # special placement features
        self.special_padd1 = {'padx': 5, 'pady': 5}
        self.special_padd2 = {'padx': 55, 'pady': 5}

        # images used in the app
        self.begin_image = tk.PhotoImage(file='.images/lock.png')
        self.quit_image = tk.PhotoImage(file='.images/exit.png')

        # contents of begin and quit buttons
        self.main_btn_frame_content = {}

        # features of main page contents 
        self.msg_frame = ttk.Frame(self).pack()
        self.main_msg = tk.Label(self.msg_frame, text="Welcome to Password Generator!", bg="darkblue", fg="grey", anchor=tk.CENTER, font=("Helvetica", 12))
        self.main_msg.pack(expand=True,fill=tk.BOTH,**self.special_padd1)
        self.main_btn_frame = ttk.Frame(self).pack()
        self.main_btn_frame_content['begin_btn'] = tk.Button(self.main_btn_frame, image=self.begin_image, anchor=tk.CENTER,command=self.begin,cursor="hand2")
        self.main_btn_frame_content['quit_btn'] = tk.Button(self.main_btn_frame, image=self.quit_image, command=lambda: self.quit(),cursor="hand2")

        # same placement settings of begin and quit buttons
        for self.content in self.main_btn_frame_content.values():
            self.content.pack(fill=tk.BOTH, anchor=tk.CENTER, expand=True,side=tk.TOP)


    def begin(self):
        # resizing the screen
        self.size(450,300)

        #deleting contents from app page
        self.main_msg.destroy()
        self.main_btn_frame_content['begin_btn'].destroy()
        self.main_btn_frame_content['quit_btn'].destroy()
        
        # features of password frame
        self.pass_frame = tk.Frame(root, bg= "darkblue")
        self.pass_frame.pack(fill=tk.BOTH, **self.special_padd1,side=tk.LEFT)

        # features of listbox frame 
        self.pass_list_frame = tk.Frame(root, bg="darkgreen")
        self.pass_list_frame.pack(fill=tk.BOTH,expand=True, **self.special_padd1, side=tk.LEFT)

        # calling essential functions
        self.pass_length()

        self.pass_content()

        self.password()

        self.pass_list()

        
    def pass_length(self):
        # features of password length frame 
        self.pass_len_frame =tk.Frame(self.pass_frame,bg="darkcyan")
        self.pass_len_title = tk.Label(self.pass_len_frame,bg="darkcyan",text="Password Length",font=("Helvetica 11 bold"))
        self.pass_len_title.pack(fill=tk.BOTH,expand=True,side=tk.TOP)

        # determining the value of the scale as a number
        self.len_value = tk.IntVar()

        # features of the scale 
        self.pass_len_range = tk.Scale(self.pass_len_frame, from_=8, to=16, orient='horizontal',variable=self.len_value)
        self.pass_len_range.pack(fill=tk.X,expand=True,side=tk.BOTTOM,padx=30)

        # placement of password length frame
        self.pass_len_frame.pack(fill=tk.BOTH,expand=True,side=tk.TOP,**self.special_padd1)

    def pass_content(self):
        # features of password content frame 
        self.pass_cont_frame =tk.Frame(self.pass_frame, bg="DarkOliveGreen")

        # features of password content items
        self.pass_cont_top_frame = tk.Frame(self.pass_cont_frame, bg="DarkOliveGreen")
        self.pass_cont_title = tk.Label(self.pass_cont_top_frame, bg="DarkOliveGreen",text="Password Content",font=("Helvetica 11 bold"))
        self.pass_cont_title.pack(fill=tk.X,expand=True,side=tk.TOP)
        self.pass_cont_top_frame.pack(fill=tk.X,expand=True,side=tk.TOP) 

        # determining the values of the check items as a number
        self.pass_check_let = tk.IntVar()
        self.pass_check_num = tk.IntVar()

        # features of the check items
        self.pass_cont_center_frame = tk.Frame(self.pass_cont_frame, bg="DarkOliveGreen")
        self.check_letter = ttk.Checkbutton(self.pass_cont_center_frame,text='Letter',variable=self.pass_check_let,onvalue=1,offvalue=0)
        self.check_letter.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=20,ipadx=6)
        self.check_number = ttk.Checkbutton(self.pass_cont_center_frame,text='Number',variable=self.pass_check_num,onvalue=1,offvalue=0)
        self.check_number.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=20)
        self.pass_cont_center_frame.pack(fill=tk.X,expand=True,side=tk.TOP)

        # features of the create button 
        self.pass_cont_bottom_frame = tk.Frame(self.pass_cont_frame, bg="DarkOliveGreen")
        self.create_button = tk.Button(self.pass_cont_bottom_frame, text="Create",command=self.create,cursor="hand2")
        self.create_button.pack(expand=True,fill=tk.X,padx=80)
        self.pass_cont_bottom_frame.pack(fill=tk.X,expand=True,side=tk.TOP)

        # placement of password content frame
        self.pass_cont_frame.pack(fill=tk.BOTH,expand=True,side=tk.TOP,**self.special_padd1)

    def password(self):
        # features of password frame 
        self.pass_text_frame =tk.Frame(self.pass_frame, bg="purple")
        self.emp = tk.Label(self.pass_text_frame,bg="purple",font=("Helvetica", 3)).pack()
        self.pass_text = tk.Text(self.pass_text_frame,width=20,height=1,font=("Helvetica", 11))
        self.pass_text.pack(expand=True,side=tk.TOP)

        # adding the password to the listbox 
        self.add_button = tk.Button(self.pass_text_frame, text="Add", command= self.add,cursor="hand2")
        self.add_button.pack(expand=True,side=tk.BOTTOM,fill=tk.X,padx=80)

        # placement of password frame
        self.pass_text_frame.pack(fill=tk.BOTH,expand=True,side=tk.TOP,**self.special_padd1)

    def pass_list(self):
        # features of the listbox frame
        self.list_frame = tk.Frame(self.pass_list_frame, bg="white")
        self.last_frame = tk.Frame(self.pass_list_frame, bg="maroon")

        # values of the listbox 
        self.passwords = ()
        self.pass_value= tk.Variable(value=self.passwords)

        # features of the listbox  
        self.pass_listbx = tk.Listbox(self.list_frame,listvariable=self.pass_value,selectmode=tk.BROWSE,font=("Helvetica", 11))
        self.pass_listbx.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
        self.pass_scroll = ttk.Scrollbar(self.pass_listbx, orient=tk.VERTICAL,command=self.pass_listbx.yview,cursor="hand2")
        self.pass_listbx['yscrollcommand'] = self.pass_scroll.set
        self.pass_scroll.pack(side=tk.RIGHT,fill=tk.Y)

        # creating a file and writing the values of the listbox into the file 
        self.last_top_bottom_frame = tk.Frame(self.last_frame,bg="maroon")
        self.save_button = tk.Button(self.last_top_bottom_frame, text="Save",command=self.pass_save,cursor="hand2")
        self.save_button.pack(side=tk.LEFT,fill=tk.X,expand=True,padx=12,ipadx=4)

        # deleting the value of the selected item inside the listbox 
        self.delete_button = tk.Button(self.last_top_bottom_frame, text="Delete",command= self.pass_delete,cursor="hand2")
        self.delete_button.pack(side=tk.RIGHT,fill=tk.X,expand=True,padx=12)
        self.last_top_bottom_frame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,**self.special_padd1)

        # exiting the app 
        self.last_button_bottom_frame = tk.Frame(self.last_frame,bg="maroon")
        self.main_btn_frame_content['quit_btn'] = tk.Button(self.last_button_bottom_frame, image=self.quit_image, command=self.pass_quit,cursor="hand2")
        self.main_btn_frame_content['quit_btn'].pack(fill=tk.BOTH,expand=True)
        self.last_button_bottom_frame.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

        # placement of listbox frame
        self.list_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True,**self.special_padd1)
        self.last_frame.pack(fill=tk.BOTH,side=tk.BOTTOM,**self.special_padd1)


    def create(self):
        # emptying the password block
        self.pass_text.delete("1.0",tk.END)
        self.passwrd = ""

        # set password length as scale value
        for i in range (self.len_value.get()):

            # password content has letters and numbers
            if (self.pass_check_let.get() == 1) & (self.pass_check_num.get() == 1):

                # generating random letters and numbers
                self.letter = random.choice(string.ascii_letters)
                self.number = str(random.randint(0,9))

                # selecting between random letter and random number 
                self.l = [self.letter,self.number]
                self.pas = random.choice(self.l)

                # combining the selected items
                self.passwrd += self.pas

            # password content has only letters
            elif (self.pass_check_let.get() == 1) & (self.pass_check_num.get() == 0):

                # generating random letters
                self.letter = random.choice(string.ascii_letters)

                # combining the selected items
                self.passwrd += self.letter

            # password content has only numbers
            elif (self.pass_check_let.get() == 0) & (self.pass_check_num.get() == 1):

                # generating random numbers
                self.number = str(random.randint(0,9))

                # combining the selected items
                self.passwrd += self.number
    
            else:
                # message that occurs when no content is selected
                showwarning(
                    title='Warning',
                    message='Please choose any content!')
                return False

        # inserting the items to the password text
        self.pass_text.insert("1.0",self.passwrd)


    def add(self):
        # when the password already exists in the listbox
        if(self.pass_text.get("1.0",tk.END) in self.pass_listbx.get(0,tk.END)):
            showinfo(
                title='Information',
                message='The password already exists!')
            return False
        
        # when the password is empty  
        elif(len(self.pass_text.get("1.0",tk.END).strip()) == 0):
            showinfo(
                title='Information',
                message='The password cannot be empty!')
            return False
        else:
            # inserting the password into the listbox
            self.pass_listbx.insert(tk.END, self.pass_text.get('1.0','end'))


    def pass_save(self):
        # checking the file already exists or not 
        self.file_exists = os.path.exists("my_passwords.txt")

        # when the file already exists and inside of the listbox is empty
        if(self.file_exists and len(self.pass_listbx.get(tk.END)) == 0):
            answer = askyesno(title='Confirmation',
                        message='There is no password!\n\nDo you still want to overwrite?')
            if answer:
                # overwriting the file without any password 
                self.file = open("my_passwords.txt","w+")
                self.file.writelines(self.pass_listbx.get(0,tk.END))
                self.file.close()
            else:
                return False
        
        # when the file already exists and inside of the listbox is not empty
        elif (self.file_exists):
            answer = askyesno(title='Confirmation',
                        message='The file already exists.\n\nDo you want to overwrite?')
            if answer:
                # overwrite the file with the passwords inside the listbox 
                self.file = open("my_passwords.txt","w+")
                self.file.writelines(self.pass_listbx.get(0,tk.END))
                self.file.close()
            else:
                return False
        
        # when the file is not exists and inside of the listbox is empty 
        elif(len(self.pass_listbx.get(tk.END)) == 0):
            answer = askyesno(title='Confirmation',
                        message='There is no password!\n\nDo you want to create a file?')
            if answer:
                # creating the file without any password 
                self.file = open("my_passwords.txt","w+")
                self.file.writelines(self.pass_listbx.get(0,tk.END))
                self.file.close()
            else:
                return False
        else:
            # creating the file and writing the passwords inside of the listbox 
            self.file = open("my_passwords.txt","w+")
            self.file.writelines(self.pass_listbx.get(0,tk.END))
            self.file.close()

    
    def pass_delete(self):
        # inside of the listbox is empty 
        if(len(self.pass_listbx.get(tk.END)) == 0):
            showwarning(
                title='Information',
                message='There is no password!')
        else:
            # deleting the selected password
            self.pass_listbx.delete(tk.ACTIVE)

    # exiting the app 
    def pass_quit(self):
        answer = askyesno(title='Confirmation',
                        message='Do you want out?')
        if answer:
            self.quit()


if __name__ == "__main__":
    root = App()
    root.mainloop()
