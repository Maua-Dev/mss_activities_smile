# Façam validação dos atributos

class Speaker:
    name: str
    bio: str
    company: str

    def __init__(self, name, bio, company):
        self.name = name
        self.bio = bio
        self.company = company