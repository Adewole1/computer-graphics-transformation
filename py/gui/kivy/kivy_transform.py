from re import I
import sys
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty

from math import radians, cos, sin
import numpy as np
import matplotlib.pyplot as plt

kivy.require("2.0.0")

kv = Builder.load_file("my.kv")


class TransformationPage(Widget):
         
    def transform(self):
        self.transformations_list = {
            'T': 'Translate',
            'O': 'Rotate',
            'C': 'Scale',
            'S': 'Shear',
            'R': 'Reflect'
        }
        # self.ids.label1.text='Enter the transformation you want to do: \nTranslate, rOtate, sCale, Shear, Reflect \nor Done when you are done or cLear to start again: \n'
        # trans_app.screen_manager.current = "TransformationPage"
        # self.enter.bind(on_press=self.transform)
        try:
            trans_app.transform_list = trans_app.transform_list
        except AttributeError:
            trans_app.transform_list = []
        # print(self.ids.input.text.capitalize())
        transform = self.ids.input.text.capitalize()
        
        if transform in self.transformations_list.keys():
            trans_app.transform_list.append(transform)
            self.ids.input.text = ''
            self.ids.label2.text = self.ids.label2.text + self.transformations_list[transform] + '\n'
            # print(self.transform_list)
             
        elif transform == "D":
            self.ids.input.text = ''
            if len(trans_app.transform_list) == 0:
                info = 'You have entered no transformation, try again.'
                popup_info(info)
                # self.ids.label2.text = info
            else:
                self.ids.label2.text = str(trans_app.transform_list)
                trans_app.screen_manager.transition = SlideTransition(direction='left')
                trans_app.screen_manager.current = "CoordPage"
                
        elif transform == 'L':
            self.ids.input.text = ''            
            self.transform_list = []
            info = "All cleared"
            self.ids.label2.text = info
            # self.transform(instance)
            
        elif transform == '':
            self.ids.input.text = ''
            info = "\nYou have entered no transformation, try again."
            popup_info(info)
            # self.label2.text = info
            # trans_app.info_page.update_info(info)
            # trans_app.screen_manager.current = "InfoPage"
            # Clock.schedule_once(self.transform, 1)
            
        else:
            info = "\nYou have entered an incorrect transformation, try again."
            self.ids.input.text = ''
            popup_info(info)
            # self.ids.label2.text = info
            

