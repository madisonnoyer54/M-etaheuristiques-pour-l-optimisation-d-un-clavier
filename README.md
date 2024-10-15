# Optimisation des Touches du Clavier

## Description

Ce projet, réalisé dans le cadre de l'UE **Optimisation** en Licence 3 Informatique, utilise l’algorithme du **recuit simulé** pour optimiser la disposition des touches d’un clavier. L'objectif est de placer les lettres de manière à réduire la distance de frappe entre les lettres fréquemment utilisées ensemble, en tenant compte de la fréquence de leurs combinaisons.

## Fonctionnalités

- **Optimisation de la disposition du clavier** : Réduction de l'énergie de frappe en fonction de la distance entre les lettres.
- **Visualisation en temps réel** : Affichage graphique de l'évolution de l'énergie au cours des itérations.

## Bibliothèques Utilisées

- **Pandas** : Pour la manipulation des données, notamment la lecture des fréquences des bigrammes.
- **Matplotlib** : Pour l'affichage graphique des résultats.

## Installation

Assurez-vous d'avoir Python installé sur votre machine, puis exécutez les commandes suivantes pour installer les bibliothèques nécessaires :

```bash
sudo apt install python3-pip
pip install pandas
pip install matplotlib
