import cherrypy

class ContactPage:
    @cherrypy.expose
    def index(self):
        return """
            <html>
                <head>
                    <title>Contact Us</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 0;
                            padding: 0;
                            background-color: #f4f4f9;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            flex-direction: column;
                            height: 100vh;
                        }
                        .header {
                            width: 100%;
                            background-color: #333;
                            color: white;
                            padding: 34px 0;
                            text-align: center;
                            font-size: 46px;
                            font-weight: bold;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            margin-bottom: 30px;
                        }
                        .container {
                            display: flex;
                            flex-direction: row;
                            width: 90%;
                            max-width: 1200px;
                            background-color: white;
                            border-radius: 8px;
                            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                            overflow: hidden;
                            gap: 20px;
                        }
                        .image-container {
                            flex: 1;
                            background-image: url('https://login.decathlon.net/assets/side_picture-B36EUE8G.jpg'); /* Replace with your actual image URL */
                            background-size: cover;
                            background-position: center;
                        }
                        .form-container {
                            flex: 1;
                            padding: 30px;
                            box-sizing: border-box;
                            display: flex;
                            flex-direction: column;
                            justify-content: center;
                        }
                        h1 {
                            color: #ff9900;
                            margin-bottom: 10px;
                        }
                        h3 {
                            color: #555;
                            margin-bottom: 20px;
                        }
                        form {
                            display: flex;
                            flex-direction: column;
                        }
                        label {
                            margin-bottom: 5px;
                            font-weight: bold;
                            font-size: 14px;
                        }
                        input, textarea {
                            margin-bottom: 15px;
                            padding: 10px;
                            border: 1px solid #ccc;
                            border-radius: 4px;
                            font-size: 14px;
                        }
                        input[type="submit"] {
                            background-color: #ff9900;
                            color: white;
                            cursor: pointer;
                            border: none;
                            border-radius: 4px;
                            font-size: 16px;
                            padding: 10px;
                            transition: background-color 0.3s ease;
                        }
                        input[type="submit"]:hover {
                            background-color: #e68a00;
                        }
                        .form-container a {
                            display: block;
                            margin-top: 10px;
                            color: #0073e6;
                            text-decoration: none;
                            font-size: 14px;
                        }
                        .form-container a:hover {
                            text-decoration: underline;
                        }
                        p {
                            font-size: 14px;
                            color: #555;
                            margin-top: 20px;
                        }
                        .gap {
                            height: 30px;
                        }
                    </style>
                </head>
                <body>
                    <div class="header">Contact Us</div>
                    <div class="gap"></div>
                    <div class="container">
                        <div class="image-container"></div>
                        <div class="form-container">
                            <h1>SportsFit</h1>
                            <form method="post" action="/contact/submit">
                                <label for="name">Name:</label>
                                <input type="text" id="name" name="name" required>
                                
                                <label for="email">Email:</label>
                                <input type="email" id="email" name="email" required>
                                
                                <label for="message">Message:</label>
                                <textarea id="message" name="message" rows="4" required></textarea>
                                
                                <input type="submit" value="Submit">
                            </form>
                            <p>New to SportsFit? <a href="#">Create your SportsFit account</a></p>
                            <a href="/">Back to Home</a>
                        </div>
                    </div>
                </body>
            </html>
        """

    @cherrypy.expose
    def submit(self, name, email, message):
        return f"""
            <html>
                <head>
                    <title>Contact Submitted</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f9;
                            text-align: center;
                            padding: 50px;
                        }}
                        .container {{
                            background-color: white;
                            padding: 30px;
                            border-radius: 8px;
                            width: 400px;
                            margin: 0 auto;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        }}
                        h1 {{
                            color: #ff9900;
                        }}
                        .message p {{
                            font-size: 16px;
                            line-height: 1.6;
                        }}
                        .container a{{
                            display: block;
                            margin-top: 10px;
                            color: #0073e6;
                            text-decoration: none;
                            font-size: 14px;
                        }}
                        .container a:hover {{
                           text-decoration: underline;
                       }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Thank you for contacting us!</h1>
                        <div class="message">
                            <p><strong>Name:</strong> {name}</p>
                            <p><strong>Email:</strong> {email}</p>
                            <p><strong>Message:</strong> {message}</p>
                        </div>
                        <hr>
                        <p><a href="/">Continue Shopping</a></p>
                    </div>
                </body>
            </html>
            """
