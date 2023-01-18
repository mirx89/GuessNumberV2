def sort(score):
    pass


class View:

    def __init__(self, model):
        self.model = model
        # print("View", model.pc_nr)  # test

    # Menu
    def menu(self):
        print()
        print("1. Lets play game")
        print("2. Näita edetabelit")
        print("3. Exit")
        print()
        return int(input("Input choice 1, 2, 3: "))

    def ask(self):
        mn = str(self.model.minimum)  # minimum, lühendame
        mx = str(self.model.maximum)  # max
        user_input = int(input("Choose number "+mn+" - "+mx+": "))
        self.model.steps += 1  # steps +1
        if user_input > self.model.pc_nr and user_input != 10000:
            print("Smaller")
        elif user_input < self.model.pc_nr and user_input != 10000:
            print("Bigger")
        elif user_input == self.model.pc_nr and user_input != 10000:
            print("You guessed number in ", str(self.model.steps) + " steps.")
            self.model.game_over = True
        elif user_input == 10000:
            self.model.cheater = True
            print("You found back door. The correct number is", self.model.pc_nr)

    def ask_name(self):
        return input("What is your name? ")

    def show_scoreboard(self):
        scores = self.model.read_score_file()
        print("Nimi".ljust(1), "Tulemus".rjust(20), "Kuupäev".rjust(14), "Kellaaeg".rjust(12))
        scores = sorted(scores, key=lambda x: (x[1], x[2]))
        if scores is not None:
            for score in scores:
                if len(score[0]) > 14:
                    print((score[0])[0: 15] + "...".ljust(1), score[1].rjust(3), score[2].rjust(20), score[3])  # Name and steps
                else:
                    print((score[0])[0: 15].ljust(19), score[1].rjust(1), score[2].rjust(20), score[3])
        else:
            print("--------\nFirst play game\n--------")
