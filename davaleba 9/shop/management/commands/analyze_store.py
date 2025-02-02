1#
items = [
    {"name": "Item1", "category": "Electronics"},
    {"name": "Item2", "category": "Clothing"},
    {"name": "Item3", "category": "Electronics"},
    {"name": "Item4", "category": "Books"},
    {"name": "Item5", "category": "Electronics"},
]


category_to_count = "Electronics"


count = sum(1 for item in items if item["category"] == category_to_count)

print(f"{category_to_count}  {count} .")

2#

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 150},
    {"name": "Smartwatch", "price": 300},
]


max_price = max(product["price"] for product in products)


min_price = min(product["price"] for product in products)


avg_price = sum(product["price"] for product in products) / len(products)

print(f '{max_price}')
print(f '{min_price}')
print(f'{avg_price:.2f}')


3#

products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Phone", "category": "Electronics", "price": 800},
    {"name": "Tablet", "category": "Electronics", "price": 500},
    {"name": "T-shirt", "category": "Clothing", "price": 20},
    {"name": "Jeans", "category": "Clothing", "price": 50},
    {"name": "Blender", "category": "Home Appliances", "price": 150},
]


category_summary = defaultdict(lambda: {"count": 0, "price_sum": 0})

for product in products:
    category = product["category"]
    category_summary[category]["count"] += 1
    category_summary[category]["price_sum"] += product["price"]


for category, data in category_summary.items():
    print(f" {category},  {data['count']},  {data['price_sum']}")


4#
products = Product.objects.select_related('category').all()


for product in products:
    print(f" {product.name}, {product.category.name}")