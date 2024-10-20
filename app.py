from flask import Flask, request, jsonify, render_template  # Ensure this is included
from rule_engine import create_rule, evaluate_rule  # Ensure this is correctly imported from your rule_engine module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template

@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    data = request.get_json()
    
    if not data or 'rule_string' not in data:
        return jsonify({'error': 'Invalid input. Please provide a rule_string.'}), 400

    try:
        ast = create_rule(data['rule_string'])
        return jsonify({'ast': ast}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    data = request.get_json()

    if not data or 'user_data' not in data or 'ast' not in data:
        return jsonify({'error': 'Invalid input. Please provide user_data and ast.'}), 400

    user_data = data['user_data']
    ast = data['ast']

    try:
        result = evaluate_rule(user_data, ast)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

