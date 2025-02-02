import cherrypy

class WishlistPage:
    def __init__(self):
        self.wishlist = {}

    @cherrypy.expose
    def index(self):
        if not self.wishlist:
            return """
            <html>
            <head>
                <title>Wishlist</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: white; }
                    h1 { color: #333; text-align: center; margin-top: 50px; }
                    .container { text-align: center; padding: 20px; }
                    a { text-decoration: none; color: #007bff; font-size: 18px; }
                    a:hover { text-decoration: underline; }
                    footer {
                        background-color: #232f3e;
                        color: white;
                        padding: 30px;
                        font-family: Arial, sans-serif;
                    }
                    footer { background-color: #333; color: white; text-align: center; padding: 80px; margin-top: 50px;}
                    .footer-grid {
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                        gap: 20px;
                        margin-bottom: 20px;
                    }

                    .footer-grid h3 {
                        font-size: 25px;
                        margin-bottom: 10px;
                        border-bottom: 1px solid #3a45533;
                        padding-bottom: 5px;
                    }

                    .footer-grid ul {
                        list-style: none;
                        padding: 0;
                    }

                    .footer-grid ul li {
                        margin: 5px 0;
                    }

                    .footer-grid ul li a {
                        color: #ddd;
                        text-decoration: none;
                        font-size: 19px;
                        line-height: 40px;
                    }

                    .footer-grid ul li a:hover {
                        color: white;
                        text-decoration: underline;
                    }

                    .footer-bottom {
                        text-align: center;
                        border-top: 1px solid #3a4553;
                        padding-top: 5px;
                        font-size: 20px;
                        line-height: 80px;
                        width: 88vw;
                    }
                    .footer-bottom svg{
                        margin: -5px;
                        width: 50px;
                    }
                </style>
            </head>
            <body>
                <h1>Your Wishlist is Empty</h1>
                <div class="container">
                    <a href="/">Continue Shopping</a>
                </div>
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

        wishlist_items = "".join(
            f"""
            <div class="card">
                <button class="remove-btn" onclick="document.getElementById('remove-{item}').submit();">&times;</button>
                <div class="image-container">
                    <img src="{details['imageUrl']}" alt="{item}" class="product-image">
                </div>
                <div class="details">
                    <h2 class="product-title">{item}</h2>
                    <p class="product-price">Price: Rs. {details['price']}</p>
                    <div class="actions">
                        <form id="remove-{item}" method="post" action="/wishlist/remove" style="display:inline;">
                            <input type="hidden" name="item" value="{item}">
                        </form>
                        <form method="post" action="/checkout" style="display:inline;">
                            <input type="hidden" name="item" value="{item}">
                            <button type="submit" class="move-btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#d0021b" fill="none">
                            <path d="M8.26872 8.49708C9.60954 7.67461 10.7798 8.00606 11.4828 8.53401C11.7711 8.75048 11.9152 8.85871 12 8.85871C12.0848 8.85871 12.2289 8.75048 12.5172 8.53401C13.2202 8.00606 14.3905 7.67461 15.7313 8.49708C17.491 9.57647 17.8891 13.1374 13.8302 16.1417C13.0571 16.7139 12.6706 17 12 17C11.3294 17 10.9429 16.7139 10.1698 16.1417C6.11086 13.1374 6.50903 9.57647 8.26872 8.49708Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                            <path d="M22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22C17.5228 22 22 17.5228 22 12Z" stroke="currentColor" stroke-width="1.5" />
                        </svg></button>
                        </form>
                    </div>
                </div>
            </div>
            """ for item, details in self.wishlist.items()
        )

        return f"""
        <html>
        <head>
            <title>Wishlist</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: white; }}
                h1 {{ color: #333; text-align: center; margin: 20px 0; }}
                .wishlist-container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 20px; }}
                .card {{ position: relative; width: 250px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background-color: #fff; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.2s; }}
                .card:hover {{ transform: translateY(-5px); }}
                .remove-btn {{ position: absolute; top: 10px; right: 10px; background: #ff6b6b; color: white; border: none; border-radius: 50%; width: 25px; height: 25px; cursor: pointer; font-size: 18px; line-height: 20px; text-align: center; }}
                .remove-btn:hover {{ background: #ff4c4c; }}
                .image-container {{ height: 151px; width: 160px; margin: auto; overflow: hidden; }}
                .product-image {{ width: 100%; height: 100%; object-fit: cover; border-bottom: 1px solid #ddd; }}
                .details {{ padding: 10px; text-align: center; }}
                .product-title {{ font-size: 18px; margin: 10px 0; color: #333; }}
                .product-price {{ font-size: 16px; color: #666; margin-bottom: 10px; }}
                .actions {{ display: flex; justify-content: center; align-items: center; gap: 10px; }}
                .move-btn {{ border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; font-size: 14px; }}
                a {{ display: block; text-align: center; text-decoration: none; color: #007bff; margin-top: 20px; font-size: 18px; }}
                a:hover {{ text-decoration: underline; }}
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
            </style>
        </head>
        <body>
            <h1>Your Wishlist</h1>
            <div class="wishlist-container">
                {wishlist_items}
            </div>
            <div class="container">
                <a href="/">Continue Shopping</a>
            </div>
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
    def add(self, item, price="10", imageUrl="None"):
        # Add item to wishlist
        price = float(price)
        if item not in self.wishlist:
            self.wishlist[item] = {'price': price, 'imageUrl': imageUrl}
        raise cherrypy.HTTPRedirect("/wishlist")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def remove(self, item):
        # Remove item from wishlist
        if item in self.wishlist:
            del self.wishlist[item]
        raise cherrypy.HTTPRedirect("/wishlist")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def to_cart(self, item):
        # Move item from wishlist to cart
        if item in self.wishlist:
            # Extract item details
            details = self.wishlist[item]

            # Use CherryPy's publish-subscribe pattern to interact with the cart
            cherrypy.engine.publish("add_to_cart", item, details['price'], details['imageUrl'])

            # Remove the item from the wishlist
            del self.wishlist[item]

        raise cherrypy.HTTPRedirect("/cart")
