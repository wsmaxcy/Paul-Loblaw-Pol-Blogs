from tkinter import *
#import Main.py
import os
import sys


root = Tk()
root.option_add('*Font', 'TkTooltipFont')

# turns off title bar, geometry
root.overrideredirect(True)
# set new geometry
root.geometry('300x125+200+200')
# set background color of title bar
back_ground = "#1b1b1b"

# set background of window
content_color = "#ffffff"
# make a frame for the title bar
title_bar = Frame(root, bg=back_ground, relief='raised', bd=0, highlightcolor=back_ground,highlightthickness=0)

# put a close button on the title bar
close_button = Button(title_bar, text='x',  command=root.destroy,bg=back_ground, padx=15, pady=0, activebackground="red", bd=0, fg='white', activeforeground="white", highlightthickness=0)

# window title
logo = PhotoImage(file='logo.png')
windowback = PhotoImage(file='working2.png')
title_window = "Paul Loblaw Pol Blog Logger"
title_name = Label(title_bar, image=logo, text=title_window, bg=back_ground, fg="white")
# a canvas for the main area of the window
window = Canvas(root, bg="#4B4B4B", highlightthickness=0)
window.create_image(0,0,image=windowback,anchor=NW)


scanBlogs = Button(window, text="Scan Blogs", command=lambda : os.system('Blogs\CrooksScraper.py & Blogs\DailyKosScraper.py'), bg='#393939', padx=10, pady=2, activebackground='#393939',bd=0, fg='white', activeforeground='white', highlightthickness=0)
loadBlogs = Button(window, text="Scan Site", command=lambda : print("Scan Site!"),  bg='#393939', padx=10, pady=2, activebackground='#393939',bd=0, fg='white', activeforeground='white', highlightthickness=0)
#scanSite = Button(window, text="Scan Site", bg=back_ground, padx=10, pady=2, activebackground='#5FD3A2',bd=0, fg='white', activeforeground='white', highlightthickness=0)
label = Entry(window, bg='#525e54', bd=0, fg='#ffffff',selectborderwidth=5, width=200)


# pack the widgets
title_bar.pack(expand=0, fill=X)
title_name.pack(side=LEFT)

close_button.pack(side=RIGHT)
label.pack(side=BOTTOM, pady=20, padx=40)
window.pack(expand=1, fill=BOTH)

scanBlogs.pack(side=LEFT,padx=35,pady=15)
loadBlogs.pack(side=RIGHT,padx=35,pady=15)


x_axis = None
y_axis = None
# bind title bar motion to the move window function


def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

# hover effect on close button
def change_on_hovering(event):
    global close_button
    close_button['bg'] = 'red'
    

def return_to_normal_state(event):
   global close_button
   close_button['bg'] = back_ground


title_bar.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>', change_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)

root.mainloop()