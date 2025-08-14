# Functions as first-class objects

- First--class object:
  - created at runtime
  - assigned to a variable or element in data structure
  - passed as an argument to a function
  - returned as the result of a function
  - e.g. integers, strings, dictionaries


## Treating function like an object
- Create function, call it, read its `__doc__` to see that it is object, or `type()`
- `new_var = some_func`, `map(some_func, range(10))`
  - some "first class" nature of function object
  - assign function to variable, pass function as argument to map function


## Higher-order function
- higher order: function that takes function as argument or returns a function
- e.g. map, filter, reduce
- `sorted(some_list, key=some_func)`

### Modern replacements for map, filter, reduce
- map and filter
  - list comprehension and generator expressions more readable
  - `list(map(factorial, range(6)))`
  - `[factorial(n) for n in range(6)]`
  - `list(map(factorial, filter(lambda n: n % 2, range(6))))`
  - `[factorial(n) for n in range(6) if n % 2]`

- sum instead of reduce
  - `reduce(add, range(100))`
  - `sum(range(100))`


## Anonymous function