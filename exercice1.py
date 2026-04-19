blocks = {
    "bloc1": [
        {"text": "Le code propre facilite la maintenance", "show": True}
    ],
    "bloc2": [
        {"text": "Tester souvent évite beaucoup d erreurs", "show": True},
        {"text": "Cette phrase ne doit pas s afficher", "show": False}
    ],
    "bloc3": [
        {"text": "Cette phrase ne doit pas s afficher", "show": False},
        {"text": "Un bon code doit rester simple et clair", "show": False},
        {"text": "La simplicité améliore la qualité du code", "show": True},
        {"text": "Refactoriser améliore la compréhension", "show": True}
    ]
}

# phrases_interdites = [
#     "Cette phrase ne doit pas s afficher",
#     "Un bon code doit rester simple et claire"
# ]

LARGEUR_MAX = 90

def print_block(lines):
    # On filtre uniquement les phrases à afficher
    visible_lines = [line["text"].lower() for line in lines if line["show"]]

    # Si aucune ligne à afficher, on ne fait rien
    if not visible_lines:
        return

    largeur_texte = LARGEUR_MAX - 2
    print("-" * LARGEUR_MAX)

    for ligne in visible_lines:
        print("|" + ligne.rjust(largeur_texte) + "|")

    print("-" * LARGEUR_MAX)

ordre_affichage = ["bloc1", "bloc2", "bloc3"]

if __name__ == "__main__":
    for bloc in ordre_affichage:
        print_block(blocks[bloc])