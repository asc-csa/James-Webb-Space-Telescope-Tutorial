<p align="center">
 <img src="https://www.asc-csa.gc.ca/images/recherche/tiles/16f69078-962d-443c-874c-e4003fe173c8.jpg" height="300">
 <br> Crédit d'image | Image credit: <a href="https://www.asc-csa.gc.ca/eng/multimedia/search/image/17461">ASC-CSA</a>
</p>

<p align="center">
 <a href="#stars">
  <img alt="Étoiles sur GitHub | GitHub Repo stars" src="https://img.shields.io/github/stars/asc-csa/James-Webb-Space-Telescope-Tutorial">
 </a>
 <a href="#watchers">
  <img alt="Spectateurs sur Github | GitHub watchers" src="https://img.shields.io/github/watchers/asc-csa/James-Webb-Space-Telescope-Tutorial">
 </a>
 <a href="https://github.com/asc-csa/James-Webb-Space-Telescope-Tutorial/commits/main">
  <img alt="Dernier commit sur GitHub | GitHub last commit" src="https://img.shields.io/github/last-commit/asc-csa/James-Webb-Space-Telescope-Tutorial">
 </a>
 <a href="https://github.com/asc-csa/James-Webb-Space-Telescope-Tutorial/graphs/contributors">
  <img alt="Contributeurs sur GitHub | GitHub contributors" src="https://img.shields.io/github/contributors/asc-csa/James-Webb-Space-Telescope-Tutorial">
 </a>
 <a href="https://twitter.com/intent/follow?screen_name=csa_asc">
  <img alt="Suivre sur Twitter | Twitter Follow" src="https://img.shields.io/twitter/follow/csa_asc?style=social">
 </a>
</p>

---

<h3 align="center">
  <a href="#titre-du-projet">Français</a> |
  <a href="#project-title">English (follows)</a>
</h3>

---

<a id="titre-du-projet"></a>
# Extraction et analyse des images du télescope spatial James Webb - Un tutoriel

> **Description brève :**
> Ce tutoriel permet d'accéder aux données JWST, de les extraire et de compter le nombre de galaxies à partir des images.

## À propos

**Extraction et analyse des images du télescope spatial James Webb - Un tutoriel** est un tutoriel qui permet d'accéder aux données JWST, de les extraire et de compter le nombre de galaxies à partir des images. Il couvre :

- Accès et téléchargement de données JWST depuis les archives officielles
- Extraction et manipulation de fichiers FITS astronomiques
- Traitement d'images pour l'identification d'objets célestes
- Algorithmes de détection et comptage automatique de galaxies

L'objectif principal de ce tutoriel est de faire connaître les données du télescope spatial James Webb (JWST) et d'améliorer son accessibilité. Ce tutoriel doit permettre aux utilisateurs d'accéder aux données JWST et de les extraire. Pour illustrer les applications potentielles de ces données, ce tutoriel guide les utilisateurs dans le comptage du nombre de galaxies à partir des images JWST.

*Ce tutoriel est strictement expérimental et les étapes de traitement sont fournies pour démontrer comment manipuler les données en Python.*

## Prérequis

- Python 3.8 ou plus récent
- Jupyter Notebook ou Jupyter Lab
- Bibliothèques Python : astropy, numpy, matplotlib, scipy
- Connexion Internet (pour le téléchargement des données JWST)
- Espace de stockage suffisant pour les fichiers FITS

## Démarrage rapide

1. 📦 **Cloner le dépôt**
   ```bash
   git clone https://github.com/asc-csa/James-Webb-Space-Telescope-Tutorial.git
   cd James-Webb-Space-Telescope-Tutorial
   ```
2. 🐍 **Créer un environnement**
   ```bash
   # Avec virtualenv
   python -m venv env
   source env/bin/activate

   # Ou avec conda
   conda create -n jwst_env python=3.8
   conda activate jwst_env
   ```
3. 📥 **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
4. 🚀 **Lancer le tutoriel**
   ```bash
   jupyter notebook JWST_Jupyter_Tutorial.ipynb
   ```

