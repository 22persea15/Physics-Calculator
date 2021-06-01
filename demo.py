
#figure out how to use this with tkinter so that we can use it for all the functions! 
#it's gonna make it more accurate, and my life easier

def electical_power(c, r, v):
    power = None
    if not v:
        power = (c**2) * r
    elif not c:
        power = (v**2)/r
    elif not r:
        power = v * c
    
    return power

print(electical_power(None, 2, 10))
print(electical_power(2, None, 10))
print(electical_power(2, 10, None))

#Imports
import os
import tkinter as tk
from tkinter import Tk
import math

#Create Root ------------
root = tk.Tk()
root.title("Test")
root.geometry("350x350")


def kinetic_energy():
    mass = float(entry_mass.get())
    velocity = float(entry_velocity.get())
    kinetic = 0.5 * mass * (velocity ** 2)
    label_result["text"] = (f"\n\n{kinetic}")

testing_this = tk.Label(root, text="Testing")
testing_this.pack()

label_mass = tk.Label(root, text="Mass")
label_mass.pack()
entry_mass = tk.Entry(root, width=5)
entry_mass.pack()

label_velocity = tk.Label(root, text="Velocity")
label_velocity.pack()
entry_velocity = tk.Entry(root, width=5)
entry_velocity.pack()

label_kinetic = tk.Label(root, text="Kinetic")
label_kinetic.pack()
entry_kinetic = tk.Entry(root, width=5)
entry_kinetic.pack()

label_instructions = tk.Label(root, text="Enter the values. Put 0 when the value is unknown")
label_instructions.pack()

label_result = tk.Label(root, text="Result")
label_result.pack()

root.mainloop()

            
