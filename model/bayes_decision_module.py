import hedgehog as hh
import pandas as pd
from pprint import pprint


class BayesDecisionModule:
    def __init__(self):
        bn = hh.BayesNet(
            (["player_emotion_face", "player_emotion_voice"], "player_emotion"),
            (["player_offer", "player_emotion"], "robot_decision"),
            (["player_offer", "player_emotion"], "robot_offer")
        )

        bn.P["player_emotion_face"] = pd.Series({
            "positive": 0.3,
            "negative": 0.3,
            "neutral": 0.4
        })

        bn.P["player_emotion_voice"] = bn.P["player_emotion_face"]

        bn.P["player_emotion"] = pd.Series({
            ("positive", "positive", "positive"): 1,
            ("positive", "positive", "negative"): 0,
            ("positive", "positive", "neutral"): 0,

            ("positive", "negative", "positive"): 0.5,
            ("positive", "negative", "negative"): 0.5,
            ("positive", "negative", "neutral"): 0,

            ("positive", "neutral", "positive"): 0.5,
            ("positive", "neutral", "negative"): 0.0,
            ("positive", "neutral", "neutral"): 0.5,
            # -----------------------------------------
            ("negative", "positive", "positive"): 0.5,
            ("negative", "positive", "negative"): 0.5,
            ("negative", "positive", "neutral"): 0,

            ("negative", "negative", "positive"): 0,
            ("negative", "negative", "negative"): 1,
            ("negative", "negative", "neutral"): 0,

            ("negative", "neutral", "positive"): 0,
            ("negative", "neutral", "negative"): 0.5,
            ("negative", "neutral", "neutral"): 0.5,
            # -----------------------------------------
            ("neutral", "positive", "positive"): 0.5,
            ("neutral", "positive", "negative"): 0,
            ("neutral", "positive", "neutral"): 0.5,

            ("neutral", "negative", "positive"): 0,
            ("neutral", "negative", "negative"): 0.5,
            ("neutral", "negative", "neutral"): 0.5,

            ("neutral", "neutral", "positive"): 0,
            ("neutral", "neutral", "negative"): 0,
            ("neutral", "neutral", "neutral"): 1,
        })

        bn.P["player_offer"] = pd.Series({
            "1": 0.03,
            "2": 0.07,
            "3": 0.1,
            "4": 0.2,
            "5": 0.2,
            "6": 0.2,
            "7": 0.1,
            "8": 0.07,
            "9": 0.03,
        })

        bn.P["robot_decision"] = pd.Series({
            ("positive", "1", "yes"): 0,
            ("positive", "1", "no"): 1,

            ("positive", "2", "yes"): 0,
            ("positive", "2", "no"): 1,

            ("positive", "3", "yes"): 0,
            ("positive", "3", "no"): 1,

            ("positive", "4", "yes"): 0.2,
            ("positive", "4", "no"): 0.8,

            ("positive", "5", "yes"): 0.4,
            ("positive", "5", "no"): 0.6,

            ("positive", "6", "yes"): 1,
            ("positive", "6", "no"): 0,

            ("positive", "7", "yes"): 1,
            ("positive", "7", "no"): 0,

            ("positive", "8", "yes"): 1,
            ("positive", "8", "no"): 0,

            ("positive", "9", "yes"): 1,
            ("positive", "9", "no"): 0,
            # -----------------------
            ("negative", "1", "yes"): 0.4,
            ("negative", "1", "no"): 0.6,

            ("negative", "2", "yes"): 0.5,
            ("negative", "2", "no"): 0.5,

            ("negative", "3", "yes"): 0.6,
            ("negative", "3", "no"): 0.4,

            ("negative", "4", "yes"): 0.7,
            ("negative", "4", "no"): 0.3,

            ("negative", "5", "yes"): 0.8,
            ("negative", "5", "no"): 0.2,

            ("negative", "6", "yes"): 0.9,
            ("negative", "6", "no"): 0.1,

            ("negative", "7", "yes"): 0.9,
            ("negative", "7", "no"): 0.1,

            ("negative", "8", "yes"): 1,
            ("negative", "8", "no"): 0,

            ("negative", "9", "yes"): 1,
            ("negative", "9", "no"): 0,
            # -----------------------
            ("neutral", "1", "yes"): 0,
            ("neutral", "1", "no"): 1,

            ("neutral", "2", "yes"): 0,
            ("neutral", "2", "no"): 1,

            ("neutral", "3", "yes"): 0.1,
            ("neutral", "3", "no"): 0.9,

            ("neutral", "4", "yes"): 0.3,
            ("neutral", "4", "no"): 0.7,

            ("neutral", "5", "yes"): 0.5,
            ("neutral", "5", "no"): 0.5,

            ("neutral", "6", "yes"): 0.7,
            ("neutral", "6", "no"): 0.3,

            ("neutral", "7", "yes"): 0.9,
            ("neutral", "7", "no"): 0.1,

            ("neutral", "8", "yes"): 1,
            ("neutral", "8", "no"): 0,

            ("neutral", "9", "yes"): 1,
            ("neutral", "9", "no"): 0,
        })

        bn.P["robot_offer"] = pd.Series({
            ("positive", "1", "1"): 0.95,
            ("positive", "1", "2"): 0.05,
            ("positive", "1", "3"): 0,
            ("positive", "1", "4"): 0,
            ("positive", "1", "5"): 0,
            ("positive", "1", "6"): 0,
            ("positive", "1", "7"): 0,
            ("positive", "1", "8"): 0,
            ("positive", "1", "9"): 0,

            ("positive", "2", "1"): 0.9,
            ("positive", "2", "2"): 0.1,
            ("positive", "2", "3"): 0,
            ("positive", "2", "4"): 0,
            ("positive", "2", "5"): 0,
            ("positive", "2", "6"): 0,
            ("positive", "2", "7"): 0,
            ("positive", "2", "8"): 0,
            ("positive", "2", "9"): 0,

            ("positive", "3", "1"): 0.8,
            ("positive", "3", "2"): 0.15,
            ("positive", "3", "3"): 0.05,
            ("positive", "3", "4"): 0,
            ("positive", "3", "5"): 0,
            ("positive", "3", "6"): 0,
            ("positive", "3", "7"): 0,
            ("positive", "3", "8"): 0,
            ("positive", "3", "9"): 0,

            ("positive", "4", "1"): 0.6,
            ("positive", "4", "2"): 0.2,
            ("positive", "4", "3"): 0.1,
            ("positive", "4", "4"): 0.1,
            ("positive", "4", "5"): 0,
            ("positive", "4", "6"): 0,
            ("positive", "4", "7"): 0,
            ("positive", "4", "8"): 0,
            ("positive", "4", "9"): 0,

            ("positive", "5", "1"): 0.3,
            ("positive", "5", "2"): 0.3,
            ("positive", "5", "3"): 0.2,
            ("positive", "5", "4"): 0.1,
            ("positive", "5", "5"): 0.1,
            ("positive", "5", "6"): 0,
            ("positive", "5", "7"): 0,
            ("positive", "5", "8"): 0,
            ("positive", "5", "9"): 0,

            ("positive", "6", "1"): 0.1,
            ("positive", "6", "2"): 0.2,
            ("positive", "6", "3"): 0.2,
            ("positive", "6", "4"): 0.2,
            ("positive", "6", "5"): 0.2,
            ("positive", "6", "6"): 0.1,
            ("positive", "6", "7"): 0,
            ("positive", "6", "8"): 0,
            ("positive", "6", "9"): 0,

            ("positive", "7", "1"): 0.1,
            ("positive", "7", "2"): 0.1,
            ("positive", "7", "3"): 0.2,
            ("positive", "7", "4"): 0.2,
            ("positive", "7", "5"): 0.2,
            ("positive", "7", "6"): 0.1,
            ("positive", "7", "7"): 0.1,
            ("positive", "7", "8"): 0,
            ("positive", "7", "9"): 0,

            ("positive", "8", "1"): 0.1,
            ("positive", "8", "2"): 0.1,
            ("positive", "8", "3"): 0.1,
            ("positive", "8", "4"): 0.1,
            ("positive", "8", "5"): 0.1,
            ("positive", "8", "6"): 0.2,
            ("positive", "8", "7"): 0.2,
            ("positive", "8", "8"): 0.1,
            ("positive", "8", "9"): 0,

            ("positive", "9", "1"): 0.1,
            ("positive", "9", "2"): 0.1,
            ("positive", "9", "3"): 0.1,
            ("positive", "9", "4"): 0.1,
            ("positive", "9", "5"): 0.1,
            ("positive", "9", "6"): 0.1,
            ("positive", "9", "7"): 0.1,
            ("positive", "9", "8"): 0.2,
            ("positive", "9", "9"): 0.1,
            # -----------------------
            ("negative", "1", "1"): 0,
            ("negative", "1", "2"): 0,
            ("negative", "1", "3"): 0,
            ("negative", "1", "4"): 0,
            ("negative", "1", "5"): 0.05,
            ("negative", "1", "6"): 0.15,
            ("negative", "1", "7"): 0.2,
            ("negative", "1", "8"): 0.3,
            ("negative", "1", "9"): 0.3,

            ("negative", "2", "1"): 0,
            ("negative", "2", "2"): 0,
            ("negative", "2", "3"): 0,
            ("negative", "2", "4"): 0.05,
            ("negative", "2", "5"): 0.15,
            ("negative", "2", "6"): 0.2,
            ("negative", "2", "7"): 0.2,
            ("negative", "2", "8"): 0.2,
            ("negative", "2", "9"): 0.2,

            ("negative", "3", "1"): 0,
            ("negative", "3", "2"): 0,
            ("negative", "3", "3"): 0.05,
            ("negative", "3", "4"): 0.15,
            ("negative", "3", "5"): 0.1,
            ("negative", "3", "6"): 0.2,
            ("negative", "3", "7"): 0.2,
            ("negative", "3", "8"): 0.2,
            ("negative", "3", "9"): 0.2,

            ("negative", "4", "1"): 0,
            ("negative", "4", "2"): 0,
            ("negative", "4", "3"): 0,
            ("negative", "4", "4"): 0.05,
            ("negative", "4", "5"): 0.15,
            ("negative", "4", "6"): 0.2,
            ("negative", "4", "7"): 0.2,
            ("negative", "4", "8"): 0.2,
            ("negative", "4", "9"): 0.2,

            ("negative", "5", "1"): 0,
            ("negative", "5", "2"): 0,
            ("negative", "5", "3"): 0,
            ("negative", "5", "4"): 0,
            ("negative", "5", "5"): 0.05,
            ("negative", "5", "6"): 0.15,
            ("negative", "5", "7"): 0.2,
            ("negative", "5", "8"): 0.3,
            ("negative", "5", "9"): 0.3,

            ("negative", "6", "1"): 0,
            ("negative", "6", "2"): 0,
            ("negative", "6", "3"): 0,
            ("negative", "6", "4"): 0,
            ("negative", "6", "5"): 0,
            ("negative", "6", "6"): 0.2,
            ("negative", "6", "7"): 0.2,
            ("negative", "6", "8"): 0.3,
            ("negative", "6", "9"): 0.3,

            ("negative", "7", "1"): 0,
            ("negative", "7", "2"): 0,
            ("negative", "7", "3"): 0,
            ("negative", "7", "4"): 0,
            ("negative", "7", "5"): 0,
            ("negative", "7", "6"): 0,
            ("negative", "7", "7"): 0.3,
            ("negative", "7", "8"): 0.4,
            ("negative", "7", "9"): 0.4,

            ("negative", "8", "1"): 0,
            ("negative", "8", "2"): 0,
            ("negative", "8", "3"): 0,
            ("negative", "8", "4"): 0,
            ("negative", "8", "5"): 0,
            ("negative", "8", "6"): 0,
            ("negative", "8", "7"): 0.1,
            ("negative", "8", "8"): 0.4,
            ("negative", "8", "9"): 0.5,

            ("negative", "9", "1"): 0,
            ("negative", "9", "2"): 0,
            ("negative", "9", "3"): 0,
            ("negative", "9", "4"): 0,
            ("negative", "9", "5"): 0,
            ("negative", "9", "6"): 0,
            ("negative", "9", "7"): 0,
            ("negative", "9", "8"): 0.5,
            ("negative", "9", "9"): 0.5,
            # -----------------------
            ("neutral", "1", "1"): 0.03,
            ("neutral", "1", "2"): 0.07,
            ("neutral", "1", "3"): 0.1,
            ("neutral", "1", "4"): 0.2,
            ("neutral", "1", "5"): 0.2,
            ("neutral", "1", "6"): 0.2,
            ("neutral", "1", "7"): 0.1,
            ("neutral", "1", "8"): 0.07,
            ("neutral", "1", "9"): 0.03,

            ("neutral", "2", "1"): 0.03,
            ("neutral", "2", "2"): 0.07,
            ("neutral", "2", "3"): 0.1,
            ("neutral", "2", "4"): 0.2,
            ("neutral", "2", "5"): 0.2,
            ("neutral", "2", "6"): 0.2,
            ("neutral", "2", "7"): 0.1,
            ("neutral", "2", "8"): 0.07,
            ("neutral", "2", "9"): 0.03,

            ("neutral", "3", "1"): 0.03,
            ("neutral", "3", "2"): 0.07,
            ("neutral", "3", "3"): 0.1,
            ("neutral", "3", "4"): 0.2,
            ("neutral", "3", "5"): 0.2,
            ("neutral", "3", "6"): 0.2,
            ("neutral", "3", "7"): 0.1,
            ("neutral", "3", "8"): 0.07,
            ("neutral", "3", "9"): 0.03,

            ("neutral", "4", "1"): 0.03,
            ("neutral", "4", "2"): 0.07,
            ("neutral", "4", "3"): 0.1,
            ("neutral", "4", "4"): 0.2,
            ("neutral", "4", "5"): 0.2,
            ("neutral", "4", "6"): 0.2,
            ("neutral", "4", "7"): 0.1,
            ("neutral", "4", "8"): 0.07,
            ("neutral", "4", "9"): 0.03,

            ("neutral", "5", "1"): 0.03,
            ("neutral", "5", "2"): 0.07,
            ("neutral", "5", "3"): 0.1,
            ("neutral", "5", "4"): 0.2,
            ("neutral", "5", "5"): 0.2,
            ("neutral", "5", "6"): 0.2,
            ("neutral", "5", "7"): 0.1,
            ("neutral", "5", "8"): 0.07,
            ("neutral", "5", "9"): 0.03,

            ("neutral", "6", "1"): 0.03,
            ("neutral", "6", "2"): 0.07,
            ("neutral", "6", "3"): 0.1,
            ("neutral", "6", "4"): 0.2,
            ("neutral", "6", "5"): 0.2,
            ("neutral", "6", "6"): 0.2,
            ("neutral", "6", "7"): 0.1,
            ("neutral", "6", "8"): 0.07,
            ("neutral", "6", "9"): 0.03,

            ("neutral", "7", "1"): 0.03,
            ("neutral", "7", "2"): 0.07,
            ("neutral", "7", "3"): 0.1,
            ("neutral", "7", "4"): 0.2,
            ("neutral", "7", "5"): 0.2,
            ("neutral", "7", "6"): 0.2,
            ("neutral", "7", "7"): 0.1,
            ("neutral", "7", "8"): 0.07,
            ("neutral", "7", "9"): 0.03,

            ("neutral", "8", "1"): 0.03,
            ("neutral", "8", "2"): 0.07,
            ("neutral", "8", "3"): 0.1,
            ("neutral", "8", "4"): 0.2,
            ("neutral", "8", "5"): 0.2,
            ("neutral", "8", "6"): 0.2,
            ("neutral", "8", "7"): 0.1,
            ("neutral", "8", "8"): 0.07,
            ("neutral", "8", "9"): 0.03,

            ("neutral", "9", "1"): 0.03,
            ("neutral", "9", "2"): 0.07,
            ("neutral", "9", "3"): 0.1,
            ("neutral", "9", "4"): 0.2,
            ("neutral", "9", "5"): 0.2,
            ("neutral", "9", "6"): 0.2,
            ("neutral", "9", "7"): 0.1,
            ("neutral", "9", "8"): 0.07,
            ("neutral", "9", "9"): 0.3,
        })

        bn.prepare()
        self.bn = bn
        self.emotionSimplifier = {'happy': 'positive',
                                  'surprised': 'neutral',
                                  'calm': 'neutral',
                                  'disgusted': 'negative',
                                  'sad': 'negative',
                                  'fearful': 'negative',
                                  'angry': 'negative'}

    def start_game(self):
        pass

    def humanOffer(self, offer, emoFace, emoVoice):
        emoFaceSimple = self.emotionSimplifier[emoFace]
        emoVoiceSimple = self.emotionSimplifier[emoVoice]

        sample = {
            'player_emotion_face': emoFaceSimple,
            'player_emotion_voice': emoVoiceSimple,
            'player_offer': offer,
            'robot_offer': None,
            'robot_decision': None
        }
        response = self.bn.impute(sample)
        info = {
            "offer": int(response["robot_offer"]),
            "decision": "accepted" if response["robot_decision"] == "yes" else "declined"}

        return info

    def humanDecides(self, agreed):
        pass


if __name__ == "__main__":
    bdm = BayesDecisionModule()
    dot = bdm.bn.graphviz()
    path = dot.render('ultimatum', directory='figures', format='svg', cleanup=True)

    sample = {
        'player_emotion_face': 'neutral',
        'player_emotion_voice': 'neutral',
        'player_offer': '5',
        'robot_offer': None,
        'robot_decision': None
    }
    response = bdm.bn.impute(sample)
    pprint(response)

    # pprint(bdm.bn.sample())
