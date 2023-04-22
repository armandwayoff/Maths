<center><h1>Mathématiques</h1></center>

## Tables des Matières

* [A316667 - The Trapped Knight](#a316667---the-trapped-knight)
* [Courbe du dragon](#courbe-du-dragon)
  * [Version ```turtle```]()
  * [Version vectorielle]()
* [Courbes remplissantes](#courbes-remplissantes)
* [Fonctions continues nulle part dérivables](#fonctions-continues-nulle-part-dérivables)
  * [Courbe de Bolzano-Lebesgue](#courbe-de-bolzano-lebesgue)
  * [Courbe du blanc-manger](#courbe-du-blanc-manger)
* [Hitomezashi Stitch Patterns](#hitomezashi-stitch-patterns)
* [Marche aléatoire](#marche-aléatoire)

## A316667 - The Trapped Knight

### Lien:
[The Trapped Knight - Numberphile](https://www.youtube.com/watch?v=RGQe8waGJ4w)

<center><img src="https://github.com/armandwayoff/maths/blob/main/A316667%20-%20The%20Trapped%20Knight/A316667.jpeg" alt="A316667" width="500" align="center"/></center>

## Courbe du dragon

### Liens:
- [Dragon curve - Wikipedia](https://en.wikipedia.org/wiki/Dragon_curve)
- [Dragon Curve - Numberphile](https://www.youtube.com/watch?v=wCyC-K_PnRY)
- [Wrong Turn on the Dragon - Numberphile](https://www.youtube.com/watch?v=v678Em6qyzk)

### Version ```turtle```

La bibliothèque [```turtle```](https://github.com/PythonTurtle/PythonTurtle).

Ci-dessous la *courbe du dragon* d'ordre 10.

<center><img src="https://github.com/armandwayoff/Maths/blob/main/Courbe%20du%20dragon/courbe_du_dragon_10.png" alt="courbe du dragon" width="500" align="center"/></center>

### Version vectorielle

[à compléter]

## Courbes remplissantes

### Lien:
[Fractal charm: Space filling curves](https://www.youtube.com/watch?v=RU0wScIj36o)

Courbe de Hilbert d'ordre 5:

<center><img src="https://github.com/armandwayoff/maths/blob/main/Courbes%20remplissantes/hilbert5.jpeg" alt="hilbert5" height="500" align="center"/></center>

## Fonctions continues nulle part dérivables

### Courbe de Bolzano-Lebesgue

$$
f(x) :=
\begin{cases} 
\frac{2}{3}f(3x) &\text{si } x \in \left[0, \frac{1}{3} \right] \\
\frac{2}{3} - \frac{1}{3}f(3x-1) &\text{si } x \in \left[ \frac{1}{3}, \frac{2}{3} \right] \\
\frac{1}{3} + \frac{2}{3}f(3x-2) &\text{si } x \in \left[\frac{2}{3}, 1 \right]
\end{cases}.
$$

Une autre définition:

on pose $I := [0, 1]$ et $(f_n)$ la suite de fonctions définie par

- $f_0(x) = x$,
- $f_n$ est affine sur $\left[ \frac{k}{3^n}, \frac{k+1}{3^n}\right]$ pour tout $k \in \\{ 0, \dots, 3^n-1 \\}$,
- $f_n$ et $f_{n-1}$ sont égales en $\frac{3k}{3^n}$, $\frac{3k+1}{3^n}$, $\frac{3k+2}{3^n}$ pour tout $k \in \\{0, \dots, 3^n-1 \\}$.

<center><img src="https://github.com/armandwayoff/maths/blob/main/Fonctions%20continues%20nulle%20part%20d%C3%A9rivables/bolzano_lebesgue_8.png" alt="bolzano_lebesgue" width="500" align="center"/></center>

### Courbe du blanc-manger

<center><img src="https://github.com/armandwayoff/maths/blob/main/Fonctions%20continues%20nulle%20part%20d%C3%A9rivables/blanc_manger_15.png" alt="bolzano_lebesgue" width="500" align="center"/></center>

## Hitomezashi Stitch Patterns

### Lien:
[Hitomezashi Stitch Patterns - Numberphile](https://www.youtube.com/watch?v=JbfhzlMk2eY)

<center><img src="https://github.com/armandwayoff/maths/blob/main/Hitomezashi%20Stitch%20Patterns/hitomezashi_50.png" alt="hitomezashi_50" width="500" align="center"/></center>

## Marche aléatoire

<center><img src="Marche%20aléatoire/N=10^6.png" alt="N=10^6" height="300" align="center"/></center>
