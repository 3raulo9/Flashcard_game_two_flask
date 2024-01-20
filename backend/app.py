from flask import Flask, render_template, request, jsonify
import os
import json
from collections import defaultdict

app = Flask(__name__)

def optionsForUser():
    return """
    """

def create_flashcard():
    deck_name = request.form.get("deck_name")
    front_page = request.form.get("front_page")
    back_page = request.form.get("back_page")

    flashcard = {
        "name": deck_name,
        "front": front_page,
        "back": back_page
    }

    return flashcard

def delete_deck(deck_name, data):
    for idx, item in enumerate(data["cards"]):
        if item["name"] == deck_name:
            del data["cards"][idx]
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        choice = request.form.get("choice")

        try:
            with open('sample.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"cards": []}

        if choice == "1":
            decks = defaultdict(list)

            for card in data["cards"]:
                decks[card["name"]].append(card)

            if decks:
                result_message = "<br>".join([
                    f"Deck: {name}<br>Front: {card['front']}, Back: {card['back']}<br>---------------"
                    for name, cards in decks.items()
                ])
            else:
                result_message = "No decks available."

        elif choice == "2" or choice == "3":
            new_flashcard = create_flashcard()
            data["cards"].append(new_flashcard)

            with open('sample.json', 'w') as f:
                json.dump(data, f)

            if choice == "2":
                result_message = "Flashcard added successfully!"
            else:
                result_message = "Flashcard created successfully!"

        elif choice == "4":
            deck_name = request.form.get("deck_name")
            if delete_deck(deck_name, data):
                with open('sample.json', 'w') as f:
                    json.dump(data, f)
                result_message = f"Deck '{deck_name}' deleted successfully!"
            else:
                result_message = f"Deck '{deck_name}' not found."

        return render_template('index.html', message=optionsForUser() + result_message)

    return render_template('index.html', message=optionsForUser())

if __name__ == "__main__":
    app.run(debug=True)
