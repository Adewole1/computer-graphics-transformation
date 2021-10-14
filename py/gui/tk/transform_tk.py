import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox
from PIL import ImageTk, Image

from math import radians, cos, sin
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import sys
import os

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Transformation App')
        self.geometry('600x420+50+50')
        
        # self.icon=ImageTk.PhotoImage(Image.open('..\\icons\\jaayee.png'))
        # self.wm_iconphoto(self, self.icon)
        
        self.label1_text = StringVar()
        self.label1_text.set("Enter transformation")
        self.label1=tk.Label(self, textvariable=self.label1_text)
        self.label1.grid(row=0, column=0, padx=2, pady=5)
        
        self.word_text=tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.word_text)
        self.e1.grid(row=0, column=1, padx=5)
        
        # self.join=ImageTk.PhotoImage(Image.open('icons\\connect circle.ico'))
        self.enter_btn=tk.Button(self, text='Enter', command=self.open_transform, relief=tk.RAISED, width=10)
        self.enter_btn.grid(row=0, column=2)
        
        self.start_btn = tk.Button(self, text='Start Again', command=self.start_again, relief=tk.RAISED, width=10)
        self.start_btn.grid(row=0, column=3)
        
        self.exit_btn = tk.Button(self, text='Exit', command=self.destroy, relief=tk.RAISED, width=10)
        self.exit_btn.grid(row=0, column=4)
        
        self.instruction=tk.Label(self, text='Instruction:', justify='left')
        self.instruction.grid(row=1, column=0)
        
        self.info=tk.Label(self, text='Data:', justify='left')
        self.info.grid(row=1, column=3)
        
        self.ins_label =StringVar()
        self.ins_label.set('Enter the transformation you want to do: \nT - Translate, \nO - Rotate, \nC - Scale, \nS - Shear, \nR - Reflect, \nD - Done\nL - To clear transformations')
        self.instructions=tk.Label(self, textvariable=self.ins_label, wraplength=200, relief=tk.RIDGE, justify='left', height=20, width=30)
        self.instructions.grid(row=2, column=0, columnspan=2, padx=2, ipadx=20)
        
        self.info_label =StringVar()
        self.info_label.set('Your transformation(s):')
        self.infos=tk.Label(self, textvariable=self.info_label, wraplength=200, relief=tk.RIDGE, justify='left', height=20, width=30)
        self.infos.grid(row=2, column=3, columnspan=3, padx=2)
        
        
        self.transformations_list = {
            'T': 'Translate',
            'O': 'Rotate',
            'C': 'Scale',
            'S': 'Shear',
            'R': 'Reflect'
        }
            
    def open_transform(self):
        
        try:
            self.transform_list = self.transform_list
        except AttributeError:
            self.transform_list = []
        transform = self.word_text.get().capitalize()
        
        if transform in self.transformations_list.keys():
            value = self.info_label.get()
            self.transform_list.append(transform)
            self.info_label.set(value + '\n' + self.transformations_list[transform])
            self.word_text.set('')
        elif transform == "D":
            if len(self.transform_list) == 0:
                info = "You have entered no transformation, try again."
                messagebox.showerror("Error", info)
                # self.info_label.set(info)
            else:
                # self.enter_btn.bind("<Button>", self.point)
                info = "Enter the coordinates of the shape in the format (x,y), \nD - done, or \nL - Clear Coordinates:"
                self.ins_label.set(info)
                self.label1_text.set("Enter coordinates")
                value = self.info_label.get()
                self.info_label.set(value + '\n\n' + 'Your coordinates:')
                self.enter_btn['command'] = self.point
                self.word_text.set('')
        elif transform == 'L':
            self.transform_list = []
            messagebox.showinfo("Information", "Transformation Cleared")
            self.word_text.set('')
            self.info_label.set('')
            # self.open_transform()
        else:
            info = "You have entered an incorrect transformation, try again."
            # self.info_label.set(info)
            messagebox.showerror("Error", info)
        # print(self.transform_list)
    
    def start_again(self):
        self.transform_list = []
        self.coordinates = []
        info = "Enter the transformation you want to do: \nT - Translate, \nO - Rotate, \nC - Scale, \nS - Shear, \nR - Reflect, \nD - Done\nC - To clear transformations"
        self.ins_label.set(info)
        self.label1_text.set("Enter transformation")
        self.enter_btn['command'] = self.open_transform
        self.info_label.set('Your transformation(s):')
        self.word_text.set('')
        
    def point(self):
        # info = "Enter the coordinates of the shape in the format (x,y) or 'D' when done or cLear to start again or Start again:"
        # self.ins_label.set(info)
        try:
            self.coordinates = self.coordinates
        except AttributeError:
            self.coordinates = []
        coord = []
        coord_in = self.word_text.get()
        if coord_in == "":
            info = "You have entered no coordinates, try again."
            messagebox.showerror("Error", info)
        else:
            if str(coord_in).capitalize() == "D":
                if len(self.coordinates) == 1 and len(self.transform_list) == 1 and self.transform_list[0] == 'T':
                    pass
                elif len(self.coordinates) == 2:
                    pass
                elif len(self.coordinates) > 2:
                    pass
                elif len(self.coordinates) == 0:
                    info = "You have entered no coordinates, try again."
                    messagebox.showerror("Error", info)
                        # self.coordinates.append(self.coordinates[0])
                else:
                    info = 'Cannot transform a point, Check transformation and points.'
                    messagebox.showerror("Error", info)
                    self.transform_list = []
                    self.coordinates = []
                    info = "Enter the transformation you want to do: \nTranslate, rOtate, sCale, Shear, Reflect \nor Done when you are done or cLear to start again:"
                    self.ins_label.set(info)
                    self.enter_btn['command'] = self.open_transform
                    self.word_text.set('')
                    # self.open_transform()
                check1 = len(self.coordinates[0])
                if check1 in range(3,5):
                    for i in range(1, len(self.coordinates)):
                        if check1 == len(self.coordinates[i]):
                            # print("Check {0} complete".format(i))
                            pass
                        else:
                            # print("Coordinate {0} not homogenous".format(i+1))
                            info = 'The coordinates are not homogenous, \nInput the coordinates again.'
                            messagebox.showerror("Error", info)
                            self.coordinates = []
                        break
                else:
                    info = "Can only transform in 2D and 3D, check coordinates."
                    messagebox.showerror("Error", info)
                    self.coordinates = []
                    # self.point()
                value = self.info_label.get()
                info = "Coordinates are Homogenous"
                self.info_label.set(value + '\n\n' + info)
                self.transform_coordinates()
            elif coord_in.capitalize() == "L":
                self.coordinates = []
                messagebox.showinfo("Information", "Coordinates Cleared")
                self.word_text.set('')
                self.info_label.set('')
            else:
                try:
                    value = self.info_label.get()
                    self.info_label.set(value + '\n' + coord_in)
                    # self.info_label.set(coord_in)
                    coord_in = coord_in.split(',')
                    # print(coord_in)
                    for i in range(0, len(coord_in)):
                        coord.append(float(coord_in[i]))
                    coord.append(1)
                    self.coordinates.append(list(coord))
                    self.word_text.set('')
                    # print(self.coordinates)
                except:
                    info = 'An error occured with the coordinates, try again.'
                    messagebox.showerror("Error", info)
                    
        # pass
          
    def transform_coordinates(self):
        # print(self.transform_list)
        # print(self.coordinates)
        
        transformations_list = {
            'T': 'Translate',
            'O': 'Rotate',
            'C': 'Scale',
            'S': 'Shear',
            'R': 'Reflect'
        }
        self.M = np.array(self.coordinates)
        self.M1 = self.M
        self.transformed_list = []
        self.rot=''
        self.cord = ''
        
        for i in self.transform_list:
            self.M3 = ''
            
            if i == 'T':
                messagebox.showinfo("Info", "Only fill translation in z direction for 3D transformation")
                translate_window = Translate(self)
                self.M1 = np.dot(self.M1, self.M3)
                
            elif i == 'C':
                messagebox.showinfo("Info", "Only fill scale in z direction for 3D transformation")
                scale_window = Scale(self)
                self.M1 = np.dot(self.M1, self.M3)
            
            elif i == 'S':
                messagebox.showinfo("Info", "Leave line parameter empty, \nif shearing is not realtive to another line")
                messagebox.showinfo("Info", "When shearing in 3D, \nEnter shear parameter in format \'shear1, shear2\'")
                shear_window = Shear(self)
                self.M1 = np.dot(self.M1, self.M3)
            
            elif i == 'R':
                messagebox.showinfo("Info", "Fill only plane to reflect about for 3D")
                messagebox.showinfo("Info", "Fill only axis of line to reflect about \nif reflecting about a line")
                reflect_window = Reflect(self)
                self.M1 = np.dot(self.M1, self.M3)
                
            elif i == 'O':
                messagebox.showinfo("Info", "Enter the angle of rotation: \n(If clockwise, add a negative before the angle.) \n")
                messagebox.showwarning("Info", "If 2D, leave \'axis\' field empty")
                rotate_window = Rotate(self)
                if self.rot == 'P':
                    try:
                        T = np.eye(3)
                        print(T)
                        # print(self.cord)
                        Tx = int(self.cord[0])
                        Ty = int(self.cord[1])
                        T[2][0] = Tx
                        T[2][1] = Ty
                        print('Translate:', T)
                        M2 = np.dot(self.M1, T)
                        print(M2)
                        M2 = np.dot(M2, self.M3)
                        print(M2)
                        T = np.eye(3)
                        Tx = -int(self.cord[0])
                        Ty = -int(self.cord[1])
                        T[2][0] = Tx
                        T[2][1] = Ty
                        
                        M6 = np.dot(M2, T.astype(np.float16))
                        self.M1 = M6.astype(np.int16)
                    except:
                        messagebox.showerror("Error", "Error rotating about a point")
                        app.mainloop()

                else:
                    self.M1 = np.dot(self.M1, self.M3)
            self.transformed_list.append(self.M3)
        
        if len(self.M1[0]) == 3:
            X1 = self.M[:, 0]
            X1 = np.append(X1, X1[0])
            Y1 = self.M[:, 1]
            Y1 = np.append(Y1, Y1[0])
            X2 = self.M1[:, 0]
            X2 = np.append(X2, X2[0])
            Y2 = self.M1[:, 1]
            Y2 = np.append(Y2, Y2[0])
            plt.plot(X1, Y1, '-')
            plt.plot(X2, Y2, '--')
            plt.legend(['Original Shape', 'Transformed shape'])
            plt.show()
        else:
            # mpl.rcParams[‘legend.fontsize’] = 10
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            X1 = self.M[:, 0]
            X1 = np.append(X1, X1[0])
            Y1 = self.M[:, 1]
            Y1 = np.append(Y1, Y1[0])
            Z1 = self.M[:, 2]
            Z1 = np.append(Z1, Z1[0])
            X2 = self.M1[:, 0]
            X2 = np.append(X2, X2[0])
            Y2 = self.M1[:, 1]
            Y2 = np.append(Y2, Y2[0])
            Z2 = self.M1[:, 2]
            Z2 = np.append(Z2, Z2[0])
            ax.plot(X1, Y1, Z1)
            ax.plot(X2, Y2, Z2)
            fig.show()
            
        # value = self.info_label.get()
        # self.info_label.set(value + '\n\n' + 'Your coordinates are:\n' + str(self.M))
        value = self.info_label.get()
        self.info_label.set(value + '\n\n' + 'Your new coordinates after transformation are:\n' + str(self.M1))
        # print("\nYour coordinates are: \n", self.M)
        # print("\nYour new coordinates after transformation are: \n", self.M1)
        # print("\nYour transformation coordinates are: \n", self.transformed_list)


