class store:
    def __init__(self, name, inventory={}, gold=200):
        self.name = name
        self.inventory = inventory
        self.gold = gold


    def display_store_items(self):
        print("You can see the following items on the shelves.\n"
              "The price tags are scribbled in a shaky handwriting")
        for item, count in self.inventory.items():
            print(f'{count} {item.name}, {item.value} gold')


    def enter(self, player):
        player_choice = 0
        print(f'Welcome to {self.name}')

        while (player_choice != '5'):
            print ('''What would you like to do
                    1 - List wares
                    2 - Buy item
                    3 - Sell item
                    4 - List your items
                    5 - Leave''')

            player_choice = input('Your choice: ')
            if (player_choice == '1'):
                self.display_store_items()

            elif (player_choice == '4'):
                print(player.show_items())

            elif (player_choice == '2'):
                player_item_choice = input("What item would you like to buy? ")
                item = player_item_choice.lower()
                if self.check_in_stock(item):
                    item = self.inventory[item]
                    self.player_buys(player, item)
                else:
                    print("I don't have that item in my wares")

            elif (player_choice == '3'):
                print(f'I currently have {self.gold} gold.\n'
                      f'what would you like to sell?')
                player_item_choice = input("What item would you like to sell? ")
                item = player_item_choice.lower()
                if item in player.inventory.keys():
                    self.player_sells(player, item)
                else:
                    print("You don't have that item on you")



        print(f'See you later {player.name}')



    def player_buys(self, player, item):
        if player.gold >= item.value:
            player.add_to_inventory(item)
            self.inventory[item] -= 1
            if self.inventory[item] <= 0:
                del self.inventory[item]
        else:
            print(f"You can't afford a {item.name}\n"
                  f"Come back when you have more gold!")


    def player_sells(self, player, item):
        if self.gold >= item.value:
            self.add_to_stock(item)
            player.inventory[item] -= 1
            if player.inventory[item] <= 0:
                del player.inventory[item]
        else:
            print(f"I'm afraid I can't afford {item.name}\n"
                  f"Maybe consider selling something less pricey")


    def add_to_stock(self, item):
        if item.name in self.inventory.keys():
            self.inventory[item.name] += 1
        else:
            self.inventory[item.name] = 1


    def check_in_stock(self, item_name):
        for items in self.inventory.keys():
            if item_name == items.name:
                return True
        return False





