import cherrypy
import json

# Example data structure for products
PRODUCTS = [
    {"id": "running-shoes", "name": "Running Shoes", "category": "sports-wear", "price": 999, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg"},
    {"id": "adjustable-dumbbells", "name": "Adjustable Dumbbells", "category": "gym-equipment", "price": 1500, "rating": 4.2, "image": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg"},
    {"id": "mountain-bike", "name": "Mountain Bike", "category": "outdoor", "price": 2500, "rating": 4.5, "image": "https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg"},
    {"id": "treadmill", "name": "Treadmill", "category": "fitness-equipment", "price": 20000, "rating": 4.8, "image": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"},
    {"id": "protein-bar", "name": "Protein Bar", "category": "nutrition", "price": 800, "rating": 4.3, "image": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg"},
    {"id": "cricket-set", "name": "Cricket Set", "category": "sports-accessories", "price": 1000, "rating": 3.2, "image": "https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg"},
    {"id": "yoga-mat", "name": "Yoga Mat", "category": "fitness-accessories", "price": 700, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/61iLVerCzOL._SX569_.jpg"},
]

class Products:

    @cherrypy.expose
    def index(self, category=None, price_range=None, min_rating=None):
        """
        Display products with optional filters for category, price range, and rating.
        """
        filtered_products = PRODUCTS

        if category:
            filtered_products = [p for p in filtered_products if p['category'] == category]

        if price_range:
            try:
                min_price, max_price = map(int, price_range.split('-'))
                filtered_products = [p for p in filtered_products if min_price <= p['price'] <= max_price]
            except ValueError:
                pass

        if min_rating:
            try:
                min_rating = float(min_rating)
                filtered_products = [p for p in filtered_products if p['rating'] >= min_rating]
            except ValueError:
                pass

        # Generate HTML for filtered products
        products_html = "".join(
            f"""
            <div class='product'>
                <img src='{product['image']}' alt='{product['name']}' />
                <h3>{product['name']}</h3>
                <p>Price: ₹{product['price']}</p>
                <p>
                    Rating: {''.join(['<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" style="fill:gold;"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></svg>' for _ in range(int(product['rating']))])}
                </p>
                <button onclick="addToCart('{product['id']}','{product['price']}', '{product['category']}', '{product['image']}')">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 229, 229, 1);transform: ;msFilter:;"><circle cx="10.5" cy="19.5" r="1.5"></circle><circle cx="17.5" cy="19.5" r="1.5"></circle><path d="M21 7H7.334L6.18 4.23A1.995 1.995 0 0 0 4.333 3H2v2h2.334l4.743 11.385c.155.372.52.615.923.615h8c.417 0 .79-.259.937-.648l3-8A1.003 1.003 0 0 0 21 7zm-4 6h-2v2h-2v-2h-2v-2h2V9h2v2h2v2z"></path></svg>
                </button>
                <button onclick="addToWishlist('{product['id']}', '{product['price']}', '{product['image']}')">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" style="fill:white;margin-right:5px;"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg>
                </button>
            </div>
            """ for product in filtered_products
        )

        return f"""
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Product Page</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }}
                .header {{
                    width: 100%;
                    background-color: #333;
                    color: white;
                    padding: 20px 0;
                    text-align: center;
                    font-size: 42px;
                    font-family: sans-serif;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    margin-bottom: 30px;
                }}
                .container {{ display: flex; }}
                .filters {{ width: 20%; padding: 20px; background: #fff; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }}
                .products {{ width: 70%; display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 20px; padding: 20px; }}
                .product {{ background: white; padding: 30px; border: 1px solid #ccc; border-radius: 8px;  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }}
                .product img {{ width: 100%; border-bottom: 1px solid #ccc; margin-bottom: 10px; }}
                .filters h3 {{ margin-bottom: 10px; }}
                .filter-group {{ margin-bottom: 20px; }}
                .filter-group label {{ display: block; margin-bottom: 5px; font-size: 20px; font-family: sans-serif; font-weight: bold; }}
                .filter-group input, .filter-group select {{ width: 100%; padding: 5px; font-size: 16px; margin-bottom: 10px; }}
                .filter-group input[type='range'] {{ width: 100%; }}
                button {{ padding: 10px; background: #333; color: white; font-size: 18px; border: none; border-radius: 5px; cursor: pointer;}}
                button:hover {{ background: #555; }}
                .back-home {{ text-align: center; text-decoration: none; font-size:25px; color: #333; margin-top: 20px; }}
                .back-home a{{text-decoration: none; color: #333;}}
                .back-home:hover{{text-decoration: underline;}}
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
            <script>
                function addToCart(productId) {{
                    alert('Added to Cart: ' + productId);
                }}
                function addToCart(productName, price, category, imageURL) {{
                    alert(productName + " has been added to your cart!");
                    window.location.href = "/cart/add?item=" + encodeURIComponent(productName) +
                          "&price=" + encodeURIComponent(price) +
                          "&category=" + encodeURIComponent(category) +
                          "&imageURL=" + encodeURIComponent(imageURL);
                }}
                function addToWishlist(productId) {{
                    alert('Added to Wishlist: ' + productId);
                }}
                function addToWishlist(name, price, imageUrl) {{
                    window.location.href = "/wishlist/add?item=" + encodeURIComponent(name) + "&price=" + encodeURIComponent(price)+
                    "&imageUrl=" + encodeURIComponent(imageUrl);
                }}
            </script>
        </head>
        <body>
         <div class="header">Products</div>
            <div class='container'>
                <div class='filters'>
                    <form method='get' action='/products'>
                        <div class='filter-group'>
                            <label for='category'>Category:</label>
                            <select name='category' id='category'>
                                <option value=''>All</option>
                                <option value='fitness-accessories'>Fitness Accessories</option>
                                <option value='gym-equipment'>Gym Equipment</option>
                                <option value='sports-wear'>Sports Wear</option>
                                <option value='sports-accessories'>Sports Accessories</option>
                                <option value='men'>Men</option>
                                <option value='women'>Women</option>
                                <option value='kids'>Kids</option>
                            </select>
                        </div>
                        <div class='filter-group'>
                            <label for='price_range'>Price:</label>
                            <select name='price_range' id='price_range'>
                                <option value=''>All</option>
                                <option value='0-1000'>Under ₹1000</option>
                                <option value='1000-2000'>₹1000 - ₹2000</option>
                                <option value='2000-5000'>₹2000 - ₹5000</option>
                                <option value='5000-10000'>₹5000 - ₹10000</option>
                                <option value='10000-30000'>₹10000 - ₹30000</option>
                            </select>
                        </div>
                        <div class='filter-group'>
                            <label for='min_rating'>Min Rating:⭐</label>
                            <input type='range' name='min_rating' id='min_rating' min='0' max='5' step='0.1'>
                        </div>
                        <button type='submit'>Apply filters</button>
                    </form>
                </div>
                <div class='products'>
                    {products_html if filtered_products else '<p>No products found matching the filters.</p>'}
                </div>
            </div>
            <div class="back-home">
             <a href="/">Back To Home</a>
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
            <p>Your Support Our Efforts</p>
            <p>&copy; 2024 SportsFit. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """


if __name__ == "__main__":
    cherrypy.quickstart(Products(), '/products')
