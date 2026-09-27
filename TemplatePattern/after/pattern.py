from abc import ABC,abstractmethod

class DataParser(ABC):
    def _parse(self):
        self._open()
        self._dataParser()
        self._close()
    
    
    def _open(self):
        print("Opening the file")
    def _close(self):
        print("Closing the file")
        
    def _dataParser(self):
        pass

class CsvParser(DataParser):
    def _dataParser(self):
        print("Parsing the  csv file")
class JsonParser(DataParser):
    def _dataParser(self):
        print("Parsing the  json file")


csv=CsvParser()
json=JsonParser()
json._parse()
csv._parse()