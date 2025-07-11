from flask import Flask, request, render_template

app = Flask(__name__)
contacts = {}

@app.route('/')
def home():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    contacts[name] = phone
    return render_template('index.html', contacts=contacts, message=f"{name} added!")

@app.route('/delete/<name>')
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return render_template('index.html', contacts=contacts, message=f"{name} deleted!")
    return render_template('index.html', contacts=contacts, message="Name not found.")

# --- NEW HEALTH CHECK ENDPOINT ---
@app.route('/health')
def health_check():
    """
    Simple health check endpoint for monitoring purposes.
    Returns a 200 OK status if the application is running.
    """
    return "OK", 200 # Returns "OK" with a 200 HTTP status code

if __name__ == '__main__':
    # When deploying with Gunicorn (as typically done on Railway),
    # Gunicorn handles the host and port.
    # For local development or Docker outside Gunicorn, these are useful.
    app.run(debug=True, host='0.0.0.0', port=5000) # Explicitly set port for clarity