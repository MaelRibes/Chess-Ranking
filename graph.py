import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from getElo import *


def graph():
    elo = list_elo()

    fig, ax1 = plt.subplots()

    # Rating axis
    ax1.set_xlabel("Number of games")
    ax1.set_ylabel("Rating")
    ax1.set_ylim(400, 2200)
    ax1.plot(elo[0], elo[1], label="rating")

    # Legend :
    plt.legend()

    # Title
    plt.title("Rating of " + player())

    plt.show()


def graph_month():

    elo = list_elo_month()
    xlabels = elo[0]

    fig, ax1 = plt.subplots()

    # Rating axis
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Rating")
    ax1.set_ylim(400, 2300)
    ax1.set_xticklabels(xlabels, rotation=35, ha="right")
    rating = ax1.plot(elo[0], elo[1], label="rating")

    # Reduction of the number of labels
    x = 0
    if len(xlabels) > 20:
        for i, tick in enumerate(ax1.xaxis.get_ticklabels()):
            if x % 2 == 0:
                tick.set_visible(False)
            x += 1

    # Accuracy axis
    ax2 = ax1.twinx()
    ax2.set_ylabel("% of accuracy")
    ax2.set_ylim(0, 100)
    accuracy = ax2.plot(elo[0], elo[2], "r", label="average accuracy")

    # Legend :
    lns = rating + accuracy
    labels = [l.get_label() for l in lns]
    plt.legend(lns, labels, loc=0)

    # Title
    plt.title("Rating of " + player() + " month by month")

    plt.show()
