""" ECE508 Project - Spring 2019 - Michael Engstrom

    GUI to help manage running shell scripts in Linux
    File dialog to open scripts
    Script paths saved one per line in list
    Read each path in list and execute scripts with
    saved console output in file for each
    Count of scripts and remaining and number completed

    Developed using Python 3.5

    Run as Super User on Linux (su + password)"""

import tkinter as tk
import os
import subprocess
from tkinter import filedialog
from tkinter import StringVar
from datetime import datetime as dt

# Create list to hold script paths
scripts_list = []

class ScriptRunner:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("ScriptRunner - Select Scripts to Run Tests")

        # Create the frames
        self.button_frame = tk.Frame(self.main_window)
        self.testlabel_frame = tk.Frame(self.main_window)
        self.textwindow_frame = tk.Frame(self.main_window)
        self.numtests_frame = tk.Frame(self.main_window)
        self.comptests_frame = tk.Frame(self.main_window)

        # Create and pack widgets for button frame
        self.addtest_button = tk.Button(self.button_frame, \
                                        text='Add Test', \
                                        command=self.add_test)
        self.removetest_button = tk.Button(self.button_frame, \
                                        text='Remove Last Test',\
                                        command=self.remove_test)
        self.runtest_button = tk.Button(self.button_frame, \
                                        text='Run Test(s)',\
                                        command=self.run_test)
        self.quit_button = tk.Button(self.button_frame, \
                                     text='Quit', \
                                     command=self.main_window.destroy)
        self.addtest_button.pack(side=tk.LEFT, pady=10, padx=20)
        self.removetest_button.pack(side=tk.LEFT, pady=10, padx=20)
        self.runtest_button.pack(side=tk.LEFT, pady=10, padx=20)
        self.quit_button.pack(side=tk.LEFT, pady=10, padx=20)

        # Create and pack widget for test label frame
        self.tests_label = tk.Label(self.testlabel_frame, \
                                  text='List of tests to be run:')
        self.tests_label.pack(side=tk.LEFT)

        # Create and pack widget for text window frame
        self.tests_text = tk.Text(self.textwindow_frame, \
                                  height=15, width=100)
        self.tests_text.pack(expand='YES', fill=tk.BOTH, pady=3)

        # Create and pack widgets for number of tests frame
        self.teststorun_label = tk.Label(self.numtests_frame, \
                                         text='Tests Queued This Run: ')
        self.runcount = tk.StringVar()  # To update numtests_label
        self.numtests_label = tk.Label(self.numtests_frame, \
                                       textvariable=self.runcount)
        self.teststorun_label.pack(side=tk.LEFT)
        self.numtests_label.pack(side=tk.LEFT)

        # Create and pack widgets for tests completed frame
        self.testcomp_label = tk.Label(self.comptests_frame, \
                                       text='Tests Completed This Run: ')
        self.completed = tk.StringVar() # To update numcomp_label
        self.numcomp_label = tk.Label(self.comptests_frame, \
                                      textvariable=self.completed)
        self.testcomp_label.pack(side=tk.LEFT)
        self.numcomp_label.pack(side=tk.LEFT)

        # Pack the frames
        self.button_frame.pack()
        self.testlabel_frame.pack()
        self.textwindow_frame.pack()
        self.numtests_frame.pack()
        self.comptests_frame.pack()

        # Start the main loop
        tk.mainloop()

    # The add_test method is the callback function for the addtest_button widget
    def add_test(self):
        # Use file dialog to add script path to list one at a time
        files = filedialog.askopenfilename(filetypes =(("Shell Scripts", "*.sh"),
                                                        ("All Files","*.*")),
                                            title = "Choose a script file.")
        if files:
            # Copy path to string and strip characters then append to path list
            temp = str(files)
            temp = temp.replace("(", "").replace(")", "")
            temp = temp.replace("'", "").replace(",", "")
            scripts_list.append(temp)

            # Write changes to text box
            self.update_text_box()


    # The remove test method pops the last test in list, writes to text box
    def remove_test(self):
        if scripts_list:    #if not empty
            scripts_list.pop()
            self.update_text_box()

    # The run_test method is the callback function for runtest_button widget
    def run_test(self):
        # Make unique folder for today's date
        mydir = dt.now().strftime('%Y-%m-%d_%H-%M')
        
        # Create directory if not already created, handle exception if so
        if not os.path.exists(mydir):
            try:
                os.makedirs(mydir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                pass
        
        completed_count = 0
        #run the tests
        for script in scripts_list:
            # Make index for naming output files to match test numbers
            test_index = scripts_list.index(script) + 1
            test_num = '/test' + str(test_index) + ".txt"

            # Check os version: add & to end of command for linux
            osname = str(os.name)
            if osname == 'posix':
                mycmd = os.path.join(script) + " >> " + mydir + test_num + " &"
            else:
                mycmd = os.path.join(script) + " >> " + mydir + test_num
                
            # Call the script
            #os.system(mycmd)

            myarg = ""

            try:
                retcode = subprocess.check_call(mycmd + " myarg", shell=True)
                if retcode < 0:
                    print("Child terminated", -retcode, file=sys.stderr)
                else:
                    print("Child returned", retcode, file=sys.stderr)
            except OSError as e:
                print("Execution failed:", e, file=sys.stderr)

            # Update Completed Tests count
            completed_count += 1
            self.completed.set(str(completed_count))

    # Method to update text box
    def update_text_box(self):
        # Clear text box for writing appended list
        self.tests_text.delete('1.0', tk.END)
        
        # Write list of scripts to text box
        for path in scripts_list:
            # Append path to line in text box
            self.tests_text.insert(tk.END, path)
            self.tests_text.insert(tk.END, '\n')
            
        # Update 'Tests to Run' count in GUI for number of scripts selected
        self.runcount.set(len(scripts_list))
    

# Create an instance of the ScriptRunner class
script_run = ScriptRunner()
    
