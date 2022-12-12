from typing import List, Callable
from math import floor


class Monkey:
    operations = {"*": int.__mul__, "+": int.__add__}

    def __init__(
        self,
        starting_items: List[int],
        operation: Callable[[int], int],
        test_num: int,
        mti: int,
        mfi: int,
    ) -> None:
        self.items = starting_items.copy()
        self.operation = operation
        self.test_num = test_num
        self.mti = mti
        self.mfi = mfi
        self.inspections = 0

    @staticmethod
    def from_data(s: List[str]):
        items = list(map(int, s[1].split(": ")[1].split(",")))
        operation_parts = s[2].split(" ")
        operation_num = (
            int(operation_parts[-1]) if operation_parts[-1].isnumeric() else None
        )
        operation = lambda x: Monkey.operations[operation_parts[-2]](
            x, operation_num or x
        )
        test_num = int(s[3].split(" ")[-1])
        mt = int(s[4].split(" ")[-1])
        mf = int(s[5].split(" ")[-1])
        return Monkey(items, operation, test_num, mt, mf)

    def catch(self, item: int):
        self.items.append(item)

    def throw_next(self, players: List["Monkey"], worry: Callable[[int], int]) -> bool:
        if not self.items:
            return False
        self.inspections += 1
        item = self.items.pop()
        item = self.operation(item)
        item = worry(item)
        test = lambda x: x % self.test_num == 0
        catcher = players[self.mti if test(item) else self.mfi]
        catcher.catch(item)
        return True

    def play_round(
        self,
        players: List["Monkey"],
        worry: Callable[[int], int],
    ):
        while self.throw_next(players, worry):
            pass
