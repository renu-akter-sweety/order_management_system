# order_management_system
Create a Django project named order_management_system, where users can manage customer
orders and calculate order totals dynamically in the view after form submission. Must be apply
Django Form on the both model.
Project Setup:
• Project Name: order_management_system
• App Name: sales
• Models: CustomerModel and OrderModel
CustomerModel:
Include the following fields:
• customer_name
• email
• phone_number
• address
OrderModel:
The user should fill only: customer, product_name, unit_price, quantity, discount_percent, and
tax_percent.
• customer (ForeignKey relation to CustomerModel)
• product_name
• unit_price
• quantity
• discount_percent
• tax_percent
• subtotal (auto-calculated)
• discount_amount (auto-calculated)
• tax_amount (auto-calculated)
• total_amount (auto-calculated)
Calculation Logic:
After the user submits the OrderForm, the following calculations should be performed in the
view, not in the form or model:
1. Subtotal = unit_price × quantity
2. Discount Amount = (subtotal × discount_percent) / 100
3. Tax Amount = ((subtotal - discount_amount) × tax_percent) / 100
4. Total Amount = subtotal - discount_amount + tax_amount
The calculated fields (subtotal, discount_amount, tax_amount, total_amount) should be saved
automatically in the database.
