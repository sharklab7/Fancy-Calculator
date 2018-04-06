

''''
Credits:

Developed by James George

This is a Fancy calculator performing the basic mathematical operations made using Tkinter module using OOP principles of the python programming language did as part of my self made projects.'''



from tkinter import Button,Label,Entry,Tk


class Calculator:

    #Constructor or the initializer method which is automatically called when this class is instantiated or when an instance / object is created 
     
    def __init__(self,master):

        # List to be accessible everywhere.    

        self.list = []

        # Global variable i which tracks the index position of elements within the list.

        self.i = -1

        self.sum = 0

        # Building up the UI part.
        
        # Setting the title which appears on the title bar of the window
        master.title('Calculator')

        # Setting both the width and height to 400 pixels
        master.geometry('400x500')

        # Setting background colour of the whole window
        master.config(bg='limegreen')

        # Preventing the windows from being resized.
        master.resizable(False, False)

        # Title
        self.heading_label = Label(text="Calculator",font='times 45 bold underline',fg='white',bg='limegreen')
        self.heading_label.grid(row=0,column=0,columnspan=4)

        # Blank label to leave a row empty so that there will be a space
        self.blank_label1 = Label(text="",font='times 30',bg='limegreen',width=16)
        self.blank_label1.grid(row=1,column=0,columnspan=4)

        # TextField where the operations performed will appear
        self.textfield = Entry(font='times 35 bold',width=16,bd=6,relief='raised')
        self.textfield.grid(row=2,column=0,columnspan=4)

        # Buttons being instantiated from the Button class by passing the requried parameters and placing them in order using the grid() method


        # First row
        
        self.seven = Button(text="7",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.seven_clicked)
        self.seven.grid(row=3,column=0)

        self.eigth = Button(text="8",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.eight_clicked)
        self.eigth.grid(row=3,column=1)

        self.nine = Button(text="9",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.nine_clicked)
        self.nine.grid(row=3,column=2)

        self.plus = Button(text="+",font='times 25 bold',relief='groove',width=4,bd=4,fg='maroon',bg='blue', command=self.add)
        self.plus.grid(row=3,column=3)

        #Second row

        self.four = Button(text="4",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.four_clicked)
        self.four.grid(row=4,column=0)

        self.five = Button(text="5",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.five_clicked)
        self.five.grid(row=4,column=1)

        self.six = Button(text="6",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.six_clicked)
        self.six.grid(row=4,column=2)

        self.subtract=Button(text="-",font='times 25 bold',relief='groove',width=4,bd=4,fg='lime',bg='magenta', command=self.subtract)
        self.subtract.grid(row=4,column=3)

        #Third row

        self.one = Button(text="1",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red',command=self.one_clicked)
        self.one.grid(row=5,column=0)

        self.two = Button(text="2",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.two_clicked)
        self.two.grid(row=5,column=1)

        self.three = Button(text="3",font='times 25 bold',relief='groove',width=4,bd=4,fg='blue',bg='red', command=self.three_clicked)
        self.three.grid(row=5,column=2)

        self.multiplication = Button(text="X",font='times 25 bold',relief='groove',width=4,bd=4,fg='skyblue',bg='darkgreen', command=self.multiply)
        self.multiplication.grid(row=5,column=3)

        #Fourth row

        self.negation = Button(text="+/-",font='times 25 bold',relief='groove',width=4,bd=4,fg='red',bg='blue', command=self.negation)
        self.negation.grid(row=6,column=0)

        self.result = Button(text="=",font='times 25 bold',relief='groove',width=4,bd=4,fg='red',bg='blue', command=self.equals)
        self.result.grid(row=6,column=1)

        self.delete = Button(text="DEL",font='times 25 bold',relief='groove',width=4,bd=4,fg='red',bg='blue', command=self.clear)
        self.delete.grid(row=6,column=2)

        self.division = Button(text="/",font='times 25 bold',relief='groove',width=4,bd=4,fg='yellow',bg='maroon', command=self.divide)
        self.division.grid(row=6,column=3)


    # These functions are invoked when buttons from 1-9 are tapped

    def one_clicked(self):
         self.textfield.insert(16, "1")


    def two_clicked(self):
         self.textfield.insert(16, "2")


    def three_clicked(self):
        self.textfield.insert(16, "3")


    def four_clicked(self):
        self.textfield.insert(16, "4")


    def five_clicked(self):
        self.textfield.insert(16, "5")


    def six_clicked(self):
        self.textfield.insert(16, "6")


    def seven_clicked(self):
        self.textfield.insert(16, "7")


    def eight_clicked(self):
        self.textfield.insert(16, "8")


    def nine_clicked(self):
        self.textfield.insert(16, "9")




    # Mathematical operations performed by these functions are invoked by respective button clicks

    def add(self):

        self.list.append(int(self.textfield.get()))
        self.i+=1
            
        self.sum += self.list[self.i]

        print(self.sum)     
             
        self.textfield.delete(0, 16)


    def subtract(self):

        self.list.append(int(self.textfield.get()))
        self.i+=1
        self.textfield.delete(0, 16)


    def multiply(self):

        self.list.append(int(self.textfield.get()))
        self.i+=1
        self.textfield.delete(0, 16)


    def divide(self):

        self.list.append(int(self.textfield.get()))
        self.i+=1
        self.textfield.delete(0, 16)


    def negation(self):

        self.textfield.insert(0, '-'+self.textfield.get())    
        self.list.append(int(self.textfield.get()*-1))

    def equals(self):
        pass


    def clear(self):

        self.textfield.delete(0, 16)


        


if __name__=='__main__':
    
    root = Tk()
    gui = Calculator(root)
    root.mainloop()
