from enum import Enum
class Country(Enum):
    India = 1
    Pakistan = 2
    China =6
    SriLanka = 3
    Nepal = 4
    Bangladesh = 5
for data in Country:
    print('{:15} = {}'.format(data.name, data.value))