class CoordinatePage(Widget):
          
    def point(self):
        # self.ids.btn.bind(on_press=self.point)
        try:
            trans_app.coordinates = trans_app.coordinates
        except AttributeError:
            trans_app.coordinates = []
        self.coord = []
        self.ids.label1.text="Enter the coordinates of the shape in the format (x,y) \nor 'D' when done or cLear to start again or \nStart again: \n"
        coord_in = self.ids.input.text
        # print(trans_app.transform_list)
        # self.transform_list = trans_app.screen_manager.screens[1].ids.label2.text
        # self.label.text = str(self.transform_list)
        if coord_in == "":
            info = "You have entered no coordinates, Try again."
            popup_info(info)
            # self.ids.label2.text = info
            
        else:
            if str(coord_in).capitalize() == "D":
                if len(trans_app.coordinates) == 1 and len(trans_app.transform_list) == 1 and trans_app.transform_list[0] == 'T':
                    pass
                elif len(trans_app.coordinates) == 2:
                    pass
                elif len(trans_app.coordinates) > 2:
                    pass
                        # self.coordinates.append(self.coordinates[0])
                else:
                    info = '\nCannot transform a point, \nCheck transformation and points.'
                    popup_info(info)
                    trans_app.screen_manager.transition = SlideTransition(direction='right')
                    trans_app.screen_manager.current = "TransformationPage"
                    # self.transform()
                self.check_coordinates()
            elif coord_in.capitalize() == "L":
                info = "All cleared"
                self.ids.label2.text = info
                trans_app.coordinates = []
                self.coord = []
            elif coord_in.capitalize() == "S":
                # Clock.schedule_once(self.transform, 1)
                trans_app.transfrom_list = []
                trans_app.coordinates = []
                trans_app.screen_manager.current = "TransformationPage"
            else:
                try:
                    self.ids.label2.text = self.ids.label2.text + str(coord_in) + '\n'
                    coord_in = coord_in.split(',')
                    for i in range(0, len(coord_in)):
                        self.coord.append(int(coord_in[i]))
                    self.coord.append(1)
                    trans_app.coordinates.append(list(self.coord))
                    self.ids.input.text = ''
                except:
                    info = 'An error occured with the coordinates, try again.'
                    # self.label2.text = info
                    popup_info(info)
                    self.ids.input.text = ''
                    # continue
                    
    def check_coordinates(self):
        check1 = len(trans_app.coordinates[0])
        if check1 in range(3,5):
            for i in range(1, len(trans_app.coordinates)):
                if check1 == len(trans_app.coordinates[i]):
                    # print("Check {0} complete".format(i))
                    pass
                else:
                    # print("Check {0} not complete".format(i))
                    info = 'The coordinates are not homogenous, \nInput the coordinates again.'
                    popup_info(info)
                    trans_app.coordinates = []
                    # self.point()  
                break
        else:
            info = "Can only transform in 2D and 3D, \ncheck coordinates."
            popup_info(info)
            trans_app.coordinates = []
            # self.point()
        print("\nCoordinates are Homogenous")
        # trans_app.screen_manager.current = "TranslatePage"
        self.transform_coordinates()
        
        
    def transform_coordinates(self):
        transformations_list = {
            'T': 'Translate',
            'O': 'Rotate',
            'C': 'Scale',
            'S': 'Shear',
            'R': 'Reflect'
        }
        transformations = {
                'T': "TranslatePage",
                'O': "RotatePage",
                'C': "ScalePage",
                'S': "ShearPage",
                'R': "ReflectPage"
        }
        transform = {
            'T' : trans_app.T,
            'O' : trans_app.O,
            'C' : trans_app.C,
            'S' : trans_app.S,
            'R' : trans_app.R,
        }
        self.M = np.array(trans_app.coordinates)
        # self.M = np.transpose(self.M)
        self.M1 = self.M
        self.transformed_list = []
        self.rot=''
        trans_app.screen_manager.current = "TransformationPage"
        for i in trans_app.transform_list:
            func = transformations[i]
            print(func)
            trans_app.screen_manager.transition = SlideTransition(direction='left')
            trans_app.screen_manager.current = "TransformationPage"
            M3 = transform[i]
            self.transformed_list.append(M3)
            # print(M3)
            if i == 'O':
                if self.rot == 'P':
                    trans_app.Tx = self.cord[0]
                    trans_app.Ty = self.cord[1]
                    print(trans_app.Tx, trans_app.Ty)
                    M4 = TranslatePage.translate()
                    print('1\n',M4)
                    M2 = np.dot(self.M1, M4)
                    print('2\n',M2)
                    M2 = np.dot(M2, M3)
                    print('3\n',M2)
                    trans_app.Tx = -int(self.cord[0])
                    trans_app.Ty = -int(self.cord[1])
                    M5 = TranslatePage.translate()
                    print('4\n',M5)
                    M6 = np.dot(M2, M5)
                    print('5\n',M6)
                    self.M1 = M6

                else:
                    self.M1 = np.dot(self.M1, M3)
            else:
                self.M1 = np.dot(self.M1, M3)
        # M1 = np.array(M1, np.int64)
        self.Tx = ''
        self.Ty = ''
        # self.M = np.delete(self.M, [-1], axis=1)
        # self.M1 = np.delete(self.M1, [-1], axis=1)
        if len(trans_app.transform_list) == 1:
            print("\nYour Transformation is: ", trans_app.transformations_list[trans_app.transform_list[0]])
        else:
            print("\nYour Transformation(s) are: \n")
            for trans in range(0, len(trans_app.transform_list)):
                print(trans_app.transformations_list[trans_app.transform_list[trans]])
        
        
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
            
        
        print("\nYour coordinates are: \n", self.M)
        print("\nYour new coordinates after transformation are: \n", self.M1)
        print("\nYour transformation coordinates are: \n", self.transformed_list)
              
                    
