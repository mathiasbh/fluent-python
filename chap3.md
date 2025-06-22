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

## Automatic Handling of Missing Keys

## Variations of dict

## Set theory

## Practical consequences of how sets works