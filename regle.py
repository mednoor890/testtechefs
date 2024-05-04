from db_connection import get_connection

# Define the rules
regles = [
    ("En cours d'accrochage", None, "(Rien OR 1.1 OR 1.2 OR 1.1 AND 1.2) AND NOT 1.3 AND NOT 6.4"),
    ("En cours d'accrochage", "Initialisation du projet d'accrochage", "1.1 AND 1.2 AND 1.3 AND NOT 2.1 ... NOT 5.5 AND NOT 6.4"),
    ("En cours d'accrochage", "Accrochage technique", "1.1 AND 1.2 AND 1.3 AND 2.1 AND 2.2 AND NOT 5.5 AND NOT 6.4"),
    ("En cours d'accrochage", "Validation de conformité", "1.1 AND 1.2 AND 1.3 AND 2.1 AND 2.2 AND 3.1 AND 3.2 AND 3.3 AND 3.4 AND 3.5 AND NOT 5.5 AND NOT 6.4"),
    ("En cours d'accrochage", "Mise en production", "1.1 AND ... AND 4.4 AND NOT 5.1 ... NOT 5.5 AND NOT 6.4"),
    ("En production", None, "1.1 AND ... AND 3.5 AND 4.1 AND 4.2 AND 5.1 ... AND 5.5 AND NOT 6.4"),
    ("En production - OK", None, "1.1 AND ... AND 5.5 AND NOT 6.4"),
    ("En production - Adaptations spécifiques", None, "1.1 AND ... AND 3.5 AND NOT 3.6 AND 4.1 AND ... AND 5.5 AND NOT 6.4"),
    ("En production - Requalification CA", None, "1.1 AND ... AND 3.5 AND 4.1 AND 4.2 AND (NOT 4.3 OR NOT 4.4 OR (NOT 4.3 AND NOT 4.4)) AND 5.1 AND ... AND 5.5 AND NOT 6.4"),
    ("Accrochage stoppé", None, "6.4")
]

# Get a database connection
conn = get_connection()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Regles (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    Statut VARCHAR(255),
                    SousStatut VARCHAR(255),
                    Regle TEXT
                )''')

# Insert the rules into the "Regles" table
print("Inserting rules into the database...")
for regle in regles:
    cursor.execute('''INSERT INTO Regles (Statut, SousStatut, Regle) VALUES (%s, %s, %s)''', regle)
    print(f"Inserted rule: {regle[0]} - {regle[1]}")

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
print("Rule insertion completed.")
