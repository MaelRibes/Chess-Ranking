import requests
import re
from tqdm import tqdm


def player():
    return player


def input_player():
    global player
    player = input("Enter your username : ")
    return player


def find_date(url):
    try:
        found = re.search('/games/(.+?)$', url).group(1)
    except AttributeError:
        pass
    return found


def get_list_url():
    url = 'https://api.chess.com/pub/player/' + input_player() + '/games/archives'
    req = requests.get(url)  # On recupere l'archive d'un joueur
    list_url = req.json()[
        'archives']  # On recupere la liste des url de parties du joueur. Chaque url correspond à la liste des parties jouées durant un mois
    return list_url


def list_elo():
    res = [[], []]
    list_url = get_list_url()
    cpt = 0

    # Parcours differents mois :
    for url in tqdm(list_url, bar_format='{desc:<5.5}{percentage:3.0f}%|{bar:50}{r_bar}'):
        u = str(url)
        req = requests.get(u)
        games = req.json()['games']

        # Parcours des parties :
        for game in games:
            if game['rules'] == 'chess':
                if game['white']['username'] == player:
                    res[1].append(game['white']['rating'])
                else:
                    res[1].append(game['black']['rating'])
                res[0].append(cpt)
                cpt += 1
    print("\nSuccess")
    return res


def list_elo_month():
    res = [[], [], []]
    list_url = get_list_url()
    bkup = 0

    # Parcours differents mois :
    for url in tqdm(list_url, bar_format='{desc:<5.5}{percentage:3.0f}%|{bar:50}{r_bar}'):
        u = str(url)
        req = requests.get(u)
        games = req.json()['games']
        date = find_date(url)
        sum = 0
        accuracy = 0.0
        x = 0
        y = 0

        # Parcours des parties :
        for game in games:
            if game['rules'] == 'chess':
                if game['white']['username'] == player:
                    sum += game['white']['rating']
                    try :
                        accuracy += game['accuracies']['white']
                        y += 1
                    except KeyError:
                        pass
                else:
                    sum += game['black']['rating']
                    try :
                        accuracy += game['accuracies']['black']
                        y += 1
                    except KeyError:
                        pass
                x += 1
        moy = sum // x
        if y != 0:
            auc = accuracy / y
            bkup = auc
        else :
            auc = bkup
        res[2].append(auc)
        res[1].append(moy)
        res[0].append(date)
    print("\nSuccess")
    return res


