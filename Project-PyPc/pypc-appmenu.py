import pypcfunc
import tkinter as tk
   
class A:
    #creates parent window
    def __init__(self):
               
        self.root = tk.Tk()
        self.root.geometry('500x500')
   
        self.frame1 = tk.Label(self.root,
                                    width = 400,
                                    height = 400,
                                    bg = '#AAAAAA')
        self.frame1.pack()
   
    #create menu
    def popup(self):
        self.popup_menu = tk.Menu(self.root,
                                       tearoff = 0)
          
        self.popup_menu.add_command(label = "Firefox",
                                    command = pypcfunc.app1)
          
        self.popup_menu.add_command(label = "Text Edit",
                                    command = pypcfunc.app2)
        
        self.popup_menu.add_command(label = "Minecraft",
                                    command = pypcfunc.app3)

        self.popup_menu.add_command(label = "File Browser", command = pypcfunc.app4)

        self.popup_menu.add_command(label = "Google Chrome", command = pypcfunc.app5)

        self.popup_menu.add_command(label = "Terminal", command = pypcfunc.app6)

        self.popup_menu.add_command(label = "Snapinator", command = pypcfunc.app7)
    
        self.popup_menu.add_command(label = "Gmail", command = pypcfunc.app8)

        self.popup_menu.add_command(label = "Spotfy", command = pypcfunc.app9)
        
        self.popup_menu.add_command(label = "Scratch", command = pypcfunc.app10)
        
        self.popup_menu.add_command(label = "Snap", command = pypcfunc.app11)
        
        self.popup_menu.add_command(label = "Photopea", command = pypcfunc.app12)

        self.popup_menu.add_command(label = "Calculator", command = pypcfunc.app13)

    #display menu on right click
    def do_popup(self,event):
        try:
            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)
        finally:
            self.popup_menu.grab_release()
   
    def hey(self,s):
        self.frame1.configure(text = s)
          
    def run(self):
        self.popup()
        self.root.bind("<Button-3>",self.do_popup)
        tk.mainloop()
  
a = A()
a.run()