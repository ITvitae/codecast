# codecast

Run code on your machine, from a browser window.

This as meant as an alternative to a terminal emulator, for teaching programming et cetera.

> Please think before you use this: don't deploy this on a web facing server (if you don't understand why not, turn back!).

## Project state
Most of the original work on the project was done in 2021.
However, a few things are still missing, most notably a way to interact with scripts (think Python's `input()`).
Since nothing was done with the tool since 2021, it seemed about time to open source what's here.

## Requirements

`python3` and it's version of `pip`.

## Quickstart

### With `virtualenv`

```bash
# Clone this repository.
git clone `https://github.com/ITvitae/codecast`.

# Create a new virtual environment, here called `env3`
virtualenv -p python3 env3

# Activate the new environment
source env3/bin/activate

# Install flask
pip install flask

# Start the codecast server
python codecast.py
```

Connect to the server with your browser by going to [http://localhost:5001](http://localhost:5001).

### Without `virtualenv`

```bash
# Clone this repository.
git clone git@gitlab.com:Descrypt/codecast.git

# Install flask
pip3 install flask

# Start the codecast server
python3 codecast.py
```

Connect to the server with your browser by going to [http://localhost:5001](http://localhost:5001).
