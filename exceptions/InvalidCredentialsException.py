class InvalidCredentialsException(Exception):

    def __init__(self):
        super().__init__("senha e/ou registro inválidos")
