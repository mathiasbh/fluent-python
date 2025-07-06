from typing import NamedTuple

class Coordinate_2(NamedTuple):
    lat: float
    lon: float
    
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
    # a = Coordinate(10, -50)
    # print(a) -> "10.0°N, 50.0°W"


from dataclasses import dataclass
    
@dataclass(frozen=True) # cannot be modified
class Coordinate_3:
    lat: float
    lon: float
    
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
    # a = Coordinate(10, -50)
    # print(a) -> "10.0°N, 50.0°W"
    
    
    
c2 = Coordinate_2(10, -50)
c3 = Coordinate_3(10, -50)