# Mouse Restrictor - README

## Description

**Mouse Restrictor** est une application Python conçue pour restreindre le mouvement du curseur de la souris dans une zone définie sur l'écran. Elle est équipée d'une interface utilisateur graphique pour le débogage et propose des raccourcis clavier pour un contrôle facile. L'application surveille en continu l'inactivité de la souris et recentre le curseur s'il n'a pas bougé pendant une durée spécifiée. Elle est destinée à simuler le comportement d'un joystick en contrôlant le pointeur dans l'API Windows.

## Fonctionnalités

- **Activer/Désactiver la restriction du curseur** : Activer ou désactiver la restriction du curseur de la souris à l'aide d'un raccourci clavier global.
- **Fenêtre de débogage** : Afficher des informations de débogage en temps réel dans une fenêtre séparée.
- **Surveillance de l'inactivité de la souris** : Recentrer automatiquement le curseur après une période d'inactivité.
- **Raccourcis clavier globaux** :
  - `F1` : Activer/Désactiver la restriction du curseur.
  - `F2` : Ouvrir la fenêtre de débogage.
  - `F4` : Quitter l'application.

## Prérequis

- Python 3.x
- Les bibliothèques Python suivantes :
  - `ctypes`
  - `time`
  - `threading`
  - `keyboard`
  - `tkinter`

## Installation

1. **Installer Python** : Assurez-vous que Python 3.x est installé sur votre système.
2. **Installer les bibliothèques nécessaires** :
   - Installer la bibliothèque `keyboard` avec pip :
     ```
     pip install keyboard
     ```
   - `ctypes` et `tkinter` font partie de la bibliothèque standard de Python et n'ont pas besoin d'être installés séparément.

## Utilisation

1. **Lancer l'application** :
   - Enregistrez le script Python fourni dans un fichier, par exemple, `mouse_restrictor.py`.
   - Exécutez le script :
     ```
     python mouse_restrictor.py
     ```

2. **Contrôler l'application** :
   - **F1** : Appuyez sur `F1` pour activer ou désactiver la restriction du curseur. Lorsqu'elle est activée, le curseur sera confiné à une zone de 200x200 pixels au centre de l'écran.
   - **F2** : Appuyez sur `F2` pour ouvrir la fenêtre de débogage, qui fournit des informations en temps réel sur l'état de l'application, y compris si la restriction est active, le temps écoulé depuis le dernier mouvement de la souris et le nombre de recentrages du curseur.
   - **F4** : Appuyez sur `F4` pour quitter l'application.

## Fonctionnalités détaillées

- **Restriction du curseur** :
  - Lorsqu'elle est activée, le curseur est confiné à une zone de 200x200 pixels au centre de l'écran.
  - La zone de restriction est définie en utilisant `ctypes` pour interagir avec l'API Windows.

- **Surveillance de l'inactivité de la souris** :
  - L'application surveille la position de la souris et recentre le curseur s'il reste inactif pendant plus de 0,25 seconde.

- **Fenêtre de débogage** :
  - La fenêtre de débogage fournit une zone de texte pour enregistrer les messages et une étiquette affichant des informations en temps réel sur l'état de l'application.

## Aperçu du code

- **Classe principale** : `MouseRestrictor`
  - **Initialisation** : Configure l'application, les raccourcis clavier et initialise Tkinter.
  - **toggle_restriction()** : Active ou désactive la restriction.
  - **activate()** : Active la restriction du curseur.
  - **deactivate()** : Désactive la restriction du curseur.
  - **update_clip()** : Définit la zone de restriction.
  - **release_clip()** : Libère le curseur de la zone de restriction.
  - **print_message()** : Enregistre les messages dans la fenêtre de débogage.
  - **open_debug_window()** : Ouvre la fenêtre de débogage.
  - **show_debug_window()** : Affiche la fenêtre de débogage.
  - **update_debug_info()** : Met à jour la fenêtre de débogage avec des informations en temps réel.
  - **on_debug_window_close()** : Gère l'événement de fermeture de la fenêtre de débogage.
  - **stop()** : Arrête l'application.
  - **center_cursor()** : Recentre le curseur de la souris.
  - **monitor_mouse_inactivity()** : Surveille l'inactivité de la souris et recentre le curseur si nécessaire.

## Remarques

- Cette application est destinée à être utilisée sur les systèmes d'exploitation Windows en raison de la dépendance à l'API Windows via `ctypes`.
- Assurez-vous que la bibliothèque `keyboard` est installée avec des permissions suffisantes pour capturer les pressions de touches globales.

Profitez de l'utilisation de Mouse Restrictor pour contrôler le mouvement de votre curseur de souris !
