class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds."):
        super().__init__(message)

class AccountNotFoundError(Exception):
    def __init__(self, message="Account not found."):
        super().__init__(message)
