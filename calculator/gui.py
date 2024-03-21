import tkinter as tk
from tkinter import ttk
from plotting import rangefinder
from plotting import window

def calculate(gunDistEntry, gunAzimEntry, targDistEntry, targAzimEntry, firingDistLabel, firingAzimLabel):
    gunDist = float(gunDistEntry.getEntry())
    gunAzim = float(gunAzimEntry.getEntry())
    targDist = float(targDistEntry.getEntry())
    targAzim = float(targAzimEntry.getEntry())
    app.solution.set(gunDist,gunAzim,targDist,targAzim)

    firingDist, firingAzim = rangefinder.calculateFiringSolution(gunDist, gunAzim, targDist, targAzim)
    flippedAzim = (firingAzim+180) % 360
    
    firingDistLabel.config(text=f"Firing Distance: {firingDist}")
    firingAzimLabel.config(text=f"Firing Azimuth: {firingAzim}")
    flippedAzimLabel.config(text=f"Flipped Azimuth: {flippedAzim}")
    return

fgColor = (0, 0, 0)
bgColor = (240, 240, 240)

class TkWindow:
    def __init__(self, title, app):
        self.root = tk.Tk()
        self.root.title(title)
        self.app = app
    
    def run(self):
        self.app.start()
        self.root.mainloop()
        self.app.end()

class TkComponent:
    def __init__(self, root, padX=0, padY=0):
        self.padX = padX
        self.padY = padY
        
class TkButton(TkComponent):
    def __init__(self, root, message, func, padX=0, padY=3):
        super().__init__(root, padX, padY)
        self.message = message
        self.button = ttk.Button(root, text=message, command=func)
        self.pack()
        
    def pack(self):
        self.button.pack(padx=self.padX, pady=self.padY)
        
class TkLabel(TkComponent):
    def __init__(self, root, message, padX=0, padY=3, fg=fgColor, bg=bgColor):
        super().__init__(root, padX, padY)
        self.label = ttk.Label(root, text=message, foreground=self.getColorHex(fg), background=self.getColorHex(bg))
        self.message = message
        self.value = ""
        self.pack()
            
    def set(self, value):
        self.label.config(text=f"{self.message}: {value}")
        
    def getColorHex(self, rgb):
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def pack(self):
        self.label.pack(padx=self.padX, pady=self.padY)
        
class TkEntryField(TkComponent):
    def __init__(self, root, labelText, padX=0, padY=0):
        super().__init__(root, padX=0, padY=0)
        self.label = ttk.Label(root, text=labelText)
        self.entry = ttk.Entry(root)
        self.pack()
    
    def getEntry(self):
        return self.entry.get()
 
    def pack(self):
        self.label.pack(padx=self.padX, pady=self.padY)
        self.entry.pack(padx=self.padX, pady=self.padY)

#Pygame Window
screenWidth = 800
screenHeight = 600
pygameWinTitle = "Plotter"
app = window.PygameWindow(pygameWinTitle, screenWidth, screenHeight)

#TKinter Window
tkWinTitle = "Firing Solution Calculator"
tkWindow = TkWindow(tkWinTitle, app)

#INPUTS
gunDistEntry = TkEntryField(tkWindow.root, "Distance to GUN:")
gunAzimEntry = TkEntryField(tkWindow.root, "Azimuth to GUN:")
targDistEntry = TkEntryField(tkWindow.root, "Distance to TARGET:")
targAzimEntry = TkEntryField(tkWindow.root, "Azimuth to TARGET:")

#BUTTON
calcualteFn = lambda: calculate(gunDistEntry, gunAzimEntry, targDistEntry, targAzimEntry, firingDist.label, firinAzimuth.label)
calculateButton = TkButton(tkWindow.root, "Calculate", calcualteFn)

#OUTPUT
firingDist = TkLabel(tkWindow.root, "Firing Distance:")
firinAzimuth = TkLabel(tkWindow.root, "Firing Azimuth:")
flippedAzim = TkLabel(tkWindow.root, "Flipped Azimuth:")

#FOOTER
footer = TkLabel(tkWindow.root, "github.com/KevinFerryJr", padX=40, padY=6, fg=(150,150,150))

tkWindow.run()