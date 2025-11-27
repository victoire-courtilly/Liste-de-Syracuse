"""Module contenant des fonctions pour étudier et afficher la suite de Syracuse."""

#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Affiche la suite de Syracuse passée en paramètre sous forme de graphique."""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    # return None
#######################

def syracuse_l(n):
    """Retourne la suite de Syracuse de source n."""

    # votre code ici
    l = [n]
    while n != 1 :
        if n % 2 == 0:
            n = n // 2
        else :
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse."""

    # votre code ici
    return len(l)-1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse."""

    # votre code ici
    for i, elt in enumerate(l) :
        if l[0] > elt :
            return i-1
    return 0

def altitude_maximale(l):
    """Retourne l'altitude maximale d'une suite de Syracuse."""

    # votre code ici
    return max(l)



#### Fonction principale


def main():
    """ Fonction principale : génère une suite de Syracuse, l'affiche, puis affiche le temps de vol, 
    le temps de vol en altitude et l’altitude max."""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
