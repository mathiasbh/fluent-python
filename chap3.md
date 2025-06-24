# Dictionaries and Sets

- The type `dict` is a fundamental part of Python's implementation. Class and instance attributes, module namespaces, and function keyword arguments are some of the core Python constructs represented by dictionaries in memory.
- Dictionaries are highly optimized
- Hash tables are the engines behind
  - Also `set` and `frozenset`.

## Modern dict Syntax

- Dict comprehensions
  - listcomps and genexps was adapted to `dict` comprehensions (and `set` comprehensions)
  - A `dictcomp` builds a dictionary from any iterable
  - `some_dict = {country: code for code, country in some_list}`


- Unpacking mappings
  - We can apply `**` to mor ethan one argument. This works when keys are all strings and unique across all arguments
  - see 3_unpacking_mappings.py
  -  `{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}`, the second `z` overwrites the first one.


- Merge mappings with `|`
  - `|` and `|=` to merge mappings
  - They are set union operators
  ```
  >>> d1 = {'a': 1, 'b': 3} 
  >>> d2 = {'a': 2, 'b': 4, 'c': 6} 
  >>> d1 | d2 
  {'a': 2, 'b': 4, 'c': 6}
  ```
  - `d1 |= d2` updates `d1` inplace.


- Pattern matching with mappings (`match/case`)
  - see 3_pattern_matching.py


## Standard API of Mapping Types

- `collections.abc` (abstract base classes) provide `Mapping` and `MutableMapping`
- Main value of ABCs is documenting and formalizing the standard interfaces for mappings, and serving as criteria for `isinstance` tests in code.
  - `isinstance({}, abc.Mapping) -> True`
  - Using `isinstance` is often better than checking if is of concrete `dict` type


- What is hashable
  - An object is hashable if it has a hash code which never changes during its lifetime (needs `__hash__()` method)
  - And can be compared to other objects (needs an `__eq__()` method)
  - Hashable objects which compare equal must have same hash code
  - Hashing converts input data (string, file, object, ...) into fixed-size string of bytes
  - Common use in security is password storage.
  - A tuple is hashable only if all its items are hashable


- Inserting of Updating mutable values
  - In line with "fail fast", `dict` access with `d[k]` raises error if not existing key. `d.get(k, default)` is an alternative whenever default value is more convenient than an error.
  - If you want to retrieve mutable value and update, there is a better way 
  - using `my_dict.setdefault(key, []).append(new_value)`
  - checks if key is not in dictionary, then inserts `[]`, else appends new value to existing key.


## Automatic Handling of Missing Keys

- defaultdict
  - Creats items with a default value on demand whenever a missing key is searched
  - Uses the special method `__missing__`


- The `__missing__` method
  - Deals with missing keys
  - Not defined in `dict`, but aware of it. So if you subclass `dict` and provide a `__missing__`, the `__getitem__` will call it whenever a key is not found instead of `KeyError`
  

## Variations of dict

- `collections.OrderedDict`
  - Built-in dict keeps the key ordered by default now.
  - So this is for backward compatibility

- `collections.ChainMap`
  - This instance holds a list of mappings that can be searched as one.
  - Lookup is performed on each input mapping in the order it appears and succeeds as soon as key is found.
  - `chain = ChainMap(some_dict1, some_dict2)`
  - The chainmap does not copy input mappings, but holds references.
  - Updates or insertions only affect the first input mapping
  - "ChainMap is useful to implement interpreters for languages with nested scopes, where ecah mapping represents a scope context, from the inntermost enclosing scope to the outermost scope."

- `collections.Counter`
  - Holds an integer count for each key.
  - Updaing an existing key adds to its count (`ct.update('aaabbc')` --> `Counter({'a':3, ...})`)
  - `ct.most_common(3)` -> three most common of `ct`.

- `shelve.Shelf`
  - Provides persistent storage for a mapping of string keys, serialized in `pickle` binary format.
  - Pickle is easy to use in simplest case, but has drawbacks.


- Subclassing `UserDict` instead of dict
  - It's better to create new mapping type by extending `collections.UserDict` than `dict`.
  - When using `dict`, we end up overriding methods


## Immutable Mappings


## Dictionary Views




## Practical consequences of how dict works


## Set theory

## Practical consequences of how sets works

