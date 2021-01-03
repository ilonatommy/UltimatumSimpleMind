import hedgehog as hh

class BayesDecisionModule:
    def __init__(self):
        pass
    
    def start_game(self):
        pass

    def humanOffer(self, offer, emoFace, emoVoice):
        pass

    def humanDecides(self, agreed):
        pass


if __name__ == "__main__":
    bdm = BayesDecisionModule()
    bn = hh.examples.asia()
    dot = bn.graphviz()
    path = dot.render('asia', directory='figures', format='svg', cleanup=True)