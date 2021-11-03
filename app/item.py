class Item():
    """
    Documentation here
    """
    
    def __init__(self, category=''):
        """
        Documentation here
        """
        
        #validations
        assert isinstance(category, str), 'category must be a string'

        self.category = category

    def __str__(self):
        return "Hello World!"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.category})"