from Tkinter import *
import Tkinter as tk

import os
import pyglet

from optparse import OptionParser

class RemindeCron(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+100+100".format(
            master.winfo_screenwidth()/2-pad, master.winfo_screenheight()/2-pad))


parser = OptionParser()
parser.add_option("-m", "--message", help="Reminder message")

(options, args) = parser.parse_args()


root=tk.Tk()
root.title("Reminder")

explanation = options.message
w2 = Label(root,
           justify=LEFT,
           pady = 50,
           font = "Helvetica 32",
           text="Reminder").pack(side="top")

w2 = Label(root,
           justify=LEFT,
           font = "Helvetica 32",
           text=explanation).pack(side="top")

root.wm_attributes('-topmost', 1)

app=RemindeCron(root)

crons_dir = os.path.dirname(os.path.realpath(__file__))
sound_file_path = os.path.join(crons_dir, 'tone.wav')

explosion = pyglet.media.load(sound_file_path, streaming=False)
explosion.play()

root.mainloop()
