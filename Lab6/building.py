from typing import TypeVar, Generic, List

T = TypeVar('T')

class Building(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def add_item(self, item: T) -> None:
        """
        Add an item to the building.
        """
        self.items.append(item)

    def remove_item(self, index: int) -> T:
        """
        Remove an item from the building by its index.
        """
        if self.items:
            return self.items.pop(index)
        else:
            print("The building is empty.")

    def get_item(self, index: int) -> T:
        """
        Get an item from the building by its index.
        """
        if self.items:
            return self.items[index]
        else:
            print("The building is empty.")

    def num_items(self) -> int:
        """
        Get the number of items in the building.
        """
        return len(self.items)
