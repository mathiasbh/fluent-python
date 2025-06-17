
metro_areas = [
    ('São Paulo 2', 'BR 2', 19.649, (-23.547778, -40.635833), 'test'),
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)), 
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)), 
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)), 
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        #print(record) 
        match record:  # subject of match is "record"
            case [name, _, _, (lat, lon)] if lon <= 0:  # check if subject have same number of items AND item matches including nested items
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
            case [name, _, _, (lat, lon), *rest] if lon <= 0:
                print("case 2")
            case [name, _, _, (int(lat), int(lon))]:
                print("case 3")
                
    # checks if subject has 4 elements, and last element is tuple of two.       
if __name__ == "__main__":
    main()