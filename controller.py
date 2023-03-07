# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:17:46 2023

@author: marce
"""

import tkinter as tk
from tkinter import Label
import subprocess
import os
import sys
import time

from ahk import AHK, Hotkey, ActionChain



currentpath = os.getcwd()
newpath = os.path.join(currentpath, "addons")
os.chdir(newpath)

wait_time = 28000

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x800")  # Set initial window size
        self.master.title("My App")

        # Create label with instructions
        instructions = "NOTE: TO CLOSE AN ACTIVE FEATURE PRESS CTRL + ESC"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "bold"), fg="black")
        label.pack(pady=10)
        
        # Create label with instructions
        instructions = "To launch the activations press:\nRight Ctrl+Shift + the corresponding key \n only Ctrl + Numpad key for mouse \n Deactivation lasts 10 seconds"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "bold"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Invert Mouse Axis\n (right Ctrl+Numpad7)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Swap Left and Right Click\n (right Ctrl+Numpad8)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Disable Mouse Clicks\n (right Ctrl+Numpad9)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Disable W key (right Ctrl+Shift+W)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Disable S key (right Ctrl+Shift+S)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Disable D key (right Ctrl+Shift+D)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)

        # Create label with instructions
        instructions = "Disable A key (right Ctrl+Shift+A)"
        label = tk.Label(self.master, text=instructions, font=("Helvetica", 10, "italic"), fg="black")
        label.pack(pady=10)



        ahk = AHK()
        wait_time = 10000

        key_combo_mai = '>^Numpad7'
        script_mai = "Run mouse_axis_invert.exe\n sleep, {wait_time} \n Process, Close, mouse_axis_invert.exe".format(wait_time=wait_time)
        mouse_axis_invert_hotkey = Hotkey(ahk, key_combo_mai, script_mai)
        mouse_axis_invert_hotkey.start()

        key_combo_mbi = '>^Numpad8'
        script_mbi = "Run mouse_buttons_invert.exe\n sleep, {wait_time} \n Process, Close, mouse_buttons_invert.exe".format(wait_time=wait_time)
        m_b_invert_hotkey = Hotkey(ahk, key_combo_mbi, script_mbi)
        m_b_invert_hotkey.start()

        key_combo_mbd = '>^Numpad9'
        script_mbd = "Run mouse_buttons_disabled.exe\n sleep, {wait_time} \n Process, Close, mouse_buttons_disabled.exe".format(wait_time=wait_time)
        m_b_disable_hotkey = Hotkey(ahk, key_combo_mbd, script_mbd)
        m_b_disable_hotkey.start()


        key_combo_W = '>^>+W'
        script_W = "Run no_W.exe\n sleep, {wait_time} \n Process, Close, no_W.exe".format(wait_time=wait_time)
        W_disable_hotkey = Hotkey(ahk, key_combo_W, script_W)
        W_disable_hotkey.start()

        key_combo_A = '>^>+A'
        script_A = "Run no_A.exe\n sleep, {wait_time} \n Process, Close, no_A.exe".format(wait_time=wait_time)
        A_disable_hotkey = Hotkey(ahk, key_combo_A, script_A)
        A_disable_hotkey.start()
        
        key_combo_S = '>^>+S'
        script_S = "Run no_S.exe\n sleep, {wait_time} \n Process, Close, no_S.exe".format(wait_time=wait_time)
        S_disable_hotkey = Hotkey(ahk, key_combo_S, script_S)
        S_disable_hotkey.start()
        
        key_combo_D = '>^>+D'
        script_D = "Run no_D.exe\n sleep, {wait_time} \n Process, Close, no_D.exe".format(wait_time=wait_time)
        D_disable_hotkey = Hotkey(ahk, key_combo_D, script_D)
        D_disable_hotkey.start()
    


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
