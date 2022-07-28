# MyStore
My online store selling appliances.

Functional:
  - registration, login, log out;
  Admin:
    - view products - a list of existing products, indicating prices and quantity of goods in stock. Link to change the product next to the description.;
    - add product - create a new product, specifying all fields, including price and quantity in stock;
    - modify product - modify an existing product. You can change all fields, including the number of products in stock (to replenish the number of products);
   
   User:
    - view a list of products, with prices and quantities in stock. 
    - near the description there is a form with the ability to specify the number of products and a buy button. If there are not enough goods in the warehouse, a corresponding message is displayed; if the user does not have enough money for this purchase, a corresponding message is also displayed. If all conditions are met, a purchase object is created, the quantity of the goods in the warehouse decreases, and the amount in the user's wallet is reduced.






admin View returns - List with return objects (regular users can create them) with two buttons, confirm or reject. 
If the admin approves the return, the purchase object should be deleted, the product quantity should be returned to the product model, and the cost of the products returned in the user's wallet field.
If the admin deletes the return - delete the return request. You cannot delete a product.
