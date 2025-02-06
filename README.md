# Projet : Quiz pour 2AC

## Description
Ce projet est une application de quiz interactive conçue pour les élèves de 2e année collège. Il contient deux quiz distincts :
- Un quiz sur le langage de programmation Logo
- Un quiz sur les réseaux informatiques

L'application est développée en Python en utilisant Tkinter pour l'interface graphique et ReportLab pour générer un fichier PDF contenant les résultats des étudiants.

## 🎯 Objectif
Ce projet permet aux élèves de tester leurs connaissances sur Logo et les réseaux informatiques. 

## Fonctionnalités
- Interface utilisateur avec Tkinter
- Questions à choix multiples sur Logo et les réseaux informatiques
- Enregistrement du nom et de la classe de l'élève
- Affichage du score final
- Génération d'un fichier PDF avec le résultat

## Prérequis
Avant d'exécuter le programme, assurez-vous d'avoir installé Python (>=3.6) et les bibliothèques nécessaires.

## Installation
1. Clonez ce dépôt ou téléchargez les fichiers :
   ```bash
   git clone https://github.com/Saraiin/work_project1
   cd quiz-2AC
   ```
2. Installez les dépendances requises :
   ```bash
   pip install tk reportlab
   ```

## Utilisation
1. Pour exécuter le quiz sur Logo :
   ```bash
   python quiz_logo_2AC.py
   ```
2. Pour exécuter le quiz sur les réseaux informatiques :
   ```bash
   python quiz_reseau_2AC.py
   ```
3. Entrez le nom de l'étudiant et sa classe.
4. Répondez aux questions du quiz.
5. Consultez le score affiché à la fin.
6. Un fichier PDF contenant le score est généré automatiquement.

## Structure du projet
```
quiz-2AC/
│── quiz_logo_2AC.py   # Quiz sur le langage Logo
│── quiz_reseau_2AC.py # Quiz sur les réseaux informatiques
│── README.md          # Documentation du projet
```

## Améliorations possibles
- Ajout de plus de questions
- Sauvegarde des résultats dans une base de données
- Ajout d'un mode multi-joueurs

## Auteur
- **[Pr. SARA]**

N'hésitez pas à proposer des améliorations ou signaler des bugs ! 🚀

