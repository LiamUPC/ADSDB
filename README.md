# ADSDB Data Management Backbone

This repository contains our data management backbone to our ADSDB project.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries necessary for running the backbone.

```bash
pip install -r requirements.txt
```

## Usage

By default, the repository comes with all the available files in the data/temporal directory. There are two options:

- Running scripts/main.py with all the files in data/temporal
- Keeping some files back and running scripts/main.py. Then placing the files you have saved back into the data/temporal
  directory and running scripts/main.py again. That way you can simulate the process of the data management backbone
  receiving new data, processing and adding it to the exploitation zone database.


```bash
python main.py
```