# Test technique - Trustia

## 📌 Description

Mon dépôt contient les solutions aux deux exercices du test technique.

L'objectif était de produire un code simple, structuré et facilement maintenable, en respectant les contraintes fournies.

---

## 🧩 Exercice 1 : Blocs de texte encadrés

### 🎯 Objectif
Afficher des blocs de texte encadrés dans la console.

### ⚙️ Fonctionnement
- Les données sont stockées dans un **dictionnaire centralisé**
- Chaque phrase possède :
  - un texte
  - un booléen `show` pour gérer son affichage
- Les phrases non affichées restent dans la structure de données
- L'ordre des blocs est modifiable directement dans le dictionnaire

### ✅ Contraintes respectées
- Texte affiché en minuscules
- Largeur maximale configurable (`MAX_WIDTH`)
- Bordures avec `-` et `|`
- Possibilité d’activer/désactiver une phrase sans modifier la logique

---

## 🍽️ Exercice 2 : Menu de restaurant

### 🎯 Objectif
Afficher un menu structuré par catégories dans la console.

### ⚙️ Fonctionnement
- Utilisation d’un dictionnaire contenant :
  - des catégories (entrées, plats, desserts)
  - une liste de plats par catégorie
- Chaque plat contient :
  - un nom
  - un prix
  - un booléen `available`

### ✅ Contraintes respectées
- Affichage par catégories
- Filtrage des plats non disponibles
- Noms en minuscules
- Prix affichés avec "€"

---

## 🧠 Choix techniques

- Structure de données simple et centralisée
- Séparation claire entre données et logique
- Code lisible et facilement modifiable

---

## 🚀 Lancement

On doit d'abord s'assurez d’avoir Python installé, puis exécutez :

```bash
python exercice1.py
python exercice2.py
