#!/usr/bin/env python

from pyswip import Prolog
import os

PROLOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model'))


class DecisionModule:
    def __init__(self, prolog_path=PROLOG_PATH):
        self.prolog = Prolog()
        self.prolog.consult(os.path.join(prolog_path, 'load.pl'))

    def start_game(self):
        init_pos = list(self.prolog.query("init_state"))

    def humanOffer(self, offer, emoFace, emoVoice):
        response = list(
            self.prolog.query("humanOffers({}, {}, {}, RobotOffer, RobotDecision)"
                                          .format(offer, emoFace, emoVoice)))[0]
        info = {
            "offer": response["RobotOffer"], 
            "decision": "accepted" if response["RobotDecision"] > 0 else "declined"}

        return info

    def humanDecides(self, agreed):
        decision = "yes" if agreed else "no"
        response = list(
            self.prolog.query("humanDecides({})"
                .format(decision)))[0]


if __name__ == "__main__":
    # dorobic parametry wyjsciowe do prologa Y_out, X_out
    offer = 5
    emoFace = "disgusted"
    emoVoice = "sad"

    dm = DecisionModule()
    dm.start_game()
    robotOffer, robotDecision = dm.humanOffer(offer, emoFace, emoVoice)
    print(robotOffer, robotDecision)
    agreed = True
    dm.humanDecides(agreed)
