import cherrypy

# In-memory dictionary to store users (username: password)
users = {"admin": "password"}  # Default admin account

class LoginPage:
    @cherrypy.expose
    def index(self, error_message=None):
        error_script = f"<script>alert('{error_message}');</script>" if error_message else ""
        return f"""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Login</title>
            <style>
                body {{
                    font-family: 'Roboto', sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f8f9fa;
                }}
                .container {{
                    display: flex;
                    width: 80%;
                    height: 70%;
                    background: white;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                }}
                .left {{
                    flex: 1;
                    background: url('https://i.pinimg.com/originals/92/58/c3/9258c3b6ea028e789f2c9420c28cab33.jpg') no-repeat center center/cover;
                }}
                .right {{
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    padding: 2rem;
                }}
                h3 {{
                    margin-bottom: 1rem;
                }}
                .form-group {{
                    margin-bottom: 1rem;
                    position: relative;
                }}
                .form-group label {{
                    display: block;
                    margin-bottom: 0.5rem;
                    font-weight: bold;
                }}
                .form-group input {{
                    width: 100%;
                    padding: 0.5rem;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }}
                .eye-icon {{
                    position: absolute;
                    top: 70%;
                    right: 10px;
                    transform: translateY(-50%);
                    cursor: pointer;
                    width: 20px;
                    height: 20px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 0.75rem 1.5rem;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    text-align: center;
                }}
                .btn:hover {{
                    background-color: #0056b3;
                    transform: scale(1.05);
                }}
                .link-container {{
                    text-align: center;
                    margin-top: 1rem;
                }}
                .link {{
                    color: #007bff;
                    text-decoration: none;
                }}
                .link:hover {{
                    text-decoration: underline;
                    transform: scale(1.05);
                }}
                .social-btn-container {{
                    margin-top: 1rem;
                    display: flex;
                    justify-content: center;
                    gap: 1rem;
                }}
                .social-btn {{
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-size: 20px;
                    cursor: pointer;
                    color: white;
                    text-decoration: none;
                }}
                .social-btn.facebook {{
                    
                }}
                .social-btn.insta {{
                    background-color: #1da1f2;
                }}
                .social-btn.google {{
                    background-color: #FAF9F6;
                }}
                 .social-btn:hover {{
                    transform: scale(1.1);
                }}
                .social-btn img {{
                    width: 25px;
                    height: 25px;
                }}
            </style>
        </head>
        <body>
            {error_script}
            <div class="container">
                <div class="left"></div>
                <div class="right">
                    <h3 style=" text-align: center;">Login to SportsFit</h3>
                    <form action="login" method="post">
                        <div class="form-group">
                            <label for="username">Username</label>
                            <input type="text" id="username" name="username" placeholder="Enter your username" required>
                        </div>
                        <div class="form-group">
                            <label for="password">Password</label>
                            <input type="password" id="password" name="password" placeholder="Enter your password" required>
                            <img src="https://cdn-icons-png.flaticon.com/512/709/709612.png" alt="Show Password" class="eye-icon" id="toggle-password" onclick="togglePassword('password', 'toggle-password')">
                        </div>
                        <div class="form-group">
                            <input type="submit" value="Login" class="btn">
                        </div>
                    </form>
                       <div class="link-container">
                        <a style= "text-decoration: none;" href="register" class="link">Create an Account</a>
                        <h4>Sign up using:</h4>
                         <div class="social-btn-container">
                            <div class="social-btn-container">
                                 <a href="https://www.facebook.com/login" target="_blank" class="social-btn facebook">
                                 <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" style="width: 40px; height: 40px;">
                                 </a>
                                 <a href="https://www.instagram.com/accounts/login/" target="_blank" class="social-btn instagram">
                                 <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width: 40px; height: 40px;">
                                 </a>
                                 <a href="https://accounts.google.com/signin" target="_blank" class="social-btn google">
                                 <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" style="width: 40px; height: 40px;">
                                 </a>
                             </div>
                        </div>
                    </div>
                </div>
            </div>
            <script>
                function togglePassword(fieldId, iconId) {{
                    const passwordField = document.getElementById(fieldId);
                    const eyeIcon = document.getElementById(iconId);
                    if (passwordField.type === "password") {{
                        passwordField.type = "text";
                        eyeIcon.src = "https://cdn-icons-png.flaticon.com/512/709/709612.png"; // Icon for "showing"
                    }} else {{
                        passwordField.type = "password";
                        eyeIcon.src = "https://cdn-icons-png.flaticon.com/512/709/709605.png"; // Icon for "hidden"
                    }}
                }}
            </script>
        </body>
        </html>
        """

  
    @cherrypy.expose
    def login(self, username, password):
        # Check if the username and password are valid
        if username in users and users[username] == password:
            raise cherrypy.HTTPRedirect("/")  # Redirect to the home page on success
        else:
            # Redirect to index with an error message on failure
            raise cherrypy.HTTPRedirect(f"/login?error_message=Invalid credentials. Please try again.")

    @cherrypy.expose
    def register(self, error_message=None):
        error_script = f"<script>alert('{error_message}');</script>" if error_message else ""
        return f"""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Register</title>
            <style>
                body {{
                    font-family: 'Roboto', sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f8f9fa;
                }}
                .register-container {{
                    width: 30%;
                    background: white;
                    padding: 2rem;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                    text-align: center;
                }}
                .form-group {{
                    margin-bottom: 1rem;
                }}
                .form-group label {{
                    display: block;
                    margin-bottom: 0.5rem;
                    font-weight: bold;
                }}
                .form-group input {{
                    width: 100%;
                    padding: 0.5rem;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 0.75rem 1.5rem;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    text-align: center;
                }}
                .btn:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            {error_script}
            <div class="register-container">
                <h3>Create an Account</h3>
                <form action="process_register" method="post">
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input type="text" id="username" name="username" placeholder="Enter a username" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" placeholder="Enter a password" required>
                    </div>
                    <div class="form-group">
                        <input type="submit" value="Register" class="btn">
                    </div>
                </form>
            </div>
        </body>
        </html>
        """

    @cherrypy.expose
    def process_register(self, username, password):
        # Check if the username is already taken
        if username in users:
            raise cherrypy.HTTPRedirect("/login?error_message=Username already exists. Please choose another.")
        # Add the new user to the dictionary
        users[username] = password
        raise cherrypy.HTTPRedirect("/login?error_message=Registration successful! Please log in.")

    @cherrypy.expose
    def home(self):
        return """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Home Page</title>
            <style>
                body {{
                    font-family: 'Roboto', sans-serif;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                    background-color: #f8f9fa;
                }}
                .container {{
                    margin-top: 10%;
                }}
                h1 {{
                    color: #007bff;
                }}
                .btn {{
                    display: inline-block;
                    padding: 0.75rem 1.5rem;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    text-align: center;
                    text-decoration: none;
                }}
                .btn:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Home Page!</h1>
                <p>Congratulations! You have successfully logged in.</p>
                <a href="/" class="btn">Logout</a>
            </div>
        </body>
        </html>
        """

   
if __name__ == "__main__":
    cherrypy.quickstart(LoginPage())
