# coding: utf-8-sig

import argparse
from random import randint

import csv
import requests
import uuid

# Paramétrer ici la Clé d'auhentification et le Endpoint
subscription_key = "YOUR_KEY"
endpoint = "https://api.cognitive.microsofttranslator.com"
path = '/detect'

constructed_url = endpoint + path

# Liste des 6 langues les plus parlées dans le monde
populars_languages = ['eng', 'zho', 'hin', 'spa', 'fra', 'ara']


def define_text(text: str):
    language_expected = None

    if not text:
        with open("data/x_train.txt", 'r', encoding="utf-8") as text_file:
            text_data = text_file.readlines()
        with open("data/y_train.txt", 'r', encoding="utf-8") as language_file:
            language_data = language_file.readlines()

        random = randint(0, len(text_data))

        while (language_data[random].strip()) not in populars_languages:
            random = randint(0, len(text_data))

        text = text_data[random].strip()
        language = language_data[random].strip()

        with open("data/labels.csv", 'r', encoding="utf-8") as labels_file:
            labels = csv.reader(labels_file, delimiter=';')
            for row in labels:
                if language == row[0]:
                    language_expected = row[2]
                    break

    return text, language_expected


def azure_request(text: str, language_expected: str):
    # Construction de la requête pour appeler le endpoint microsoft azure translator
    body = [{"text": text}]

    params = {
        'api-version': '3.0'
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        "X-ClientTraceId": str(uuid.uuid4())
    }

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    # Affichage du résultat dans le terminal
    if language_expected:
        print("Texte tiré au hasard dans le fichier de data :\n")
        print(text + "\n")
        print("Langue attendue : " + language_expected)
        print("Langue détectée : " + response[0]['language'])
    else:
        print("Texte indiqué par l'utilisateur :\n")
        print(text + "\n")
        print("Langue détectée : " + response[0]['language'])
        print("Indice de confiance : " + str(response[0]['score'] * 100) + "%")


def main():
    parser = argparse.ArgumentParser(
        description="Permet de détecter la langue d'un texte donné (Texte choisi par l'utilisateur ou tiré au hasard dans un fichier de data)")
    parser.add_argument("-t", "--text", help='Le texte dont on veut détecter la langue (tiré au hasard dans un fichier de data si non renseigné)')
    args = parser.parse_args()

    text, expected_language = define_text(args.text)

    azure_request(text, expected_language)


if __name__ == "__main__":
    main()
