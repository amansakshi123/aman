from tkinter import *
from tkinter import messagebox
a=Tk()
# #widgets
# #textbox
# t=Text(a,height=4,width=20)
# t.pack()

# #checkbox
# c=Checkbutton(a,text="choose1",variable=IntVar())
# c.pack()

# #scale
# s=Scale(a,from_=0,to=20,orient=HORIZONTAL)
# s.pack()

# #spinbox
# ss=Spinbox(a,from_=0,to=5)
# ss.pack()
def submit_form():
    name=name_entry.get()
    Email=Email_entry.get()
    if not name or not Email:
        messagebox.showerror("error","All fields are Required")
    else:
        messagebox.showinfo("done","Form is submitted ")    
name=Label(a,text="name")
name.pack()
name_entry=Entry(a)
name_entry.pack()

Email=Label(a,text="email")
Email.pack()
Email_entry=Entry(a)
Email_entry.pack()

b=Button(a,text="Submit",command=submit_form)
b.pack()





a.mainloop()

