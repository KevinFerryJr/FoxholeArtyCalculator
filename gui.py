import tkinter as tk
from tkinter import ttk
import rangefinder
import chart

def calculate():
    gunDist = int(gunDistEntry.get())
    gunAzim = int(gunAzimEntry.get())
    targDist = int(targDistEntry.get())
    targAzim = int(targAzimEntry.get())
    adjHoriz = int(adjHorizEntry.get())
    
    firingDist, firingAzim, adjustedDist, adjustedAzim = rangefinder.calculateFiringSolution(gunDist, gunAzim, targDist, targAzim, adjHoriz)

    firingDistLabel.config(text=f"Firing Distance: {firingDist}")
    firingAzimLabel.config(text=f"Firing Azimuth: {firingAzim}")
    adjustedDistLabel.config(text=f"Adjusted Firing Distance: {adjustedDist}")
    adjustedAzimLabel.config(text=f"Adjusted Azimuth: {adjustedAzim}")


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

adjHorizLabel = ttk.Label(root, text="Horizontal Adjustment:")
adjHorizLabel.pack()
adjHorizEntry = ttk.Entry(root)
adjHorizEntry.pack()

calculateButton = ttk.Button(root, text="Calculate", command=calculate)
calculateButton.pack(pady=5)

# Create output labels
firingDistLabel = ttk.Label(root, text="Firing Distance:")
firingDistLabel.pack(pady=5)

firingAzimLabel = ttk.Label(root, text="Firing Azimuth:")
firingAzimLabel.pack(pady=5)

adjustedDistLabel = ttk.Label(root, text="Adjusted Firing Distance:")
adjustedDistLabel.pack(pady=5)

adjustedAzimLabel = ttk.Label(root, text="Adjusted Azimuth:")
adjustedAzimLabel.pack(pady=5)

app = chart.PygameWindow()
app.start()
root.mainloop()