class Translate(tk.Toplevel):
    
    def __init__(self, master):
        
        super().__init__(master)
        # self.root=root
        self.title('Translate page')
        self.maxsize(width=550,height=280)
        
        self.label1 = tk.Label(self, text='Translation in X-direction')
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label1 = tk.Label(self, text='Translation in Y-direction')
        self.label1.grid(row=2, column=0, padx=5, pady=5)
        
        self.label1 = tk.Label(self, text='Translation in Z-direction')
        self.label1.grid(row=4, column=0, padx=5, pady=5)
        
        self.word1_text=tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.word1_text)
        self.e1.grid(row=1,column=0)
        
        self.word2_text=tk.StringVar()
        self.e2=tk.Entry(self, textvariable=self.word2_text)
        self.e2.grid(row=3,column=0)
        
        self.word3_text=tk.StringVar()
        self.e3=tk.Entry(self, textvariable=self.word3_text)
        self.e3.grid(row=5,column=0)
        
        self.btn = tk.Button(self, command=self.okay, text='Done', relief=tk.RAISED)
        self.btn.grid(row=6, column=0, columnspan=2)
        
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
        
        
    def okay(self):
        try:
            if len(self.master.M1[0]) == 3:
                T = np.eye(3)
                Tx = self.word1_text.get()
                Ty = self.word2_text.get()
                T[2][0] = Tx
                T[2][1] = Ty
            else:
                T = np.eye(4)
                Tx = self.word1_text.get()
                Ty = self.word2_text.get()
                Tz = self.word3_text.get()
                T[3][0] = Tx
                T[3][1] = Ty
                T[3][2] = Tz
            self.master.M3 = T
            self.destroy()
        except:
            messagebox.showerror("Error", "An error occured, try again")
            self.word1_text.set('')
            self.word2_text.set('')
            self.word3_text.set('')
            

