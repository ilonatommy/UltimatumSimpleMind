import hedgehog as hh

class BayesDecisionModule:
    def __init__(self):
        self.model = hh.BayesNet(
            (["player_emotion_face", "player_emotion_voice"], "player_emotion"),
            (["player_offer", "player_emotion"], "robot_decision")
        )
    
    def start_game(self):
        pass

    def humanOffer(self, offer, emoFace, emoVoice):
        pass

    def humanDecides(self, agreed):
        pass

if __name__ == "__main__":
    bdm = BayesDecisionModule()
    dot = bdm.model.graphviz()
    path = dot.render('ultimatum', directory='figures', format='svg', cleanup=True)