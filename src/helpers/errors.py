class MISSING_FIELD(Exception):
    def __init__(self, field: str):
        self.field: str = field
        super().__init__(f'{field} is required')

