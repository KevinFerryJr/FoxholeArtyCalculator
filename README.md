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
- Generating a static firing solution:
  - Input the angle & distance from the spotter to the target and press the calculate button.
  - The calculator will display the necessary information for your artillery shot.
  - Note: Ignore flipped azimuth when spotting statically. The max targeting range for static spotting is 250m.
- Dynamic spotting:
  - Input the spotter's initial measurements as though setting up a static shot, but select the next position as the target.
  - Calculate the solution and update the inputs accordingly for the next position.
  - Repeat this process until ready to fire from the desired position.

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
