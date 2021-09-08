# Détecteur de langue

Projet 1 - Découvrez le métier d'ingénieur IA

## Utilisation

### Détecter la langue d'un texte aléatoire

Dans un invite de commande, lancer `python detect_language.py` pour détecter la langue d'un texte tiré au hasard dans un fichier de data, parmis les 6 langues les plus parlées au monde

```bash
$ python detect_language.py

  Texte tiré au hasard dans le fichier de data :

  In 1981, Bantam Books published a movie tie-in novelization written by Mike McQuay that adopts a lean, humorous style reminiscent of the film. The novel is significant because it includes scenes that were cut out of the film, such as the Federal Reserve Depository robbery that results in Snake's incarceration. The novel provides motivation and backstory to Snake and Hauk — both disillusioned war veterans — deepening their relationship that was only hinted at it in the film. The novel explains how Snake lost his eye during the Battle for Leningrad in World War III, how Hauk became warden of New York, and Hauk's quest to find his crazy son who lives somewhere in the prison. The novel fleshes out the world that these characters exist in, at times presenting a future even bleaker than the one depicted in the film. The book explains that the West Coast is a no-man's land, and the country's population is gradually being driven crazy by nerve gas as a result of World War III.

  Langue attendue : en
  Langue détectée : en
```

### Détecter la langue d'un texte passé en paramètre

Dans un invite de commande, lancer `python detect_language.py --text TEXT` pour détecter la langue du texte passé en argument

```bash
$ python detect_language.py --text "Hello, my name is Romain"

  Texte indiqué par l'utilisateur :

  Hello, my name is Romain

  Langue détectée : en
  Indice de confiance : 100.0%
```