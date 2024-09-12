class Product:  
    # Class to represent a product with basic attributes like name, price, etc.
    def __init__(self, name, price, deal_price, ratings):  
        # Constructor initializing name, price, deal price, and ratings of a product
        self.name = name  # Product name
        self.price = price  # Original price of the product
        self.deal_price = deal_price  # Discounted price during a deal
        self.ratings = ratings  # Customer ratings of the product
        self.you_saved = price - deal_price  # Calculates the amount saved

    def display_product_details(self):  
        # Method to display details of the product
        print("Product: {}".format(self.name))  # Displays product name
        print("Price: {}".format(self.price))  # Displays original price
        print("Deal Price: {}".format(self.deal_price))  # Displays discounted price
        print("Rating: {}".format(self.ratings))  # Displays product rating
        print("You_saved: {}".format(self.you_saved))  # Displays the amount saved

    def get_deal_price(self):  
        # Method to get the deal price of the product
        return self.deal_price  


class ElectronicItem(Product):  
    # Subclass of Product for electronic items with additional warranty attribute
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):  
        # Constructor initializing electronic item with warranty
        super().__init__(name, price, deal_price, ratings)  
        # Calls the constructor of the Product class to initialize inherited attributes
        self.warranty_in_months = warranty_in_months  # Sets warranty duration for the electronic item
    
    def display_product_details(self):  
        # Overrides the parent class method to include warranty details
        super().display_product_details()  # Calls the parent class method to display basic details
        print("Warranty in months: {}".format(self.warranty_in_months))  # Displays warranty details


class GroceryItem(Product):  
    # Subclass of Product for grocery items with additional expiry date attribute
    def __init__(self, name, price, deal_price, ratings, Expiry_date):  
        # Constructor initializing grocery item with expiry date
        super().__init__(name, price, deal_price, ratings)  
        # Calls the constructor of the Product class to initialize inherited attributes
        self.Expiry_date = Expiry_date  # Sets expiry date for the grocery item
    
    def display_product_details(self):  
        # Overrides the parent class method to include expiry date details
        super().display_product_details()  # Calls the parent class method to display basic details
        print("Expiry Date: {}".format(self.Expiry_date))  # Displays expiry date


class order:  
    # Class representing an order with delivery options and items in the cart
    delivery_charges = {  
        # Class-level dictionary containing delivery methods and their charges
        "Normal": 0,  # No charge for normal delivery
        "Prime": 100  # Charge of 100 for prime delivery
    }

    def __init__(self, delivery_method, delivery_address):  
        # Constructor initializing delivery method and address
        self.items_in_cart = []  # Initializes an empty cart (list to hold products)
        self.delivery_method = delivery_method  # Sets delivery method
        self.delivery_address = delivery_address  # Sets delivery address
    
    def add_items(self, product, quantity):  
        # Method to add products to the cart along with quantity
        items = (product, quantity)  # Creates a tuple of product and quantity
        self.items_in_cart.append(items)  # Adds the tuple to the cart
    
    def display_order_details(self):  
        # Method to display details of the order including products and bill
        print("Delivery Method: {}".format(self.delivery_method))  # Displays delivery method
        print("Delivery Address: {}".format(self.delivery_address))  # Displays delivery address
        print("Products")  # Header for the product section
        print("----------------")  
        for product, quantity in self.items_in_cart:  # Loops through all items in the cart
            product.display_product_details()  # Calls product's display method to show details
            print("Quantity: {}".format(quantity))  # Displays the quantity of each product
            print()  
            print("-----------------------------------")  
        
        total_bill = self.get_total_bill()  # Calls method to calculate the total bill
        print("Total Bill: {}".format(total_bill))  # Displays the total bill amount
    
    def get_total_bill(self):  
        # Method to calculate the total bill amount
        total_bill = 0  # Initializes total bill as 0
        for product, quantity in self.items_in_cart:  
            # Loops through all products in the cart and adds the deal price * quantity to total bill
            total_bill += product.get_deal_price() * quantity
        
        order_delivery_charges = order.delivery_charges[self.delivery_method]  
        # Fetches delivery charges based on delivery method
        total_bill += order_delivery_charges  # Adds delivery charges to the total bill
        return total_bill  # Returns the total bill amount
    
    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):  
        # Class method to update delivery charges for a particular method
        cls.delivery_charges[delivery_method] = charges  # Updates the class-level dictionary with new charges


# Creating instances of ElectronicItem and GroceryItem
Tv = ElectronicItem("TV", 25000, 15000, 3.5, 24)  # Creates an electronic item (TV) with 24-month warranty
Milk = GroceryItem("Milk", 100, 80, 4, "2025")  # Creates a grocery item (Milk) with expiry date

# Creating an instance of order
my_order = order("Normal", "kovvur")  # Creates an order with normal delivery and address as "kovvur"
my_order.add_items(Tv, 1)  # Adds one TV to the cart
my_order.add_items(Milk, 3)  # Adds three Milk items to the cart

order.update_delivery_charges("Normal", 50)  # Updates delivery charges for Normal delivery method to 50
my_order.display_order_details()  # Displays the order details including products and total bill
