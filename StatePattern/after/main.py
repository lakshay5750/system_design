from transport_mode import TransportMode
from transport_service import TransportService
from bike_mode import BikeMode
from train_mode import TrainMode


bike=BikeMode()
train=TrainMode()
service=TransportService(bike)
service.direction()
service.eta()