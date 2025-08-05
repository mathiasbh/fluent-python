from dataclasses import dataclass, field, fields
from enum import Enum, auto
import datetime

class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()
    
@dataclass
class Resource:
    """Media resource description"""
    identifier: str  # required
    title: str = '<untitled>'  # first field with default, anything below must have defaults!
    creators: list[str] = field(default_factory=list) 
    date: datetime.date | None = None  # newer syntax than Optional[date]
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)
    
    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')

        res.append(')')
        return '\n'.join(res)


description = 'Improving the design of existing code'
book = Resource(
    '978-0-13-475759-9', 
    'Refactoring, 2nd Edition', 
    ['Martin Fowler', 'Kent Beck'], 
    datetime.date(2018, 11, 19), 
    ResourceType.BOOK, description, 'EN', 
    ['computer programming', 'OOP'])

print(book) # doctest: +NORMALIZE_WHITESPACE 
#Resource(
#    identifier='978-0-13-475759-9', 
#    title='Refactoring, 2nd Edition', 
#    creators=['Martin Fowler', 'Kent Beck'], 
#    date=datetime.date(2018, 11, 19), 
#    type=<ResourceType.BOOK: 1>, 
#    description='Improving the design of existing code', 
#    language='EN', 
#    subjects=['computer programming', 'OOP'])