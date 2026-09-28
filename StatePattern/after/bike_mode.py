from transport_mode import TransportMode

class BikeMode(TransportMode):
    def eta(self):
        print("it require to reach approx 20 min")
    def direction(self):
        print("turn left then right")