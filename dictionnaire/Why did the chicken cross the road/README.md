# Dossier pour les exercices sur les dictionnaires
## Définition
Un dictionnaire est une structure de données visant à stocker les valeurs en les associant à une clef. Ceci permet de récupérer les informations sans passer par les indices numériques.
  
## Opérations
- Set: La méthode pour ajouter un valeur en pair avec son clef. 
- Get: La méthode pour accéder à la valeur à partir de son clef.
- Delete: La méthode pour supprimer une valeur à partir de sa clef.
- Verify: La méthode pour vérifier si la clef est dans le doctionnaire.

## Avantages
- Accès par clef
- lisibilité du code
## Inconvénients
- consommation de mémoire
- Contrainte sur les clefs (Chaque clef doit être unique.)
- absence d'ordre

## Des exemples d'utilisation en sciences ou en informatique
- Gestion des bases de données (NoSQL) : Dans des systèmes comme MongoDB ou Redis, les données sont stockées sous forme de paires clé-valeur (ex: l'ID utilisateur est la clé, et l'objet contenant son nom, e-mail et préférences est la valeur).
- Systèmes de Cache : Pour accélérer l'affichage d'un site web, on stocke le résultat d'une requête lourde dans un dictionnaire. La clé est l'URL de la page, et la valeur est le contenu HTML déjà généré.
- Analyse de texte (NLP) : Pour compter la fréquence des mots dans un livre, on utilise un dictionnaire où chaque mot est une clé et le nombre d'apparitions est la valeur associée.
- Routage réseau : Les routeurs utilisent des tables de correspondance (dictionnaires) pour associer une adresse IP de destination (clé) à une interface de sortie spécifique (valeur).
