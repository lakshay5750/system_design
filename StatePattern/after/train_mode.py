from transport_mode import TransportMode

class TrainMode(TransportMode):
    def eta(self):
        print("it require to reach approx 10 min")
    def direction(self):
        print("just sit in the train it will reach at your destination")