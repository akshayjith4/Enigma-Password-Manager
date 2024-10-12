# 🦸‍♂️ Enigma – Your Personal Password Superhero! 

Ahoy, intrepid internet traveler! You've stumbled upon **Enigma**, the password manager that swoops in to save the day when your brain has turned into a scrambled mess of usernames and passwords.

No more scribbling down passwords on sticky notes or relying on your cat's name plus your birth year for every login! (Yes, we know. We've all been there.)

## 🎉 What Does Enigma Do?
- **Add New Passwords**: Easily store passwords for your apps, sites, or that secret portal to another dimension.
- **Retrieve Passwords**: Forgot your login? Enigma's got your back.
- **Update Passwords**: Change it up, keep things fresh.
- **Delete Passwords**: Done with an app? Poof! Password gone.

> Because who needs 20 different variations of “Password123”?

## 🛠️ Setting Up Enigma (It's Easy, We Swear!)
So, you're ready to make Enigma your own? Let's dive in!

### 🧰 Step 1: Prerequisites
You'll need the following sidekicks before embarking on this mission:
- **Python 3.x** (because who codes without Python?)
- **MySQL** (where your passwords chill and relax)
- **Flask** (the glue holding everything together)
- **MySQL Connector** (so Flask can talk to your database like old friends)

### 🦸‍♂️ Step 2: Installation (As Epic as It Sounds)

#### Set Up a Virtual Environment (optional, but come on, it’s best practice):
python -m venv venv

# Activate it
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
## Install All the Magic:
pip install Flask mysql-connector-python
Prepare the Database (Yes, we're going full hacker mode here):

## Open MySQL and run:
CREATE DATABASE password_manager;
USE password_manager;

CREATE TABLE passwords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    app_name VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(255)
);

## Connect Flask to MySQL:
Edit app.py and sprinkle in your database credentials:
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="password_manager"
)
## Launch the App Like a Boss:
python app.py

## Open Your Browser:
Type http://127.0.0.1:5000 in the address bar and voilà, you're in!

## 🧙‍♂️ Enigma's Magic Commands
Here’s how you control this mighty app with a wave of your wand terminal:

## 🛠️ Saving a Password
Endpoint: /save-password
Method: POST
Body:
{
    "app_name": "AppName",
    "username": "YourUsername",
    "password": "SuperSecretPassword"
}

Response:
{
    "message": "Password saved! 🗝️"
}

## 🔍 Fetching a Password
Endpoint: /get-password/<app_name>
Method: GET
Response:
json
Copy code
{
    "username": "YourUsername",
    "password": "SuperSecretPassword"
}
✨ Updating a Password
Endpoint: /update-password
Method: PUT
Body:
{
    "app_name": "NewAppName",
    "username": "NewUsername",
    "password": "NewSuperSecretPassword"
}
Response:
json
Copy code
{
    "message": "Password updated successfully! 🔄"
}
🗑️ Deleting a Password
Endpoint: /delete-password/<app_name>
Method: DELETE
Response:
{
    "message": "Password deleted! 🗑️"
}

## 🌟 Future Superpowers (aka Features)
We’re not done yet! Enigma has a bright future ahead:

Encryption: Lock your passwords down even tighter. 🛡️
User Authentication: Because passwords should be extra safe.
Improved UI: Making it even prettier to look at.
💬 Let's Chat!
Found a bug? Got a feature idea? Or just want to say "Hi!"? Feel free to open an issue or drop us a message.
