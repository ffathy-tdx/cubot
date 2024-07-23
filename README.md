# Rubik's Cube Solver
## Project Documentation

**Contributors:**  
Fares Fathy  
Abdulrahman Saeed

**Course:**  
Embedded Systems & IOT

This repository contains the code and documentation for a Rubik's Cube solver project. The project includes Arduino code for controlling a motorized Rubik's Cube mechanism and Python code for image processing and generating the Rubik's Cube solution.

## Project Overview

The Rubik's Cube solver project aims to automate the process of solving a Rubik's Cube. The motorized Rubik's Cube mechanism is controlled using an Arduino board, which receives commands from a Python script based on image processing. The Python script captures an image of the Rubik's Cube and extracts the colors of each facelet, allowing for the generation of the Rubik's Cube solution. The solution is then sent back to the Arduino, which moves the motorized mechanism to solve the Rubik's Cube accordingly.

## Repository Structure

The repository is structured as follows:

- `arduino_code/`: Contains the Arduino code for controlling the motorized Rubik's Cube mechanism.
- `image_processing/`: Contains the Python code for image processing and generating the Rubik's Cube solution.
- `faces/`: Contains example images of Rubik's Cube faces for testing and development.
- `README.md`: Provides an overview of the project, installation instructions, and usage guidelines.
- `LICENSE`: Specifies the license under which the project is distributed.

## Installation and Usage

To replicate this project on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/rubiks-cube-solver.git`
2. Set up the hardware components according to the provided documentation.
3. Upload the Arduino code to the Arduino board.
4. Install the required Python dependencies using `pip install -r requirements.txt`.
5. Adjust the pin connections in the Arduino code based on your hardware setup.
6. Run the Python script facecapture.py to capture an image from a camera. Then, to extract the face colors from the images run the python script facetostring.py
7. Ue the face colors to generate the Rubik's Cube solution using the solver.py script.
8. Modify the Python code to send the generated solution commands to the Arduino using the provided Arduino communication protocol.
9. Run the modified Python code to send the solution commands to the Arduino and control the motorized Rubik's Cube mechanism accordingly.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please submit an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
---

For further questions, please contact us at [ffathy2004@gmail.com](mailto:ffathy2004@gmail.com) or [abdosaaed749@gmail.com](mailto:ffathy2004@gmail.com). 
