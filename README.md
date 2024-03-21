# Foxhole Game Artillery Calculator

This project is a Foxhole game artillery calculator designed to assist players in calculating accurate artillery shots within the game.

## How to Use the Artillery Calculator

### Requirements
- Python 3.x or higher
- Pygame library

### Installation
1. Clone or download the repository from [GitHub Repository Link](https://github.com/KevinFerryJr/FoxholeArtyCalculator).
2. Install Python if you haven't already.
3. Install the Pygame library by running `pip install pygame` in your terminal or command prompt.

### Running the Calculator
- Navigate to the directory where the repository is located.
- If you're running the python script directly, run `gui.py` as that is the project entry point. Otherwise, just run the `.exe` file from the release section and enjoy!

### Using the Calculator
- There are two ways you can use this tool, for static or dynamic spotting.
- __Generating a static firing solution__:
  - Generating a static firing solution is very simple.
  - **Step 1:** Input the angle & distance from the spotter to the target and press the calculate button.
  - **Step 2:** The calculator will display the necessary information for your artillery shot (Ignore flipped azimuth when spotting staticly).
  - **Note:** When spotting staticly your spotters max targeting range will be 250m as the binoculars only have a range of 125m (dynamic spotting is recommended for 150mm).

- __Dynamic spotting__:
  - Dynamic spotting on the other hand is not as simple but will allow you to advance your spotter as far away from the cannon as needed.
  - **Step 1:** Input the spotters initial measurments as though you're setting up a static shot but instead of selecting a target the spotter should select the next position that they intend to measure from.
  - **Step 2:** After calculating the solution change the "Azimuth to GUN" input to the "FLIPPED azimuth" result, and the "Distance to GUN" to the "Firing distance" result, but don't press calculate yet (ignore the target azimuth and distance for now, we will update them in a moment).
  - **Step 3:** Now move to exactly the next position that you selected in "Step 1".
    - If you wish to fire from this position, select and input a target azimuth and distance from where you are and fire on the new firing distance and azimuth.
    - Otherwise if you want to advance to another position, set the target azimuth and distance to the measurments of the new position, calculate and repeat from "Step 2" until ready to fire.

## Features
- Calculate distance and azimuth to the target.
- Plotting chart to visualize firing solutions.

## Tips for Accuracy
- If calculating firing solutions for the 150mm cannon, dynamic spotting is recommended.
- Check wind direction before firing to avoid friendly fire (wind has about a 20m effect on the firing position for 120mm and 150mm).

## Contributions and Issues
- Contributions to the project are welcome. Fork the repository and submit pull requests.
- For issues or suggestions, create an issue on the GitHub repository.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Credits
- Developed by KevinFerryJr & CartV2
- Inspired by the Foxhole game artillery mechanics.
