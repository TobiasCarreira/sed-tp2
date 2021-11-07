En este trabajo práctico vamos a analizar una variante del Dilema del Prisionero (ref a wiki).

En nuestra variante la grilla representa una prisión y los prisioneros se mueven de forma aleatoria por ella, al encontrarse con otro prisionero deciden o no traicionarlo.
Al ocurrir una traición, se aumenta la condena en 1 año, pero la víctima se enterará de que fue traicionado un determinado tiempo después.
La mejor solución es Quid-Pro-Quo, ya que fue estudiado que ésta reduce la dispersión de los tiempos de condena, pero esta se basa en la inmediatez
con la que un prisionero conoce que otro lo delató o traicionó. En una situación de esparcimiento de información falsa o no comprobable (como esta)
con objetivos de manipulación, para conseguir una reducción de la condena un alcaide es informado de que alguien traiciona a alguien y éste decide
que hace con la información. Esto es lo que deseamos modelar.

En general nuestro modelo se explica por:
- un tamaño de la grilla
- una cantidad de prisioneros inicial (``N``) con sus respectivas condenas iniciales
- encuentros entre prisioneros que con probabilidad ``1/p`` desata una traición informada al oponente con retraso ``0,..,M`` iteraciones (equiprobable)
- encuentros entre prisioneros que ya saben que fueron buchoneados por su oponente en algún instante anterior y entonces siempre traicionan (Quid-Pro-Quo) con retraso de información de ``0,..,M`` iteraciones (equiprobable)
- el paso del tiempo
- cuańto se agrega a la condena cuando se es traicionado (``c``)

Si bien sobre esta variante introdujimos algunas particularidades:
- si un prisionero todavía no sabe que fue buchoneado por otro que se vuelve a encontrar, entonces la condena se aumenta pero se toma el mínimo retraso de información, entre la nueva traición y la anterior
- las condenas nunca se reducen
- no se distingue entre traición-traición y traición-no traición (a diferencia del Dilema original cuya condena agregada es menor en el primer caso)
- si la condena es 0, el prisionero inmediatamente sale de la prisión

Con el objetivo de entender el modelo, experimentaremos con distintos valores de ``c``, ``p``, ``N`` y ``M``.

Para esto usamos CD++ y un archivo ``.ma`` generado de forma dinámica, pero cuyas bases son las reglas de:
- _Movimiento_: mueven a un prisionero en la dirección a la que está mirando si el casillero está libre, además hacen que pase el tiempo.
- _Eliminación_: remueven a un prisionero que se movió de lugar del casillero anterior.
- _Buchoneo_: determinan si mi oponente me buchonea y cuanto tiempo pasa hasta que me entere. Se usa 0 como código de que fuí traicionado, -1 para no haber sido traicionado y n como la cantidad de iteraciones que faltan para saber que me traicionaron.

Se codifica una tupla en la que:
- Lugar 0-ésimo: identificador del prisionero
- Lugar 1-ésimo: dirección (de mirada)
- Lugar 2-ésimo: duración de la condena
- Lugar i+3-ésimo: 0 si el prisionero i me traicionó y lo se, n si faltan n iteraciones para saber que el prisionero i me traicinó y -1 para no haber sido traicionado por éste.

NOTA: las reglas y sus condiciones se encuentras comentadas para mayor claridad.