class Rotate(tk.Toplevel):
    
    def __init__(self, master):
        
        super().__init__(master)
        # self.root=root
        self.title('Rotate page')
        self.maxsize(width=700,height=300)
        
        self.label1 = tk.Label(self, text='Rotation angle')
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label2 = tk.Label(self, text='Rotate about a Point or Origin?')
        self.label2.grid(row=2, column=0, padx=5, pady=5)
        
        self.label3 = tk.Label(self, text='Enter arbitrary point to rotate about in format \'x,y\':')
        self.label3.grid(row=4, column=0, padx=5, pady=5)
        
        self.label4 = tk.Label(self, text='Enter axis of rotation (X or Y or Z):')
        self.label4.grid(row=6, column=0, padx=5, pady=5)
        
        self.word1_text=tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.word1_text)
        self.e1.grid(row=1,column=0)
        
        self.word2_text=tk.StringVar()
        self.e2=tk.Entry(self, textvariable=self.word2_text)
        self.e2.grid(row=3,column=0)
        
        self.word3_text=tk.StringVar()
        self.e3=tk.Entry(self, textvariable=self.word3_text)
        self.e3.grid(row=5,column=0)
        
        self.word4_text=tk.StringVar()
        self.e4 = tk.Entry(self, textvariable=self.word4_text)
        self.e4.grid(row=7,column=0)
        
        self.btn = tk.Button(self, command=self.okay, text='Done', relief=tk.RAISED)
        self.btn.grid(row=8, column=0)
        
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
        
        
    def okay(self):
        try:
            tita = int(self.word1_text.get())
            costita = cos(radians(tita))
            sintita = sin(radians(tita))
            self.master.rot = self.word2_text.get().capitalize()
            if len(self.master.M1[0]) == 3:
                O = np.eye(3)
                O[0][0] = costita
                O[1][1] = costita
                O[0][1] = sintita
                O[1][0] = -sintita
                
                # print(O)
                
                if self.master.rot == 'P':
                    self.master.cord = self.word3_text.get().split(',')
                    
                
                else:
                    pass
            
            else:
                O = np.eye(4)
                axis = self.word4_text.get().capitalize()
                if axis.capitalize() == 'X':
                    O[1][1] = costita
                    O[2][2] = costita
                    O[1][2] = sintita
                    O[2][1] = -sintita
                elif axis.capitalize() == 'Y':
                    O[0][0] = costita
                    O[2][2] = costita
                    O[2][0] = sintita
                    O[0][2] = -sintita
                elif axis.capitalize() == 'Z':
                    O[0][0] = costita
                    O[1][1] = costita
                    O[0][1] = sintita
                    O[1][0] = -sintita
                    
            self.master.M3 = O
            self.destroy()
        except:
            messagebox.showerror("Error", "An error occured, try again")
            self.word1_text.set('')
            self.word2_text.set('')
            self.word3_text.set('')
            self.word4_text.set('')
            
            
