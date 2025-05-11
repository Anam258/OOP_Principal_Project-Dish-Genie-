from dish import Dish

def get_dishes_by_weather():
    return {
        "Sunny": [
            Dish("Grilled Sandwich🥪", "Light and crispy for sunny days!", ""),
            Dish("Lemonade Salad 🥗", "Refreshing and juicy summer mix.", ""),
            Dish("Fruit Chaat 🍉", "Cool mix of seasonal fruits.", ""),
            Dish("Cold Coffee 🥤", "Chilled and creamy.", ""),
            Dish("Ice Cream 🍦", "Beat the heat with a scoop!", ""),
            Dish("Watermelon Smoothie 🍉", "Sweet and hydrating.", ""),
            Dish("Chicken Wrap 🌯", "A quick and tasty lunch option.", ""),
            Dish("Mango Lassi 🥭", "A tropical drink to refresh you.", ""),
            Dish("Cucumber Sandwich 🥒", "Light and healthy for summer.", ""),
            Dish("Pineapple Cake 🍍", "A tropical dessert to beat the heat.", ""),
        ],
        "Rainy": [
            Dish("Tomato Soup 🍲", "Perfect match with the rain.", ""),
            Dish("Pakoras 🧆", "Crispy snacks for rainy cravings.", ""),
            Dish("Masala Chai 🍵", "Warm hug in a cup.", ""),
            Dish("Bread Rolls 🍞", "Spicy and crunchy.", ""),
            Dish("Bhutta (Corn) 🌽", "Grilled corn for monsoon feels.", ""),
            Dish("Vegetable Pulao 🍚", "Comfort food for rainy days.", ""),
            Dish("Besan ki Roti 🫓", "Spicy flatbread for the rainy season.", ""),
            Dish("Hot Samosas 🥟", "Crispy and warm for the rainy mood.", ""),
            Dish("Cheese Toast 🧀", "Melted cheese on toasted bread.", ""),
            Dish("Ginger Tea 🍵", "Warm and spicy drink to cozy up.", ""),
        ],
        "Cold": [
            Dish("Paneer Tikka 🍢", "Spicy warmth for chilly days.", ""),
            Dish("Hot Chocolate ☕", "Cozy and comforting.", ""),
            Dish("Methi Paratha 🫓", "Winter favorite.", ""),
            Dish("Gajar ka Halwa 🍮", "Sweet seasonal delight.", ""),
            Dish("Khichdi 🍛", "Warm and filling.", ""),
            Dish("Spicy Soup 🍲", "A hot and spicy treat for cold days.", ""),
            Dish("Aloo Gobi 🥔", "Hearty and comforting winter dish.", ""),
            Dish("Garlic Bread 🥖", "Perfect with a hot bowl of soup.", ""),
            Dish("Dum Aloo 🍛", "Spicy and aromatic winter dish.", ""),
            Dish("Masala Maggi 🍜", "Hot and flavorful noodles.", ""),
        ]
    }
