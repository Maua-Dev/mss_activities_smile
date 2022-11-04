class MISSING_FIELD(Exception):
    def __init__(self, field: str):
        self.field: str = field
<<<<<<< HEAD
        super().__init__(f'{field} is required')
=======
        super().__init__(f'{field} is required')
>>>>>>> d3464796e57b55bc7ae5cb668b78098a4fc2f4ec
