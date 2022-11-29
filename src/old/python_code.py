import sys
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Scrollbar
from PIL import Image, ImageTk
from screeninfo import get_monitors
import webbrowser

f_n = 9
f_t1 = 18
f_t2 = 14

bl = '#2c56b0'
#bl1='#1e5b69'
bl1='#69281e'

class MyWindow:
    def __init__(self, window, width, height, RATIO):

        # _________________________________________________________________________________________________ #

        self.root = window
        self.main = ttk.Notebook(root)

        self.win = ttk.Frame(self.main)
        self.win2 = ttk.Frame(self.main)
        self.win3 = ttk.Frame(self.main)

        self.main.add(self.win, text = "Home")
        self.main.add(self.win2, text = "About")
        self.main.add(self.win3, text = "Analyzer")

        self.main.pack(expand = 1, fill = "both")

        self.w = width
        self.h = height

        # _________________________________________________________________________________________________ #
        
        self.bg = Image.open("steel.jpg")
        self.bg_tk = ImageTk.PhotoImage(self.bg.resize((width, height)))

        self.bg1_label = Label(self.win, image = self.bg_tk)
        self.bg1_label.place(relx=0, rely=0, anchor=NW)

        self.logo = Image.open("logo.jpg")
        self.logo = self.logo.resize((int(width/4), int(height/4)))
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logo_label = Label(self.win, image = self.logo)
        self.logo_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.logo_label.bind("<Button-1>", lambda e: self.show_website())

        self.title = Label(self.win, padx=20, pady=10, text="Atmospheric Corrosion Application", bg=bl, fg='white', font="Arial %d bold" % (RATIO*(f_t1+5)))
        self.title.place(relx = 0.5, rely=0.58, anchor=CENTER)

        self.info_text1 = Text(self.win, padx=16, pady=10, highlightthickness=0, height=7, width=80, bg=bl, fg="white", wrap=WORD, font="Arial %d" % (RATIO*f_n))
        self.info_text1.place(relx = 0.5, rely=0.8, anchor=CENTER)
        self.msg1 = '''This application is aimed towards users that would like to select stainless steel materials that may be susceptible atmoshperic corrosion. Simply specify an environment and the application will determine what materials are suitable for that environment. \n\nThe "About" tab provides an overview on atmpospheric corrosion. The analyzer can be found in the "Analyzer" tab.'''
        self.info_text1.insert("end", self.msg1)
        self.info_text1.config(state="disabled")
        
        # _________________________________________________________________________________________________ #

        self.bg2_label = Label(self.win2, image = self.bg_tk)
        self.bg2_label.place(relx=0, rely=0, anchor=NW)

        self.title = Label(self.win2, pady=8, text="Background to atmospheric corrosion\n                    and material selection with EN 1993-1-4                    ", bg=bl, fg='white', font="Arial %d bold" % (RATIO*f_t1))
        self.title.place(relx = 0.5, rely=0.1, anchor=CENTER)

        self.info_text1 = Text(self.win2,  padx=16, pady=10, highlightthickness=0, height=6, width=105, bg=bl, fg="white", wrap=WORD, font="Arial %d" % (RATIO*f_n))
        self.info_text1.place(relx = 0.5, rely=0.3, anchor=CENTER)
        self.msg1 = '''Atmospheric corrosion is the corrosion of metals exposed to air and its pollutants. It is an electrochemical process where a film of electrolyte forms on the metal surface due to condensation or even dew. When air pollutants such as SO2, CO2, NOX and salts dissolve in a film of water, they increase its conductivity and corrosivity. Atmospheric corrosion is a serious worldwide problem affecting people in all walks of life. It is of concern to homeowners, architects, engineers, designers, maintenance personnel and accountants. All outdoor and indoor materials exposed to the elements are potentially subjected to degradation resulting from atmospheric conditions.'''
        self.info_text1.insert("end", self.msg1)
        self.info_text1.config(state="disabled")
        
        self.info_text2 = Text(self.win2,  padx=16, pady=10, highlightthickness=0, height=13, width=105, bg=bl, fg="white", wrap=WORD, font="Arial %d" % (RATIO*f_n))
        self.info_text2.place(relx = 0.5, rely=0.64, anchor=CENTER)
        self.msg2 = "awe"
        self.info_text2.insert("end", self.msg2)
        self.info_text2.config(state="disabled")
        
        self.btn = Button(self.win2, padx=16, pady=10, text="Show corrosion map (RSA)", bg=bl, fg="white", font="Arial %d bold" % (RATIO*(f_t2)), command=self.show_map)
        self.btn.place(relx = 0.5, rely=0.92, anchor=CENTER)

        # _________________________________________________________________________________________________ #

        self.bg3_label = Label(self.win3, image = self.bg_tk)
        self.bg3_label.place(relx=0, rely=0, anchor=NW)

        self.title = Label(self.win3, padx=18, pady=10, text="Atmospheric Corrosion Analyzer", bg=bl, fg='white', font="Arial %d bold" % (RATIO*f_t1))
        self.title.place(relx = 0.5, rely=0.07, anchor=CENTER)

        self.select = Label(self.win3, padx=12, pady=7, text="Select the environment below:", bg=bl, fg='white', font="Arial %d bold" % (f_t2*RATIO))
        self.select.place(relx = 0.05, rely=0.2, anchor=NW)

        self.labelF1 = Label(self.win3, padx=10, pady=7, text="Risk of exposure to chlorides (F1):",  bg=bl, fg='white',font="Arial %d" % (f_n*RATIO))
        self.labelF1.bind("<Button-1>", lambda e: self.show_f1())

        self.labelF1.bind("<Enter>", lambda e: self.e1())
        self.labelF1.bind("<Leave>", lambda e: self.l1())

        self.labelF1.place(relx = 0.1, rely=0.275, anchor=NW)
        self.cb1 = Combobox(self.win3, state="readonly", values = ("Controlled", "Low", "Medium", "High", "Very High", "Severe"), width=int(f_n*RATIO), foreground="black",font="Arial %d bold" % (f_n*RATIO))
        self.cb1.place(relx = 0.75, rely=0.275, anchor=NW)

        self.labelF2 = Label(self.win3, padx=10, pady=7, text="Risk of exposure to sulpher dioxide (F2):", bg=bl, fg='white',font="Arial %d" % (f_n*RATIO))
        self.labelF2.bind("<Button-1>", lambda e: self.show_f2())
        self.labelF2.bind("<Enter>", lambda e: self.e2())
        self.labelF2.bind("<Leave>", lambda e: self.l2())

        self.labelF2.place(relx = 0.1, rely=0.325, anchor=NW)
        self.cb2 = Combobox(self.win3, state="readonly", values = ("Low", "Medium", "High"), width=int(f_n*RATIO), foreground="black",font="Arial %d bold" % (f_n*RATIO))
        self.cb2.place(relx = 0.75, rely=0.325, anchor=NW)

        self.labelF3 = Label(self.win3, padx=10, pady=7, text="Risk in cleaning regime (F3):", bg=bl, fg='white',font="Arial %d" % (f_n*RATIO))
        self.labelF3.bind("<Button-1>", lambda e: self.show_f3())
        self.labelF3.bind("<Enter>", lambda e: self.e3())
        self.labelF3.bind("<Leave>", lambda e: self.l3())

        self.labelF3.place(relx = 0.1, rely=0.375, anchor=NW)
        self.cb3 = Combobox(self.win3, state="readonly", values = ("Low", "Medium", "High"), width=int(f_n*RATIO), foreground="black",font="Arial %d bold" % (f_n*RATIO))
        self.cb3.place(relx = 0.75, rely=0.375, anchor=NW)

        self.calculate = Label(self.win3, padx=12, pady=7, text="Calculate Risk Class", bg=bl1, fg='white', font="Arial %d bold" % (f_t2*RATIO))
        self.calculate.place(relx = 0.05, rely=0.475, anchor=NW)

        self.btn = Button(self.win3, padx=16, pady=10, text="Calculate", bg=bl1, fg='white', font="Arial %d bold" % (f_n*RATIO), command=self.calc)
        self.btn.place(relx = 0.75, rely=0.475, anchor=NW)
        
        self.labelCRF = Label(self.win3, padx=10, pady=7, text="", bg=bl1, fg='white', font="Arial %d" % (f_n*RATIO))
        self.labelCRC = Label(self.win3, padx=10, pady=7, text="", bg=bl1, fg='white', font="Arial %d" % (f_n*RATIO))

        self.suit = Label(self.win3, padx=12, pady=7, text="", bg='#262c3b', fg='white', font="Arial %d bold" % (f_t2*RATIO))

        self.T = Text(self.win3,  padx=16, pady=10, highlightthickness=0, height = 4.5, width = 38, background='#262c3b', foreground='white', font="Arial %d" % (f_n*RATIO))
        self.T_label = Label(self.win3, text="Note that the textbox above can scroll.", bg='#262c3b', fg='white', font="Arial %d" % ((f_n-1)*RATIO))

    # _________________________________________________________________________________________________ #

    def show_website(self):
        webbrowser.open_new_tab("https://sassda.co.za/")

    def show_map(self):
        root = Toplevel()

        w = int(0.75*self.w)
        h = int(0.6*self.h)

        root.geometry("%dx%d" % (w, h))
        root.title("Corrosion Map")
        
        bg = Image.open("map.jpg")
        bg = bg.resize((w, h))
        bg = ImageTk.PhotoImage(bg)
        bg_label = Label(root, image = bg)
        bg_label.place(relx=0, rely=0, anchor=NW)
        bg_label.image = bg

        root.mainloop()

    # _________________________________________________________________________________________________ #

    def show_f1(self):
        root = Toplevel()

        root.title("F1: Risk of exposure to chlorides")

        lst = [("Risk", "Description", "F1"),
                ("Controlled", "Internally controlled environment", 1),
                ("Low", "M > 10km  OR  S > 0.1km", 0),
                ("Medium", "5km < M <= 10km  OR  0.01km < S <= 0.1km", -3),
                ("High", "0.5km < M <= 5km  OR  S <= 0.01km", -7),
                ("Very High", "M <= 0.5km", -10),
                ("Severe", "M <= 0.25km", -15)] 
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):

                if (i == 0):
                    e = Entry(root, width=40, fg=bl, font=('Arial',20,'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])
                else:
                    e = Entry(root, width=40, fg="black", font=('Arial',20))
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])

        root.mainloop()
    
    def show_f2(self):
        root = Toplevel()
        root.title("F2: Risk of exposure to sulpher dioxide")
        
        lst = [("Risk", "Description", "F2"),
                ("Low", "10 μg/m³ average deposition", 0),
                ("Medium", "10 to 90 μg /m³ average deposition", -5),
                ("High", "90 to 250 μg /m³ average deposition", -10)]
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):

                if (i == 0):
                    e = Entry(root, width=40, fg=bl, font=('Arial',20,'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])
                else:
                    e = Entry(root, width=40, fg="black", font=('Arial',20))
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])

        root.mainloop()
    
    def show_f3(self):
        root = Toplevel()
        root.title("F3: Risk in cleaning regime")

        lst = [("Risk", "Description", "F3"),
                ("Low", "Fully exposed to washing by rain", 0),
                ("Medium", "Specified cleaning regime", -2),
                ("High", "No washing by rain /No specified cleaning", -7)]
         
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):

                if (i == 0):
                    e = Entry(root, width=40, fg=bl, font=('Arial',20,'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])
                else:
                    e = Entry(root, width=40, fg="black", font=('Arial',20))
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])

        root.mainloop()

    def e1(self):
        self.labelF1.config(bg="darkblue")

    def l1(self):
        self.labelF1.config(bg=bl)

    def e2(self):
        self.labelF2.config(bg="darkblue")

    def l2(self):
        self.labelF2.config(bg=bl)

    def e3(self):
        self.labelF3.config(bg="darkblue")

    def l3(self):
        self.labelF3.config(bg=bl)

    def calc(self):
        if ((self.cb1.get() == "") or (self.cb2.get() == "") or (self.cb3.get() == "")):
            messagebox.showinfo("Warning", "Please select the environment (F1, F2, & F3)")
            return

        d1 = {
                "Controlled" : 1,
                "Low" : 0,
                "Medium" : -3,
                "High" : -7,
                "Very High" : -10,
                "Severe" : -15
        }

        d2 = {
                "Low" : 0,
                "Medium" : -5,
                "High" : -10
        }

        d3 = {
                "Low" : 0,
                "Medium" : -2,
                "High" : -7
        }

        # /** CRF **/

        f1 = d1.get(self.cb1.get(), self.cb1.get())
        f2 = d2.get(self.cb2.get(), self.cb2.get())
        f3 = d3.get(self.cb3.get(), self.cb3.get())

        i_crf = f1+f2+f3
        crf = "Corrosion Risk Factor (CRF) = " + str(i_crf)
        self.labelCRF.config(text=crf)

        # /** CRC **/

        class1 = ("3CR12 (Ferritic)", "430 (Ferritic)", "409 (Ferritic)")
        class2 = ("304 (MO Austenitic)", "304L (MO Austenitic)", "304LN (MO Austenitic)", "321 (MO Austenitic)", "301LN (MO Austenitic)", "304 DDQ (MO Austenitic)", "304Cu (MO Austenitic)", "2001 (Lean Duplex)")
        class3 = ("316 (Standard Austenitic)", "316L (Standard Austenitic)", "316L2.5Mo (Standard Austenitic)", "316Ti (Standard Austenitic)", "316LN (Standard Austenitic)", "316LCu (Standard Austenitic)", "2404 (Standard Austenitic)", "2304 (Lean Duplex)", "2202 (Lean Duplex)", "2102 (Lean Duplex)")
        class4 = ("317LMN (Super Austenitic)", "904L (Super Austenitic)", "2205 (Duplex / Super Duplex)")
        class5 = ("254SMO (Super Austenitic)", "S34565 (Super Austenitic)", "NO8926 (Super Austenitic)", "2507 (Duplex / Super Duplex)", "S32760 (Duplex / Super Duplex)", "UNS32520 (Duplex / Super Duplex)")

        crc_class = ""
        
        self.T.config(state=NORMAL)        
        
        if (i_crf == 1):
            crc = "Corrosion Risk Class (CRF) = I"
            for i in range(len(class1)):
                crc_class += class1[i] + "\n"
        elif (i_crf <= 0 and i_crf > -7):
            crc = "Corrosion Risk Class (CRF) = II"
            for i in range(len(class2)):
                crc_class += class2[i] + "\n"
        elif (i_crf <= -7 and i_crf > -15):
            crc = "Corrosion Risk Class (CRF) = III"
            for i in range(len(class3)):
                crc_class += class3[i] + "\n"
        elif (i_crf <= -15 and i_crf > -20):
            crc = "Corrosion Risk Class (CRF) = IV"
            for i in range(len(class4)):
                crc_class += class4[i] + "\n"
        else:
            crc = "Corrosion Risk Class (CRF) = V"
            for i in range(len(class5)):
                crc_class += class5[i] + "\n"
        
        self.labelCRC.config(text=crc)
        self.suit.config(text="Suitable Materials")
        self.T.delete('1.0', END)
        self.T.insert(END, crc_class)
        self.T.delete(END)
        self.T.config(state=DISABLED)
        
        self.labelCRF.place(relx = 0.1, rely=0.55, anchor=NW)
        self.labelCRC.place(relx = 0.1, rely=0.60, anchor=NW)
        self.suit.place(relx = 0.05, rely=0.70, anchor=NW)
        self.T.place(relx=0.1, rely=0.775, anchor=NW)
        self.T_label.place(relx=0.1, rely=0.99, anchor=SW)

# _________________________________________________________________________________ #

root = Tk()

RATIO = 1.0
if sys.platform == "darwin":
    RATIO = 1.5
elif sys.platform == "win32":
    RATIO = 1.9
else:
    RATIO = 1.0

width, height = -1, -1
for m in get_monitors():
    if (m.is_primary):
        width = m.width
        height = m.height

# _________________________________________________________________________________ #

root.option_add('*Dialog.msg.font', 'Arial 9')
root.title("Atmospheric Corrosion Application")
root.geometry("%dx%d" % (width, height))

style = ttk.Style(root)
style.configure('TFrame', background=bl)

window = MyWindow(root, width, height, RATIO)

root.mainloop()
