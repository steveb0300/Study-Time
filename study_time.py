# This is a GUI program that uses a timer for periods of studying and taking breaks 

# Imports
from tkinter import *
import os
import winsound
import app_global_variables as vars

def show_home():
    # Open study timer settings window
    home_frame.place(in_=window, anchor="c", relx=.5, rely=.5)
    study_timer_settings_frame.place_forget()

def show_study_time_settings():
    # Open study timer settings window
    home_frame.place_forget()
    study_timer_settings_frame.place(in_=window, anchor="c", relx=.5, rely=.5)

def btn_ten_selected():
    # Set time
    vars.study_timer_time = 10

    # Create a string and format to assign to label
    time_string = StringVar()
    time_string.set("{}:00".format(vars.study_timer_time))
    vars.lbl_study_timer_count_down.config(text = time_string.get())
    
    btn_ten.configure(bg="#00DF06") 
    btn_fifteen.configure(bg="azure3") 
    btn_twenty.configure(bg="azure3") 
    btn_twentyfive.configure(bg="azure3")
    btn_thirty.configure(bg="azure3")

def btn_fifteen_selected():
    # Set time
    vars.study_timer_time = 15
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.study_timer_time))
    vars.lbl_study_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_ten.configure(bg="azure3") 
    btn_fifteen.configure(bg="#00DF06") 
    btn_twenty.configure(bg="azure3") 
    btn_twentyfive.configure(bg="azure3")
    btn_thirty.configure(bg="azure3")

def btn_twenty_selected():
    # Set time
    vars.study_timer_time = 20
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.study_timer_time))
    vars.lbl_study_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_ten.configure(bg="azure3") 
    btn_fifteen.configure(bg="azure3") 
    btn_twenty.configure(bg="#00DF06") 
    btn_twentyfive.configure(bg="azure3")
    btn_thirty.configure(bg="azure3")

def btn_twentyfive_selected():
    # Set time
    vars.study_timer_time = 25
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.study_timer_time))
    vars.lbl_study_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_ten.configure(bg="azure3") 
    btn_fifteen.configure(bg="azure3") 
    btn_twenty.configure(bg="azure3") 
    btn_twentyfive.configure(bg="#00DF06")
    btn_thirty.configure(bg="azure3")

def btn_thirty_selected():
    # Set time
    vars.study_timer_time = 30
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.study_timer_time))
    vars.lbl_study_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_ten.configure(bg="azure3") 
    btn_fifteen.configure(bg="azure3") 
    btn_twenty.configure(bg="azure3") 
    btn_twentyfive.configure(bg="azure3")
    btn_thirty.configure(bg="#00DF06")

def btn_break_five_selected():
    # Set time
    vars.break_timer_time = 5
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.break_timer_time))
    vars.lbl_break_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_break_five.configure(bg="#00DF06") 
    btn_break_ten.configure(bg="azure3") 
    btn_break_fifteen.configure(bg="azure3")

def btn_break_ten_selected():
    # Set time
    vars.break_timer_time = 10
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.break_timer_time))
    vars.lbl_break_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_break_five.configure(bg="azure3") 
    btn_break_ten.configure(bg="#00DF06") 
    btn_break_fifteen.configure(bg="azure3")

def btn_break_fifteen_selected():
    # Set time
    vars.break_timer_time = 15
    
    time_string = StringVar()
    time_string.set("{}:00".format(vars.break_timer_time))
    vars.lbl_break_timer_count_down.config(text = time_string.get())
    
    # Create a string and format to assign to label
    btn_break_five.configure(bg="azure3") 
    btn_break_ten.configure(bg="azure3") 
    btn_break_fifteen.configure(bg="#00DF06")

def btn_test_app_selected():
    # Get module global variable button reference
    global btn_test_app

    # Toggle test app bool
    if vars.is_app_test == False:
        vars.is_app_test = True
    else:
        vars.is_app_test = False

    # Change color and text off button based off test app bool
    if vars.is_app_test:
        btn_test_app.configure(text = "ON")
        btn_test_app.configure(bg="#00DF06")
    else:
        btn_test_app.configure(text = "OFF")
        btn_test_app.configure(bg="azure4")

def start_pressed():

    vars.is_timers_running = True

    vars.is_study_time = True
    
    vars.mins = vars.study_timer_time - 1
    vars.secs = 59
    vars.btn_start.place_forget()
    vars.btn_reset.place(relx=0.5, rely=0.88, anchor=CENTER)

    vars.lbl_study_timer_count_down.configure(bg="green2")
    vars.lbl_study_timer_count_down.configure(fg="black")

    timers_countdown()

