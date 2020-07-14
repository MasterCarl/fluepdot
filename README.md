# Fluepdot HTTP API Python wrapper

This Python wrapper provides several convenience methods to interface with the HTTP API of the hardware/software project 
[fluepdot](https://fluepdot.readthedocs.io/).
It relies on the _Pillow_ library to render text and load images/bitmaps.

## Installation
Install it by running `pip3 install fluepdot`.

## Usage
There is a CLI for basic functions. To view the help, run `python3 -m fluepdot --help`.

To use it in Python code, instantiate a Fluepdot class:
```python
from fluepdot import Fluepdot
fluepdot = Fluepdot("http://fluepdot.local")
```

For more details, check out the `examples` folder.