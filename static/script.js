async function createRule() {
    const ruleInput = document.getElementById('ruleInput').value;

    try {
        const response = await fetch('/create_rule', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rule_string: ruleInput })
        });

        const result = await response.json();
        const resultElement = document.getElementById('result');

        if (response.ok) {
            resultElement.textContent = 'AST: ' + JSON.stringify(result.ast, null, 2);
        } else {
            resultElement.textContent = 'Error: ' + result.error;
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: ' + error.message;
    }
}

async function evaluateRule() {
    const jsonInput = document.getElementById('jsonInput').value;

    try {
        const userData = JSON.parse(jsonInput);
        const response = await fetch('/evaluate_rule', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_data: userData, ast: ast }) // Ensure AST is properly structured
        });

        const result = await response.json();
        const resultElement = document.getElementById('result');

        if (response.ok) {
            resultElement.textContent = 'Result: ' + JSON.stringify(result.result, null, 2);
        } else {
            resultElement.textContent = 'Error: ' + result.error;
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error parsing JSON: ' + error.message;
    }
}