def timers_countdown():
    # If test app. Run app quicker by setting time to 5 vars.secs
    if vars.is_app_test:
        vars.mins = 0
        if vars.secs > 5:
            vars.secs = 5
    
    # Timer is greater than zero and timer is running
    if vars.mins >= 0 and vars.is_timers_running:
        
        # Create string to format for timer labels
        time_string = StringVar()
        time_string.set("{}:{:02}".format(vars.mins, vars.secs))

        # Update the label text
        if vars.is_study_time:
            vars.lbl_study_timer_count_down.config(text = time_string.get())
        else:
            vars.lbl_break_timer_count_down.config(text = time_string.get())

        # Check if time is zero and is study time. Flip to break time if true
        if vars.mins == 0 and vars.secs == 0:
            if vars.is_study_time:
                vars.is_study_time = False
                vars.mins = vars.break_timer_time - 1
                vars.secs = 60
                # Set timer labels colors
                vars.lbl_study_timer_count_down.configure(bg="azure3")
                vars.lbl_study_timer_count_down.configure(fg="azure4")
                vars.lbl_break_timer_count_down.configure(bg="green2")
                vars.lbl_break_timer_count_down.configure(fg="black")
                
                # Reset study timer label for next cycle
                vars.study_timer_time = vars.study_timer_time
                study_time_string = StringVar()
                study_time_string.set("{}:00".format(vars.study_timer_time))
                vars.lbl_study_timer_count_down.config(text = study_time_string.get())

                # Play sound
                timer_sound = "time_switch.wav"
                current_dir = os.path.dirname(__file__) 
                timer_sound_path = os.path.join(current_dir, timer_sound)
                winsound.PlaySound(timer_sound_path, winsound.SND_ASYNC)
            else:
                vars.is_study_time = True
                vars.mins = vars.study_timer_time - 1
                vars.secs = 60
                # Set timer labels colors
                vars.lbl_study_timer_count_down.configure(bg="green2")
                vars.lbl_study_timer_count_down.configure(fg="black")
                vars.lbl_break_timer_count_down.configure(bg="azure3")
                vars.lbl_break_timer_count_down.configure(fg="azure4")
                
                # Reset break timer label for next cycle
                vars.break_timer_time = vars.break_timer_time
                break_time_string = StringVar()
                break_time_string.set("{}:00".format(vars.break_timer_time))
                vars.lbl_break_timer_count_down.config(text = break_time_string.get())
                
                # Play sound
                timer_sound = "time_switch.wav"
                current_dir = os.path.dirname(__file__) 
                timer_sound_path = os.path.join(current_dir, timer_sound)
                winsound.PlaySound(timer_sound_path, winsound.SND_ASYNC)

        # Count down time and wait for one second to call this function again     
        if vars.secs > 0:
            vars.secs -= 1
            window.after(1000, lambda: timers_countdown())
        elif vars.mins > 0:
            vars.mins -= 1
            vars.secs = 59            
            window.after(1000, lambda: timers_countdown())

def reset_pressed():
    # Reset study time label
    vars.study_timer_time = vars.study_timer_time
    study_time_string = StringVar()
    study_time_string.set("{}:00".format(vars.study_timer_time))
    vars.lbl_study_timer_count_down.config(text = study_time_string.get())
    vars.lbl_study_timer_count_down.configure(bg="azure3")
    vars.lbl_study_timer_count_down.configure(fg="azure4")

    # Reset break timer label
    vars.break_timer_time = vars.break_timer_time
    break_time_string = StringVar()
    break_time_string.set("{}:00".format(vars.break_timer_time))
    vars.lbl_break_timer_count_down.config(text = break_time_string.get())
    vars.lbl_break_timer_count_down.configure(bg="azure3")
    vars.lbl_break_timer_count_down.configure(fg="azure4")

    # Reset timer running and study time bools
    vars.is_timers_running= False
    vars.is_study_time = False

    # Show the start button and hide the reset button
    vars.btn_start.place(relx=0.5, rely=0.88, anchor=CENTER)
    vars.btn_reset.place_forget()

