from flask import Flask, request, render_template

app = Flask(__name__) # Corrected: __name__
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

if __name__ == '__main__': # Corrected: __name__ and __main__
    app.run(debug=True, host='0.0.0.0') # Added host='0.0.0.0' for Docker compatibility