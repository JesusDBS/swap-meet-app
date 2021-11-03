class Item():
    """
    Documentation here
    """
    
    def __init__(self, category='', condition=0):
        
        #validations
        assert isinstance(category, str), 'category must be a string'
        assert condition >= 0, 'condition must be greater or equal than zero'
        assert condition < 6, 'condition must be an integer between zero and five'

        self.category = category
        self.condition = condition

    def condition_description(self):
        """
        Documentation here
        """
        if self.condition == 0:
            return "new"
        elif self.condition == 1:
            return "pretty new"
        elif self.condition == 2:
            return "almost new"
        elif self.condition == 3:
            return "used"
        elif self.condition == 4:
            return "heavily used"
        elif self.condition == 5:
            return "I'd don't use it"

    def __str__(self):
        return "Hello World!"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.category})"