# Load home window    
def load_home():

    # Create home page header label
    study_time_lbl = Label(home_frame, text="Study Time", fg="orange", bg='#368DFF', font=("Arial Bold", 40))

    # Create study timer header label
    lbl_study_timer_desc = Label(home_frame, text="Study Time Remaining", fg="black", bg='#368DFF', font=("Arial Bold", 20))

    # Create study timer label
    vars.lbl_study_timer_count_down = Label(home_frame,
                                          text=vars.study_timer_time,
                                          fg="azure4",
                                          bg="azure3",
                                          font=("Arial Bold", 30),
                                          width=10,
                                          relief=SUNKEN)
    study_time_string = StringVar()
    study_time_string.set("25:00")
    vars.lbl_study_timer_count_down.config(text = study_time_string.get())

    # Create study timer header label
    lbl_break_timer_desc = Label(home_frame, text="Break Time Remaining", fg="black", bg='#368DFF', font=("Arial Bold", 20))

    # Create break time label
    vars.lbl_break_timer_count_down = Label(home_frame,
                                          text=vars.break_timer_time,
                                          fg="azure4",
                                          bg="azure3",
                                          font=("Arial Bold", 30),
                                          width=10,
                                          relief=SUNKEN)
    break_time_string = StringVar()
    break_time_string.set("5:00")
    vars.lbl_break_timer_count_down.config(text = break_time_string.get())

    # Add a button to go to settings
    img_file_name_settings = "settings.png"
    current_dir = os.path.dirname(__file__) 
    img_path_settings = os.path.join(current_dir, img_file_name_settings)
    image_settings = PhotoImage(file = img_path_settings)
    btn_study_time_settings = Button(
        master=home_frame,
        image = image_settings,
        bg='#368DFF',
        bd=0,
        command=show_study_time_settings
    )
    btn_study_time_settings.image = image_settings

    # Add a button to close app
    img_file_name_close = "close.png" 
    img_path_close = os.path.join(current_dir, img_file_name_close)
    image_close = PhotoImage(file = img_path_close)
    btn_close = Button(
        master=home_frame,
        image = image_close,
        bg='#368DFF',
        bd=0,
        command=window.destroy
    )
    btn_close.image = image_close

    # Add a start timer button
    vars.btn_start = Button(
        master=home_frame,
        text="Start",
        font = ("Arial", 20),
        bg="green",
        fg="black",
        width=15,
        command=lambda: start_pressed()
    )

    # Add a reset timer button
    vars.btn_reset = Button(
        master=home_frame,
        text="Reset",
        font = ("Arial", 20),
        bg="royal blue",
        fg="black",
        width=15,
        command=lambda: reset_pressed()
    )

    # Asign the elements to proper grid locations
    study_time_lbl.place(relx=0.5, rely=0.1, anchor=CENTER)
    btn_study_time_settings.place(relx=0.07, rely=0.1, anchor=CENTER)
    btn_close.place(relx=0.93, rely=0.1, anchor=CENTER)
    lbl_study_timer_desc.place(relx=0.5, rely=0.29, anchor=CENTER)
    vars.lbl_study_timer_count_down.place(relx=0.5, rely=0.4, anchor=CENTER)
    lbl_break_timer_desc.place(relx=0.5, rely=0.57, anchor=CENTER)
    vars.lbl_break_timer_count_down.place(relx=0.5, rely=0.68, anchor=CENTER)
    vars.btn_start.place(relx=0.5, rely=0.88, anchor=CENTER)
    vars.btn_reset.place_forget()

