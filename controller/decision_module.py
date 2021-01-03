#!/usr/bin/env python

import os
from model.BayesDecisionModule import BayesDecisionModule
from model.prolog_decision_module import PrologDecisionModule

class DecisionModule:
    def __init__(self):
        self.dm = PrologDecisionModule()

    def start_game(self):
        self.dm.start_game()

    def humanOffer(self, offer, emoFace, emoVoice):
        return self.dm.humanOffer(offer, emoFace, emoVoice)

    def humanDecides(self, agreed):
        self.dm.humanDecides(agreed)


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
