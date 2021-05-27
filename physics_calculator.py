
#Imports
import os
import tkinter as tk
import math

#Create Root ------------
root = tk.Tk()
root.title("Physics Calculator")
root.geometry("475x350")

#def createNewWindow():
#    newWindow = tk.Toplevel(app)
#    labelExample = tk.Label(newWindow, text = "New Window")
#    buttonExample = tk.Button(newWindow, text = "New Window button")

#    labelExample.pack()
#   buttonExample.pack()

#app = tk.Tk()
#buttonExample = tk.Button(app, 
#              text="Create new window",
#              command=createNewWindow)
#buttonExample.pack()


def kinetic_energy():
    pass
#Classes ------------
class Calculator():
    def __init__(self, X):
        self.X = X
        
#----- AP Physics 1

class Kinematics(Calculator):
    def __init__ (self, X, v_initial, v_final, acceleration, time, distance):
        Calculator.__init__(self, X)
        #def average_velocity(self, distance, time):
            #velocity_average = distance/time
            #return velocity_average
            #label_result["text"] = (f"\n\n{velocity_average}")
        
        #def average_acceleration(self, v_final, v_initial, time):
           # ave_acceleration = (v_final - v_initial)/time
            #return ave_acceleration
            #label_result["text"] = (f"\n\n{ave_acceleration}")
        #acceleration 
        
        #def constant_acceleration(self, v_initial, v_final, acceleration, time, distance):
            #pass
            # v = u + at
            # v**2 = U**2 + 2as
            # s = 1/2(u-v)+t
            # s = ut + 1/2at**2
        self.v_initial = v_initial
        self.v_final = v_final
        self.acceleration = acceleration
        self.time = time
        self.distance = distance
        
class Dynamics(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something

class Circular_Motion(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something
            
class Energy(Calculator):
    def __init__(self, values):
        Calculator.__init__(self, values)
        self.mass = 1
        self.velocity = 1
        self.height = 1
        self.spring = 1
        self.compression = 1
    
    def kinetic_energy(self, mass, velocity):
        kinetic = 0.5 * mass * (velocity ** 2)
        
    def get_kinetic(self):
        #label_result["text"] = (f"\n\n{kinetic}")
        return kinetic
    
    def gravitational_energy(self, mass, height):
        gravitational = mass * 9.8 * height
    
    def get_gravitational(self):
        #label_result["text"] = (f"\n\n{gravitational}")
        return gravitational 
    
    def elastic_energy(self, spring, comprehension):
        elastic = 0.5 * spring * (compression ** 2)
    
    def get_elastic(self):
        #label_result["text"] = (f"\n\n{elastic}")
        return elastic 

class Momentum(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something

class Simple_Harmonic(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something
            
class Rotational_Motion(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something
        
class Electricity(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something
            
class Waves(Calculator):
    def __init__(self, values, something):
        Calculator.__init__(self, values)
        self.something = something

#----- AP Physics 2
#fluids
#thermodynamics
#electric force, field and potential 
#electric circuits
#magnetism and electromagnetic induction
#geometric and physical optics
#quantum, atomic, and nuclear physics


#Functions ------------

def reset():
    entry_mass.delete(0,5)
    entry_height.delete(0,5)
    entry_velocity.delete(0,5)
    entry_spring.delete(0,5)
    entry_compression.delete(0,5)
    
    label_result["text"] = ("\n\nWhat would you like to calculate?")

#Widgets ------------

label_result = tk.Label(root, text="\n\nWhat would you like to calculate?")
label_result.pack()

btn_solve_for_mass = tk.Button(root, text="Solve for Mass", command=kinetic_energy)
btn_solve_for_mass.pack()

btn_solve_for_velocity = tk.Button(root, text="Solve for Velocity", command=kinetic_energy)
btn_solve_for_velocity.pack()

btn_solve_for_height = tk.Button(root, text="Solve for Height", command=kinetic_energy)
btn_solve_for_height.pack()

btn_solve_for_spring = tk.Button(root, text="Solve for Spring Constant", command=kinetic_energy)
btn_solve_for_spring.pack()

btn_solve_for_compression = tk.Button(root, text="Solve for Compression Distance", command=kinetic_energy)
btn_solve_for_compression.pack()


#solve for u
#solve for v
#solve for a
#solve for t
#solve for s


#solve for average v
#solve for displacement
#solve for t


#Mainloop ------------


root.mainloop()

