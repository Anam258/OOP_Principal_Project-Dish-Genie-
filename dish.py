# dish.py
class Dish:
    """
    This class encapsulates the properties of a dish.
    It represents a single dish with its name, description, and image.
    """
    def __init__(self, name, description, image=None):
        self.name = name  # The name of the dish
        self.description = description  # The description of the dish
        self.image = image  # Optional image of the dish

    def get_name(self):
        """Return the name of the dish"""
        return self.name

    def get_description(self):
        """Return the description of the dish"""
        return self.description

    def get_image(self):
        """Return the image of the dish (if provided)"""
        return self.image
