
import csv
import json
import re
import hashlib
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

dossier = Path(__file__).resolve().parent
fichier_csv = dossier / "bureauengros_brut.csv"
fichier_json = dossier / "donnees.json"

def nettoyer_texte(valeur):
    texte = " ".join((valeur or "").split())
    return texte if texte else None

def nettoyer_prix(valeur):
    if not valeur:
        return None

    texte = valeur.replace("\u00a0", "").replace(" ", "")
    texte = texte.replace("$", "").replace(",", ".")
    texte = re.sub(r"[^\d.]", "", texte)

    try:
        return float(texte)
    except ValueError:
        return None

def nettoyer_url(valeur):
    if not valeur:
        return None

    parties = urlsplit(valeur.strip())
    return urlunsplit((
        parties.scheme,
        parties.netloc.lower(),
        parties.path.rstrip("/"),
        "",
        ""
    ))

produits = []
identifiants = set()
total_lignes = 0
doublons = 0
sans_url = 0

with open(fichier_csv, "r", encoding="utf-8-sig", newline="") as fichier:
    lecteur = csv.DictReader(fichier)

    for ligne in lecteur:
        total_lignes += 1
        url = nettoyer_url(ligne.get("lien_Produits"))

        if not url:
            sans_url += 1
            continue

        identifiant = "produit_" + hashlib.sha256(
            url.encode("utf-8")
        ).hexdigest()[:24]

        if identifiant in identifiants:
            doublons += 1
            continue

        identifiants.add(identifiant)

        modele = nettoyer_texte(ligne.get("modele_Produit"))
        if modele and modele.lower().startswith("modèle:"):
            modele = modele.split(":", 1)[1].strip() or None

        produit = {
            "_id": identifiant,
            "type": "produit",
            "nom": nettoyer_texte(ligne.get("description_Produit")),
            "modele": modele,
            "stockage": nettoyer_texte(ligne.get("capacite_stockage")),
            "processeur": nettoyer_texte(ligne.get("type_Processeur")),
            "prix": nettoyer_prix(ligne.get("prix")),
            "url_source": url,
            "image_url": nettoyer_texte(ligne.get("image"))
        }

        produits.append(produit)

with open(fichier_json, "w", encoding="utf-8") as fichier:
    json.dump(produits, fichier, ensure_ascii=False, indent=2)

print("Lignes du CSV :", total_lignes)
print("Doublons supprimés :", doublons)
print("Lignes sans URL :", sans_url)
print("Produits conservés :", len(produits))
print("Fichier créé :", fichier_json.name)

if len(produits) < 2500:
    print("ATTENTION : moins de 2500 produits distincts.")
