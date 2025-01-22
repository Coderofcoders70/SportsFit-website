import cherrypy

class CheckoutPage:
    @cherrypy.expose
    def index(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SportsFit-Checkout Page</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: Arial, sans-serif;
                }

                body {
                    background-color: #f8f9fa;
                    padding: 20px;
                }

                header {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 10px 20px;
                    background-color: white;
                    box-shadow: 0px 1px 5px rgba(0, 0, 0, 0.1);
                }

                .logo {
                    font-size: 41px;
                    font-weight: bold;
                    color: orange;
                }

                .verified {
                    color: green;
                    font-size: 40px;
                }

                .container {
                    display: flex;
                    gap: 20px;
                    max-width: 1200px;
                    margin: 80px auto;
                }

                .section {
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }

                .address-section,
                .payment-section {
                    flex: 1;
                }

                #address-form {
                    margin: 40px;
                }

                .form-group {
                    margin-bottom: 15px;
                    font-size: 20px;
                }

                label {
                    display: block;
                    font-weight: bold;
                    margin-bottom: 5px;
                }

                input,
                select {
                    width: 100%;
                    padding: 8px;
                    font-size: 18px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }

                .btn {
                    background: #ff4081;
                    color: #fff;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    font-size: 16px;
                    cursor: pointer;
                    margin-top: 10px;
                }

                .btn:hover {
                    background: #e91e63;
                }

                .radio-group {
                    display: flex;
                    flex-direction: column;
                    gap: 7px;
                    margin: 20px;
                }

                .thank-you {
                    text-align: center;
                    padding: 20px;
                    margin-top: 20px;
                    background: #e8f5e9;
                    border: 1px solid #c8e6c9;
                    border-radius: 8px;
                    color: #388e3c;
                    font-size: 18px;
                    font-weight: bold;
                    display: none;
                }

                .address-summary {
                    background: #fff8e1;
                    padding: 15px;
                    border: 1px solid #ffe082;
                    border-radius: 8px;
                    color: #795548;
                    font-size: 16px;
                    margin-top: 20px;
                }
                .back-home { 
                    text-align: center; 
                    text-decoration: none; 
                    font-size:25px; 
                    color: #333; 
                    margin-top: 50px; 
                }
                .back-home a {
                    text-decoration: none; 
                    color: #333;
                }
                .back-home:hover {
                     text-decoration: underline;
                }
            </style>
        </head>
        <body>
        <header>
            <div class="logo">Sportsfit</div>
            <span class="verified"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="44" height="34" color="#008000" fill="none">
                <path d="M9 13C9 13 10 13 11 15C11 15 14.1765 10 17 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M21 11.1833V8.28029C21 6.64029 21 5.82028 20.5959 5.28529C20.1918 4.75029 19.2781 4.49056 17.4507 3.9711C16.2022 3.6162 15.1016 3.18863 14.2223 2.79829C13.0234 2.2661 12.424 2 12 2C11.576 2 10.9766 2.2661 9.77771 2.79829C8.89839 3.18863 7.79784 3.61619 6.54933 3.9711C4.72193 4.49056 3.80822 4.75029 3.40411 5.28529C3 5.82028 3 6.64029 3 8.28029V11.1833C3 16.8085 8.06277 20.1835 10.594 21.5194C11.2011 21.8398 11.5046 22 12 22C12.4954 22 12.7989 21.8398 13.406 21.5194C15.9372 20.1835 21 16.8085 21 11.1833Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
            </svg>100% Verified</span>
        </header>
        <div class="container">
            <div class="address-section section">
                <h2>Address Details</h2>
                <form id="address-form">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" placeholder="Enter your name">
                    </div>
                    <div class="form-group">
                        <label for="mobile">Mobile No.</label>
                        <input type="text" id="mobile" placeholder="Enter your mobile number">
                    </div>
                    <div class="form-group">
                        <label for="pincode">Pin Code</label>
                        <input type="text" id="pincode" placeholder="Enter your pin code">
                    </div>
                    <div class="form-group">
                        <label for="address">Address</label>
                        <input type="text" id="address" placeholder="Enter your address">
                    </div>
                    <div class="form-group">
                        <label for="city">City</label>
                        <select id="city">
                            <option value="">Select City</option>
                            <option value="Delhi">Delhi</option>
                            <option value="Mumbai">Mumbai</option>
                            <option value="Bangalore">Bangalore</option>
                            <option value="Kolkata">Kolkata</option>
                            <option value="Chennai">Chennai</option>
                            <option value="Ajmer">Ajmer</option>
                            <option value="Jaipur">Jaipur</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="state">State</label>
                        <select id="state">
                            <option value="">Select State</option>
                            <option value="Rajasthan">Rajasthan</option>
                            <option value="Maharashtra">Maharashtra</option>
                            <option value="Karnataka">Karnataka</option>
                            <option value="West Bengal">West Bengal</option>
                            <option value="Tamil Nadu">Tamil Nadu</option>
                        </select>
                    </div>
                    <button type="button" class="btn" id="save-address">Add Address</button>
                </form>
            </div>
            <div class="payment-section section">
                <h2>Payment Options</h2>
                <div class="radio-group">
                    <label><input type="radio" name="payment" value="upi"> Add UPI</label>
                    <label><input type="radio" name="payment" value="cod"> Cash on Delivery</label>
                </div>
                <button type="button" class="btn" id="proceed-to-pay">Proceed to Pay</button>
                <div class="thank-you" id="thank-you-message">
                    Thank you for shopping with us! Delivery will arrive soon.
                </div>
                <div class="address-summary" id="address-summary">
                    <p><strong>Saved Addresses:</strong></p>
                    <div id="saved-addresses"></div>
                </div>
            </div>
        </div>
        <script>
            document.getElementById("save-address").addEventListener("click", function() {
                const name = document.getElementById("name").value;
                const mobile = document.getElementById("mobile").value;
                const address = document.getElementById("address").value;
                const city = document.getElementById("city").value;
                const state = document.getElementById("state").value;

                if (!name || !mobile || !address || !city || !state) {
                    alert("Please fill all the address details.");
                    return;
                }

                const savedAddresses = document.getElementById("saved-addresses");
                const newAddress = document.createElement("div");
                newAddress.innerHTML = `
                    <p>Name: ${name}</p>
                    <p>Mobile: ${mobile}</p>
                    <p>Address: ${address}</p>
                    <p>City: ${city}</p>
                    <p>State: ${state}</p>
                    <hr>
                `;
                savedAddresses.appendChild(newAddress);

                document.getElementById("address-form").reset();
            });

            document.getElementById("proceed-to-pay").addEventListener("click", function() {
                const paymentMethod = document.querySelector('input[name="payment"]:checked');
                if (!paymentMethod) {
                    alert("Please select a payment method.");
                    return;
                }
                document.getElementById("thank-you-message").style.display = "block";
            });
        </script>
        <div class="back-home">
             <a href="/">Continue Shopping</a>
        </div>
        </body>
        </html>
        """
