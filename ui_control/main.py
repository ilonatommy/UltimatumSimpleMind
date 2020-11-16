from pyswip import Prolog
import os

PROLOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'prolog'))


def start_game(prolog):
    init_pos = list(prolog.query("init_state(Y,X)"))[0]
    print(init_pos["Y"], init_pos["X"])
    return init_pos["Y"], init_pos["X"]


def humanOffer(prolog, y, x, offer, emoFace, emoVoice):
    response = list(prolog.query("humanOffers({}, {}, {}, {}, {}, RobotOffer, RobotDecision, Y_out, X_out)"
                                 .format(y, x, offer, emoFace, emoVoice)))[0]
    return response["Y_out"], response["X_out"], response["RobotOffer"], response["RobotDecision"]


def humanDecides(prolog, y, x, decision):
    response = list(prolog.query("humanDecides({}, {}, {}, Y_out, X_out)".format(y, x, decision)))[0]
    return response["Y_out"], response["X_out"]


prolog = Prolog()
prolog.consult(os.path.join(PROLOG_PATH, 'load.pl'))
y, x = start_game(prolog)
offer = 5
emoFace = "disgusted"
emoVoice = "sad"
y, x, robotOffer, robotDecision = humanOffer(prolog, y, x, offer, emoFace, emoVoice)
print(robotOffer, robotDecision)
decision = "yes"
y, x = humanDecides(prolog, y, x, decision)
print(y, x)
