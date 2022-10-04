
# Façam validação dos atributos

class Activity:
    title: str
    type: str
    code: str
    description: str
    initialDate: str
    finalDate: str

    def __init__(self, title, type, code, description, initialDate, finalDate):
        self.title = title
        self.type = type
        self.code = code
        self.description = description
        self.initialDate = initialDate
        self.finalDate = finalDate





