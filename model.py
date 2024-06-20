from dataclasses import dataclass, field
import pandas as pd
from credentials import *
import random

params = load_simulation_parameters()


@dataclass
class Player:
    id: int
    level: int = 1
    xp: int = 0
    sc: int = 0
    n_day: int = 1
    n_slots: int = 5
    inventory: dict = field(default_factory=dict)
    orders: list = field(default_factory=list)

    def modify_inventory(self, product, quantity):
        self.inventory[product] += quantity
        
        available_products

    def refill_orders(self):
        df_available_products = params["df_products"]
        available_products = df_available_products.query(f"`Level Unlocked` <= {self.level}")["Name"].values

        while len(self.orders) < self.n_slots:
            new_order_product = random.choice(available_products)
            self.orders.append({new_order_product : random.randint(2, 6)})

        return self.orders

    def compute_product_cost(product):



    def pick_and_complete_order(self):
        # Let's simulate a player taking random tasks, not aware of inventory
        self.refill_orders()

        order_picked = False

        # Check if ingredients are ready, if not produce them
        
 
        # Get reward from order TO DO

        self.orders.pop(n_order)
        self.refill_orders()

        return f"Order completed! {self.orders[n_order]}"

products = dict(zip(params["products_list"], [0] * len(params["products_list"])))
player = Player(1, inventory=products)

simulation_minutes = 5

# for minute in range(simulation_minutes):
#     player.check_if_order_complete()
#     player.pick_and_action_order()








