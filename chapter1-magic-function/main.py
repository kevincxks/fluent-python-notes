import collections
from math import hypot
import random



Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks: list = [str(n) for n in range(2, 11)] + list('JQKA')
    suits: list = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards: list = [Card(rank, suit) for suit in self.suits
                                              for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()


print(len(deck))
print(deck[0])
print(deck[-1])

for card in deck:
    print(card)


def my_order(card: Card):
    suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)
    return FrenchDeck.ranks.index(card.rank) * 10 + suit_values[card.suit]

for card in sorted(deck, key=my_order):
    print(card)


class Vector:
    
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    # 优先实现__repr__
    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    # 用在bool上下文中, bool()调用该函数, 如果不存在该函数会判断__len__()是否为0
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

print(v * 3)
print(abs(v * 3))



