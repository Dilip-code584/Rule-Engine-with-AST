class Node:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children if children is not None else []

    def to_dict(self):
        return {
            "node_type": self.node_type,
            "value": self.value,
            "children": [child.to_dict() for child in self.children]
        }

def parse_rule(rule_string):
    # A placeholder for your parsing logic to convert the rule_string into an AST
    # This should return a Node object representing the AST
    # For demonstration, let's create a simple AST
    # (In a real scenario, you'd replace this with your actual parsing logic)

    # Example: Simple parsing (you will replace this with your logic)
    if "AND" in rule_string:
        parts = rule_string.split(" AND ")
        children = [Node("condition", part.strip()) for part in parts]
        return Node("and", children=children)
    else:
        return Node("condition", rule_string.strip())

def create_rule(rule_string):
    root_node = parse_rule(rule_string)
    return root_node.to_dict()  # Convert to a dictionary for JSON serialization

def evaluate_rule(user_data, ast):
    # Implement your evaluation logic based on the AST and user_data
    # For demonstration, this is a placeholder implementation
    
    def evaluate_node(node):
        if node["node_type"] == "condition":
            # Example: condition evaluation
            left_side, operator, right_side = node["value"].partition(' ')
            if operator == '>':
                return user_data[left_side] > int(right_side)
            elif operator == '=':
                return user_data[left_side] == right_side.strip("'")
        elif node["node_type"] == "and":
            return all(evaluate_node(child) for child in node["children"])
        return True

    return evaluate_node(ast)

# Example usage
if __name__ == "__main__":
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    print("AST:", ast)

    user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(user_data, ast)
    print("Evaluation Result:", result)

