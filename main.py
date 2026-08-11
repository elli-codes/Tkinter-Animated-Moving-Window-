from tkinter import *

class my_class:
    

    def __init__(self):
        
        self.m = 0
        self.n = 0

        self.root = Tk()
        #print(self.root.winfo_screenwidth())
        #print(self.root.winfo_screenheight())
        self.root.geometry("40x40+%d+%d" % (self.m, self.n))

        self.root.overrideredirect(True)
        self.root.config(bg="#ff0000")
        self.root.wm_attributes("-topmost",True)  
        self.root.after(500,self.move)

        self.root.mainloop()

    def move(self):

        if self.m <self.root.winfo_screenwidth()-100:
            self.m += 50
            self.root.geometry("40x40+%d+%d" % (self.m, self.n))

            self.root.after(500, self.move)

        else:
            self.root.config(bg="#00ff00")
            self.root.after(500, self.move_down)

    def move_down(self):

        if self.n < self.root.winfo_screenheight()-150:
            self.n += 50

            self.root.geometry("40x40+%d+%d" % (self.m, self.n))

            self.root.after(500, self.move_down)
        else:
            self.root.config(bg="#0000ff")
            self.root.after(500, self.move_left)

    def move_left(self):

         if self.m > 0:
        
            self.m -= 50
            self.root.geometry("40x40+%d+%d" % (self.m, self.n))

            self.root.after(500, self.move_left)
         else:
            self.root.config(bg="#ffffff")
            self.root.after(500, self.move_up)
            
    def move_up(self):

         if self.n > 0:
        
            self.n -= 50
            self.root.geometry("40x40+%d+%d" % (self.m, self.n))

            self.root.after(500, self.move_up)         

def main():
    x = my_class()
    

if __name__ == "__main__":main()
