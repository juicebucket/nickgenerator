from flask import Flask, render_template, request
import json
import random

generator = Flask(__name__)

with open('names.json', 'r') as f:
    names_data = json.load(f)

@generator.route('/')
def index():
    return render_template('index.html')

@generator.route('/generate', methods=['POST'])
def generate():
    gender = request.form['gender']
    nationality = request.form['nationality']

    first_names = names_data[gender][nationality]['first_names']
    last_names = names_data[gender][nationality]['last_names']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return render_template('index.html', nickname=f"{first_name}_{last_name}", gender=gender, nationality=nationality)

if __name__ == '__main__':
    generator.run(debug=True)
