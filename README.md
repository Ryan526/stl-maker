# WIP STL Maker

STL Maker is a Python project that allows you to generate 3D models of bolts and export them to the STL format.

## Installation

This project requires Python 3.8 or later. The recommended way to install the necessary dependencies is by using a virtual environment.

1. Clone this repository:
    ```bash
    git clone https://github.com/Ryan526/stl-maker.git
    ```
2. Change into the project directory:
    ```bash
    cd stl-maker
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To generate an STL model of a bolt, you need to provide the necessary parameters (diameter, length, thread pitch, head diameter, head height, and torx size) and then run the script `bolt.py`.

Example:
```bash
python bolt.py
