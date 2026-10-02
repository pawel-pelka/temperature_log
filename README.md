# Temperature Log

A small command-line Python learning project for recording city temperatures in Celsius and exploring saved measurements.

## Requirements

Python **3.14 or newer**. The exception syntax in `check_temperature.py` requires Python 3.14. The programs use only the standard library; tests require pytest.

## Record measurements

Run commands from the project directory:

```bash
python3 temperature_log.py
```

Enter `y` to add a city and its temperature. Enter `n` to finish, display a summary, and save the measurements to `measurements.json`.

The summary includes the overall average, the average for each city, and the cities tied for the highest individual temperature reading.

Saved measurements are loaded on the next run. A missing data file starts an empty log; invalid JSON stops the program without overwriting the file. `measurements.json` is excluded from Git.

## Filter measurements

Find cities with at least one temperature above 15 degrees Celsius:

```bash
python3 check_temperature.py ">" 15
```

For measurements Berlin: 20, London: 15, and Paris: 10, the result is:

```text
['Berlin']
```

Supported operators are `<`, `=`, and `>`. Keep the operator in quotes so the shell passes it to Python. Results contain unique city names in alphabetical order.

Run without arguments to enter the operator and temperature interactively:

```bash
python3 check_temperature.py
```

## Tests

In an activated Python 3.14+ virtual environment, install pytest and run the tests:

```bash
python -m pip install pytest
python -m pytest
```

Tests cover the overall average, empty input for averaging, comparison operators, multiple matches, duplicate removal, sorting, no matching cities, and invalid operators.
