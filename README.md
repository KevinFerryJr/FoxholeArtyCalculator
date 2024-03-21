Foxhole Game Artillery Calculator

This project is a Foxhole game artillery calculator designed to assist players in calculating accurate artillery shots within the game.

How to Use the Artillery Calculator
Requirements
Python 3.x or higher
Pygame library
Installation
Clone or download the repository from GitHub Repository Link.
Install Python if you haven't already.
Install the Pygame library by running pip install pygame in your terminal or command prompt.
Running the Calculator
Navigate to the directory where the repository is located.
If you're running the python script directly run the gui.py as that is the project entry point.
Otherwise just run the .exe binary file and enjoy!
Using the Calculator
There are two ways you can use this tool, that is for either static or dynamic spotting.
Generating a static firing solution is very simple.
Input the angle & distance from the spotter to the target and press the calculate button.
The calculator will display the necessary information for your artillery shot (Ignore flipped azimuth when spotting staticly).
Note: When spotting staticly your spotters max targeting range will be 250m as the binoculars only have a range of 125m (dynamic spotting is recommended for 150mm).
Dynamic spotting on the other hand is not as simple but will allow you to advance your spotter as far away from the cannon as needed.
To use the calculator for dynamic spotting you can follow the steps below:
    -Input the spotters initial measurments as though you're setting up a static shot but instead of selecting a target the spotter should select the next position that they intend to measure from.
    -After calculating the solution change the "Azimuth to GUN" input to the "FLIPPED azimuth" result, and the "Distance to GUN" to the "Firing distance" result, but don't press calculate yet (ignore the target azimuth and distance for now, we will update them in a moment).
    -Now move to exactly the next position that you selected in step 1.
        -If you wish to fire from this position, select and input a target azimuth and distance from where you are and fire on the new firing distance and azimuth.
        -Otherwise if you want to advance to another position, set the target azimuth and distance to the measurments of the new position, calculate and repeat from step 2 until ready to fire.
Features
Calculate distance and azimuth to the target.
Plotting chart to visualive firing solutions.
Display directional information for adjusting artillery aim.
Tips for Accuracy
If you're calculating firing solutions for the 150mm cannon it's best to spot dynamically (check "Using the Calculator" section).
Check wind direction before firing to avoid friendly fire! (wind has about a 20m effect on the firing position for 120mm and 150mm)
Contributions and Issues
Contributions to the project are welcome. Feel free to fork the repository and submit pull requests.
If you encounter any issues or have suggestions for improvements, please create an issue on the GitHub repository.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Credits
Developed by KevinFerryJr & CartV2
Inspired by the Foxhole game artillery mechanics.