# I M P O R T I N G
import time
import webbrowser as wb
import random as rd
import sys, subprocess
import tkinter as tk
from tkinter import *
from tkinter import messagebox

subprocess.run('cls', shell=True)
root= tk.Tk()
root1 = Tk()
#M I D D L E
def middle():
    subprocess.run('cls',shell=True)
    for i in range (15):
        for i in range (158):
            print(' ',end='')
    print("\n")

#C O N V E R T I N G
def converting():
        print("converting",end="")
        for i in range (3):
            time.sleep(0.8)
            print(".",end="")

    # Y E T   T O  BE  A D D E D
def exclemetry():
        for i in range (3):
            time.sleep(0.8)
            print("!",end ="")

    #C L E A R I N G   T H E   S C R E E N 
def clear_screen():
        run_again = 'PRESS ENTER TO RUN AGAIN...'
        for r in run_again:
            time.sleep(0.08)
            print(r,end='')
        input()
        subprocess.run('cls', shell=True)
    
    # O P E N I N G . . .

def opening():
        pr = "\nopening"
        for g in pr:
            time.sleep(0.008)
            print(g, end='')
        for v in range(3):
            time.sleep(0.18)
            print(".", end='')
        print("\n")   
        subprocess.run('cls',shell=True) 
middle()
opening()


    #E X I T 
def Exit():
        ex = "Initiating exiting protocal ..."
        for e in ex :
            time.sleep(0.08)
            print(e,end='')
        print("\n")
        time.sleep(3)
        quit()
        

def index():
        print('''

    choose the lesson that you want to study''')
        time.sleep(0.08)
        print('''
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 1: Electric Charges And Fields
    ----------------------------------------------------------------------------''')

        time.sleep(0.08)
        print('''Chapter 2: Electrostatic Potential And Capacitance
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 3:Current Electricity
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 4:Moving Charges and Magnetism
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 5:Magnetism and Matter
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 6:Electromagnetic Induction
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 7:Alternating Current
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 8:Electromagnetic Waves
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 9:Ray Optics and Optical Instruments
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 10:Wave Optics
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 11:Dual Nature of Radiation and Matter
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 12:Atoms
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 13: Nuclei
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 14:Semiconductor Electronics: Materials, Devices, and Simple Circuits
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''15. Extra revision notes
    ----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''16. EXIT
    ----------------------------------------------------------------------------''')
        time.sleep(0.18)
        print("Enter the chapter that you want to study: ")


# M E N U
def pdf():
        global root1
        root1.destroy()
        middle()
        opening()
        time.sleep(1)

# I N D E X
        index()

