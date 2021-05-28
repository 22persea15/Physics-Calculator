
#Imports
import os
import tkinter as tk
from tkinter import Tk
import math

#Create Root ------------
root = tk.Tk()
root.title("Physics Calculator")
root.geometry("475x350")

#Functions -----------

#I have a sneaking suspicion I should be putting these new windows in the Classes
#But I don't know how to use class methods in the widgets so
    

def show():
    root.deiconify()
       
def kinematics_window():
    root.withdraw()
    kinematics_window = tk.Toplevel(root)
    kinematics_window.title("Physics Calculator: Kinematics")
    kinematics_window.geometry("475x350")
    
    #-----Kinematics Widgets
    topic_label = tk.Label(kinematics_window, text = "Kinematics")
    topic_label.pack()
    average_velocity = tk.Button(kinematics_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()()

def dynamics_window():
    root.withdraw()
    dynamics_window = tk.Toplevel(root)
    dynamics_window.title("Physics Calculator: Dynamics")
    dynamics_window.geometry("475x350")
    
    #-----Dynamics Widgets
    average_velocity = tk.Button(dynamics_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()()
    
def cmotion_window():
    root.withdraw()
    cmotion_window = tk.Toplevel(root)
    cmotion_window.title("Physics Calculator: Circular Motion")
    cmotion_window.geometry("475x350")
    
    #-----Circular Motion Widgets
    average_velocity = tk.Button(cmotion_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()
    
def energy_window():
    root.withdraw()
    energy_window = tk.Toplevel(root)
    energy_window.title("Physics Calculator: Energy")
    energy_window.geometry("475x350")
    #-----Functions
    def kinetic_energy():
        mass = float(entry_mass.get())
        velocity = float(entry_velocity.get())
        kinetic = 0.5 * mass * (velocity ** 2)
        label_result["text"] = (f"\n\n{kinetic}")
            
        entry_mass.delete(0,5)
        entry_height.delete(0,5)
        entry_velocity.delete(0,5)
        entry_spring.delete(0,5)
        entry_compression.delete(0,5)
        
    def gravitational_energy():
        mass = float(entry_mass.get())
        height = float(entry_height.get())
        gravitational = mass * 9.8 * height
        label_result["text"] = (f"\n\n{gravitational}")
        
        entry_mass.delete(0,5)
        entry_height.delete(0,5)
        entry_velocity.delete(0,5)
        entry_spring.delete(0,5)
        entry_compression.delete(0,5)
        
    def elastic_energy():
        spring = float(entry_spring.get())
        compression = float(entry_compression.get())
        elastic = 0.5 * spring * (compression ** 2)
        label_result["text"] = (f"\n\n{elastic}")
        
        entry_mass.delete(0,5)
        entry_height.delete(0,5)
        entry_velocity.delete(0,5)
        entry_spring.delete(0,5)
        entry_compression.delete(0,5)
        
    def mechanical_energy():
        mass = float(entry_mass.get())
        velocity = float(entry_velocity.get())
        height = float(entry_height.get())
        spring = float(entry_spring.get())
        compression = float(entry_compression.get())
        mechanical = (0.5 * mass * (velocity ** 2) )+(mass * 9.8 * height)+(0.5 * spring * (compression ** 2))
        label_result["text"] = (f"\n\n{mechanical}")
        
        entry_mass.delete(0,5)
        entry_height.delete(0,5)
        entry_velocity.delete(0,5)
        entry_spring.delete(0,5)
        entry_compression.delete(0,5)
    
    #-----Energy Widgets
    kinetic_energy = tk.Button(energy_window, text = "Kinetic Energy", width=20, command=kinetic_energy)
    kinetic_energy.grid(column=1, row=1)
    
    gravitational_energy = tk.Button(energy_window, text = "Gravitational Potential Energy", width=20, command=gravitational_energy)
    gravitational_energy.grid(column=1, row=2)
    
    elastic_energy = tk.Button(energy_window, text = "Elastic Potential Energy", width=20, command=elastic_energy)
    elastic_energy.grid(column=1, row=3)
    
    mechanical_energy = tk.Button(energy_window, text = "Mechanical Energy", width=20, command=mechanical_energy)
    mechanical_energy.grid(column=1, row=4)
    
    label_mass = tk.Label(energy_window, text="Mass")
    label_mass.grid(column=2, row=1)
    entry_mass = tk.Entry(energy_window, width=5)
    entry_mass.grid(column=2, row=2)

    label_velocity = tk.Label(energy_window, text="Velocity")
    label_velocity.grid(column=2, row=3)
    entry_velocity = tk.Entry(energy_window, width=5)
    entry_velocity.grid(column=2, row=4)

    label_height = tk.Label(energy_window, text="Height")
    label_height.grid(column=2, row=5)
    entry_height = tk.Entry(energy_window, width=5)
    entry_height.grid(column=2, row=6)

    label_spring = tk.Label(energy_window, text="Spring")
    label_spring.grid(column=2, row=7)
    entry_spring = tk.Entry(energy_window, width=5)
    entry_spring.grid(column=2, row=8)

    label_compression = tk.Label(energy_window, text="Compression")
    label_compression.grid(column=2, row=9)
    entry_compression = tk.Entry(energy_window, width=5)
    entry_compression.grid(column=2, row=10)
    
    label_result = tk.Label(energy_window, text="Result")
    label_result.grid(column=2, row=15)
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.grid(column=1, row=15)

def momentum_window():
    root.withdraw()
    momentum_window = tk.Toplevel(root)
    momentum_window.title("Physics Calculator: Momentum")
    momentum_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(momentum_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()

def simple_harmonic_window():
    root.withdraw()
    simple_harmonic_window = tk.Toplevel(root)
    simple_harmonic_window.title("Physics Calculator: Simple Harmonic Motion")
    simple_harmonic_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(simple_harmonic_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()
    
def rotational_window():
    root.withdraw()
    rotational_window = tk.Toplevel(root)
    rotational_window.title("Physics Calculator: Rotational Motion")
    rotational_window.geometry("475x350")
    
    #-----Momentum Widgets
    average_velocity = tk.Button(rotational_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()

def electricity_window():
    root.withdraw()
    electricity_window = tk.Toplevel(root)
    electricity_window.title("Physics Calculator: Electricity")
    electricity_window.geometry("475x350")
    
    #-----Electricity Widgets
    average_velocity = tk.Button(electricity_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()
    
def waves_window():
    root.withdraw()
    waves_window = tk.Toplevel(root)
    waves_window.title("Physics Calculator: Waves")
    waves_window.geometry("475x350")
    
    #-----Waves Widgets
    average_velocity = tk.Button(waves_window, text = "average velocity", width=20)
    average_velocity.pack()
    
    back = tk.Button(energy_window, text = "Return", width=20, command=show)
    back.pack()

def reset():
    entry_mass.delete(0,5)
    entry_height.delete(0,5)
    entry_velocity.delete(0,5)
    entry_spring.delete(0,5)
    entry_compression.delete(0,5)
    
    label_result["text"] = ("\n\nWhat would you like to calculate?")

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

        
#----- AP Physics 1
#kinematics
#dynamics
#circular            
#energy
#momentum
#simple harmonic
#rotational motion
#electicity
#waves

#----- AP Physics 2
#fluids
#thermodynamics
#electric force, field and potential 
#electric circuits
#magnetism and electromagnetic induction
#geometric and physical optics
#quantum, atomic, and nuclear physics


#Widgets ------------
#in the new window functions!
# refer to energy gui we made earlier


#Mainloop ------------


root.mainloop()

