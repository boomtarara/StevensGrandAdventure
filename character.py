import random

class character:
    def __init__(self, name, max_health, inventory={}, stat_attack=1, stat_defence=1, gold=0):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.stat_attack = stat_attack
        self.stat_defence = stat_defence
        self.inventory = inventory
        self.gold = gold
        self.alive = True


    def show_combat_stats(self):
        text =(f'{self.name} has:\n'
              f'{self.health} health\n'
              f'{self.stat_attack} attack\n'
              f'{self.stat_defence} defence\n')
        return text

    def show_items(self):
        text = "Your backpack currently contains:\n"
        for item, count in self.inventory.items():
            text += f'{count} {item.name}, worth {item.value} gold each\n'
        text += f"You also have {self.gold} gold coins in your man-purse"
        return text


    def combat(self, opponent):
        if not opponent.is_dead():
            hit_power = self.stat_attack - opponent.stat_defence
            self.try_break_defence(opponent)
            opponent.health -= hit_power if hit_power > 0 else 0
            print(f"{self.name} hits {opponent.name} for {hit_power} damage\n"
                  f"{opponent.name}'s health is now {opponent.health}")
        else:
            opponent.alive = False
            self.victory(opponent)


    def try_break_defence(self, opponent):
        if random.randrange(0, 11) == 10 and opponent.stat_defence > 0:
            opponent.stat_defence -= 1
            print(f"{self.name} has broken through {opponent.name}'s guard\n"
                  f"{opponent.name}'s defense is now: {opponent.stat_defence}")

    def is_dead(self):
        return True if self.health <= 0 else False


    def AI_action(self):
        if self.health <= self.max_health / 2:
            if 'super potion' in self.inventory.keys():
                self.use_item(self.inventory['super potion'])
            if 'potion' in self.inventory.keys():
                self.use_item(self.inventory['potion'])


    def check_in_inventory(self, item_name):
        for items in self.inventory.keys():
            if item_name == items.name:
                return True
        return False


    def add_to_inventory(self,item):
        if self.check_in_inventory(item.name):
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1


    def use_item(self, item):
        self.max_health += item.max_health_up
        self.health += item.max_health_up
        self.stat_attack += item.stat_attack_up
        self.stat_defence += item.stat_defence_up


    def victory(self, opponent):
        print('\n'*30)
        print('well done you have vanquished the ' + opponent.name)
        if len(opponent.inventory) > 0:
            combat_reward = random.choice(list(opponent.inventory.keys()))
            reward_item_count = opponent.inventory[combat_reward]
            for i in range(reward_item_count):
                self.add_to_inventory(combat_reward)
            print(f'for your victory you win {reward_item_count} {combat_reward.name}')
