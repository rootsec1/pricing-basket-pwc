# Pricing Basket

**Minimum python version required: `3.7`**

Given a list of items (shopping cart), this command line tool is modelled to apply any eligible offers to the cart and return the net amount to be paid.

## Usage

Syntax: `$ python3 index.py --cart [{Soup,Bread,Milk,Apple} ...]`

Example: `$ python3 index.py --cart soup bread soup apple bread soup soup apple`

Tests: `$ python3 -m unittest discover`

## Screenshot
![Screenshot](https://i.imgur.com/vv3Exf5.png)

## Directory Structure

```
.
├── README.md
├── cli
│   ├── __init__.py
│   └── cmd_parser.py
├── constants
│   ├── __init__.py
│   ├── color_codes.py
│   ├── descriptive_strings.py
│   └── enums.py
├── core
│   ├── __init__.py
│   └── process.py
├── data
│   ├── __init__.py
│   ├── sample_data.json
│   └── setup_data.py
├── index.py
├── models
│   ├── __init__.py
│   ├── item_model.py
│   └── offer.py
└── util
    ├── __init__.py
    └── index.py
```
