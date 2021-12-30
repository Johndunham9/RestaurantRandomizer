import random
from Singleton import Singleton


@Singleton
class RestaurantStore:
    """A Singleton class that stores user added restaurants into a list"""

    def __init__(self):
        self.list = []

    def add_restaurant(self, restaurant):
        self.list.append(restaurant)


def randomizer(the_list):
    """Gives a suggestion for a random restaurant"""
    suggestion = random.choice(the_list)
    return suggestion


# test main
def main():
    s = RestaurantStore()
    s.add_restaurant("McDonalds")
    s.add_restaurant("Pizza Hut")
    s.add_restaurant("Cains")
    s.add_restaurant("Subway")


if __name__ == "__main__":
    main()

