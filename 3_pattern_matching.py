def get_creator(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            # match any mapping with type=book, api=2 and authors=sequence
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            # match any mapping with type=book, api=1 and authors=any object
            return [name]
        case {'type': 'book'}:
            # any other mapping type=book is invalid
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            # type=movie, director=single object
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        
        
from collections import OrderedDict
        
b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
b3 = {'type': 'book', 'pages': 770}

#print(get_creator(b1)) -> ['Douglas Hofstadter']
#print(get_creator(b2)) -> ['Martelli', 'Ravenscroft', 'Holden']
#print(get_creator(b3)) -> error