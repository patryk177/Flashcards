import random
from io import StringIO
from collections import defaultdict

class Flashcards:
    def __init__(self):
        self.cards_dict = {}
        self.mistakes = defaultdict(int)
        self.sio = StringIO()
        self.sio.read()
        self.menu()

    def add_card(self):
        n_cards = 1
        for i in range(n_cards):
            print("The card:")
            self.sio.write("The card:")
            term = input()
            self.sio.write(term + "\n")
            while term in self.cards_dict.keys():
                term = input(f'The card "{term}" already exists. Try again:\n')
                self.sio.write(f'The card "{term}" already exists. Try again:\n')
                self.sio.write(term + "\n")
            print("The definition for the card:", self.sio.read())
            definition = input()
            self.sio.write(definition + "\n")
            while definition in self.cards_dict.values():
                definition = input(f'The definition "{definition}" already exists. Try again:\n')
                self.sio.write(f'The definition "{definition}" already exists. Try again:\n')
                self.sio.write(definition + "\n")
            self.cards_dict[term] = definition
        print(f'The pair ("{term}":"{definition}") has been added.')
        self.sio.write(f'The pair ("{term}":"{definition}") has been added.')

    def ask(self):
        print("How many times to ask?")
        self.sio.write("How many times to ask?")
        n_ask = int(input())
        self.sio.write(str(n_ask) + "\n")
        try:
            for i in range(n_ask):
                term = random.choice(list(self.cards_dict))
                answer = input(f'Print the definition of "{term}":\n')
                self.sio.write(f'Print the definition of "{term}":\n')
                self.sio.write(answer + "\n")
                if answer == self.cards_dict[term]:
                    print("Correct!")
                    self.sio.write("Correct!")
                elif answer in self.cards_dict.values():
                    proper_answer = [key for key, value in self.cards_dict.items() if value == answer]
                    print(f'Wrong. The right answer is "{self.cards_dict[term]}", but your definition is correct for "{proper_answer[0]}".')
                    self.sio.write(f'Wrong. The right answer is "{self.cards_dict[term]}", but your definition is correct for "{proper_answer[0]}".')
                    self.mistakes[term] += 1
                else:
                    print(f'Wrong. The right answer is "{self.cards_dict[term]}".')
                    self.sio.write(f'Wrong. The right answer is "{self.cards_dict[term]}".')
                    self.mistakes[term] += 1
        except ValueError:
            print("There are no cards with errors.")
            self.sio.write("There are no cards with errors.")
        except IndexError:
            print("There are no cards with errors.")
            self.sio.write("There are no cards with errors.")

    def remove_card(self):
        print("Which card?")
        self.sio.write("Which card?")
        del_card = input()
        self.sio.write(del_card + "\n")
        if del_card in self.cards_dict.keys():
            del self.cards_dict[del_card]
            print("The card has been removed.")
            self.sio.write("The card has been removed.")
        else:
            print(f'Can\'t remove "{del_card}": there is no such card.')
            self.sio.write(f'Can\'t remove "{del_card}": there is no such card.')

    def import_cards(self):
        n = 0
        try:
            print("File name:")
            self.sio.write("File name:")
            file_name = input()
            self.sio.write(file_name + "\n")
            import_file = open(f"{file_name}", "r")
            for line in import_file:
                (self.term, self.definition) = line.split()
                self.cards_dict[self.term] = self.definition
                n += 1
            print(f"{n} cards have been loaded")
            self.sio.write(f"{n} cards have been loaded")
            import_file.close()
        except FileNotFoundError:
            print("File not found.")
            self.sio.write("File not found.")

    def export_cards(self):
        n = 0
        print("File name:")
        self.sio.write("File name:")
        export_name = input()
        self.sio.write(export_name + "\n")
        with open(f"{export_name}", 'w') as export_file:
            for key, value in self.cards_dict.items():
                export_file.write('%s %s\n' % (key, value))
                n += 1
        export_file.close()
        print(f"{n} cards have been saved.")
        self.sio.write(f"{n} cards have been saved.")

    def log(self):
        print("The file name:")
        self.sio.write("The file name:")
        file_txt = input()
        self.sio.write(file_txt + "\n")
        self.sio.seek(0)
        with open(file_txt, 'w') as f:
            for input_line in self.sio.readlines():
                f.write(input_line)
        print("The log has been saved.")
        self.sio.write("The log has been saved.")

    def hardest_card(self):
        try:
            max_mistakes = max(self.mistakes.values())
            equal = [key for key, value in self.mistakes.items() if value == max_mistakes]
            if len(equal) > 1:
                print(f'The hardest cards are "{equal[0]}", "{equal[1]}". You have "{max_mistakes}" errors answering them.')
                self.sio.write(f'The hardest cards are "{equal[0]}", "{equal[1]}". You have "{max_mistakes}" errors answering them.')
            else:
                print(f'The hardest card is "{equal[0]}". You have "{max_mistakes}" errors answering it.')
                self.sio.write(f'The hardest card is "{equal[0]}". You have "{max_mistakes}" errors answering it.')
        except ValueError:
            print("There are no cards with errors.")
            self.sio.write("There are no cards with errors.")
        except IndexError:
            print("There are no cards with errors.")
            self.sio.write("There are no cards with errors.")

    def reset_stats(self):
        self.mistakes = defaultdict(int)
        print("Card statistics have been reset.")
        self.sio.write("Card statistics have been reset.")

    def menu(self):
        while True:
            print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):", end='\n')
            self.sio.write("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            menu_choice = input()
            self.sio.write(menu_choice + "\n")
            if menu_choice == "add":
                self.add_card()
            elif menu_choice == "remove":
                self.remove_card()
            elif menu_choice == "import":
                self.import_cards()
            elif menu_choice == "export":
                self.export_cards()
            elif menu_choice == "ask":
                self.ask()
            elif menu_choice == "exit":
                self.sio.write('exit' + "\n")
                print("Bye bye")
                quit()
            elif menu_choice == "log":
                self.log()
            elif menu_choice == "hardest card":
                self.hardest_card()
            elif menu_choice == "reset stats":
                self.reset_stats()


if __name__ == '__main__':
    Flashcards()