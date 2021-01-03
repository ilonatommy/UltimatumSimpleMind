import hedgehog as hh
import pandas as pd
from pprint import pprint

class BayesDecisionModule:
    def __init__(self):
        bn = hh.BayesNet(
            (["player_emotion_face", "player_emotion_voice"], "player_emotion") #,
            #(["player_offer", "player_emotion"], "robot_decision")
        )

        bn.P["player_emotion_face"] = pd.Series({
            "sad": 0.5,
            "happy": 0.5
        })

        bn.P["player_emotion_voice"] = bn.P["player_emotion_face"]
    
        bn.P["player_emotion"] = pd.Series({
            ("sad", "sad", "sad"): 1.0,

            ("happy", "happy", "happy"): 1.0,

            ("happy", "sad", "happy"): 0.66,
            ("happy", "sad", "sad"): 0.44,

            ("sad", "happy", "sad"): 0.66,
            ("sad", "happy", "happy"): 0.44,
        })

        bn.prepare()
        self.bn = bn

    def start_game(self):
        pass

    def humanOffer(self, offer, emoFace, emoVoice):
        pass

    def humanDecides(self, agreed):
        pass

if __name__ == "__main__":
    bdm = BayesDecisionModule()
    dot = bdm.bn.graphviz()
    path = dot.render('ultimatum', directory='figures', format='svg', cleanup=True)

    sample = {
        "player_emotion_face": "happy",
        "player_emotion_voice": "sad",
        "player_emotion": None
    }

    pprint(bdm.bn.impute(sample))
    pprint(bdm.bn.sample())