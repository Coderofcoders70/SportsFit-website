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
                    body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #ffddbc; }
                    h1 { color: #333; text-align: center; }
                    .container { text-align: center; padding: 20px; }
                    a { text-decoration: none; color: #007bff; }
                    a:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                <h1>Your Wishlist is Empty</h1>
                <div class="container">
                    <a href="/">Continue Shopping</a>
                </div>
            </body>
            </html>
            """

        wishlist_items = "".join(
            f"""
            <div class="card">
                <button class="remove-btn" onclick="document.getElementById('remove-{item}').submit();">&times;</button>
                <div style = "height: 195px; width:170px; margin: auto;"><img src="{details['imageUrl']}" alt="{item}" class="product-image"></div>
                <div class="details">
                    <h2 class="product-title">{item}</h2>
                    <p class="product-price">Price: Rs. {details['price']}</p>
                    <div class="actions">
                        <form id="remove-{item}" method="post" action="/wishlist/remove" style="display:inline;">
                            <input type="hidden" name="item" value="{item}">
                        </form>
                        <form method="post" action="/wishlist/to_cart" style="display:inline;">
                            <input type="hidden" name="item" value="{item}">
                            <button type="submit" class="move-btn">Move to Cart</button>
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
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #ffddbc; }}
                h1 {{ color: #333; text-align: center; margin: 20px 0; }}
                .wishlist-container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 20px; }}
                .card {{ position: relative; width: 250px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background-color: #fff; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }}
                .remove-btn {{ position: absolute; top: 10px; right: 10px; background: #ff6b6b; color: white; border: none; border-radius: 50%; width: 25px; height: 25px; cursor: pointer; font-size: 18px; line-height: 20px; text-align: center; }}
                .remove-btn:hover {{ background: #ff4c4c; }}
                .product-image {{ width: 100%; object-fit: cover; }}
                .details {{ padding: 10px; text-align: center; }}
                .product-title {{ font-size: 18px; margin: 10px 0; color: #333; }}
                .product-price {{ font-size: 16px; color: #666; margin-bottom: 10px; }}
                .actions {{ display: flex; justify-content: center; align-items: center; gap: 10px; }}
                .move-btn {{ background-color: #007bff; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; }}
                .move-btn:hover {{ background-color: #0056b3; }}
                a {{ display: block; text-align: center; text-decoration: none; color: #007bff; margin-top: 20px; }}
                a:hover {{ text-decoration: underline; }}
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
        </body>
        </html>
        """

    @cherrypy.expose
    def add(self, item, price="10",imageUrl="None"):
        # Add item to wishlist
        price = float(price)
        if item not in self.wishlist:
            self.wishlist[item] = {'price': price,'imageUrl': imageUrl}
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
            price = self.wishlist[item]['price']
            cherrypy.engine.publish("add_to_cart", item, price)
            del self.wishlist[item]
        raise cherrypy.HTTPRedirect("/cart")
