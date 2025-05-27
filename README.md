# RPG Combat Arena

Un jeu de rôle en ligne de commande développé en Python, proposant des combats tactiques au tour par tour avec un système de classes, d'équipements et de sorts.

## 🎮 Description du Projet

Ce projet est un RPG textuel qui propose deux modes de jeu :
- **Mode Combat (1vs1)** : Affrontement entre deux joueurs
- **Mode Histoire** : Aventure solo contre des ennemis de difficulté croissante

Le jeu intègre un système de combat stratégique avec différentes classes de personnages, équipements variés et sorts magiques.

## 🛠️ Technologies Utilisées

- **Python 3.x** - Langage principal
- **Modules Python standard** :
  - `random` - Pour la génération de nombres aléatoires (critiques, esquives, récupération)
  - Programmation orientée objet (POO)

## 📁 Structure du Projet

```
rpg-game/
├── main.py                 # Point d'entrée du jeu
├── arena.py                # Logique principale des combats
├── characters/             # Classes de personnages
│   ├── character.py        # Classe de base Character
│   ├── barbarian.py        # Classe Barbarian
│   └── mage.py            # Classe Mage
├── gears/                  # Équipements et sorts
│   ├── armor.py           # Armures
│   ├── weapon.py          # Armes
│   └── spell.py           # Sorts magiques
└── ennemis/               # Ennemis
    └── ennemi.py          # Classe Enemy
```

## 🎯 Classes de Personnages

### 🗡️ Barbarian
- **Points de vie** : 200
- **Spécialité** : Combat rapproché, attaques multiples
- **Capacité spéciale** : Peut attaquer deux fois par tour
- **Récupération** : Régénère 20-60 PV en se reposant

### 🔮 Mage
- **Points de vie** : 100
- **Mana** : 300
- **Spécialité** : Magie offensive et sorts puissants
- **Capacité spéciale** : Lance des sorts magiques
- **Récupération** : Régénère 10-50 points de mana en se reposant

## ⚔️ Système d'Équipement

### Armes Physiques
- **À la main** : 10 dégâts
- **Massue** : 20 dégâts, 40 d'armure
- **Lance** : 50 dégâts, 20% de critique
- **Hache** : 30 dégâts, 20 d'armure, 15% de critique

### Armes Magiques
- **Bâton** : 20 dégâts, +1 magie, 10 d'armure
- **Baguette** : +3 magie, 50 de mana
- **Sceptre** : 20 dégâts, +2 magie, 100 de mana

### Armures Physiques
- **Aucune armure** : 0 protection
- **Armure légère** : 30 d'armure, 50 de résistance magique
- **Armure moyenne** : 75 d'armure, 10 de thorns, 20 de résistance magique
- **Armure lourde** : 130 d'armure, 15 de thorns

### Armures Magiques
- **Armure magique** : 20 d'armure, 100 de résistance magique
- **Armure de renvoi** : 75 de thorns
- **Armure d'archimage** : 150 de résistance magique

## 🔥 Sorts Disponibles

- **Étincelle** : 10 de dégâts, coût 45 mana
- **Boule de feu** : 20 de dégâts, coût 60 mana  
- **Vague tonante** : 50 de dégâts, coût 100 mana

## 👹 Ennemis

### Ennemis Physiques
1. **Gobelin** (Difficulté 1) : 50 PV, armure légère, massue
2. **Hobogoblin** (Difficulté 2) : 150 PV, armure moyenne, lance
3. **Orc** (Difficulté 3) : 250 PV, armure lourde, hache
4. **Ogre** (Difficulté 4) : 350 PV, aucune armure, massue

### Ennemis Magiques
1. **Salamandre de feu** (Difficulté 1) : 100 PV, armure de renvoi
2. **Sorcière** (Difficulté 2) : 150 PV, armure d'archimage, baguette
3. **Golem magique** (Difficulté 3) : 450 PV, armure lourde
4. **Esprit élémentaire** (Difficulté 4) : 200 PV, armure d'archimage, sceptre

## 🎲 Mécaniques de Combat

### Système de Dégâts
- **Formule d'armure** : `dégâts_finaux = (1 - armure/500) × dégâts_base`
- **Critiques** : Chance de critique selon l'arme (5-20%), dégâts ×1.5
- **Esquive** : 5% de chance d'esquiver complètement une attaque
- **Thorns** : Les armures peuvent renvoyer des dégâts à l'attaquant

### Actions Possibles
- **Attaquer** : Infliger des dégâts à l'adversaire
- **Lancer un sort** (Mage uniquement) : Attaque magique coûtant de la mana
- **Se reposer** : Récupérer des PV (Barbarian) ou de la mana (Mage)

## 🚀 Installation et Lancement

### Prérequis
- Python 3.x installé sur votre système

### Lancement du Jeu
```bash
# Cloner ou télécharger le projet
cd rpg-game

# Lancer le jeu
python main.py
```

### Première Utilisation
1. Choisissez votre mode de jeu (0 pour Combat, 1 pour Histoire)
2. Créez votre personnage :
   - Entrez votre nom
   - Choisissez votre classe (0: Mage, 1: Barbarian)
   - Sélectionnez votre armure
   - Choisissez votre arme
3. Combattez et utilisez la stratégie pour l'emporter !

## 🎯 Modes de Jeu

### Mode Combat (1vs1)
- Deux joueurs créent leur personnage
- Combat au tour par tour jusqu'à la mort de l'un des combattants
- Le Barbarian joue deux fois par tour

### Mode Histoire
- Un joueur affronte une série d'ennemis de difficulté croissante
- Choisissez votre niveau de difficulté (1 à 4)
- Battez tous les ennemis pour gagner la partie

## 🔧 Fonctionnalités Techniques

- **Héritage POO** : Système de classes avec Character comme classe de base
- **Polymorphisme** : Différents comportements selon les classes
- **Encapsulation** : Méthodes getter/setter pour la gestion des stats
- **Gestion d'état** : Suivi des PV, mana et équipements
- **Système aléatoire** : Critiques, esquives et récupération dynamiques

## 🤝 Contribution

Ce projet est ouvert aux améliorations ! Vous pouvez :
- Ajouter de nouvelles classes de personnages
- Créer de nouveaux sorts et équipements
- Implémenter de nouveaux ennemis
- Améliorer l'interface utilisateur
- Ajouter un système de sauvegarde

## 📝 Notes de Développement

Le jeu utilise une approche modulaire avec séparation claire entre :
- La logique de jeu (arena.py)
- Les entités (characters/, ennemis/)
- Les équipements (gears/)
- Le point d'entrée (main.py)

Cette architecture facilite la maintenance et l'extension du code.