""" ECE508 Project - Spring 2019 - Michael Engstrom

    GUI to help manage running shell scripts in Linux
    File dialog to open scripts
    Scripts saved one per line in file
    Read each line in file and execute scripts with
    saved console output in file for each
    Nice to Have: count of scripts and remaining or
    number completed

    Developed using Python 3.5"""

import tkinter as tk

class ScriptRunner:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()

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
        self.runtest_button = tk.Button(self.button_frame, \
                                        text='Run test(s)',\
                                        command=self.run_test)
        self.quit_button = tk.Button(self.button_frame, \
                                     text='Quit', \
                                     command=self.main_window.destroy)
        self.addtest_button.pack(side=tk.LEFT, pady=10, anchor='w')
        self.runtest_button.pack(side=tk.LEFT, pady=10)
        self.quit_button.pack(side=tk.LEFT, pady=10)

        # Create and pack widget for test label frame
        self.tests_label = tk.Label(self.testlabel_frame, \
                                  text='List of tests to be run:')
        self.tests_label.pack(side=tk.LEFT)

        # Create and pack widget for text window frame
        self.tests_text = tk.Text(self.textwindow_frame, \
                                  height=15, width=60)
        self.tests_text.pack(expand='YES', fill=tk.BOTH, pady=3)

        # Create and pack widgets for number of tests frame
        self.numtests_label = tk.Label(self.numtests_frame, \
                                       text='#')
        self.teststorun_label = tk.Label(self.numtests_frame, \
                                         text='Tests to Run')
        self.numtests_label.pack(side=tk.LEFT)
        self.teststorun_label.pack(side=tk.LEFT)

        # Create and pack widgets for tests completed frame
        self.numcomp_label = tk.Label(self.comptests_frame, \
                                      text='#')
        self.testcomp_label = tk.Label(self.comptests_frame, \
                                       text='Tests Completed')
        self.numcomp_label.pack(side=tk.LEFT)
        self.testcomp_label.pack(side=tk.LEFT)

        # Pack the frames
        self.button_frame.pack()
        self.testlabel_frame.pack()
        self.textwindow_frame.pack()
        self.numtests_frame.pack()
        self.comptests_frame.pack()

        # Start the main loop
        tk.mainloop()

    # The add_test method is the callback function for the
    # addtest_button widget

    def add_test(self):
        #file dialog
        print('printy!')

    # The run_test method is the callback function for the
    # runtest_button widget

    def run_test(self):
        #run the tests
        print('printoo!')

# Create an instance of the ScriptRunner class

script_run = ScriptRunner()
    
