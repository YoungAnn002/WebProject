# Boats

class boat:
    def _init_(self, id) -> None:
        self.boat_id: int = id
        self.boat_type: str = None
        self.next_boat: 'boat' = None
        self.prev_boat: 'boat' = None

b1 = boat(id = 1)
b2 = boat(id = 2)
b3 = boat(id = 3)
b4 = boat(id = 4)
b5 = boat(id = 5)

b1.next_boat = b2
b2.next_boat = b3
b3.next_boat = b4
b4.next_boat = b5

print(b1.next_boat.boat_id)

#loop
cur_boat = b1 #theboat we are intered in
while(cur_boat.next_boat):
    print(cur_boat.boat_id)
    cur_boat = cur_boat.next_boat