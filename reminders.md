# collections module - container datatypes

- Implements specialized container datatypes provinding alternatives to Python's general purpose built-in containers (`dict`, `list`, `set`, `tuple`)


# Mappings
- Mappings are structures that store data in key-value pairs.
- Efficient for lookups, insertions, deletions.
- Dictionaries are the most common


# Hash tables
- Data structure that stores key- value pairs and allow for fast data retrieval
- It uses hash function to compute and index (hash code) into an array
- They offer average-case constant time complexity `O(1)` for lookups, insertions, deletion
- `dict`.


# Dataclass.dataclass
- Decorator `@dataclass` for classes to build data class.
- Easier to instantiate without using `__init__` and `self`.
- Implements a `__repr__()` and `__eq__()` for nicer string representation and comparison

```
@dataclass
class SomeClass"
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)
```

# Type hints
A way to declare expected type of function arguments, return values, variables, attributes
- `list[int], tuple[str, float]`
- `typing,Optional` like `Optional[str]` to declare field that can be `str` or `None`
- `var_name: some_type = some_value` (`lat: float = 1.5`)