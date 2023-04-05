

@dataclass.dataclass
class Config:
    user: str
    password: str
    host: str
    email_content: str
    receiver: str
    
class MessageBody:
    def __init__(self, config):
        self.body = config.email_content
    
    def format(self):
        return f"Some HTML {self.body} More HTML "
    
class Email:
    def __init__(self, config: Config):
        self.config = config
    
    def create_mail(self):
        return MessageBody(config).create()
    
    def send(self):
        message = self.create_mail()
        EmailServer(config, message)