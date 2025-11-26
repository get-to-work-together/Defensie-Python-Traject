from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nep Printer Server ....'

all_data = [
    {'name': 'Printer ABC - 134.233.120.001', 'levels': [65, 40, 25, 72]},
    {'name': 'Printer 5 - 134.233.120.011', 'levels': [45, 40, 15, 72]},
    {'name': 'Printer AdBC - 134.233.120.201', 'levels': [85, 40, 25, 72]},
    {'name': 'Printer asssd - 134.233.120.031', 'levels': [75, 40, 25, 72]},
    {'name': 'Printer oiupo - 134.233.120.041', 'levels': [100, 100, 100, 100]},
    {'name': 'Printer dummy - 134.233.120.044', 'levels': [10, 10, 10, 10]},
]

@app.route('/api/v1/printers')
def api():
    return jsonify(all_data)


if __name__ == '__main__':
    app.run()