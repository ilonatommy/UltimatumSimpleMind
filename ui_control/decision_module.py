#!/usr/bin/env python

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
        self.y = init_pos["Y"]
        self.x = init_pos["X"]

    def humanOffer(self, offer, emoFace, emoVoice):
        response = list(self.prolog.query("humanOffers({}, {}, {}, {}, {}, RobotOffer, RobotDecision, Y_out, X_out)"
                                     .format(self.y, self.x, offer, emoFace, emoVoice)))[0]
        self.y = response["Y_out"]
        self.x = response["X_out"]
        return response["RobotOffer"], response["RobotDecision"]


    def humanDecides(self, decision):
        response = list(self.prolog.query("humanDecides({}, {}, {}, Y_out, X_out)".format(self.y, self.x, decision)))[0]
        self.y = response["Y_out"]
        self.x = response["X_out"]

if __name__ == "__main__":
    offer = 5
    emoFace = "disgusted"
    emoVoice = "sad"

    dm = DecisionModule()
    dm.start_game()
    robotOffer, robotDecision = dm.humanOffer(offer, emoFace, emoVoice)
    print(robotOffer, robotDecision)
    decision = "yes"
    dm.humanDecides(decision)
