# gui.py
import tkinter as tk
from tkinter import messagebox
from models import ProductManager, Customer, Product

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management Application")
        self.geometry("400x400")
        self._initialize_ui()

    def _initialize_ui(self):
        self.main_menu()

    def main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Main Menu", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Product Manager", command=self.product_manager_menu).pack(pady=10)
        tk.Button(self, text="Customer", command=self.customer_menu).pack(pady=10)
        tk.Button(self, text="Exit", command=self.quit).pack(pady=10)

    def product_manager_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Product Manager Menu", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Register", command=self.pm_register).pack(pady=10)
        tk.Button(self, text="Login", command=self.pm_login).pack(pady=10)
        tk.Button(self, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def customer_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Customer Menu", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Register", command=self.customer_register).pack(pady=10)
        tk.Button(self, text="Login", command=self.customer_login).pack(pady=10)
        tk.Button(self, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def pm_register(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Product Manager Registration", font=("Helvetica", 16)).pack(pady=20)
        username_label = tk.Label(self, text="Username")
        username_label.pack(pady=5)
        username_entry = tk.Entry(self)
        username_entry.pack(pady=5)
        password_label = tk.Label(self, text="Password")
        password_label.pack(pady=5)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack(pady=5)

        def register():
            username = username_entry.get()
            password = password_entry.get()
            pm = ProductManager(username, password)
            pm.register()
            messagebox.showinfo("Success", "Product Manager Registered Successfully")
            self.product_manager_menu()

        tk.Button(self, text="Register", command=register).pack(pady=10)
        tk.Button(self, text="Back", command=self.product_manager_menu).pack(pady=10)

    def pm_login(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Product Manager Login", font=("Helvetica", 16)).pack(pady=20)
        username_label = tk.Label(self, text="Username")
        username_label.pack(pady=5)
        username_entry = tk.Entry(self)
        username_entry.pack(pady=5)
        password_label = tk.Label(self, text="Password")
        password_label.pack(pady=5)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack(pady=5)

        def login():
            username = username_entry.get()
            password = password_entry.get()
            pm = ProductManager(username, password)
            if pm.login():
                messagebox.showinfo("Success", "Logged in Successfully")
                self.pm_dashboard(pm)
            else:
                messagebox.showerror("Error", "Invalid Credentials")
                self.product_manager_menu()

        tk.Button(self, text="Login", command=login).pack(pady=10)
        tk.Button(self, text="Back", command=self.product_manager_menu).pack(pady=10)

    def pm_dashboard(self, pm):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Product Manager Dashboard", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Manage Products", command=self.manage_products).pack(pady=10)
        tk.Button(self, text="View All Stocks", command=self.view_all_stocks).pack(pady=10)
        tk.Button(self, text="Logout", command=self.main_menu).pack(pady=10)

    def customer_register(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Customer Registration", font=("Helvetica", 16)).pack(pady=20)
        username_label = tk.Label(self, text="Username")
        username_label.pack(pady=5)
        username_entry = tk.Entry(self)
        username_entry.pack(pady=5)
        password_label = tk.Label(self, text="Password")
        password_label.pack(pady=5)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack(pady=5)

        def register():
            username = username_entry.get()
            password = password_entry.get()
            customer = Customer(username, password)
            customer.register()
            messagebox.showinfo("Success", "Customer Registered Successfully")
            self.customer_menu()

        tk.Button(self, text="Register", command=register).pack(pady=10)
        tk.Button(self, text="Back", command=self.customer_menu).pack(pady=10)

    def customer_login(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Customer Login", font=("Helvetica", 16)).pack(pady=20)
        username_label = tk.Label(self, text="Username")
        username_label.pack(pady=5)
        username_entry = tk.Entry(self)
        username_entry.pack(pady=5)
        password_label = tk.Label(self, text="Password")
        password_label.pack(pady=5)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack(pady=5)

        def login():
            username = username_entry.get()
            password = password_entry.get()
            customer = Customer(username, password)
            if customer.login():
                messagebox.showinfo("Success", "Logged in Successfully")
                self.customer_dashboard(customer)
            else:
                messagebox.showerror("Error", "Invalid Credentials")
                self.customer_menu()

        tk.Button(self, text="Login", command=login).pack(pady=10)
        tk.Button(self, text="Back", command=self.customer_menu).pack(pady=10)

    def customer_dashboard(self, customer):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Customer Dashboard", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Purchase Stock", command=lambda: self.purchase_stock(customer)).pack(pady=10)
        tk.Button(self, text="View All Orders", command=self.view_all_orders).pack(pady=10)
        tk.Button(self, text="Logout", command=self.main_menu).pack(pady=10)

    def manage_products(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Manage Products", font=("Helvetica", 16)).pack(pady=20)
        name_label = tk.Label(self, text="Product Name")
        name_label.pack(pady=5)
        name_entry = tk.Entry(self)
        name_entry.pack(pady=5)
        stock_label = tk.Label(self, text="Stock")
        stock_label.pack(pady=5)
        stock_entry = tk.Entry(self)
        stock_entry.pack(pady=5)
        price_label = tk.Label(self, text="Price")
        price_label.pack(pady=5)
        price_entry = tk.Entry(self)
        price_entry.pack(pady=5)

        def add_product():
            name = name_entry.get()
            stock = int(stock_entry.get())
            price = float(price_entry.get())
            product = Product(name, stock, price)
            product.add_product()
            messagebox.showinfo("Success", "Product Added Successfully")
            self.pm_dashboard(None)

        tk.Button(self, text="Add Product", command=add_product).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: self.pm_dashboard(None)).pack(pady=10)

    def view_all_stocks(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="All Product Stocks", font=("Helvetica", 16)).pack(pady=20)
        products = Product.get_all_products()
        for product in products:
            tk.Label(self, text=f"Product ID: {product[0]}, Name: {product[1]}, Stock: {product[2]}, Price: {product[3]}").pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.pm_dashboard(None)).pack(pady=10)

    def purchase_stock(self, customer):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Purchase Stock", font=("Helvetica", 16)).pack(pady=20)
        product_id_label = tk.Label(self, text="Product ID")
        product_id_label.pack(pady=5)
        product_id_entry = tk.Entry(self)
        product_id_entry.pack(pady=5)
        quantity_label = tk.Label(self, text="Quantity")
        quantity_label.pack(pady=5)
        quantity_entry = tk.Entry(self)
        quantity_entry.pack(pady=5)

        def purchase():
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product WHERE product_id=%s", (product_id,))
            product = cursor.fetchone()
            if product and product[2] >= quantity:
                total_price = product[3] * quantity
                if customer.get_balance() >= total_price:
                    customer.update_balance(-total_price)
                    new_stock = product[2] - quantity
                    Product.update_stock(product_id, new_stock)
                    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)", (customer.customer_id, product_id, quantity, total_price))
                    conn.commit()
                    messagebox.showinfo("Success", "Purchase Successful")
                else:
                    messagebox.showerror("Error", "Insufficient Balance")
            else:
                messagebox.showerror("Error", "Insufficient Stock")
            cursor.close()
            conn.close()
            self.customer_dashboard(customer)

        tk.Button(self, text="Purchase", command=purchase).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: self.customer_dashboard(customer)).pack(pady=10)

    def view_all_orders(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="All Orders", font=("Helvetica", 16)).pack(pady=20)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        cursor.close()
        conn.close()
        for order in orders:
            tk.Label(self, text=f"Order ID: {order[0]}, Customer ID: {order[1]}, Product ID: {order[2]}, Quantity: {order[3]}, Total Price: {order[4]}").pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.customer_dashboard(None)).pack(pady=10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
