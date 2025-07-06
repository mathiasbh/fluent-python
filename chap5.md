# Data Class Builders

- Data class: In python it's easy to build simple class that is just a collection of fields, with little or no extra functionality
- This chapter cover three class builders you may use as shortcuts to write data classes
  - `collections.namedtuple`
  - `collectionstyping.NamedTuple`: requires type hints on fields
  - `@dataclasses.dataclass`: decorator that allows for more custom



## Overview of Data Class builders 

```
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
```

- Does the job of holding latitiude and longitude attributes
- `__init__` boilerplate becomes old fast 
- and it doesnt even give basic features that we expect (`==` compares object IDs, `__repr__` not helpful)
- Implementation using `namedtuple`
```
from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')

import typing 
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
```
  - now printing gives info, comparison works
- `5_coordinates.py`
  - although `NamedTuple` appears as super-class, it is not. It uses metaclass


### Main features

- Mutable instances: 
  - `namedtuples` build `tuple` subclasses and therefore immutable.
  - `dataclass` mutable, but accepts `frozen=True`
- Class statement syntax
  - `typing` and `dataclass` support regular class statement - easier to add methods and docstrings...
- Construct dict 
  - both `tuples` provide `._asdict` to construct dict. `dataclass` provides function `dataclasses.asdict`
- Get field names and default values
  - all three lets you get field names and values


## Classic named tuples

## Typed named tuples


## Type hints 101


## More about `@dataclass`


