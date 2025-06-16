## Built-in Sequences

- Container sequences: 
  - Can hold items of different types (list, tuple, collection.deque)
  - Holdes references to the objects it contains.

- Flat sequences: 
  - Hold items of simple type (str, bytes, array.array)
  - Stores the value of its contents in its own memory space  
  - more compact, but limited toholding primitive machine values

- Mutable sequences
  - list, bytearray, array.array, collections.deque

- Immutable sequences
  - typle, str, bytes


## List comprehension, generator expr

Walrus operator (:=), Remains accssible

To initialize tuples, arrays, ..., you could start from listcomp, but genexp saves memory because it yields items one by one (iterator protocol). Syntax is similar but with parentheses.


## Tuples are not just immutable lists
1) Tuples can be used as immutable lists and
2) also as records with no field names


- Tuples as Records
  - When using a tuple as collection of fields, the number of items is usually fixed and their order is always important
  - This is maybe irrelevant when thinking of tuple as immutable list.
  - tuple unpacking

- Tuples as Immutable Lists
  - Clarity: length will never change
  - Performance: Uses less memory than a list of same length. Python can do some optimizations.
  - An element in a tuple can be a list, which is then mutable... Avoid this?

## Unpacking Sequences and Iterables

```
>>> divmod(20, 8) = (2, 4)
>>> t = (20, 8)
>>> divmod(*t) = (2, 4)
>>> divmod(t) = divmod expected 2 arguments, got 1
```

- Using * to Grab Excess Items (*args)
  - *args: to grab arbitrary excess arguments
  - ```>>> a, b, *rest = range(5)```
  - ```>>> a, b, *rest = (0, 1, [2,3,4])```


- Unpacking with * in Function calls and sequence literals
```
>>> def fun(a, b, c, d, *rest): 
...     return a, b, c, d, rest 
... 
>>> fun(*[1, 2], 3, *range(4, 7)) 
(1, 2, 3, 4, (5, 6))
```


## Pattern Matching with Sequences


## Slicing



## Using + and *