# O P E N E R
        chapterp = int(input())

        if chapterp == 1:
            pathp1 = 'https://drive.google.com/file/d/17RnbEFGoup4WIfhsBl7RtDuBI-T9L6dl/view?usp=sharing'
            opening()
            wb.open_new(pathp1)

        elif chapterp == 2:
            pathp2 = 'https://drive.google.com/file/d/1lDwUgWOo578hfvEb8L0fheZ16VtO2t5e/view?usp=sharing'
            opening()
            wb.open_new(pathp2)

        elif chapterp == 3:
            pathp3 = 'https://drive.google.com/file/d/1VQyjrpurD_oOoVme80YWRWoP0quMDHhZ/view?usp=sharing'
            opening()
            wb.open_new(pathp3)

        elif chapterp == 4:
            pathp4 = 'https://drive.google.com/file/d/1XBzUWpLTBR1VXB3t8c1GgusiB7gzWWl6/view?usp=sharing'
            opening()
            wb.open_new(pathp4)

        elif chapterp == 5:
            pathp5 = 'https://drive.google.com/file/d/1WV-Cks0cCA3AnNoAiyFQezOm8VW68Bt3/view?usp=sharing'
            opening()
            wb.open_new(pathp5)

        elif chapterp == 6:
            pathp6 = 'https://drive.google.com/file/d/1IDLaBboThXPcfbljfsLiXOQMy3jbBBJJ/view?usp=sharing'
            opening()
            wb.open_new(pathp6)

        elif chapterp == 7:
            pathp7 = 'https://drive.google.com/file/d/12X9we22fs5igH5DoNeRwJgaNZwi8YVc1/view?usp=sharing'
            opening()
            wb.open_new(pathp7)

        elif chapterp == 9:
            pathp9 = 'https://drive.google.com/file/d/1ywN6FtYJ1s6cAHuK8x6DDJ571ePKnQec/view?usp=sharing'
            opening()
            wb.open_new(pathp9)

        elif chapterp == 10:
            pathp10 = 'https://drive.google.com/file/d/1MuJpknBuaqHmoofhRVcOJq6j7_C_1DxY/view?usp=sharing'
            opening()
            wb.open_new(pathp10)

        elif chapterp == 11:
            pathp11 = 'https://drive.google.com/file/d/1Lsf7OLgmm0nbKWwCfIEScxDF2qnQKqBp/view?usp=sharing'
            opening()
            wb.open_new(pathp11)

        elif chapterp == 12:
            pathp12 = 'https://drive.google.com/file/d/1MwWPTBVQDyqUx4_CjNWbX_Z0X-ZAMTEg/view?usp=sharing'
            opening()
            wb.open_new(pathp12)

        elif chapterp == 13:
            pathp13 = 'https://drive.google.com/file/d/1LCkS4TCifVlv_-AZ4Ul0qVWqs_j3QVyy/view?usp=sharing'
            opening()
            wb.open_new(pathp13)

        elif chapterp == 14:
            pathp14 = 'https://drive.google.com/file/d/1a78WVeu9hIkBv-q9Ls5ZUK7E4olwf1ex/view?usp=sharing'
            opening()
            wb.open_new(pathp14)

        elif chapterp == 15:
            pathp15 = 'https://www.savemyexams.co.uk/a-level/physics/cie/22/revision-notes/'
            opening()
            wb.open_new(pathp15)

        elif chapterp == 16:
            quit()

        else:
            print("I N V A L I D  I N P U T")

def notes_opener():
        global root1
        root1.destroy()
        middle()
        opening()

        # O P E N E R
        print('''

    choose the lesson that you want to study''')
        time.sleep(0.08)
        print('''
----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''Chapter 1: Electric Charges And Fields
----------------------------------------------------------------------------''')

        time.sleep(0.08)
        print('''Chapter 2: Electrostatic Potential And Capacitance
----------------------------------------------------------------------------''')
        time.sleep(0.08)
        print('''3. Derivations
----------------------------------------------------------------------------''')
        print("4. EXIT")
        print("----------------------------------------------------------------------------")


        time.sleep(1)
        choice = int(input("Choose the chapter number: "))

        if choice == 1:
            pathn1 = "https://drive.google.com/file/d/12lknvtIK7uaHSOoz6vJ1rI7746eHgSCv/view?usp=share_link"
            opening()
            wb.open_new(pathn1)
            

        elif choice == 2:
            pathn2 = "https://drive.google.com/file/d/1Zc-FHi_VLshbH5o-6uZRAGOeOzgzUl6l/view?usp=share_link"
            opening()
            wb.open_new(pathn2)

        elif choice == 3:
            pathn3 = "https://drive.google.com/file/d/1GB5B9cT8svMTO2x-3uS7zpxr7sv_Nz5g/view?usp=share_link"
            opening()
            wb.open_new(pathn3)

        elif choice == 4:
            quit()

        else:
            print("I N V A L I D  I N P U T")
        print("\n")    

def sample_paper():
        paper_links = {1: "https://drive.google.com/file/d/10ArP6HtGo5pKQBK3_9M3FMVCxvdPfydZ/view?usp=share_link", 2: "https://drive.google.com/file/d/1XQkR8sa8bB8mu2iQpk5EHibSSgw8jRd6/view?usp=share_link",
                       3: "https://drive.google.com/file/d/1Yl0cd7Xdnqq-YWA8CsVxKEKob6gJVz6E/view?usp=share_link", 4: "https://drive.google.com/file/d/1JMOjfLSmEMxJ2iymQuLI5i5Cnu33YAAb/view?usp=share_link", 5: "https://drive.google.com/file/d/1ymDqJcv7Qy3qjrZfFzaSohLf091SEyBi/view?usp=share_link"}

