class Speaker:
    name: str
    bio: str
    company: str

    def __init__(self, name, bio, company):
        self.name = name
        self.bio = bio
        self.company = company


        @staticmethod
        def validate_name(name: str) -> bool:
        
            if name == None:
                return False

            if type(name) != str:
                return False

            return True

        @staticmethod
        def validate_bio(bio: str) -> bool:
        
            if bio == None:
                return False

            if type(bio) != str:
                return False

            return True


        # considerando que não seja um representante de uma empresa
        # @staticmethod
        # def validate_company(company: str)->bool:
        
        #     if type(company) != str:
        #         return False