class Scale(tk.Toplevel):
    def __init__(self, master):
        
        super().__init__(master)
        # self.root=root
        self.title('Scale page')
        self.maxsize(width=700,height=300)
        
        self.label1 = tk.Label(self, text='Enter the scale size in x-direction:')
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label2 = tk.Label(self, text='Enter the scale size in y-direction:')
        self.label2.grid(row=2, column=0, padx=5, pady=5)
        
        self.label3 = tk.Label(self, text='Enter the scale size in z-direction:')
        self.label3.grid(row=4, column=0, padx=5, pady=5)
        
        self.word1_text=tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.word1_text)
        self.e1.grid(row=1,column=0)
        
        self.word2_text=tk.StringVar()
        self.e2=tk.Entry(self, textvariable=self.word2_text)
        self.e2.grid(row=3,column=0)
        
        self.word3_text=tk.StringVar()
        self.e3=tk.Entry(self, textvariable=self.word3_text)
        self.e3.grid(row=5,column=0)
        
        self.btn = tk.Button(self, command=self.okay, text='Done', relief=tk.RAISED)
        self.btn.grid(row=6, column=0)
        
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
        
        
    def okay(self):
        try:
            if len(self.master.M1[0]) == 3: #For 2D
                C = np.eye(3)
                Cx = float(self.word1_text.get())
                Cy = float(self.word2_text.get())
                C[0][0] = Cx
                C[1][1] = Cy
                
            else: #For 3D
                C = np.eye(4)
                Cx = float(self.word1_text.get())
                Cy = float(self.word2_text.get())
                Cz = float(self.word3_text.get())
                C[0][0] = Cx
                C[1][1] = Cy
                C[2][2] = Cz
            self.master.M3 = C
            self.destroy()
        except:
            messagebox.showerror("Error", "An error occured, try again")
            self.word1_text.set('')
            self.word2_text.set('')
            self.word3_text.set('')


