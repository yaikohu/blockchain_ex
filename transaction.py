class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
    
    if self.sender == "genesis":
        identity = "genesis"
    else:
        identity = self.sender.identity
        