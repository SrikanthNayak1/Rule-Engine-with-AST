# test_cases.py

from app import create_rule, combine_rules, evaluate_rule

def test_create_rule():
    rule = "age > 30 and department == 'Sales'"
    ast_tree = create_rule(rule)
    print("AST Tree Created:", ast_tree)

def test_combine_rules():
    rule1 = create_rule("age > 30 and department == 'Sales'")
    rule2 = create_rule("salary > 50000 or experience > 5")
    combined_rule = combine_rules([rule1, rule2], operator="OR")
    print("Combined AST:", combined_rule)

def test_evaluate_rule():
    rule1 = create_rule("age > 30 and department == 'Sales'")
    rule2 = create_rule("salary > 50000 or experience > 5")
    combined_rule = combine_rules([rule1, rule2], operator="OR")
    
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(combined_rule, data)
    print("Evaluation Result:", result)

if __name__ == "__main__":
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
