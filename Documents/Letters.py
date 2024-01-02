# Letters

from dataclasses import dataclass

class Letter:
    letter_id: str = ""
    letter_next: 'Letter' = None
    letter_prev: 'Letter' = None
    letter_up: 'Letter' = None
    letter_down: 'Letter' = None

a = Letter()
a.letter_id = 'a'

b = Letter()
b.letter_id = 'b'

a.letter_next = b
print(a.letter_next)