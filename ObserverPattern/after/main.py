from tv import TvStation
from mobile import Mobile
from weather_station import WeatherStation

ws=WeatherStation()
tv=TvStation()
mobile=Mobile()
ws.add_observer(tv)
ws.add_observer(mobile)
ws.update(50)


