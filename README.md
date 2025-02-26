# Educational Ransomware Simulation

## Overview
This project is an **Educational Ransomware Simulation**, designed to demonstrate file encryption and decryption techniques using Python's `cryptography` library. It provides insights into cybersecurity threats and defensive measures.

## Features
- Encrypts files using the **Fernet symmetric encryption algorithm**.
- Decrypts files with a valid key.
- Simple web-based interface using **Flask**.
- Demonstrates the risks and security implications of ransomware.

## Technologies Used
- **Python** (Flask, cryptography)
- **HTML, CSS, JavaScript** (for the front-end)
- **SQLite** (if needed for user data storage)

## Setup Instructions

### Prerequisites
Make sure you have **Python 3** installed. You can install dependencies using:

```sh
pip install -r requirements.txt
```

### Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/educational-ransomware-simulation.git
   cd educational-ransomware-simulation
   ```
2. Generate a key for encryption:
   ```sh
   python generate_key.py
   ```
3. Start the Flask server:
   ```sh
   python educational_ransomware.py
   ```
4. Open your web browser and visit:  
   `http://127.0.0.1:5000/`

## Usage
- Upload files to be encrypted.
- Decrypt files using the correct key.
- Understand how ransomware affects systems and learn about preventive measures.

## Disclaimer
This project is **strictly for educational purposes**. Do not use it for malicious activities. The author holds no responsibility for any misuse.

## License
This project is licensed under the **MIT License**. See the full license below.

---


