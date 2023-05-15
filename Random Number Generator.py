from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

excluded_chars = ['0', '5', 'O', 'Z']

def generate_random_alphanumeric(length):
    characters = [c for c in string.ascii_letters + string.digits if c not in excluded_chars]
    return ''.join(random.choices(characters, k=length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    number = int(request.form['number'])
    random_number = generate_random_alphanumeric(number)
    return render_template('Results.html', number=random_number)

if __name__ == '__main__':
    app.run(debug=True)


