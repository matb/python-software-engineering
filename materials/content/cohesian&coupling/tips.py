import types

class QueryableProtocol(types.Protocol):
    
    def query(self, sql: str) -> pd.DataFrame:
        ...
        

class SQLiteData:
    
    def __init__(self, db_path: str):
        self.path = db_path
        
    def query(self, sql: str) -> pd.DataFrame:
        query = "Select * from patient data where" + sql
        return pd.read_sql_query(query, self.path)
    
    
class ETLpipeline():
    
    def __init__(self, data: QueryableProtocol):
        self.data = data
        
    def main(self) -> pd.DataFrame :
        return self.data.query('height > 100')
    
if __name__ == '__main__':
    data = SQLiteData('data.db') # SQLite db containing paitant data with their age and height
    # data = pd.DataFrame(data=[("Max", 23, 97.3, 176.5), ("Alice", 22, 55.8, 169.3), ("Tom", 22, 84.1, 172.2),
    #                          ("Matthias", 43, 87.3, 172.5), ("Anna", 32, 60.8, 177.3), ("Britta", 22, 64.1, 167.2)],
    #                        columns=["name", "age", "weight", "height"])
    pipeline = ETLpipeline(data)
    pipeline.main()