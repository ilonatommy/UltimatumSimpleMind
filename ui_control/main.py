from pyswip import Prolog
import os

PROLOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'prolog'))

class DecisionModule:
    def __init__(self, prolog_path=PROLOG_PATH):
        self.prolog = Prolog()
        self.prolog.consult(os.path.join(prolog_path, 'load.pl'))

    def start_game(self):
        init_pos = list(self.prolog.query("init_state(Y,X)"))[0]
        print(init_pos["Y"], init_pos["X"])
        return init_pos["Y"], init_pos["X"]

    def humanOffer(self, y, x, offer, emoFace, emoVoice):
        response = list(self.prolog.query("humanOffers({}, {}, {}, {}, {}, RobotOffer, RobotDecision, Y_out, X_out)"
                                     .format(y, x, offer, emoFace, emoVoice)))[0]
        return response["Y_out"], response["X_out"], response["RobotOffer"], response["RobotDecision"]


    def humanDecides(self, y, x, decision):
        response = list(self.prolog.query("humanDecides({}, {}, {}, Y_out, X_out)".format(y, x, decision)))[0]
        return response["Y_out"], response["X_out"]




if __name__ == "__main__":
    offer = 5
    emoFace = "disgusted"
    emoVoice = "sad"

    dm = DecisionModule()
    y, x = dm.start_game()
    y, x, robotOffer, robotDecision = dm.humanOffer(y, x, offer, emoFace, emoVoice)
    print(robotOffer, robotDecision)
    decision = "yes"
    y, x = dm.humanDecides(y, x, decision)
    print(y, x)