class Shear(tk.Toplevel):
    def __init__(self, master):
        
        super().__init__(master)
        # self.root=root
        self.title('Shear page')
        self.maxsize(width=700,height=300)
        
        self.label1 = tk.Label(self, text='Shear parameter:')
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label2 = tk.Label(self, text='Direction of shear (x, y or z):')
        self.label2.grid(row=2, column=0, padx=5, pady=5)
        
        self.label3 = tk.Label(self, text='Shear relative to another line? R or N):')
        self.label3.grid(row=4, column=0, padx=5, pady=5)
        
        self.label4 = tk.Label(self, text='Line parameter:')
        self.label4.grid(row=6, column=0, padx=5, pady=5)
        
        self.word1_text=tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.word1_text)
        self.e1.grid(row=1,column=0)
        
        self.word2_text=tk.StringVar()
        self.e2=tk.Entry(self, textvariable=self.word2_text)
        self.e2.grid(row=3,column=0)
        
        self.word3_text=tk.StringVar()
        self.e3=tk.Entry(self, textvariable=self.word3_text)
        self.e3.grid(row=5,column=0)
        
        self.word4_text=tk.StringVar()
        self.e4 = tk.Entry(self, textvariable=self.word4_text)
        self.e4.grid(row=7,column=0)
        
        self.btn = tk.Button(self, command=self.okay, text='Done', relief=tk.RAISED)
        self.btn.grid(row=8, column=0)
        
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
        
        
    def okay(self):
        try:
            if len(self.master.M1[0]) == 3: #For 2D
                S = np.eye(3)
                sh = self.word1_text.get()
                axis = self.word2_text.get()
                rel = self.word3_text.get()
                sh = float(sh)
                if rel.capitalize() == 'R':
                    rel_para = self.word4_text.get()
                    rel_para = float(rel_para)
                    if axis.capitalize() == 'Y':
                        S[2][1] = -sh*rel_para
                    elif axis.capitalize() == 'X':
                        S[2][0] = -sh*rel_para
                elif rel.capitalize() == 'N':
                    pass
                
                if axis.capitalize() == 'Y':
                    S[0][1] = sh
                
                elif axis.capitalize() == 'X':
                    S[1][0] = sh
                    
            else: #For 3D
                S = np.eye(4)
                sh = self.word1_text.get()
                axis = self.word2_text.get()
                rel = self.word3_text.get()
                axes = ['X', 'Y', 'Z']
                axes.remove(axis)
                sh = sh.split(',')
                if axis.capitalize() == 'X':
                    S[0][1] = float(sh[0])
                    S[0][2] = float(sh[1])
                elif axis.capitalize() == 'Y':
                    S[1][0] = float(sh[0])
                    S[1][2] = float(sh[1])
                elif axis.capitalize() == 'Z':
                    S[2][0] = float(sh[0])
                    S[2][1] = float(sh[1])
            self.master.M3 = S.astype(np.float16)
            self.destroy()
        except:
            messagebox.showerror("Error", "An error occured, try again")
            self.word1_text.set('')
            self.word2_text.set('')
            self.word3_text.set('')
            self.word4_text.set('')
            
            