# Load study timer settings window    
def load_study_timer_settings():

    # Create home page header label
    lbl_study_time_settings = Label(study_timer_settings_frame,
                                       text="Study Timer Settings",
                                       fg="orange",
                                       bg='#368DFF',
                                       font=("Arial Bold", 30))
    
    # Load and image from the relative path
    img_file_name = "home.png"
    current_dir = os.path.dirname(__file__) 
    img_path = os.path.join(current_dir, img_file_name)
    image = PhotoImage(file = img_path)

    # Add a button to return to home and assign image to it
    btn_go_home = Button(
        master=study_timer_settings_frame,
        image = image,
        bg='#368DFF',
        bd=0,
        command=show_home
    )
    btn_go_home.image = image

    # Create a study duration label
    lbl_study_time = Label(study_timer_settings_frame,
                                  text="Study Time (mins)",
                                  fg="black", bg='#368DFF',
                                  font=("Arial Bold", 20))

    # Create break time duration label
    lbl_break_time = Label(study_timer_settings_frame,
                                  text="Break Time (mins)",
                                  fg="black", bg='#368DFF',
                                  font=("Arial Bold", 20))

    # Create break time duration label
    lbl_test_app = Label(study_timer_settings_frame,
                                  text="Test App",
                                  fg="black", bg='#368DFF',
                                  font=("Arial Bold", 20))

    # Add a button to set time = 10
    global btn_ten 
    btn_ten = Button(
        master=study_timer_settings_frame,
        text="10",
        font = ("Arial", 20),
        bg="azure3",
        fg="black",
        width=5,
        command=btn_ten_selected
    )

    # Add a button to set time = 15
    global btn_fifteen
    btn_fifteen = Button(
        master=study_timer_settings_frame,
        text="15",
        font = ("Arial", 20),
        bg="azure3",
        fg="black",
        width=5,
        command=btn_fifteen_selected
    )

    # Add a button to set time = 20
    global btn_twenty
    btn_twenty = Button(
        master=study_timer_settings_frame,
        text="20",
        font = ("Arial", 20),
        bg="azure3",
        fg="black",
        width=5,
        command=btn_twenty_selected
    )

    # Add a button to set time = 25
    global btn_twentyfive
    btn_twentyfive = Button(
        master=study_timer_settings_frame,
        text="25",
        font = ("Arial", 20),
        bg="#00DF06",
        fg="black",
        width=5,
        command=btn_twentyfive_selected
    )

    # Add a button to set time = 30
    global btn_thirty
    btn_thirty = Button(
        master=study_timer_settings_frame,
        text="30",
        font = ("Arial", 20),
        bg="azure3",
        fg="black",
        width=5,
        command=btn_thirty_selected
    )

    # Add a button to set break time = 5
    global btn_break_five
    btn_break_five = Button(
        master=study_timer_settings_frame,
        text="5",
        font = ("Arial", 20),
        bg="#00DF06",
        fg="black",
        width=5,
        command=btn_break_five_selected
    )

    # Add a button to set break time = 10
    global btn_break_ten
    btn_break_ten = Button(
        master=study_timer_settings_frame,
        text="10",
        font = ("Arial", 20),
        bg="azure3",
        fg="black",
        width=5,
        command=btn_break_ten_selected
    )
    
    # Add a button to set break time = 15
    global btn_break_fifteen
    btn_break_fifteen = Button(
        master=study_timer_settings_frame,
        text="15",
        font = ("Arial", 20),
        bg="azure3",
        fg="black",
        width=5,
        command=btn_break_fifteen_selected
    )

    # Add a button to test app
    global btn_test_app
    btn_test_app = Button(
        master=study_timer_settings_frame,
        text="OFF",
        font = ("Arial", 20),
        bg="azure4",
        fg="black",
        width=5,
        command=btn_test_app_selected
    )
    
    # Asign the elements to proper grid locations
    lbl_study_time_settings.place(in_=study_timer_settings_frame, relx=0.5, rely=0.1, anchor=CENTER)
    btn_go_home.place(in_=study_timer_settings_frame, relx=0.07, rely=0.1, anchor=CENTER)
    lbl_study_time.place(in_=study_timer_settings_frame, relx=0.5, rely=0.27, anchor=CENTER)
    lbl_break_time.place(in_=study_timer_settings_frame, relx=0.5, rely=0.72, anchor=CENTER)
    btn_ten.place(in_=study_timer_settings_frame, relx=0.1, rely=0.4, anchor=CENTER)
    btn_fifteen.place(in_=study_timer_settings_frame, relx=0.3, rely=0.4, anchor=CENTER)
    btn_twenty.place(in_=study_timer_settings_frame, relx=0.5, rely=0.4, anchor=CENTER)
    btn_twentyfive.place(in_=study_timer_settings_frame, relx=0.7, rely=0.4, anchor=CENTER)
    btn_thirty.place(in_=study_timer_settings_frame, relx=0.9, rely=0.4, anchor=CENTER)
    btn_break_five.place(in_=study_timer_settings_frame, relx=0.3, rely=0.85, anchor=CENTER)
    btn_break_ten.place(in_=study_timer_settings_frame, relx=0.5, rely=0.85, anchor=CENTER)
    btn_break_fifteen.place(in_=study_timer_settings_frame, relx=0.7, rely=0.85, anchor=CENTER)
    lbl_test_app.place(in_=study_timer_settings_frame, relx=0.1, rely=0.72, anchor=CENTER)
    btn_test_app.place(in_=study_timer_settings_frame, relx=0.1, rely=0.85, anchor=CENTER)

# Add global button variables
btn_ten = None
btn_fifteen = None
btn_twenty = None
btn_twentyfive = None
btn_thirty = None
btn_break_five = None
btn_break_ten = None
btn_break_fifteen = None
btn_test_app = None

# Create window
window = Tk()
window.title("Study Time")
window.geometry("600x400")
window.resizable(width=False, height=False)
window['background']='#368DFF'
window.attributes("-topmost", True) # Forces window to stay on top of other windows

# Create a frame for main window
home_frame = Frame(window, width=600, height=400, background='#368DFF')
home_frame.place(in_=window, anchor="c", relx=.5, rely=.5)

# Create a frame for settings window
study_timer_settings_frame = Frame(window, width=600, height=400, background='#368DFF')
study_timer_settings_frame.place_forget()
   
# Load all windows
load_home()
load_study_timer_settings()

# Call the main loop
window.mainloop()
