class Item():
    """
    Documentation here
    """
    
    def __init__(self, category='', condition=0):
        
        #validations
        assert isinstance(category, str), 'category must be a string'
        assert condition >= 0, 'condition must be greater or equal than zero'
        assert condition < 6, 'condition must be an integer between zero and five'

        self.__category = category
        self.condition = condition

        self.__category_ = None

        if self.__category:
            self.__category_ = True


    @property
    def category(self):
        return self.__category


    @category.setter
    def category(self, value):
        """
        Documentation here
        """
        assert isinstance(value, str), 'category must be a string'

        if value:
            if not self.__category_:
                self.__category = value
                self.__category_ = True

            else:
                raise Exception("You can't change the category of the item")          
        else:
            raise Exception("Empty Category")
        

    def condition_description(self):
        """
        Documentation here
        """
        if self.condition == 5:
            return "new"
        elif self.condition == 4:
            return "pretty new"
        elif self.condition == 3:
            return "almost new"
        elif self.condition == 2:
            return "used"
        elif self.condition == 1:
            return "heavily used"
        elif self.condition == 0:
            return "I'd don't use it"

    def __str__(self):
        return "Hello World!"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.category})"