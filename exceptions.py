class InvalidCredentialsException(Exception):

    def __init__(self):
        super().__init__("senha e/ou registro inválidos")


class InvalidFieldException(Exception):

    def __init__(self, invalid_field: str):
        self.invalid_field = invalid_field
        super().__init__(f"invalid input for the field {invalid_field}")


class UniqueViolationException(Exception):

    def __init__(self, invalid_field: str, value: str):
        self.invalid_field = invalid_field
        self.value = value
        super().__init__(f"value {value} already exists for field {invalid_field}")
