# 🔒 Enigma - Your Secret Keeper

Welcome to **Enigma**! 🧙‍♂️ The ultimate password manager that keeps your secrets safer than a dragon guarding its treasure! Whether you're juggling a dozen passwords like a circus performer or just want to keep your social media accounts secure, Enigma is here to save the day (and your passwords)!

## 🚀 Features That Make You Go "Wow!"
- **Add a New Password**: Store passwords for your favorite apps like a wizard hoarding gold coins! 🪙
- **Retrieve a Password**: Need to remember that elusive app login? Just summon it from Enigma!
- **Update a Password**: Change your passwords more often than your socks? Update them effortlessly! 🧦
- **Delete a Password**: No longer using that app? Wave goodbye and delete its password with a flick of your wrist!

## 💻 Technologies Used
- **Backend**: Built with **Flask** (Python) – because who doesn’t love a little Python magic? 🐍✨
- **Database**: **MySQL** – for all your password-storing needs. Think of it as your enchanted vault! 🔒
- **Frontend**: Just some basic **HTML** forms for interaction. Simplicity is key, but we’ll dress it up later!

## 📦 Installation Guide - Let’s Get This Party Started!

### Prerequisites
Before diving in, make sure you have the following:
- 🐍 Python 3.x
- 🗄️ MySQL Server
- 🛠️ MySQL Workbench (optional, but it makes life easier)
- 🔮 Flask
- 🧙‍♂️ MySQL Connector for Python

### Steps to Get Started

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/enigma-password-manager.git
    cd enigma-password-manager
    ```

2. **Set Up a Virtual Environment (because who doesn’t love a cozy space?)**:
    ```bash
    python -m venv venv
    # Activate it
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On Linux/Mac
    ```

3. **Install All the Magic**:
    ```bash
    pip install Flask mysql-connector-python
    ```

4. **Prepare the Database (Let’s channel our inner hacker)**:
    Open MySQL and run:
    ```sql
    CREATE DATABASE password_manager;
    USE password_manager;

    CREATE TABLE passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        app_name VARCHAR(100),
        username VARCHAR(100),
        password VARCHAR(255)
    );
    ```

5. **Connect Flask to MySQL**:
    Edit `app.py` and sprinkle in your database credentials like magic dust:
    ```python
    db = mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",        # Change this to your MySQL username
        password="your_mysql_password",     # Change this to your MySQL password
        database="password_manager"         # Ensure this matches the database you created
    )
    ```

6. **Launch the App Like a Boss**:
    ```bash
    python app.py
    ```

7. **Open Your Browser**:
   Type `http://127.0.0.1:5000` in the address bar and voilà, you're in! 🎉

## 🧙‍♂️ Enigma's Magic Commands
Here’s how you control this mighty app with a wave of your wand terminal:

### 🛠️ Saving a Password
- **Endpoint**: `/save-password`
- **Method**: POST
- **Body**:
    ```json
    {
        "app_name": "AppName",
        "username": "YourUsername",
        "password": "SuperSecretPassword"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Password saved! 🗝️"
    }
    ```

### 🔍 Fetching a Password
- **Endpoint**: `/get-password/<app_name>`
- **Method**: GET
- **Response**:
    ```json
    {
        "username": "YourUsername",
        "password": "SuperSecretPassword"
    }
    ```

### ✨ Updating a Password
- **Endpoint**: `/update-password`
- **Method**: PUT
- **Body**:
    ```json
    {
        "app_name": "NewAppName",
        "username": "NewUsername",
        "password": "NewSuperSecretPassword"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Password updated successfully! 🔄"
    }
    ```

### 🗑️ Deleting a Password
- **Endpoint**: `/delete-password/<app_name>`
- **Method**: DELETE
- **Response**:
    ```json
    {
        "message": "Password deleted! 🗑️"
    }
    ```

## 🌟 Future Superpowers (aka Features)
We’re not done yet! Enigma has a bright future ahead:
- **Encryption**: Lock your passwords down even tighter. 🛡️
- **User Authentication**: Because passwords should be extra safe!
- **Improved UI**: Making it even prettier to look at. 🎨

## 📄 License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as you like!

## 💬 Let's Chat!
Found a bug? Got a feature idea? Or just want to say "Hi!"? Feel free to open an issue or drop us a message. Your feedback is the magic potion that helps us grow! 🌱

For any updates or changes to the code, please contact me at:
- **Email**: [your-email@example.com](mailto:your-email@example.com)

Now go forth and secure your digital life with Enigma! 🚀🔐
