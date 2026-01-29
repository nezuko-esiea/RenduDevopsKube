# Centralisation des TPs DevOps - Rendu Global

Ce dépôt regroupe l'ensemble des travaux pratiques réalisés. Le pipeline CI/CD sur cette branche est configuré pour gérer le déploiement multi-projets.

## Contenu du Dépôt
* **Python/** : Scripts et tests unitaires , Dockerfile et docker compose du TP python.
* **Wordpress/** : Configuration Docker Compose pour le déploiement WordPress.
* **.github/workflows/main.yml** : Workflow centralisé pour la génération des artefacts.

## ⚙️ CI/CD & Déploiement FTP
Le workflow `main.yml` s'exécute à chaque push sur cette branche :
1. **Conversion Kompose** : Transforme le `docker-compose.yml` en manifestes Kubernetes.
2. **Packaging** : Crée une archive ZIP nommée `BoudjemaDyhiaWordpress.zip` et une archive `BoudjemaDyhiaPython.zip` .
3. **Livraison** : Déploie automatiquement le rendu sur le serveur FTP de la professeure dans le dossier `RenduDevopsKube/`.

**Note :** Assurez-vous que les secrets `FTP_SERVER`, `FTP_USERNAME`, et `FTP_PASSWORD` sont configurés dans les paramètres du dépôt GitHub.
