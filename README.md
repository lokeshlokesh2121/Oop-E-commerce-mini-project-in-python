Product Ordering System

This Python-based product ordering system showcases key Object-Oriented Programming (OOP) concepts such as inheritance, encapsulation, polymorphism, and class-level variables. It simulates a basic e-commerce order management system by allowing users to create and manage products, add them to orders, and calculate the total bill with dynamic delivery charges.

Key Features:

1)Product Management:

    Products have attributes like:

    Name
    
    Original Price
    
    Deal Price (discounted price)
    
    Customer Ratings
    
Automatic calculation of the savings (you_saved) by comparing the original and deal price.

2)Specialized Product Types:

    ElectronicItem: Includes a warranty period in months.
    
    GroceryItem: Tracks the expiry date of the product.
    
    These subclasses override the product details display method to include their specific attributes.

3)Order Management:

    Users can:
    
       Create orders with a delivery method and address.
       
       Add multiple items with different quantities to the cart.

       View the total bill, including delivery charges.

    Supported delivery methods (with charges):

        Normal: Default delivery.

        Prime: Faster delivery with an additional fee.

4)Dynamic Delivery Charges:

     Delivery charges can be updated at runtime using the class method update_delivery_charges().

5)Polymorphism and Method Overriding:

     Each product type (electronics or groceries) overrides the display_product_details() method to provide customized output.




How the system works:


Create Products:
       
       Instantiate products with their respective attributes, such as:
       
       Tv = ElectronicItem("TV", 25000, 15000, 3.5, 24)

       Milk = GroceryItem("Milk", 100, 80, 4, "2025")

Create and Manage Orders:
      
      Create an order by selecting a delivery method and address. Add products with their respective quantities:
      
      my_order = order("Normal", "Kovvur")
      my_order.add_items(Tv, 1)
      my_order.add_items(Milk, 3)
    
Update Delivery Charges:

      Adjust delivery charges dynamically using:
      order.update_delivery_charges("Normal", 50)


Display Order Details:
       
      View the complete order summary, including product details, delivery method, and total bill:
      my_order.display_order_details()

      
Example Output

Delivery Method: Normal  

Delivery Address: Kovvur  

Products  
---------------- ------------- 
Product: TV  
Price: 25000  
Deal Price: 15000  
Rating: 3.5  
You_saved: 10000  
Warranty in months: 24  
Quantity: 1  

-----------------------------------  
Product: Milk  
Price: 100  
Deal Price: 80  
Rating: 4  
You_saved: 20  
Expiry Date: 2025  
Quantity: 3  

-----------------------------------  
Total Bill: 16290  

Future Enhancements:
      
      Add more product categories (e.g., fashion, furniture).
      Implement a database to store products and orders.
      Create a CLI or web-based interface to improve usability.
      Add user authentication and account management.


This project offers a great starting point for understanding how OOP principles can be applied in real-world applications. It can be expanded into a full-fledged e-commerce application with more features and functionality.

You can use this enhanced description to make your repository detailed and professional. Let me know if you need further adjustments!












     


