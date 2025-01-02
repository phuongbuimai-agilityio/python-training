import os
import csv

from utils.error_handler import handle_io_error


class HistoryManager:
    def __init__(self, file_name="conversion_history.csv") -> None:
        self.file_name = file_name

    def save_to_history(
        self,
        conversion_type: str,
        source_unit: str,
        target_unit: str,
        value: float,
        result: float,
    ) -> None:
        """Save conversion history to a CSV file.

        Args:
            conversion_type (str): Type of unit conversion (e.g., 'length', 'weight', 'temperature', 'liquid')
            source_unit (str): The source unit
            target_unit (str): The target unit
            value (float): The numeric value to convert
            result (float): The converted value
        """
        try:
            file_exits = os.path.isfile(self.file_name)
            with open(self.file_name, "a", newline="") as file:
                writer = csv.writer(file)

                # Write the header if the file is new
                if not file_exits:
                    writer.writerow(
                        [
                            "Conversion Type",
                            "Source Unit",
                            "Target Unit",
                            "Value",
                            "Result",
                        ]
                    )
                writer.writerow(
                    [conversion_type, source_unit, target_unit, value, result]
                )

            print(f"Conversion history saved to {self.file_name}")
        except IOError as e:
            handle_io_error(e, "writing")

    def display_history(self) -> None:
        """Display conversion history from a CSV file."""
        try:
            # Validate file exists or not
            if not os.path.isfile(self.file_name):
                print("Conversion history file not found.")
                return
            # Read the CSV file
            with open(self.file_name, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)
                history = list(reader)

            if not history:
                print("Conversion history is empty.")
                return

            print("Conversion History:")
            print("==============")
            print("\n")
            for row in history:
                print(f"Conversion Type: {row[0]}")
                print(f"Source Unit: {row[1]}")
                print(f"Target Unit: {row[2]}")
                print(f"Value: {row[3]}")
                print(f"Result: {row[4]}")
                print("==============")

        except IOError as e:
            handle_io_error(e, "reading")
