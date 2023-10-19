class Hello:
    def __init__(self) -> None:
        self.message = 'Yahallo'
    
    def set_message(self, message):
        self.message = message
        
    def print_message(self):
        print(self.message)
            
    def concatenate(self, string):
        self.message += string
        
    def __str__(self) -> str:
        return self.message