class Reflect(tk.Toplevel):
    def __init__(self, master):
        
        super().__init__(master)
        # self.root=root
        self.title('Reflect page')
        self.maxsize(width=700,height=300)
        
        self.label1 = tk.Label(self, text='Enter the axis to reflect about (X, Y, Origin, Line):')
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label2 = tk.Label(self, text='Enter the axis of the line to reflect about \'X, Y\':')
        self.label2.grid(row=2, column=0, padx=5, pady=5)
        
        self.label3 = tk.Label(self, text='Plane to reflect about (1-XY, 2-XZ, 3-YZ):')
        self.label3.grid(row=4, column=0, padx=5, pady=5)
        
        self.word1_text=tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.word1_text)
        self.e1.grid(row=1,column=0)
        
        self.word2_text=tk.StringVar()
        self.e2=tk.Entry(self, textvariable=self.word2_text)
        self.e2.grid(row=3,column=0)
        
        self.word3_text=tk.StringVar()
        self.e3=tk.Entry(self, textvariable=self.word3_text)
        self.e3.grid(row=5,column=0)
        
        self.btn = tk.Button(self, command=self.okay, text='Ok', relief=tk.RAISED)
        self.btn.grid(row=6, column=0)
        
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
        
        
    def okay(self):
        try:
            if len(self.master.M1[0]) == 3:
                R = np.eye(3)
                axis = self.word1_text.get()
                if axis.capitalize() == 'X':
                    R[1][1] = -1
                elif axis.capitalize() == 'Y':
                    R[0][0] = -1
                elif axis.capitalize() == 'O':
                    R[1][1] = -1
                    R[0][0] = -1
                elif axis.capitalize() == 'L':
                    ref = self.word2_text.get()
                    if ref.capitalize() == 'X':
                        R[0][0] = 0
                        R[1][1] = 0
                        R[0][1] = 1
                        R[1][0] = 1
                    elif ref.capitalize() == 'Y':
                        R[0][0] = 0
                        R[1][1] = 0
                        R[0][1] = -1
                        R[1][0] = -1
            
            else:
                R = np.eye(4)
                plane = self.word3_text.get()
                if int(plane) == 1:
                    R[2][2] = -1
                elif int(plane) == 2:
                    R[1][1] = -1
                elif int(plane) == 3:
                    R[0][0] = -1
            self.master.M3 = R.astype(np.float16)
            self.destroy()   
        except:
            messagebox.showerror("Error", "An error occured, try again")
            self.word1_text.set('')
            self.word2_text.set('')
            self.word3_text.set('')
        
        

if __name__=='__main__':
    app=App()
    datafile = "flow.ico" 
    if not hasattr(sys, "frozen"):
        datafile = os.path.join(os.path.dirname(__file__), datafile) 
    else:  
        datafile = os.path.join(sys.prefix, datafile)
        
    app.iconbitmap(default=datafile)
    app.maxsize(600,420)
    app.mainloop()