class TranslatePage(Widget):
    
    def translate(self):
        
        try:
            if len(trans_app.coordinates[0]) == 3: #For 2D
                trans_app.T = trans_app.N_2
                late = []
                
                if trans_app.Tx == '':
                    late.append(self.ids.input.text)
                    self.ids.input.text = ''
                    # self.Tx = int(input(""))
                    self.ids.trans_label.text = "Enter the translation in y-direction: \n"
                    if len(late) == 2:
                        trans_app.T[2][0] = int(late[0])
                        trans_app.T[2][1] = int(late[0])
                        trans_app.screen_manager.current = trans_app.screen_manager.previous()
                        
                else:
                    trans_app.T[2][0] = trans_app.Tx
                    trans_app.T[2][1] = trans_app.Ty
                    #     pass
            
            else: #For 3D
                T = trans_app.N_3
                
                if trans_app.Tx == '':
                    trans_app.Tx = int(input("Enter the translation in x-direction: \n"))
                    trans_app.Ty = int(input("Enter the translation in y-direction: \n"))
                    trans_app.Tz = int(input("Enter the translation in z-direction: \n"))
                    T[3][0] = self.Tx
                    T[3][1] = self.Ty
                    T[3][2] = self.Tz
                    
            
        except:
            print('\nAn error occurred, try again. \n')
            self.translate()
        
        # print(T)
        # return T.astype(np.int64)
    

class RotatePage(GridLayout):
    pass
    

class ScalePage(GridLayout):
    pass

    
class ShearPage(GridLayout):
    pass

    
class ReflectPage(GridLayout):
    pass
            

def popup_info(text):
          
        layout = GridLayout(cols = 2, padding = 10)
  
        popupLabel = Label(text = text)
        closeButton = Button(text = "Close")
  
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)       
  
        # Instantiate the modal popup and display
        popup = Popup(title ='INFO', content = layout, size=(50,50))  
        popup.open()   
  
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)
    
    
       
        
class TransApp(App):
    
    transfrom_list = []
    coordinates = []
    N_2 = np.eye(3)
    N_3 = np.eye(4)
    
    Tx = ''
    Ty = ''
    
    T = None
    R = None
    O = None
    C = None
    S = None
    
    transformations_list = {
            'T': 'Translate',
            'O': 'Rotate',
            'C': 'Scale',
            'S': 'Shear',
            'R': 'Reflect'
        }
    transformations = {
            'T': "TranslatePage",
            'O': "RotatePage",
            'C': "ScalePage",
            'S': "ShearPage",
            'R': "ReflectPage"
        }
    
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.transform_page = TransformationPage()
        screen = Screen(name="TransformationPage")
        screen.add_widget(self.transform_page)
        self.screen_manager.add_widget(screen)
        
        self.coord_page = CoordinatePage()
        screen = Screen(name="CoordPage")
        screen.add_widget(self.coord_page)
        self.screen_manager.add_widget(screen)
        
        self.translate_page = TranslatePage()
        screen = Screen(name="TranslatePage")
        screen.add_widget(self.translate_page)
        self.screen_manager.add_widget(screen)
        
        self.rotate_page = RotatePage()
        screen = Screen(name="RotatePage")
        screen.add_widget(self.rotate_page)
        self.screen_manager.add_widget(screen)
        
        self.scale_page = ScalePage()
        screen = Screen(name="ScalePage")
        screen.add_widget(self.scale_page)
        self.screen_manager.add_widget(screen)
        
        self.shear_page = ShearPage()
        screen = Screen(name="ShearPage")
        screen.add_widget(self.shear_page)
        self.screen_manager.add_widget(screen)
        
        self.reflect_page = ReflectPage()
        screen = Screen(name="ReflectPage")
        screen.add_widget(self.reflect_page)
        self.screen_manager.add_widget(screen)
        
        
        return self.screen_manager
        
        # return Transformation()
    
if __name__ == '__main__':
    trans_app = TransApp()
    trans_app.run()
    