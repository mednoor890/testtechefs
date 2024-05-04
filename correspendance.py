from db_connection import get_connection

def construct_expression(rule):
    if rule is None:
        return None

    # Define a mapping for logical operators
    operators_mapping = {
        'AND': 'and',
        'OR': 'or',
        'NOT': 'not'
    }
    
    # Split the rule into tokens
    tokens = rule.split()
    
    # Replace operators with Python equivalents
    for i, token in enumerate(tokens):
        if token.upper() in operators_mapping:
            tokens[i] = operators_mapping[token.upper()]
    
    # Join the tokens to form a Python expression
    expression = ' '.join(tokens)
    
    return expression





# Get a database connection
conn = get_connection()
cursor = conn.cursor()

# Get all rules from the "Regles" table
cursor.execute("SELECT * FROM Regles")
rules = cursor.fetchall()

# Get all combinations from the "Combinaisons" table
cursor.execute("SELECT * FROM Combinaisons")
combinations = cursor.fetchall()

# Create the "correspondance_combinaison_regle" table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS correspondance_combinaison_regle (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    CombinaisonID INT,
                    RegleID INT
                )''')

# Check each combination against each rule
print("Checking combinations against rules...")
for combinaison in combinations:
    for rule in rules:
        expression = construct_expression(rule[2])
        if expression is not None:
            try:
                if eval(expression, {}, combinaison[1]):
                    cursor.execute('''INSERT INTO correspondance_combinaison_regle (CombinaisonID, RegleID) VALUES (%s, %s)''', (combinaison[0], rule[0]))
            except SyntaxError:
                print(f"Invalid expression: {expression}")
                continue

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
print("Correspondence check completed.")
