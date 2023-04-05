import time 
import typing 
import dataclasses


@dataclasses.dataclass(frozen=True, eq=True)
class SchedulerConfig:
    start_time: time.Time
    
@dataclasses.dataclass(frozen=True, eq=True)
class DevConfig(SchedulerConfig):
    source:  str
    source_type: str
    sink: Any
    

class ClientDataETLPipelines():
    
    def __init__(self, config):
        self.start_time = config.start_time
        self.source = config.source
        self.source_type = config.source_type
        self.sink = config.sink
        self.transformations = config.transformations
        
    def main(self):
        self.wait_for_timing()
        data = self.load_data()
        data = self.process_data(data)
        self.save_data(data)
    
    def wait_for_timing(self):
        while time.time() < self.start_time:
            time.sleep(0.1)
    
    def load_data(self):
        if self.source_type == "CSV":
            return CSVReader(self.config).read()
        elif self.source_type == "DB":
            return DBReader(self.config).read()
        else:
            raise ValueError(f"Unknown source type: {self.source_type}")
    
    def process_data(self, data):
        for transformation in self.transformations:
            if transformation.type == "filter":
                data = self.filter(data)
            elif transformation.type == "map":
                data = self.map(data)
                
        return data
    
    def save_data(self, data):
        if self.sink == "CSV":
            CSVWriter(self.config).write(data)
        elif self.sink == "DB":
            DBWriter(self.config).write(data)
        else:
            raise ValueError(f"Unknown sink type: {self.sink}")
    
    def filter(self, data):
        """Pseudo filter function"""
        return data
    
    def map(self, data):
        """Pseudo map function"""
        return data