# app.py

import ast

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Left child (another Node)
        self.right = right  # Right child (another Node)
        self.value = value  # Holds condition for operand nodes (e.g. 'age > 30')

def create_rule(rule_string):
    parsed_rule = ast.parse(rule_string, mode='eval')
    
    def build_ast(node):
        if isinstance(node, ast.BoolOp):
            return Node(
                node_type="operator",
                left=build_ast(node.values[0]),
                right=build_ast(node.values[1]),
                value=type(node.op).__name__
            )
        elif isinstance(node, ast.Compare):
            left = node.left.id
            op = type(node.ops[0]).__name__
            right = node.comparators[0].n
            return Node(
                node_type="operand",
                value=f"{left} {op} {right}"
            )
    
    ast_root = build_ast(parsed_rule.body)
    return ast_root

def combine_rules(rules, operator="AND"):
    if not rules:
        return None
    
    root = rules[0]
    for rule in rules[1:]:
        root = Node(
            node_type="operator",
            left=root,
            right=rule,
            value=operator
        )
    return root

def evaluate_rule(ast_node, data):
    if ast_node.type == "operand":
        return eval(ast_node.value, {}, data)
    
    elif ast_node.type == "operator":
        left_val = evaluate_rule(ast_node.left, data)
        right_val = evaluate_rule(ast_node.right, data)
        
        if ast_node.value == "And":
            return left_val and right_val
        elif ast_node.value == "Or":
            return left_val or right_val
