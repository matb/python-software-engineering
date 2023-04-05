import time 
import typing 
import dataclasses
import sqlite3

from loguru import logger
import pandas as pd 


class CSVWriter:
    
    def __init__(self, config):
        self.file_path = config["sink"]
        
    def write_to_file(self, data):
        """Mocks writing data to a file"""
        self.log_start()
        time.sleep(1)
        self.log_end()
        
    def log_start(self):
        logger.info("Start writing to CSV file")
    
    def log_end(self):
        logger.info("End writing to CSV file")
    
    
class  CSVReader():
    
    def __init__(self, config):
        self.file_path = config["source"]
        
    def read_csv(self):
        """Mocks reading a csv file """
        return pd.DataFrame(data=[("Max", 23, 97.3, 176.5), ("Alice", 22, 55.8, 169.3), ("Tom", 22, 84.1, 172.2),
                                  ("Matthias", 43, 87.3, 172.5), ("Anna", 32, 60.8, 177.3), ("Britta", 22, 64.1, 167.2)],
                            columns=["name", "age", "weight", "height"])
class DBReader:
    
    def __init__(self, config):
        self.table = config["source"]
    
    def read_db(self):
        return_obj = {"table": self.table}
        data = self._read_table()
        return_obj["data"] = data
        return return_obj
    
    def _read_table(self):
        """Mocks reading a database table """
        return pd.DataFrame(data=[("Max", 23, 97.3, 176.5), ("Alice", 22, 55.8, 169.3), ("Tom", 22, 84.1, 172.2),
                                  ("Matthias", 43, 87.3, 172.5), ("Anna", 32, 60.8, 177.3), ("Britta", 22, 64.1, 167.2)],
                            columns=["Name", "Age", "Weight", "Height"])
class DBWriter:
    
    def __init__(self, config):
        self.table = config["sink"]
        
    def write_to_db(self, data):
        self.log_start()
        self._write_table(data)
        self.log_end()
    
    def _write_table(self, data):
        """Mocks writing a database table """
        time.sleep(1)
    
    def log_start(self):
        logger.info("Start writing to DB")
        
    def log_end(self):
        logger.info("End writing to DB")
    

class StudentsDataETLPipelines():
    
    def __init__(self, config):
        self.config = config
        self.source = config["source"]
        self.source_type = config["source_type"]
        self.sink = config["sink"]
        self.sink_type = config["sink_type"]
        self.transformations = config["transformations"]
        
    def main(self):
    
        if self.source_type == "CSV":
            data = CSVReader(self.config).read_csv()
        elif self.source_type == "DB":
            data = DBReader(self.config).read_db()
        else:
            raise ValueError(f"Unknown source type: {self.source_type}")
        
        for transformation in self.transformations:
            if transformation == "filter":
                if self.source_type == "CSV":
                    data = self.filter_csv(data)
                elif self.source_type == "DB":
                    data = self.filter_db(data)
            elif transformation == "map":
                data = self.map(data)
                
        self.save_data(data) 
        
        
    def save_data(self, data):
        if self.sink_type == "CSV":
            CSVWriter(self.config).write_to_file(data)
        elif self.sink_type == "DB":
            DBWriter(self.config).write_to_db(data)
        else:
            raise ValueError(f"Unknown sink type: {self.sink}")
    
    def filter_csv(self, data):
        """Pseudo filter function"""
        return data.query("height > 170")

    def filter_db(self, data):
        """Pseudo filter function"""
        return data["data"].query("Height > 170")
    
    def map(self, data):
        data["isTall"] = True 
        return data


class DevStudentETL(StudentsDataETLPipelines):
    
    def __init__(self):
        config = {"source":  "psuedo_output.csv",
                  "source_type": "DB",
                  "sink": "output.csv",
                  "sink_type": "DB",
                  "transformations": ["filter"] }
        super(DevStudentETL, self).__init__(config)
    
if __name__ == "__main__":
    pipe = DevStudentETL()
    pipe.main()
    