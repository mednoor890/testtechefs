# Processus de Suivi de l'Accrochage Technique des Plateformes

Ce projet vise à mettre en place un processus métier permettant de suivre l'avancement de l'accrochage technique de plusieurs plateformes. Le processus est composé de 23 étapes, réparties en 4 statuts principaux avec des sous-statuts pour certains. Chaque statut ou sous-statut est défini par une règle de gestion spécifique.

## Méthodologie Utilisée

1. **Définition des Étapes et des Statuts :** Définition des 23 étapes du processus et des 4 statuts principaux, avec identification des sous-statuts nécessaires.

2. **Modélisation des Règles de Gestion :** Traduction des règles de gestion métier pour chaque statut et sous-statut en expressions logiques compréhensibles par Python, enregistrées dans la table "Regles".

3. **Génération des Combinaisons :** Écriture d'un code Python pour générer toutes les combinaisons possibles des 23 étapes, enregistrées dans la table "Combinaisons".

4. **Vérification des Correspondances :** Développement d'un code Python pour vérifier chaque combinaison par rapport à chaque règle de gestion. Les correspondances sont enregistrées dans la table "correspondance_combinaison_regle".

5. **Déploiement sur un Dépôt Git :** Dépôt de tous les scripts Python et SQL sur un dépôt Git public pour la gestion de version et la collaboration.

## Résultats Obtenu

- Génération et enregistrement de toutes les combinaisons possibles.
- Traduction et enregistrement des règles de gestion en expressions logiques Python.
- Vérification des correspondances entre les combinaisons et les règles, enregistrées dans la table "correspondance_combinaison_regle".

## Conclusion

Le processus de suivi de l'accrochage technique des plateformes a été mis en place avec succès. Les règles de gestion métier ont été intégrées dans un système automatisé permettant de valider les différentes étapes du processus, offrant une traçabilité complète et facilitant le suivi de l'avancement des accrochages techniques.

## Questions Optionelles
### Identifier les combinaisons qui ne sont pas dans un statut ou sous-statut

```sql
SELECT c.*
FROM Combinaisons c
LEFT JOIN correspondance_combinaison_regle ccr ON c.ID = ccr.CombinaisonID
WHERE ccr.ID IS NULL;
```
### Identifier les combinaisons qui sont dans plusieurs statuts ou sous-statuts

```sql
SELECT CombinaisonID
FROM correspondance_combinaison_regle
GROUP BY CombinaisonID
HAVING COUNT(DISTINCT RegleID) > 1;
```

### Identifier s'il y a une correspondance exacte entre les combinaisons d'un statut et de l'ensemble de ses sous-statuts

```sql
SELECT ccr.CombinaisonID
FROM correspondance_combinaison_regle ccr
JOIN Regles r ON ccr.RegleID = r.ID
GROUP BY ccr.CombinaisonID
HAVING COUNT(DISTINCT r.StatutSousStatut) = (SELECT COUNT(DISTINCT StatutSousStatut) FROM Regles WHERE Statut = r.Statut);
```

---