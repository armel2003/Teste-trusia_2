menu = {
    "entrees": [
        {"name": "Salade César", "price": 8, "available": True},
        {"name": "Soupe du jour", "price": 6, "available": False}
    ],
    "plats": [
        {"name": "Steak frites", "price": 15, "available": True},
        {"name": "Poisson grillé", "price": 14, "available": True},
        {"name": "Plat du chef", "price": 18, "available": False}
    ],
    "desserts": [
        {"name": "Tiramisu", "price": 7, "available": True},
        {"name": "Glace", "price": 5, "available": True},
        {"name": "Dessert mystère", "price": 9, "available": False}
    ]
}



for category, items in menu.items():
    print(category.upper())

    for item in items:
        if item["available"]:
            name = item["name"].lower()
            price = item["price"]
            print(f"- {name} : {price}€")

    print()
