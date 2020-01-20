# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:57:21 2019

@author: T-GOTOH
"""

import tkinter as tk
from canvas_extended import My_Canvas
#import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.canvas = My_Canvas(self, width=640, height=480, bg="#000000")
        self.canvas.pack(side="bottom")
        
        self.button_frame = tk.Frame(self.master)
                
        self.button_frame.next_state = tk.Button(self)
        self.button_frame.next_state["text"] = "Next"
        self.button_frame.next_state["command"] = self.canvas.next_state
        self.button_frame.next_state.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Start Simulation"
        self.button_frame.start_f["command"] = self.canvas.start_sim
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.stop_f = tk.Button(self)
        self.button_frame.stop_f["text"] = "Stop Simulation"
#        self.button_frame.stop_f["state"] = "disabled"
        self.button_frame.stop_f["command"] = self.canvas.stop_sim
        self.button_frame.stop_f.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Show ID"
        self.button_frame.start_f["command"] = self.canvas.show_id
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Hide ID"
        self.button_frame.start_f["command"] = self.canvas.hide_id
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Show exploration time"
        self.button_frame.start_f["command"] = self.canvas.show_time
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Hide exploration time"
        self.button_frame.start_f["command"] = self.canvas.hide_time
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Show delta"
        self.button_frame.start_f["command"] = self.canvas.show_delta
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.start_f = tk.Button(self)
        self.button_frame.start_f["text"] = "Hide delta"
        self.button_frame.start_f["command"] = self.canvas.hide_delta
        self.button_frame.start_f.pack(side="left")
        
        self.button_frame.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.button_frame.quit.pack(side="left")

        self.button_frame.pack(side="top")

root = tk.Tk()
app = Application(master=root)
app.mainloop()