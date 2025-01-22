import cherrypy
from hashlib import sha256
import json
import os

USER_DB_FILE = "user_db.json"

# Function to load the user database
def load_user_db():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save the user database
def save_user_db(user_db):
    with open(USER_DB_FILE, "w") as file:
        json.dump(user_db, file)

USER_DB = load_user_db()

class LoginPage:
    @cherrypy.expose
    def index(self, msg=""):
        username = cherrypy.session.get("username", None)
        user_display = f"<p>Welcome, {username} | <a href='/logout'>Logout</a></p>" if username else "<p><a href='/login'>Login</a></p>"
        
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home Page</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }}
                header {{
                    background-color: #333;
                    color: white;
                    padding: 10px;
                    text-align: right;
                }}
                .container {{
                    padding: 20px;
                    text-align: center;
                }}
                .error-msg {{
                    color: red;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <header>
                {user_display}
            </header>
            <div class="container">
                <h1>Welcome to the Website</h1>
                {"<p class='error-msg'>" + msg + "</p>" if msg else ""}
            </div>
        </body>
        </html>
        """

    @cherrypy.expose
    def login(self, username=None, password=None):
        global USER_DB
        if username and password:
            hashed_password = sha256(password.encode()).hexdigest()
            if username in USER_DB and USER_DB[username] == hashed_password:
                cherrypy.session["username"] = username
                return """
                <script>
                    alert('Login successful!');
                    window.location.href = '/';
                </script>
                """
            else:
                return self.index(msg="Invalid username or password.")
        return self.index()

    @cherrypy.expose
    def register(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Register</title>
        </head>
        <body>
            <div class="container">
                <h1>Register</h1>
                <form method="post" action="save_user">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" required><br><br>
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" required><br><br>
                    <button type="submit">Register</button>
                </form>
                <a href="/login">Back to Login</a>
            </div>
        </body>
        </html>
        """

    @cherrypy.expose
    def save_user(self, username, password):
        global USER_DB
        if username in USER_DB:
            return """
            <script>
                alert('Username already exists.');
                window.location.href = '/register';
            </script>
            """
        USER_DB[username] = sha256(password.encode()).hexdigest()
        save_user_db(USER_DB)
        return """
        <script>
            alert('Registration successful! Please log in.');
            window.location.href = '/login';
        </script>
        """

    @cherrypy.expose
    def logout(self):
        cherrypy.session.pop("username", None)
        return """
        <script>
            alert('You have been logged out.');
            window.location.href = '/';
        </script>
        """

if __name__ == "__main__":
    cherrypy.config.update({
        "tools.sessions.on": True,
        "tools.sessions.timeout": 60,  # Session expires after 60 minutes of inactivity
    })
    cherrypy.quickstart(LoginPage())
