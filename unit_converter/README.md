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

---

## Design Patterns Used

---

## Structure
unit_converter/
│
├── converters/              # Contains all conversion logic
│   ├── __init__.py          # Marks directory as a Python package
│   ├── base.py              # Abstract base class
│   ├── length.py            # Length conversions
│   ├── weight.py            # Weight conversions
│   ├── temperature.py       # Temperature conversions
│   ├── liquid.py            # Liquid conversions
│
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── validator.py         # Validation logic
│   ├── errors.py            # Custom error classes
|   ├── error_handler.py     # Error handling logic
│
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

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```
