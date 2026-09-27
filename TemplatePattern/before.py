class CsvParser:
    def open(self):
        print("Opening the file")
    def close(self):
        print("Closing of the file")
    def parser(self):
        self.open()
        print("parsing of the csv file")
        self.close()
        
class JsonParser:
    def open(self):
        print("Opening the file")
    def close(self):
        print("Closing of the file")
    def parser(self):
        self.open()
        print("parsing of the json file")
        self.close()       

csv=CsvParser()
json=JsonParser()
json.parser()
csv.parser()