# O P E N E R
        random_index = rd.randint(1, 5)
        paper = paper_links[random_index]
        opening()
        wb.open_new(paper)


def unit_con():
        global root1
        root1.destroy()
        middle()
        opening()

        print("Select conversion type:")
        menu_unit_converter='''
1. Length
2. Temperature
3. Weight
4. EXIT'''
        for menu_unit in menu_unit_converter:
            time.sleep(0.008)
            print(menu_unit,end='')
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            from_unit = input("Enter the unit you want to convert from (m, cm, ft): ")
            to_unit = input("Enter the unit you want to convert to (m, cm, ft): ")
            value = float(input("Enter the value: "))

            if from_unit == 'm' and to_unit == 'cm':
                converting()
                print("\n",value * 100, "cm")
            elif from_unit == 'cm' and to_unit == 'm':
                converting()
                print("\n",value / 100, "m")
            elif from_unit == 'm' and to_unit == 'ft':
                converting()
                print("\n",value * 3.28084, "ft" )
            elif from_unit == 'ft' and to_unit == 'm':
                converting()
                print("\n",value / 3.28084,"m")
            else:
                print("Invalid conversion")

        elif choice == 2:
            from_unit = input("Enter the unit you want to convert from (C, F): ")
            to_unit = input("Enter the unit you want to convert to (C, F): ")
            value = float(input("Enter the value: "))

            if from_unit == 'C' and to_unit == 'F':

                converting()
                print("\n",value * 9/5 + 32,"F")
            elif from_unit == 'F' and to_unit == 'C':
                converting()
                print("\n",value - 32 * 5/9,"C")
            else:
                print("Invalid conversion")

        elif choice == 3:
            from_unit = input("Enter the unit you want to convert from (kg, lb, g): ")
            to_unit = input("Enter the unit you want to convert to (kg, lb, g): ")
            value = float(input("Enter the value: "))
            if from_unit == 'kg' and to_unit == 'lb':
                converting()
                print("\n",value * 2.20462,"lb")
            elif from_unit == 'lb' and to_unit == 'kg':
                converting()
                print("\n",value / 2.20462,"kg")
            elif from_unit == 'kg' and to_unit == 'g':
                converting()
                print("\n",value * 1000,"g")
            elif from_unit == 'g' and to_unit == 'kg':
                converting()
                print("\n",value / 10000,"kg")
            else:
                print("Invalid conversion")
        elif choice == 4:
            Exit()
        
        else:
            print("I N V A L I D  I N P U T")
        print("\n")    




def check_password():
    global root
    global root1
    password = "i"
    if password_entry.get() == password:
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()
        root1.geometry("1080x720")
        root1.title("PHYSIC GUIDE")

        pdf_opener = Button(root1,text="BOOK PDF",padx = 120,pady = 50,command=pdf)
        pdf_opener.pack()

        notes = Button(root1,text="NOTES",padx = 130,pady = 50,command=notes_opener)
        notes.pack()        
        
        sample_question= Button(root1,text="SAMPLE PAPERS",padx = 100,pady = 50,command=sample_paper)
        sample_question.pack()

        unit_converter = Button(root1,text="UNIT CONVERTER",padx = 100,pady= 50,command = unit_con)
        unit_converter.pack()
        root1.mainloop

        
        # Add your code for displaying a video here
        
        root.mainloop()

    else:
        messagebox.showerror("Error", "Incorrect password")


#O U T P U T


root.geometry("1080x720")
root.title("PHYSIC GUIDE")

# Create the username label and entry
username_label = Label(root, text="Username:",)
username_label.pack()
username_entry = Entry(root,width=50,borderwidth=5)
username_entry.pack()

# Create the password label and entry
password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*",width=50,borderwidth=5)
password_entry.pack()

# Create the login button
login_button = Button(root, text="Login", command=check_password,fg="cyan") 
login_button.pack()

while True:
     root.mainloop()
