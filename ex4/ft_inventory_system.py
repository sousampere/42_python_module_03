#!/usr/bin/python3

class Player:
    """
    Player class. Is a player.
    """
    def __init__(self, name: str) -> None:
        """Creates the player

        Args:
            name (str): Name of the player

        Returns:
            None
        """
        self.name = name
        self._inventory = []
        return (None)

    def add_item(self, item: dict) -> None:
        """Adds an item to the player's inventory

        Args:
            item (dict): item to add

        Raises:
            ValueError: Incorrect value inside the item

        Returns:
            None
        """
        self._inventory.append(item)
        if (item.keys == {'name', 'type', 'rarity', 'count', 'value'}):
            if (type(item['name']) is not str or
                type(item['type']) is not str or
                type(item['count']) is not int or
                    type(item['value']) is not int):
                raise ValueError(f"Wrong value type : {item}")
            else:
                self._inventory.append(item)
        return (None)

    def display_items(self) -> None:
        """Displays the item in the stdout

        Returns:
            None
        """
        for item in self._inventory:
            print(f"{item['name']} ({item['type']} {item['rarity']}): "
                  f"{item['count']}x @ {item['value']} gold each "
                  f"= {item['count'] * item['value']} gold")
        return (None)

    def get_inventory_value(self) -> int:
        """Returns the sum of the gold value of each item

        Returns:
            int: gold value
        """
        value = 0
        for item in self._inventory:
            value += item['count'] * item['value']
        return (value)

    def count_items(self) -> int:
        """Return the number of items of the players

        Returns:
            int: Number of items
        """
        count = 0
        for item in self._inventory:
            count += item['count']
        return (count)

    def get_inventory(self) -> list:
        """Returns the player's inventory as a list of items (dict)

        Returns:
            list: items
        """
        return (self._inventory)

    @staticmethod
    def get_categories(*players: "Player") -> list:
        """Returns a list of the available categories of the items, with count

        Returns:
            list: items
        """
        categories = {}
        for player in players:
            for item in player.get_inventory():
                if (item['type'] in categories.keys()):
                    categories['type'] += item['type']
                else:
                    categories.update({item['type']: item['count']})
        return (categories)

    @staticmethod
    def get_most_valuable_player(*players: "Player") -> dict:
        """Returns the most valuable player among all, with its value

        Returns:
            dict: player name and value
        """
        top_player = {'name': "", 'value': -1}
        for player in players:
            if (player.get_inventory_value() > top_player['value']):
                top_player = {
                    'name': player.name, 'value': player.get_inventory_value()}
        return (top_player)

    @staticmethod
    def get_most_items_player(*players: "Player") -> dict:
        """Returns the most playes with the most items

        Returns:
            dict: Player name and items
        """
        top_player = {'name': "", 'items': -1}
        for player in players:
            if (player.count_items() > top_player['items']):
                top_player = {
                    'name': player.name, 'items': player.count_items()}
        return (top_player)

    @staticmethod
    def get_rarest_items(*players: "Player") -> dict:
        """Returns the rarest item as a list with its name and the count
        (rarest form all given players)

        Returns:
            dict: _description_
        """
        items = {}
        for player in players:
            for item in player.get_inventory():
                if (item['name'] in items.keys()):
                    items.update({item['name']: items[item['name']]
                                  + item['count']})
                else:
                    items[item['name']] = item['count']
        return (sorted(items.items())[-1])

    def transfer_item(self, target: "Player",
                      target_item: str, count: int) -> None:
        """Transfers an item from the player to the target

        Args:
            target (Player): targeted player
            target_item (str): item to transfer
            count (int): amount to transfer

        Raises:
            Exception: Not enough items to transfer

        Returns:
            None
        """
        for item in self._inventory:
            # For each item the player has
            if (item['name'] == target_item):
                # If this is the item we want to transfer
                item['count'] -= count  # We take if from the owner
                if (item['count'] < 0):
                    raise Exception("Not enough items to send")
                if (item['count'] == 0):
                    self._inventory.remove(item)  # Removes the item
                # Checks if the target has the item
                for targeted_item in target.get_inventory():
                    if (targeted_item['name'] == target_item):
                        targeted_item['count'] += count
                        return (None)
                # Item not found, creating a new one
                target.add_item({
                    'name': item['name'],
                    'type': item['type'],
                    'rarity': item['rarity'],
                    'count': count,
                    'value': item['value']
                })
        return (None)


print("=== PLayer Inventory System ===")
print("")
alice = Player("alice")
alice.add_item({
    'name': 'sword',
    'type': 'weapon',
    'rarity': 'rare',
    'count': 1,
    'value': 500
})
alice.add_item({
    'name': 'potion',
    'type': 'consumable',
    'rarity': 'common',
    'count': 5,
    'value': 50
})
alice.add_item({
    'name': 'shield',
    'type': 'armor',
    'rarity': 'uncommon',
    'count': 1,
    'value': 200
})

print("=== Alice's inventory ===")
alice.display_items()
print("")
print(f"Inventory value: {alice.get_inventory_value()}")
print(f"Item count: {alice.count_items()} items")
print("Categories: ", end="")
for k, v in Player.get_categories(alice).items():
    print(f"{k}({v}) ", end="")
print("")

bob = Player("Bob")

print("\n=== Transaction: Alice gives Bob 2 potions ===")
try:
    alice.transfer_item(bob, 'potion', 2)
except Exception as e:
    print("Error:", e)
print("Transaction successful!")

print("\n=== Updated Inventories ===")
print("Alice :")
alice.display_items()
print("Bob :")
bob.display_items()

print("\n=== Inventory Analytics ===")
mvp = Player.get_most_valuable_player(alice, bob)
print(f"Most valuable player: {mvp['name']} ({mvp['value']})")
mip = Player.get_most_items_player(alice, bob)
print(f"Most items player: {mip['name']} ({mip['items']} items)")
rarest = Player.get_rarest_items(alice, bob)
print(f"Rarest items: {rarest[0]} ({rarest[1]} item(s))")
