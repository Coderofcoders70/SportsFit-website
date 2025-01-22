import cherrypy

class CartPage:
    def __init__(self):
        # Initialize an empty cart
        self.cart = {}
        self.products = [
            {"name": "Running Shoes", "category": "sports-wear", "price": 999, "imageURL": "https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg"},
            {"name": "Adjustable Dumbbells", "category": "gym-equipment", "price": 1500, "imageURL": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg"},
            {"name": "Mountain Bike", "category": "outdoor", "price": 2500,  "imageURL": "https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg"},
            {"name": "Treadmill", "category": "fitness-equipment", "price": 20000,  "imageURL": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"},
            {"name": "Protein Bar", "category": "nutrition", "price": 800,  "imageURL": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg"},
            {"name": "Cricket Set", "category": "sports-accessories", "price": 1000, "imageURL": "https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg"},
            {"name": "Yoga Mat", "category": "fitness-accessories", "price": 700, "imageURL": "https://m.media-amazon.com/images/I/61iLVerCzOL._SX569_.jpg"},
            {"name": "Resistance Bands", "category": "fitness-accessories", "price": 500, "imageURL": "https://m.media-amazon.com/images/I/612c73jZt1L._SX569_.jpg"},
            {"name": "Skipping Rope", "category": "fitness-accessories", "price": 200, "imageURL": "https://m.media-amazon.com/images/I/81O6gfeClDL._SX569_.jpg"},
            {"name": "Foam Roller", "category": "fitness-accessories", "price": 800, "imageURL": "https://m.media-amazon.com/images/I/41gZtYEhabL._AC_UL320_.jpg"},
            {"name": "Ankle Weights", "category": "fitness-accessories", "price": 450, "imageURL": "https://m.media-amazon.com/images/I/41b81SJr4dL._AC_UL320_.jpg"},
        ]
        self.coupon_code = "DISCOUNT20"
    
    def get_recommendations(self):
        cart_categories = {details["category"] for details in self.cart.values()}
        recommendations = [
            product for product in self.products if product["category"] in cart_categories
        ]
        return recommendations

    @cherrypy.expose
    def index(self, coupon_code=None, selected_items=None):
        # Handle discount logic
        total_amount = sum(details['price'] * details['quantity'] for details in self.cart.values())
        discount = 0
        if coupon_code == self.coupon_code:
            discount = total_amount * 0.2
            total_amount -= discount

        # Generate cart items
        cart_items = "".join(
            f"""
            <div class="cart-item">
              <input type="checkbox" class="item-select" data-price="{details['price']}" data-quantity="{details['quantity']}">
                <div class="item-image">
                    <img src="{details['imageURL']}" alt="{item}">
                </div>
                <div class="item-details">
                    <h3>{item}</h3>
                    <p class="category">Category: {details['category']}</p>
                    <p class="description">{details['description']}</p>
                    <p class="price">Price: ₹{details['price']}</p>
                    <div class="quantity-controls">
                        <form method="post" action="/cart/update" class="quantity-form">
                            <input type="hidden" name="item" value="{item}">
                            <button class="quantity-btn" name="quantity" value="{details['quantity'] - 1}" type="submit">−</button>
                            <span>{details['quantity']}</span>
                            <button class="quantity-btn" name="quantity" value="{details['quantity'] + 1}" type="submit">+</button>
                        </form>
                    </div>
                    <form method="post" action="/cart/remove" class="remove-form">
                        <input type="hidden" name="item" value="{item}">
                        <button class="remove-btn" title="Remove Item">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50" height="54" color="#000000" fill="none">
                        <path d="M19.5 5.5L18.8803 15.5251C18.7219 18.0864 18.6428 19.3671 18.0008 20.2879C17.6833 20.7431 17.2747 21.1273 16.8007 21.416C15.8421 22 14.559 22 11.9927 22C9.42312 22 8.1383 22 7.17905 21.4149C6.7048 21.1257 6.296 20.7408 5.97868 20.2848C5.33688 19.3626 5.25945 18.0801 5.10461 15.5152L4.5 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M3 5.5H21M16.0557 5.5L15.3731 4.09173C14.9196 3.15626 14.6928 2.68852 14.3017 2.39681C14.215 2.3321 14.1231 2.27454 14.027 2.2247C13.5939 2 13.0741 2 12.0345 2C10.9688 2 10.436 2 9.99568 2.23412C9.8981 2.28601 9.80498 2.3459 9.71729 2.41317C9.32164 2.7167 9.10063 3.20155 8.65861 4.17126L8.05292 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M9.5 16.5L9.5 10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M14.5 16.5L14.5 10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        </svg>
                        </button>
                    </form>
                </div>
            </div>
            """ for item, details in self.cart.items()
        )

        # Generate recommendations
        recommendations = "".join(
            f"""
            <div class="recommendation-item">
                <img src="{product['imageURL']}" alt="{product['name']}">
                <p>{product['name']}</p>
                <p>₹{product['price']}</p>
                <form method="post" action="/cart/add">
                    <input type="hidden" name="item" value="{product['name']}">
                    <input type="hidden" name="price" value="{product['price']}">
                    <input type="hidden" name="category" value="{product['category']}">
                    <input type="hidden" name="imageURL" value="{product['imageURL']}">
                    <button type="submit">Add to Cart</button>
                </form>
            </div>
            """
            for product in self.get_recommendations()
        )

        # Render the page
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Your Cart</title>
            <style>
            body{{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f3f3f3;
            }}

            header {{
                background-color: #232f3e;
                padding: 10px 20px;
                color: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            header a {{
                color: white;
                text-decoration: none;
                margin-right: 20px;
                font-size: 22px;
            }}

            .cart-icon {{
                display: flex;
                align-items: center;
                margin-top: 10px;
            }}

            .cart-counter {{
                background-color: #ff9900;
                border-radius: 50%;
                padding: 5px 10px;
                margin-left: 5px;
                color: white;
            }}

            h1, h2 {{
                color: #232f3e;
                text-align: center;
            }}

            .cart-container {{
                display: flex;
                margin: 20px;
                background-color: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }}
            .cart-item {{ display: flex; align-items: center; margin-bottom: 20px; }}
            .item-checkbox {{ margin-right: 10px; }}
            .item-details, .item-image {{ margin-left: 10px; }}
            .summary-header {{ font-size: 18px; margin-bottom: 10px; }}

            .left-container, .right-container {{
                width: 50%;
            }}
            .cart-item {{
                display: flex;
                margin-bottom: 20px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 15px;
            }}

            .item-image img {{
                width: 100px;
                height: 100px;
                object-fit: contain;
            }}
            .item-details {{
                margin-left: 20px;
                display: grid;
                grid-template-columns: 1fr 1fr;
                flex-grow: 1;
                gap: 20px;
            }}

            .price {{
                font-weight: bold;
                color: #B12704;
            }}
            .quantity-controls {{
                display: flex;
                align-items: center;
            }}

            .quantity-btn {{
                background-color: #ddd;
                border: none;
                padding: 5px 10px;
                margin: 0 5px;
                cursor: pointer;
                border-radius: 3px;
            }}

            .quantity-btn:hover {{
                background-color: #ccc;
            }}
            .remove-btn svg {{
                width: 20px;
                height: 20px;
                cursor: pointer;
            }}
            .right-container {{
                padding-left: 20px;
                border-left: 1px solid #ddd;
            }}
            .recommendations-container {{
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                margin: 20px;
            }}

            .recommendation-item {{
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 4px;
                margin: 10px;
                width: 15%;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                text-align: center;
            }}
            .recommendation-item img {{
                width: 100%;
                height: 150px;
                object-fit: contain;
                margin-bottom: 10px;
            }}

            .recommendation-item button {{
                background-color: #ff9900;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
                margin: 20px;
            }}
            .coupon_text{{
               font-size: 20px;
               color: orange;
            }}
            .Delivery_container {{ 
            background-color: #ff9900; 
            width: 61%; 
            border-radius: 15px; 
            }}
            .Delivery {{ 
                background-color: #ff9900; 
                color: white; 
                padding: 2%; 
                text-align: right; 
                font-size: 20px; 
                border-radius: 15px; 
            }}
            .bar {{ 
                width: 100%; 
            }}  
            .recommendation-item button:hover {{
                background-color: #e68a00;
            }}

            .proceed-btn {{
                width: 25%;
                margin-top: 20px;
                background-color: #ff9900;
                color: white;
                border: none;
                padding: 14px;
                font-size: 16px;
                border-radius: 42px;
                cursor: pointer;
            }}

            .proceed-btn:hover {{
                background-color: #e68a00;
            }}
            .coupon_code{{
                padding: 5px;
            }}
            .applybtn{{
                padding: 8px;
                width: 95px;
                font-size: 15px;
            }}
            footer {{
                background-color: #232f3e;
                color: white;
                padding: 30px;
                font-family: Arial, sans-serif;
            }}
            footer {{ background-color: #333; color: white; text-align: center; padding: 80px; margin-top: 50px;}}
            .footer-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 20px;
            }}

            .footer-grid h3 {{
                font-size: 25px;
                margin-bottom: 10px;
                border-bottom: 1px solid #3a45533;
                padding-bottom: 5px;
            }}

            .footer-grid ul {{
                list-style: none;
                padding: 0;
            }}

            .footer-grid ul li {{
                margin: 5px 0;
            }}

            .footer-grid ul li a {{
                color: #ddd;
                text-decoration: none;
                font-size: 19px;
                line-height: 40px;
            }}
            .footer-grid ul li a:hover {{
                color: white;
                text-decoration: underline;
            }}
            .footer-bottom {{
                text-align: center;
                border-top: 1px solid #3a4553;
                padding-top: 5px;
                font-size: 20px;
                line-height: 80px;
                width: 88vw;
            }}
            .footer-bottom svg{{
                margin: -5px;
                width: 50px;
            }}
            .item-select{{
                width: 18px;
                height: 21px;
            }}
        </style>
        </head>
        <body>
            <header>
                <nav>
                    <a href="/">Cart</a>
                    <a href="/cart" class="cart-icon">
                    <span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#f3ecec" fill="none">
                    <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                    <path d="M11 8.5C11.4915 9.0057 12.7998 11 13.5 11M16 8.5C15.5085 9.0057 14.2002 11 13.5 11M13.5 11V3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                    <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                    <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                    </svg></span>
                    <span class="cart-counter">{sum(details['quantity'] for details in self.cart.values())}</span>
                    </a>
                </nav>
            </header>
            <h1>Your Shopping Cart</h1>
            <div class="cart-container">
                <div class="left-container">
                     <div class="summary-header">
                        Total Items: <span id="total-items">{sum(details['quantity'] for details in self.cart.values())}</span> |
                        Selected Items: <span id="selected-items">0</span>
                    </div>
                    {cart_items}
                </div>
                <div class="right-container">
                    <h3>Order Summary</h3> 
                    <p><strong>Subtotal:</strong> ₹<span id="subtotal">{total_amount + discount}</span></p>
                    <p><strong>Discount:</strong> ₹<span id="discount">{discount}</span></p>
                    <p><strong>Total:</strong> ₹<span id="total">{total_amount}</span></p>
                    <div class="Delivery_container"> 
                     <div class="Delivery bar"></div> 
                    </div>
                    <br>
                    <p class="coupon_text">For best experience use coupon code to get the best deals.</p>
                    <form method="get" action="/cart">
                        <label for="coupon_code"><strong>Coupon Code:</strong></label>
                        <input class= "coupon_code" type="text" name="coupon_code" id="coupon_code">
                        <button class= "applybtn" type="submit">Apply</button>
                    </form>
                    <form method="POST" action="/checkout">
                      <input type="hidden" name="selected_items" value="{','.join(selected_items) if selected_items else ''}">
                        <button class="proceed-btn">Proceed to Checkout</button>
                    </form>
                </div>
            </div>
            <h2>Recommended Products</h2>
            <div class="recommendations-container">
                {recommendations}
            </div>
             <script>
                document.addEventListener('DOMContentLoaded', () => {{
                    const checkboxes = document.querySelectorAll('.item-select');
                    const subtotalElement = document.getElementById('subtotal');
                    const discountElement = document.getElementById('discount');
                    const totalElement = document.getElementById('total');
                    const selectedItemsElement = document.getElementById('selected-items');

                    function updateSummary() {{
                        let selectedSubtotal = 0;
                        let selectedDiscount = 0;
                        let selectedTotal = 0;
                        let selectedCount = 0;

                        checkboxes.forEach(checkbox => {{
                            if (checkbox.checked) {{
                                const price = parseFloat(checkbox.dataset.price);
                                const quantity = parseInt(checkbox.dataset.quantity);
                                selectedSubtotal += price * quantity;
                                selectedCount += quantity;
                            }}
                        }});

                        selectedDiscount = selectedSubtotal * 0.2; // Assuming discount logic remains the same
                        selectedTotal = selectedSubtotal - selectedDiscount;

                        subtotalElement.textContent = selectedSubtotal.toFixed(2);
                        discountElement.textContent = selectedDiscount.toFixed(2);
                        totalElement.textContent = selectedTotal.toFixed(2);
                        selectedItemsElement.textContent = selectedCount;
                    }}

                    checkboxes.forEach(checkbox => {{
                        checkbox.addEventListener('change', updateSummary);
                    }});
                }});
            </script>
            <footer>
                <div class="footer-grid">
            <!-- Section: Get to Know Us -->
            <div>
                <h3>Get to Know Us</h3>
                <ul>
                    <li><a href="#">About SportsFit</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Press Releases</a></li>
                    <li><a href="#">SportsFit Science</a></li>
                </ul>
            </div>

            <!-- Section: Connect with Us -->
            <div>
                <h3>Connect with Us</h3>
                <ul>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">Instagram</a></li>
                </ul>
            </div>

            <!-- Section: Make Money with Us -->
            <div>
                <h3>Make Money with Us</h3>
                <ul>
                    <li><a href="#">Sell on SportsFit</a></li>
                    <li><a href="#">Sell under SportsFit Accelerator</a></li>
                    <li><a href="#">Protect and Build Your Brand</a></li>
                    <li><a href="#">SportsFit Global Selling</a></li>
                    <li><a href="#">Supply to sportsFit</a></li>
                    <li><a href="#">Become an Affiliate</a></li>
                    <li><a href="#">Fulfilment by SportsFit</a></li>
                    <li><a href="#">Advertise Your Products</a></li>
                    <li><a href="#">SportsFit Pay on Merchants</a></li>
                </ul>
            </div>

            <!-- Section: Let Us Help You -->
            <div>
                <h3>Let Us Help You</h3>
                <ul>
                    <li><a href="#">Your Account</a></li>
                    <li><a href="#">Returns Centre</a></li>
                    <li><a href="#">Recalls and Product Safety Alerts</a></li>
                    <li><a href="#">100% Purchase Protection</a></li>
                    <li><a href="#">Help</a></li>
                </ul>
            </div>
        </div>
            <div class="footer-bottom">
             <p><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(245, 236, 236, 1);transform: ;msFilter:;"><path d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm7.931 9h-2.764a14.67 14.67 0 0 0-1.792-6.243A8.013 8.013 0 0 1 19.931 11zM12.53 4.027c1.035 1.364 2.427 3.78 2.627 6.973H9.03c.139-2.596.994-5.028 2.451-6.974.172-.01.344-.026.519-.026.179 0 .354.016.53.027zm-3.842.7C7.704 6.618 7.136 8.762 7.03 11H4.069a8.013 8.013 0 0 1 4.619-6.273zM4.069 13h2.974c.136 2.379.665 4.478 1.556 6.23A8.01 8.01 0 0 1 4.069 13zm7.381 6.973C10.049 18.275 9.222 15.896 9.041 13h6.113c-.208 2.773-1.117 5.196-2.603 6.972-.182.012-.364.028-.551.028-.186 0-.367-.016-.55-.027zm4.011-.772c.955-1.794 1.538-3.901 1.691-6.201h2.778a8.005 8.005 0 0 1-4.469 6.201z"></path></svg>English India</p>
            </div>
            <p style = "line-height: 44px; margin-top: -25px;">Your Support Our Efforts</p>
            <p>&copy; 2024 SportsFit. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """
    
    @cherrypy.expose
    def add(self, item, price=None, description=None, imageURL=None, category=None):
        price = float(price) if price else 0.0
        if item in self.cart:
            self.cart[item]['quantity'] += 1
        else:
            self.cart[item] = {
                'quantity': 1,
                'price': price,
                'description': description,
                'imageURL': imageURL,
                'category': category,
            }
        raise cherrypy.HTTPRedirect("/cart")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def remove(self, item):
        if item in self.cart:
            del self.cart[item]
        raise cherrypy.HTTPRedirect("/cart")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def update(self, item, quantity):
        quantity = int(quantity)
        if item in self.cart:
            if quantity > 0:
                self.cart[item]['quantity'] = quantity
            else:
                del self.cart[item]
        raise cherrypy.HTTPRedirect("/cart")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def proceed(self):
        return """
        <h1>Thank you for your purchase!</h1>
        """
