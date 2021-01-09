import os
from pyswip import Prolog


class PrologDecisionModule:
    def __init__(self):
        self.prolog = Prolog()
        prolog_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model/prolog'))
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
