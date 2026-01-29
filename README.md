# TP WordPress - Pipeline Dédié

Cette branche contient la version finalisée du TP WordPress . La structure a été simplifiée pour que le `docker-compose.yml` soit à la racine du projet.

## Modifications de Structure
Contrairement à la branche `main`, les fichiers de configuration sont situés à la racine pour faciliter l'exécution directe des commandes Docker.


## CI/CD spécifique
Le workflow sur cette branche (`.github/workflows/wordpress-ci-cd.yml`) a été modifié pour :
* **Trigger** : S'activer sur la branche `wordpress-only`.
