class InvalidFieldException(Exception):

    def __init__(self, invalid_field: str):
        self.invalid_field = invalid_field
        super().__init__(f"invalid input for the field {invalid_field}")
