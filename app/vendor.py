from .item import Item

class Vendor():
    """
    Documentation here
    """

    def __init__(self, inventory=[]):

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
        assert isinstance(category, str), 'category must be a string!'

        list_by_category = [item for item in self.inventory if item.category == category]
        return list_by_category

    def swap_items(self, vendor, my_item, their_item):
        """
        Documentation here
        """
        #validations
        assert isinstance(vendor, Vendor), 'vendor must be instance of Vedor!'
        assert isinstance(my_item, Item), 'my_item must be instance of Item!'
        assert isinstance(their_item, Item), 'their_item must be instance of Item!'
        
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            self.add(their_item)

            vendor.add(my_item)
            vendor.remove(their_item)
            return True
        
        return False

    def swap_first_item(self, vendor):
        """
        Documentation here
        """
        #validations
        assert isinstance(vendor, Vendor), 'vendor must be instance of Vedor!'

        if self.inventory and vendor.inventory:
            self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]
            return True
        
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.inventory})"


