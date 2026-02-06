# ClaudIA - Bot Discord

Bot Discord développé en Python avec discord.py.

## 📋 Prérequis

- Python 3.8 ou supérieur
- Un compte Discord
- Un token de bot Discord (voir section Configuration)

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/EdgarMolard/ClaudIA.git
cd ClaudIA
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
```

### 3. Activer l'environnement virtuel

**Linux/Mac :**
```bash
source venv/bin/activate
```

**Windows :**
```bash
venv\Scripts\activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Créer votre bot Discord

1. Allez sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Cliquez sur "New Application" et donnez-lui un nom
3. Dans l'onglet "Bot", cliquez sur "Add Bot"
4. Activez les intents suivants :
   - Presence Intent
   - Server Members Intent
   - Message Content Intent
5. Copiez le token du bot (cliquez sur "Reset Token" si nécessaire)

### 2. Configurer le fichier de configuration

Créez un fichier `config.py` à la racine du projet :

```bash
cp config.exemple.py config.py
```

Éditez `config.py` et ajoutez votre token :

```python
TOKEN = "votre_token_discord_ici"
```

⚠️ **Important :** Ne partagez JAMAIS votre token ! Le fichier `config.py` est ignoré par Git.

### 3. Inviter le bot sur votre serveur

1. Dans le Developer Portal, allez dans l'onglet "OAuth2" → "URL Generator"
2. Sélectionnez les scopes :
   - `bot`
   - `applications.commands`
3. Sélectionnez les permissions nécessaires pour votre bot
4. Copiez l'URL générée et ouvrez-la dans votre navigateur
5. Sélectionnez le serveur où inviter le bot

## ▶️ Lancement

Assurez-vous que l'environnement virtuel est activé, puis :

```bash
python bot.py
```

Vous devriez voir le message "Connecté en tant que [nom_du_bot]!" dans la console.

## 📁 Structure du projet

```
ClaudIA/
├── bot.py              # Point d'entrée du bot
├── config.py           # Configuration (token, etc.) - NON VERSIONNÉ
├── config.exemple.py   # Exemple de configuration
├── requirements.txt    # Dépendances Python
├── .gitignore         # Fichiers ignorés par Git
├── cogs/              # Modules de commandes (cogs)
├── data/              # Données persistantes
└── utils/             # Utilitaires et fonctions helper
```

## 🔧 Développement

### Ajouter des dépendances

```bash
pip install package_name
pip freeze > requirements.txt
```

### Désactiver l'environnement virtuel

```bash
deactivate
```

## 📝 Licence

Ce projet est sous licence libre.

## 👥 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.
