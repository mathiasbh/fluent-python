## uv project

```
uv init [project-name]
cd [project-name]
```

or 

```
mkdir [project-name]
cd [project-name]
uv init
```

Add packages `uv add numpy==`




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

- `match/case` statement
  - May look similar to `switch/case` from C language, however...
  - Key improvement is _destructuring_: more advanced  form of unpacking
  - see 2_matchcase.py


- Pattern matching seq in interpreter
  - can replace if/else,
  - evaluate example where first argument `expression` is checked using match



## Slicing

- Why slices and ranges exclude the last item
  - `range(3)` and `my_list[:3]` produce three items
  - Easy to compute length of slice with start and stop as `stop - start`
  - Easy to split sequence in two at any index ithout overlapping `my_lsit[:x] and my_list[x:]`


- Slice objects
  - Stride with third input `s[a:b:c]`, e.g. `s[::-1]` to reverse (start-stop-step)
  - Python calls slice object `slice(a, b, c)`


- Multidimensional Slicing and Ellipsis
  - Ellipsis (`...`) is recognized as token by Python parser
  - e.g. numpy if four-dim `x[i, ...]` is shortcut for `x[i, :, :, :,]`


## Using + and *

- Usually both operands of + must be the same sequence type.
- Both + and * always create a new object, and never change their operands
- Beware: `a * n` where `a` is a sequence of mutable items. `my_list = [[]] * 3` will result in a list with three references to the same inner list
- Correct: `[['_'] * 3 for i in range(3)]`
- Wrong  : `[['_'] * 3] * 3` (same row is appended three times)


- Augmented assignment with sequences
  - Augmented operators `+=` and `*=`
  - calls `__iadd__` (inplace addition)

## When a list is not the answer

- An array saves a lot of memory when handling millions of floating-point values
- If constantly adding and removing items from opposite ends of a list, think of `deque` (double-ended queue)
- If frequently checking if item is present, consider `set`.

- Arrays
  - If list only contains numbers, `array.array` is more efficient.
  - `array.tofile` and `array.fromfile` are easy to use and very fast
  - As of Python 3.10, array type does not have in-place sort

- `memoryview`
  - Class that lets you handle slices of arrays without copying bytes
  - Essentially a generalized NumPy array in Python (without the math). Share memory between data-structures without first copying.
  - If doing advanced numeric processing, you should use NumPy (or other)

- Deques and other Queues
  - `.append` and `.pop` make a `list` usuable as a stack or queue - you get First In First Out behaviour.
  - Inserting and removing from head of list is costly, because entire list must be shifted in memory.
  - `collections.deque` is designed for this.
  ```
  from collections import deque
  dq = deque(range(10), maxlen=10)
  ```
  - queue:
  - multiprocessing
  - asyncio
  - heapq