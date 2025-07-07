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

- `collections.namedtuple` is a factory that builds subclasses of `tuple` enhanced with
  - field names
  - class name
  - informative `__repr__`
- Can be used anywhere where `tuple`s are needed
- `abc = namedtuple('typename', 'field_names') -> class with name typename(fieldname1 = ..., fieldname2 = ...)`


```
Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
Coordinate(0,0) --> Coordinate(lat=0, lon=0, reference='WGS84')
Coordinate._field_defaults --> {'reference': 'WGS84'}
```


## Typed named tuples

The above can be re-written using `typing.NamedTuple`

```
class Coordinate(typing.NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
```


## Type hints 101

Type hints or Type Annotations
- ways to declare expected type of function arguments, return values, variables, attributes
- They are not enforced at all by python bytecode compiler and interpreter


### No runtime effects

- Type hints can be thought as "documentation that can be verified by IDEs and type checkers"
- They have no impact on runtime in python
- use mypy

### Variable annotation syntax
Syntax

- `var_name: some_type` (`lat: float`)
- `list[int], tuple[str, float]`
- `typing,Optional` like `Optional[str]` to declare field that can be `str` or `None`
- `var_name: some_type = some_value` (`lat: float = 1.5`)


### Meaning of variable annotations




## More about `@dataclass`


