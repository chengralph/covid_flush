import os, sys, json, random

class deck:
    def __init__(self, deck_path ="decks.json"):
        if not isinstance(deck_path, str):
            raise TypeError("Could not find deck")
        if not os.path.isfile(deck_path):
            for json_file in os.listdir(os.getcwd()):
                if filename.endswith(".json"):
                    self.json_file = os.path.join(os.getcwd(), filename)
        else:
            self.json_file = os.path.join(os.getcwd(), deck_path)

    def load_deck(self):
        with open(self.json_file, "a") as f:
            data = json.load(open(self.json_file, "r+"))
            self.questions = data["deck_set_1"]["Questions"]
            self.current_index = 0

    def shuffle(self):
        random.shuffle(self.questions)
        self.current_index = 0

    def draw(self):
        if self.current_index >= len(self.questions):
            return 0
        card = self.questions[self.current_index]
        self.current_index += 1
        return card, self.current_index, len(self.questions)

random_deck = deck()
random_deck.load_deck()
random_deck.shuffle()
card = random_deck.draw()

while card:
    return_key = input('Type in return: ')
    if return_key == "shuffle":
        random_deck.shuffle()
    print(card)
    card = random_deck.draw()
