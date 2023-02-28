from utils import get_products, update_products

def create():
    title = input("Введите название: ")
    price = float(input("Введите цену: "))
    # prinimaem dannye
    new_product = {"title":title, "price":price}
    # sobiraem v slovar
    products = get_products()
    # poluchaem spisok staryx produktov
    products.append(new_product)
    # dobavlyem v spisok novye dannye
    update_products(products)
    # perezapisyvaem fail s novymi dannymi

def read():
    products = get_products()
    # poluchaem spisok produktov
    for product in products:
        print(f"""=====================================
Название: {product['title']}
Цена: {product['price']} 
=============================================
""")