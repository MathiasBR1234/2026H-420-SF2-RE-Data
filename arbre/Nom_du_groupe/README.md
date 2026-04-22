# Arbres binaires de recherche
## Définition

Un arbre binaire est un arbre dans lequel chaque nœud a au plus deux enfants, appelés enfant gauche et enfant droit. Un arbre binaire de recherche (ABR) est un arbre binaire qui satisfait les propriétés suivantes :
1. Le sous-arbre gauche d'un nœud contient uniquement des nœuds avec des valeurs inférieures à la valeur du nœud.
2. Le sous-arbre droit d'un nœud contient uniquement des nœuds avec des valeurs supérieures à la valeur du nœud.

Ainsi, dans un ABR, les valeurs sont organisées de manière à faciliter la recherche puisque théoriquement, on peut ignorer la moitié des nœuds à chaque étape de la recherche.

## Opérations principales
1. add(node)
2. remove(node)
3. search(node)
4. print()
5. nb_noeuds()
6. hauteur()

## Aventages / Inconvénients
### Avantages
- Permet une recherche rapide.
- Les données sont toujours triées.
- Structure de données dynamique.
### Inconvénients
- Peut devenir déséquilibré, ce qui peut entraîner une dégradation des performances. Particulièrement lors de l'insertion de données triées. On peut créer une methode qui rééquilibre l'arbre pour éviter ce problème lors de la recherche, mais cela peut ralentir considérablement les opérations d'insertion et de suppression.
- Pas idéal pour accéder à des élément selon leur position dans l'arbre.

## Aplications
- Les ABR sont utilisés dans les bases de données pour stocker des données de manière efficace et permettre des recherches rapides.
- Systèmes de fichiers pour organiser les fichiers.
- Arbres de décisions utilisés par les intelligences artificielles.

## Sources
- chatGPT
- wikipédia
- université de Montréal
