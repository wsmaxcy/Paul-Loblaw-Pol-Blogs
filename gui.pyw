from tkinter import *
#import Main.py
import os
import time
import Main
from Blogs import GenericScraper, ACrooksScraper, ADailyKosScraper, AHotAirScraper, AHuffScraper, APowerLineScraper, ARedStateScraper



compareableSite = []

def URLScan(status):

    step = '[+] Scanning Website'
    status['text'] = "{}".format(step)
    root.update()
    global compareableSite
    compareableSite = GenericScraper.main(label.get())
    step = '[+] Scan Complete'
    status['text'] = "{}".format(step)
    root.update()
    
    #checks to see if website was scanned correctly
    if(len(compareableSite)>0):
        time.sleep(1)
        step = '[+] Blog Title Found'
        status['text'] = "{}".format(step)
        root.update()

        time.sleep(1)
        step = '[+] Blog Body Found'
        status['text'] = "{}".format(step)
        root.update()
    
        time.sleep(1)
        step = '[+] Blog: ' + compareableSite[0]+ ' ready for comparison'
        status['text'] = "{}".format(step)
        root.update()
    else:
        time.sleep(1)
        step = '[-] Please enter correct URL'
        status['text'] = "{}".format(step)
        root.update()
    

    return compareableSite

#action that balls blog scrapers. outputs which blog website is being scanned
def blogScan(status):

    step = '[+] Scraping and saving data to ~/Blogs/SavedBlogs/'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)

    step = '[+] This will take a few minuets'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(2)

    #Crooks and Liars Call
    step = '[+] Scraping Crooks and Liars'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)
    ACrooksScraper.main(status,root)

    #Daily Kos call
    step = '[+] Scraping DailyKos'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)
    ADailyKosScraper.main(status,root)
    
    #Hot Air Call
    step = '[+] Scraping Hot Air'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)
    AHotAirScraper.main(status,root)
    
    #Huffington Post call
    step = '[+] Scraping Huffington Post'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)
    AHuffScraper.main(status,root)

    #Power Line Call
    step = '[+] Scraping Power Line'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)
    APowerLineScraper.main(status,root)
    
    #Red State Call
    step = '[+] Scraping Red State'
    status['text'] = "{}".format(step)
    root.update()
    time.sleep(1)
    ARedStateScraper.main(status,root)
    
    #Completion
    step = '[+] Scraping Complete'
    status['text'] = "{}".format(step)
    root.update()

    return

def affScan(status):
    if len(compareableSite) < 1:
        step = '[-] Scan URL of blog before finding affiliation'
        status['text'] = "{}".format(step)
        root.update()
    else:
        step = '[+] Starting Process'
        status['text'] = "{}".format(step)
        root.update()
        Main.go(compareableSite,status,root)
    return


root = Tk()
root.option_add('*Font', 'TkTooltipFont')

status = Label(root,text="[+] Scrape Blog or URL to start",bg='#1b1b1b', fg='#ffffff', anchor='sw', width='300')


# turns off title bar, geometry
root.overrideredirect(True)
# set new geometry
root.geometry('300x140+200+200')
# set background color of title bar
back_ground = "#1b1b1b"

# set background of window
content_color = "#ffffff"
# make a frame for the title bar
title_bar = Frame(root, bg=back_ground, relief='raised', bd=0, highlightcolor=back_ground,highlightthickness=0)

# put a close button on the title bar
close_button = Button(title_bar, text='x',  command=root.destroy,bg=back_ground, padx=15, pady=0, activebackground="red", bd=0, fg='white', activeforeground="white", highlightthickness=0)

# window title
logo = PhotoImage(file='Data/logo.png')
windowback = PhotoImage(file='Data/background.png')
title_window = "Paul Loblaw Pol Blog Logger"
title_name = Label(title_bar, image=logo, text=title_window, bg=back_ground, fg="white")
# a canvas for the main area of the window
window = Canvas(root, bg="#4B4B4B", highlightthickness=0)
window.create_image(0,0,image=windowback,anchor=NW)


scrapeBlogs = Button(window, text="Scrape Blogs", command=lambda : blogScan(status), bg='#393939', padx=10, pady=2, activebackground='#393939',bd=0, fg='white', activeforeground='white', highlightthickness=0)
scanURL = Button(window, text="Scrape URL", command=lambda : URLScan(status),  bg='#393939', padx=10, pady=2, activebackground='#393939',bd=0, fg='white', activeforeground='white', highlightthickness=0)
compareBlog = Button(window, text="Find Affiliation", command=lambda : affScan(status), bg='#393939', padx=10, pady=2, activebackground='#393939',bd=0, fg='white', activeforeground='white', highlightthickness=0)

#Entry Text stuff

v = StringVar(root, value='Enter URL Here')
label = Entry(window, bg='#525e54', bd=0, fg='#ffffff',selectborderwidth=5, width=200, textvariable=v)

def delete_text(event):
    if default_text:
        label.delete(0,END)
        defualt_text = False
default_text=True
label.bind("<Button-1>", delete_text)



# pack the widgets
title_bar.pack(expand=0, fill=X)
title_name.pack(side=LEFT)

close_button.pack(side=RIGHT)
label.pack(side=BOTTOM, padx=40, pady=10)
window.pack(expand=1, fill=BOTH)

scanURL.pack(side=BOTTOM)
scrapeBlogs.pack(side=LEFT,padx=30,pady=5)
compareBlog.pack(side=RIGHT,padx=30,pady=5)
status.pack(side=LEFT, padx=0,pady=0)


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