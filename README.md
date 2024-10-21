# Rule Engine with AST

## Overview

This is a simple 3-tier **Rule Engine** application that determines user eligibility based on attributes like age, department, income, spend, etc. The system uses **Abstract Syntax Tree (AST)** to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features

- **Dynamic Rule Creation**: Create rules using the `create_rule` function.
- **Combine Rules**: Combine multiple rules using the `combine_rules` function.
- **Evaluate Rules**: Evaluate user data against the rule AST with the `evaluate_rule` function.
- **AST Representation**: Use Abstract Syntax Trees to represent and process rules.

## Data Structure

Each rule is represented as a tree structure (AST) with nodes that could be either:
- **Operator nodes**: Representing logical operations (e.g., `AND`, `OR`).
- **Operand nodes**: Representing conditions or comparisons (e.g., `age > 30`).

## API Functions

1. **create_rule(rule_string)**: 
   - Takes a string rule and returns the corresponding AST.
   - Example: `rule_string = "age > 30 and department == 'Sales'"`

2. **combine_rules(rules, operator="AND")**: 
   - Takes a list of rules and combines them using an operator (`AND`, `OR`).
   
3. **evaluate_rule(ast_node, data)**: 
   - Evaluates a combined rule's AST against user data. 
   - Example: `data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}`

## How to Run

### Prerequisites

- Python 3.x installed
- A virtual environment (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rule-engine-ast.git
