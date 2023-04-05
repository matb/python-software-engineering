class ETLBase:
  def __init__(self, auth):
        auth.authenticate()
      
      
class SSOETL(ETLBase):
  def __init__(self):
    super().__init__(SSO())
    
    
if __name__ == "__main__":
  etl = SSOETL()