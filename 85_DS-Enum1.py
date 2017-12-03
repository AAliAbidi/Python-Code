from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antartica = 672
print('\nMember name: {}'.format(Country.Albania.name))
print('\nMember value: {}'.format(Country.Albania.value))