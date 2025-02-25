from flask import Flask, render_template, request, flash, redirect, url_for
import os
from cryptography.fernet import Fernet, InvalidToken

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Change to a fixed secret key in production

def load_key():
    """Load the encryption key from key.key if it exists."""
    if os.path.exists("key.key"):
        return open("key.key", "rb").read()
    return None

def generate_key():
    """Generate and save an encryption key."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return "🔑 Key generated and saved to 'key.key'."

def encrypt_file(file_path, key):
    """Encrypt a file and delete the original."""
    if not os.path.isfile(file_path):
        return f"❌ File not found: {file_path}"

    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    encrypted_file_path = f"{file_path}.encrypted"

    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)
    
    os.remove(file_path)  # Delete original file
    return f"🔒 File encrypted: {encrypted_file_path}"

def decrypt_file(file_path, key):
    """Decrypt a file and delete the encrypted version."""
    if not os.path.isfile(file_path):
        return f"❌ File not found: {file_path}"

    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        return "❌ Invalid decryption key. Please check your key file."

    decrypted_file_path = file_path.replace(".encrypted", "") if file_path.endswith(".encrypted") else file_path

    with open(decrypted_file_path, "wb") as file:
        file.write(decrypted_data)

    os.remove(file_path)  # Delete encrypted file
    return f"🔓 File decrypted: {decrypted_file_path}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key', methods=['POST'])
def generate_key_route():
    message = generate_key()
    flash(message)
    return redirect(url_for('index'))

@app.route('/encrypt', methods=['POST'])
def encrypt_file_route():
    file_path = request.form.get('file_path')
    key = load_key()

    if not key:
        flash("❌ Key not found. Please generate a key first.")
        return redirect(url_for('index'))
    
    message = encrypt_file(file_path, key)
    flash(message)
    return redirect(url_for('index'))

@app.route('/decrypt', methods=['POST'])
def decrypt_file_route():
    file_path = request.form.get('file_path')
    key = load_key()

    if not key:
        flash("❌ Key not found. Please generate a key first.")
        return redirect(url_for('index'))
    
    message = decrypt_file(file_path, key)
    flash(message)
    return redirect(url_for('index'))

# New Routes for Additional Pages
@app.route('/terms')
def terms_of_service():
    return render_template('terms_of_service.html')

@app.route('/privacy')
def privacy_notice():
    return render_template('privacy_notice.html')

@app.route('/data-sharing')
def data_sharing():
    return render_template('data_sharing.html')

if __name__ == '__main__':
    app.run(debug=True)
