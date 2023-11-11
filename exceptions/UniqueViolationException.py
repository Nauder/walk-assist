class UniqueViolationException(Exception):

    def __init__(self, invalid_field: str, value: str):
        self.invalid_field = invalid_field
        self.value = value
        super().__init__(f"value {value} already exists for field {invalid_field}")
