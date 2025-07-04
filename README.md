
# Online Sales Analysis 🛒

This is a Python project that allows:
- managing an inventory of products (add, display, delete),
- simulating a shopping cart with automatic total value calculation,
- organizing the code using OOP and tracking changes with Git/GitHub.

## Project Structure
online_sales_analysis/
├── product.py # Product class: name, price, quantity
├── product_manager.py # ProductManager class: handles list of products, adding, removing, displaying, total value
├── cart.py # Cart class: handles customer's cart, add products, calculate total, show cart
├── main.py # Main script: creates ProductManager + Cart instances and runs sample logic
├── config.json # (Ignored) contains API keys or confidential data
├── .gitignore # Ensures config.json, screenshots, and cache folders are not pushed
└── README.md # Project documentation
