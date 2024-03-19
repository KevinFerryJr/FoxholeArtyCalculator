import tkinter as tk
from tkinter import ttk
from plotting import rangefinder
from plotting import chart

app = chart.PygameWindow()

def calculate():
    gunDist = float(gunDistEntry.get())
    gunAzim = float(gunAzimEntry.get())
    targDist = float(targDistEntry.get())
    targAzim = float(targAzimEntry.get())
    app.solution.set(gunDist,gunAzim,targDist,targAzim)
    
    firingDist, firingAzim = rangefinder.calculateFiringSolution(gunDist, gunAzim, targDist, targAzim)
    firingDistLabel.config(text=f"Firing Distance: {firingDist}")
    firingAzimLabel.config(text=f"Firing Azimuth: {firingAzim}")

# Create the main window
root = tk.Tk()
root.title("Firing Solution Calculator")

# Create input fields
gunDistLabel = ttk.Label(root, text="Distance to GUN:")
gunDistLabel.pack()
gunDistEntry = ttk.Entry(root)
gunDistEntry.pack(padx=40)

gunAzimLabel = ttk.Label(root, text="Angle to GUN:")
gunAzimLabel.pack()
gunAzimEntry = ttk.Entry(root)
gunAzimEntry.pack()

targDistLabel = ttk.Label(root, text="Distance to TARGET:")
targDistLabel.pack()
targDistEntry = ttk.Entry(root)
targDistEntry.pack()

targAzimLabel = ttk.Label(root, text="Angle to TARGET:")
targAzimLabel.pack()
targAzimEntry = ttk.Entry(root)
targAzimEntry.pack()

calculateButton = ttk.Button(root, text="Calculate", command=calculate)
calculateButton.pack(pady=5)

# Create output labels
firingDistLabel = ttk.Label(root, text="Firing Distance:")
firingDistLabel.pack(pady=5)

firingAzimLabel = ttk.Label(root, text="Firing Azimuth:")
firingAzimLabel.pack(pady=5)


app.start()
root.mainloop()
app.end()