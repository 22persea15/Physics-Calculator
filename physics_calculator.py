
#Imports
import os
import tkinter as tk
import math

#Create Root ------------
root = tk.Tk()
root.title("Physics Calculator")
root.geometry("475x350")

#New Window Functions -----------

#I have a sneaking suspicion I should be putting these in the Classes
#But I don't know how to use class methods in the widgets so

def kinematics_window():
    kinematics_window = tk.Toplevel(root)
    kinematics_window.title("Physics Calculator: Kinematics")
    kinematics_window.geometry("475x350")
    
    #-----Kinematics Widgets
    topic_label = tk.Label(kinematics_window, text = "Kinematics")
    topic_label.pack()
    average_velocity = tk.Button(kinematics_window, text = "average velocity", width=20)
    average_velocity.pack()

def dynamics_window():
    dynamics_window = tk.Toplevel(root)
    dynamics_window.title("Physics Calculator: Dynamics")
    dynamics_window.geometry("475x350")
    
    #-----Dynamics Widgets
    average_velocity = tk.Button(dynamics_window, text = "average velocity", width=20)
    average_velocity.pack()
    
def cmotion_window():
    cmotion_window = tk.Toplevel(root)
    cmotion_window.title("Physics Calculator: Circular Motion")
    cmotion_window.geometry("475x350")
    
    #-----Circular Motion Widgets
    average_velocity = tk.Button(cmotion_window, text = "average velocity", width=20)
    average_velocity.pack()
    
def energy_window():
    energy_window = tk.Toplevel(root)
    energy_window.title("Physics Calculator: Energy")
    energy_window.geometry("475x350")
    
    #-----Energy Widgets
    kinetic_energy = tk.Button(energy_window, text = "Kinetic Energy", width=20)
    kinetic_energy.pack()
    
    gravitational_energy = tk.Button(energy_window, text = "Gravitational Potential Energy", width=20)
    gravitational_energy.pack()
    
    elastic_energy = tk.Button(energy_window, text = "Elastic Potential Energy", width=20)
    elastic_energy.pack()
    
    mechanical_energy = tk.Button(energy_window, text = "Mechanical Energy", width=20)
    mechanical_energy.pack()
    
def momentum_window():
    momentum_window = tk.Toplevel(root)
    momentum_window.title("Physics Calculator: Momentum")
    momentum_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(momentum_window, text = "average velocity", width=20)
    average_velocity.pack()

def simple_harmonic_window():
    simple_harmonic_window = tk.Toplevel(root)
    simple_harmonic_window.title("Physics Calculator: Simple Harmonic Motion")
    simple_harmonic_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(simple_harmonic_window, text = "average velocity", width=20)
    average_velocity.pack()

def rotational_window():
    rotational_window = tk.Toplevel(root)
    rotational_window.title("Physics Calculator: Rotational Motion")
    rotational_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(rotational_window, text = "average velocity", width=20)
    average_velocity.pack()

def electricity_window():
    electricity_window = tk.Toplevel(root)
    electricity_window.title("Physics Calculator: Electricity")
    electricity_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(electricity_window, text = "average velocity", width=20)
    average_velocity.pack()
    
def waves_window():
    waves_window = tk.Toplevel(root)
    waves_window.title("Physics Calculator: Waves")
    waves_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(waves_window, text = "average velocity", width=20)
    average_velocity.pack()



#New Window Widgets ------------
ap_physics_1_topics = tk.Label(root, text="AP Physics 1")
ap_physics_1_topics.grid(column=1, row=1)

create_kinematics_window = tk.Button(root, text="Kinematics", width=20, command=kinematics_window)
create_kinematics_window.grid(column=1, row=2)

create_dynamics_window = tk.Button(root, text="Dynamics", width=20, command=dynamics_window)
create_dynamics_window.grid(column=1, row=3)

create_circular_motion_window = tk.Button(root, text="Circular Motion", width=20, command=cmotion_window)
create_circular_motion_window.grid(column=1, row=4)

create_energy_window = tk.Button(root, text="Energy", width=20, command=energy_window)
create_energy_window.grid(column=1, row=5)

create_momentum_window = tk.Button(root, text="Momentum", width=20, command=momentum_window)
create_momentum_window.grid(column=1, row=6)

create_shmotion_window = tk.Button(root, text="Simple Harmonic Motion", width=20, command=simple_harmonic_window)
create_shmotion_window.grid(column=1, row=7)

create_rotational_window = tk.Button(root, text="Rotational Motion", width=20, command=rotational_window)
create_rotational_window.grid(column=1, row=8)

create_electicity_window = tk.Button(root, text="Electricity", width=20, command=electricity_window)
create_electicity_window.grid(column=1, row=9)

create_waves_window = tk.Button(root, text="Waves", width=20, command=waves_window)
create_waves_window.grid(column=1, row=10)

ap_physics_2_topics = tk.Label(root, text="AP Physics 2 (coming soon)")
ap_physics_2_topics.grid(column=2, row=1)
    
#This function is just to get rid of the error with the widgets
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
#in the new window functions!
# refer to energy gui we made earlier


#Mainloop ------------


root.mainloop()

