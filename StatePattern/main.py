from before import TransportMode,TransportService

service=TransportService(TransportMode.WALKING)
service.eta()
service.directions()

service.set_transport(TransportMode.TRAIN)
service.eta()
service.directions()