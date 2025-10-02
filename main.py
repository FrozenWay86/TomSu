import random

# --- Liste de mots jouable ---
mots_secrets = ["BANANE", "PYTHON", "ORANGE", "CERISE"]

# --- Vérifier un essai ---
def verifier_essai(mot_secret, essai):
    resultat = []
    mot_temp = list(mot_secret)

    # Première passe (lettres bien placées)
    for i in range(len(essai)):
        if essai[i] == mot_secret[i]:
            resultat.append("🟩")
            mot_temp[i] = None  # lettre déjà utilisée
        else:
            resultat.append(None)

    # Deuxième passe (lettres mal placées ou absentes)
    for i in range(len(essai)):
        if resultat[i] is None:
            if essai[i] in mot_temp:
                resultat[i] = "🟨"
                mot_temp[mot_temp.index(essai[i])] = None
            else:
                resultat[i] = "⬛"

    return "".join(resultat)

# --- Lancer une partie ---
def jouer_tomsu():
    mot_secret = random.choice(mots_secrets)
    tentatives = 6
    taille = len(mot_secret)

    print("🎉 Bienvenue dans Tomsu !")
    print(f"Mot de {taille} lettres à deviner. Vous avez {tentatives} essais.")
    print(f"Astuce : la première lettre est {mot_secret[0]}")

    for essai_num in range(1, tentatives + 1):
        essai = input(f"\nEssai {essai_num}/{tentatives} : ").upper()

        if len(essai) != taille:
            print(f"⚠️ Le mot doit faire {taille} lettres.")
            continue

        feedback = verifier_essai(mot_secret, essai)
        print(feedback)

        if essai == mot_secret:
            print(f"🎉 Bravo, trouvé en {essai_num} essais !")
            break
    else:
        print(f"❌ Perdu ! Le mot était : {mot_secret}")

# --- Exécution ---
if __name__ == "__main__":
    jouer_tomsu()
