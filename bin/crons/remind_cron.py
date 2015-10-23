import Tkinter as tk

class RemindeCron(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+100+100".format(
            master.winfo_screenwidth()/2-pad, master.winfo_screenheight()/2-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom=geom

root=tk.Tk()
root.title("Reminder")
root.wm_attributes('-topmost', 1)

app=RemindeCron(root)

root.mainloop()
