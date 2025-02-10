# Unit Converter CLI Application

## Overview
This project provides a Command-Line Interface (CLI) tool for converting values between different units of measurement, including:
- **Length**: meters, kilometers
- **Weight**: kilograms, grams
- **Temperature**: Celsius, Fahrenheit
- **Liquid**: liters, milliliters

---

## Features
1. Allow users to choose a conversion type (length, weight, temperature, liquid)
2. Accept and validate input for source unit, target unit, and value to convert
3. Display the converted value with appropriate precision and formatting
4. Handle errors such as invalid units, unsupported conversions, non-numeric values
5. Save conversion history to a CSV file and view it

---

## Design Patterns Used

- **Factory Pattern**: Used to create converters based on the selected conversion type
- **Singleton Pattern**: Ensures only one instance of the converter factory is created

---

## Structure
unit_converter/
│
├── converters/              # Contains all conversion logic
│   ├── __init__.py          # Marks directory as a Python package
│   ├── base.py              # Abstract base class
│   ├── factory.py           # Converter factory
│   ├── length.py            # Length conversions
│   ├── weight.py            # Weight conversions
│   ├── temperature.py       # Temperature conversions
│   ├── liquid.py            # Liquid conversions
│
├── handler/                 # Handles user input and output
│   ├── input_handler.py     # Handles user input
│
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── validator.py         # Validation logic
│   ├── errors.py            # Custom error classes
|   ├── error_handler.py     # Error handling logic
|   ├── enum.py              # Enum classes
│   ├── history_manager.py   # History manager
|   ├── renderer.py          # User interface rendering
│
├── constants.py             # Contains global constants
├── main.py                  # Entry point for the program
├── requirements.txt         # Dependency list
├── README.md                # Project documentation
├── .gitignore               # Ignore unnecessary files
├── .editorconfig            # Editor configuration

---
### Prerequisites
- Python 3.10 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone https://gitlab.asoft-python.com/phuong.buimai/python-training
   cd unit-converter
   ```

2. Install uv: [Refer this link](https://docs.astral.sh/uv/getting-started/installation/)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create a virtual environment:
   ```bash
   uv venv .vituralenv
   ```

4. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

5. Run the vitual environment:
   ```bash
   source .virtualenv/bin/activate
   ```

6. Run the application:
   ```bash
   uv run main.py
   ```
7. Run unit tests:
   ```bash
   coverage run -m unittest tests/<test_file>
   ```
8. Generate coverage report:
   ```bash
   coverage report -m
   ```
