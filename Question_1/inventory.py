import csv
from datetime import datetime

FILE_NAME = "products.csv"
PURCHASE_HISTORY_FILE = "purchase_history.csv"
DELIMITER = ","


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Purchase:
    def __init__(self, product_name, quantity, total_price, purchase_date):
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price
        self.purchase_date = purchase_date

    def get_product_name(self):
        return self.product_name

    def get_quantity(self):
        return self.quantity

    def get_total_price(self):
        return self.total_price

    def get_purchase_date(self):
        return self.purchase_date

    def __str__(self):
        return (
            f"Product: {self.product_name}, "
            f"Quantity: {self.quantity}, "
            f"Total Price: ${self.total_price}, "
            f"Purchase Date: {self.purchase_date}"
        )


def load_products_from_file():
    products = []
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                products.append(Product(row[0], float(row[1])))
    except (IOError, ValueError) as e:
        print("Error loading products:", e)
    return products


def save_products_to_file(products):
    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            for product in products:
                writer.writerow([product.get_name(), product.get_price()])
    except IOError as e:
        print("Error saving products:", e)


def load_purchase_history():
    purchase_history = []
    try:
        with open(PURCHASE_HISTORY_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                purchase_history.append(
                    Purchase(
                        row[0],
                        int(row[1]),
                        float(row[2]),
                        datetime.fromtimestamp(int(row[3]))
                    )
                )
    except (IOError, ValueError) as e:
        print("Error loading purchase history:", e)
    return purchase_history


def save_purchase_history_to_file(purchase_history):
    try:
        with open(PURCHASE_HISTORY_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            for purchase in purchase_history:
                writer.writerow([
                    purchase.get_product_name(),
                    purchase.get_quantity(),
                    purchase.get_total_price(),
                    int(purchase.get_purchase_date().timestamp())
                ])
    except IOError as e:
        print("Error saving purchase history:", e)


def view_products(products):
    print("Product List:")
    for product in products:
        print(product)


def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append(Product(name, price))
    print("Product added successfully.")


def remove_product(products):
    name = input("Enter product name to remove: ")
    for product in products:
        if product.get_name().lower() == name.lower():
            products.remove(product)
            print("Product removed successfully.")
            return
    print("Product not found.")


def purchase_product(products, purchase_history):
    name = input("Enter product name to purchase: ")
    for product in products:
        if product.get_name().lower() == name.lower():
            quantity = int(input("Enter quantity to purchase: "))
            total_price = product.get_price() * quantity
            purchase = Purchase(
                product.get_name(),
                quantity,
                total_price,
                datetime.now()
            )
            purchase_history.append(purchase)
            print("Purchase successful.")
            return
    print("Product not found.")


def view_purchase_history(purchase_history):
    print("Purchase History:")
    for purchase in purchase_history:
        print(purchase)


def main():
    products = load_products_from_file()
    purchase_history = load_purchase_history()

    while True:
        print("\n1. View Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Purchase Product")
        print("5. View Purchase History")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_products(products)
        elif choice == 2:
            add_product(products)
        elif choice == 3:
            remove_product(products)
        elif choice == 4:
            purchase_product(products, purchase_history)
        elif choice == 5:
            view_purchase_history(purchase_history)
        elif choice == 6:
            save_products_to_file(products)
            save_purchase_history_to_file(purchase_history)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
