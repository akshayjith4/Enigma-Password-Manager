from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')  # Use an environment variable
db_password = os.environ.get('DB_PASSWORD', 'your_database_password_here')  # Change this to your actual database password

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd=db_password,
    database="database_name",
)
cursor = db.cursor()

# Create a table if it doesn't exist
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        app_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Route to render login.html
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'admin@enigma':  # Replace with DB validation in the future
        return redirect(url_for('options'))  
    else:
        return render_template('login.html', error="Invalid credentials, please try again.")

# Route to render options.html after login
@app.route('/options')
def options():
    return render_template('options.html')

# Route to render save.html for saving new passwords
@app.route('/save')
def save_password_page():
    return render_template('save.html')

# Route to handle the form submission for saving a new password
@app.route('/save-password', methods=['POST'])
def save_password():
    data = request.json
    app_name = data.get('app_name')
    username = data.get('username')
    password = data.get('password')  # Directly save the password
    notes = data.get('notes')

    try:
        cursor.execute(""" 
            INSERT INTO passwords (app_name, username, password, notes) 
            VALUES (%s, %s, %s, %s) 
        """, (app_name, username, password, notes))
        db.commit()
        return jsonify({'message': 'Password saved successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to render view.html for displaying saved passwords
@app.route('/view', methods=['GET'])
def view_passwords():
    cursor.execute("SELECT id, app_name, username, password FROM passwords")
    passwords = cursor.fetchall()

    formatted_passwords = []
    for password in passwords:
        formatted_passwords.append({
            'id': password[0],
            'app_name': password[1],
            'username': password[2],
            'password': password[3]
        })

    return render_template('view.html', passwords=formatted_passwords)

# Route to update a password
@app.route('/update-password/<int:id>', methods=['POST'])
def update_password(id):
    data = request.json
    app_name = data.get('app_name')
    username = data.get('username')
    password = data.get('password')
    notes = data.get('notes')

    try:
        cursor.execute("""
            UPDATE passwords SET app_name = %s, username = %s, password = %s, notes = %s WHERE id = %s
        """, (app_name, username, password, notes, id))
        db.commit()
        return jsonify({'message': 'Password updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a password
@app.route('/delete-password/<int:id>', methods=['DELETE'])
def delete_password(id):
    try:
        cursor.execute("DELETE FROM passwords WHERE id = %s", (id,))
        db.commit()
        return jsonify({'message': 'Password deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

