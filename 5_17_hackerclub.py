from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class ClubMember:
    name: str
    # default factory makes sure list is built default value when data class is created
    # Then each instance has own instance of list, i.e. not sharing across all instances!
    guests: list = field(default_factory=list)
    
    
    
    
@dataclass
class HackerClubMember(ClubMember):
    #all_handles = set() # keep list of all handles, to check if identical exists
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''
    
    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)



#anna = HackerClubMember('Anna Ravencroft', handle='AnnaRaven')
#leo = HackerClubMember('Leo Rachel', guests=[], handle='Leo')
#leo2 =HackerClubMember('Leo DaVinci') # ERROR, handle dupe