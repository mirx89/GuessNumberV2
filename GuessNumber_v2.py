from Controller import Controller
from Model import Model
from View import View


class GuessNumber_v2:

    def __init__(self):
        self.model = Model() # Loome mudeli
        self.view = View(self.model) # Loome vaate
        self.controller = Controller(self.model, self.view) # loome kontrolleri
        self.running = True # while loop jaoks
    def start(self):
        while self.running:
            result = self.view.menu()
            if result == 3:
                self.running = False
            elif result == 1: #Lets play
                self.controller.lets_play()
                if self.model.game_over:
                    name = self.view.ask_name()
                    self.model.write_score_to_file(name, self.model.steps, self.model.date)
                    self.model.steps = 0 # sammud nullid
                    self.model.game_over = False # Mäng algab uuesti
                    self.model.pc_nr = self.model.new_number() # arvuti uus number
            elif result == 2:
                self.view.show_scoreboard()

if __name__ == '__main__':
    # GuessNumber_v2().start() # ühe reaga
    game = GuessNumber_v2() # kahe reaga + rida 30
    game.start()
