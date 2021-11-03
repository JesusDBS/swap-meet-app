from .item import Item

class Vendor():
    """
    Documentation here
    """

    def __init__(self, inventory=[]):
        """
        Documentation here
        """

        #validations
        # assert all(isinstance(item, str) for item in inventory), 'all elements in inventory must be strings'

        self.inventory = inventory

    def add(self, item):
        """
        Documentation here
        """

        #validations
        # assert isinstance(item, str), 'The new item must be a string'

        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Documentation here
        """

        #validations
        # assert isinstance(item, str), 'The item must be a string'

        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False

    def get_by_category(self, category):
        """
        Documentation here
        """

        #validations
        assert isinstance(category, str), 'category must be a string'

        list_by_category = [item for item in self.inventory if item.category == category]
        return list_by_category

    def __repr__(self):
        return f"{self.__class__.__name__}({self.inventory})"


