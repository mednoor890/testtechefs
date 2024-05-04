import itertools
from db_connection import get_connection

import mysql.connector

etapes = [
    "Prise de contact",
    "Organisation et animation de la réunion d'information",
    "Réception et validation du dossier d'inscription",
    "Initialisation des informations en PFPART",
    "Attribution JDD",
    "Organisation et animation de la réunion de lancement",
    "Ouverture médiacentre et abonnements auto",
    "Elaboration de la notice ScolomFR",
    "Mise en place Accès aux ressources",
    "Mise en place Gestion des abonnements",
    "Mise en place Adaptations spécifiques",
    "Lancement de la qualification de conformité [FR]",
    "Premiers retours sur la conformité [GA]",
    "Validation de la Déclaration de conformité [GA]",
    "Validation de la Qualification de conformité [GA]",
    "Vérification du contrat d'adhésion",
    "Mise en place du certificat WS de production",
    "Initialisation des informations PFPROD & création des comptes support GAR",
    "Mise en production (Notices, DCP portail GAR)",
    "Vérification de la validation de bout en bout",
    "Message de félicitations envoyé au FR",
    "Attribution de la marque GAR",
    "Vérification de la diffusion de la ressource",
    "Stop"
]

combinaisons = list(itertools.product([0, 1], repeat=len(etapes)))

# Connexion à la base de données MySQL
conn = get_connection()
cursor = conn.cursor()

# Créer la table "Combinaisons" si elle n'existe pas
cursor.execute('''CREATE TABLE IF NOT EXISTS Combinaisons (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    Etape VARCHAR(255),
                    Valeur INT
                )''')

# Insérer chaque combinaison dans la table "Combinaisons"
print("Génération en cours...")
for i, combinaison in enumerate(combinaisons):
    for j, etape in enumerate(etapes):
        cursor.execute('''INSERT INTO Combinaisons (Etape, Valeur) VALUES (%s, %s)''', (etape, combinaison[j]))
    conn.commit()

print("Le processus est terminé. Les possibilités sont stockées dans la base de données.")

# Fermer la connexion à la base de données
conn.close()