> **Remarque :** Ce tutoriel repose sur le téléchargement de données JWST qui peuvent être volumineuses. Assurez-vous d'avoir une connexion Internet stable.

## Astuces & Conseils

- **Données JWST :** Les fichiers FITS peuvent être très volumineux (plusieurs GB), planifiez votre espace de stockage
- **Performance :** Le filtrage d'images peut être intensif, utilisez un ordinateur avec suffisamment de RAM
- **Algorithme de détection :** Le filtre expérimental peut être ajusté pour modifier le seuil de luminosité
- **Visualisation :** Les résultats sont sauvegardés comme images PNG pour faciliter le partage

### Comportement attendu
JWST_Jupyter_Tutorial.ipynb guidera l'utilisateur sur les étapes de téléchargement et d'extraction des données JWST. Le tutoriel montrera comment ouvrir les données et les enregistrer en tant qu'image pour d'autres utilisations. La dernière étape consiste à créer un filtre qui examine tous les points lumineux de l'image et présente à l'utilisateur une estimation du nombre de galaxies.

## Licence

Ce projet est sous une licence MIT modifiée – voir le fichier [LICENSE](https://github.com/asc-csa/James-Webb-Space-Telescope-Tutorial/blob/main/LICENSE.txt) pour plus de détails.

---

<h3 align="center">
  <a href="#project-title">English </a> |
  <a href="#titre-du-projet">Français (précède)</a>
</h3>

---

<a id="project-title"></a>
# Extracting and analysis of the James Webb Space Telescope images - A tutorial

> **Brief description:**
> This tutorial enables access to JWST data, extraction, and counting the number of galaxies from the images.

## About

**Extracting and analysis of the James Webb Space Telescope images - A tutorial** is a tutorial that enables access to JWST data, extraction, and counting the number of galaxies from the images. It covers:

- Accessing and downloading JWST data from official archives
- Extracting and manipulating astronomical FITS files
- Image processing for celestial object identification
- Automated galaxy detection and counting algorithms

The primary aim of this tutorial is to raise awareness about the James Webb Space Telescope (JWST) data and enhance its accessibility. This tutorial shall equip the users to access and extract JWST data. To illustrate the potential applications of this data, this tutorial guides the users in counting the number of galaxies from the JWST images.

*Please note that this tutorial is purely experimental, and processing steps are supplied to demonstrate how to manipulate the data in Python.*

## Prerequisites

- Python 3.8 or newer
- Jupyter Notebook or Jupyter Lab
- Python libraries: astropy, numpy, matplotlib, scipy
- Internet connection (for JWST data download)
- Sufficient storage space for FITS files

## Quick Start

1. 📦 **Clone the repo**
   ```bash
   git clone https://github.com/asc-csa/James-Webb-Space-Telescope-Tutorial.git
   cd James-Webb-Space-Telescope-Tutorial
   ```
2. 🐍 **Create environment**
   ```bash
   # Using virtualenv
   python -m venv env
   source env/bin/activate

   # Or using conda
   conda create -n jwst_env python=3.8
   conda activate jwst_env
   ```
3. 📥 **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. 🚀 **Run the tutorial**
   ```bash
   jupyter notebook JWST_Jupyter_Tutorial.ipynb
   ```

> **Note:** This tutorial relies on downloading JWST data which can be large. Ensure you have a stable internet connection.

## Tips & Tricks

- **JWST Data:** FITS files can be very large (several GB), plan your storage space
- **Performance:** Image filtering can be intensive, use a computer with sufficient RAM
- **Detection Algorithm:** The experimental filter can be adjusted to modify brightness threshold
- **Visualization:** Results are saved as PNG images for easy sharing

### Expected Behavior
JWST_Jupyter_Tutorial.ipynb will guide the user on the steps to downloading and extracting the JWST data. The tutorial will demonstrate how to open the data and save it as an image for further uses. The last step involves creating a filter that looks at all the brightspots in the image and presents the user with an estimate of the number of galaxies.

## License

This project is licensed under a modified MIT license - see the [LICENSE](https://github.com/asc-csa/James-Webb-Space-Telescope-Tutorial/blob/main/LICENSE.txt) file for details.
