from tkinter import *
#import Main.py
import os


root = Tk()
root.option_add('*Font', 'TkTooltipFont')

# turns off title bar, geometry
root.overrideredirect(True)
# set new geometry
root.geometry('300x100+200+200')
# set background color of title bar
back_ground = "#2c2c2c"

# set background of window
content_color = "#ffffff"
# make a frame for the title bar
title_bar = Frame(root, bg=back_ground, relief='raised', bd=0, highlightcolor=back_ground,highlightthickness=0)

# put a close button on the title bar
close_button = Button(title_bar, text='x',  command=root.destroy,bg=back_ground, padx=20, pady=0, activebackground="red", bd=0, fg='white', activeforeground="white", highlightthickness=0)

# window title
logo = PhotoImage(file='logo.png')
title_window = "Paul Loblaw Pol Blog Logger"
title_name = Label(title_bar, image=logo, text=title_window, bg=back_ground, fg="white")
# a canvas for the main area of the window
window = Canvas(root, bg="grey", highlightthickness=0)
#window.option_add('*Font', "TkTooltipFont")

scanBlogs = Button(window, text="Scan Blogs", command=lambda : os.system('Blogs\Scrape.sh'), bg=back_ground, padx=11, pady=5, activebackground='#5FD3A2',bd=0, fg='white', activeforeground='white', highlightthickness=0)
loadBlogs = Button(window, text="Load Blogs", bg=back_ground, padx=10, pady=5, activebackground='#5FD3A2',bd=0, fg='white', activeforeground='white', highlightthickness=0)


# pack the widgets
title_bar.pack(expand=0, fill=X)
title_name.pack(side=LEFT)
close_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)
scanBlogs.pack(side=LEFT)
loadBlogs.pack(side=RIGHT)
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

# change on hovering for scan button
def change_on_hovering_scan(event):
    global scanBlogs
    scanBlogs['bg'] = '#5FD3A2'
    

def return_to_normal_state_scan(event):
   global scanBlogs
   scanBlogs['bg'] = back_ground


scanBlogs.bind('<Enter>', change_on_hovering_scan)
scanBlogs.bind('<Leave>', return_to_normal_state_scan)

# change on hovering for load button
def change_on_hovering_scan(event):
    global loadBlogs
    loadBlogs['bg'] = '#5FD3A2'
    

def return_to_normal_state_scan(event):
   global loadBlogs
   loadBlogs['bg'] = back_ground


loadBlogs.bind('<Enter>', change_on_hovering_scan)
loadBlogs.bind('<Leave>', return_to_normal_state_scan)
root.mainloop()