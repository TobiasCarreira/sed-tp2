[Top]
components : personas

[personas]
type : cell
dim : (10,10)
delay : transport
defaultDelayTime  : 0
border : wrapped
neighbors : personas(-2,0)
neighbors : personas(-1,-1) personas(-1,0) personas(-1,1)
neighbors : personas(0,-2) personas(0,-1)  personas(0,0)  personas(0,1) personas(0,2)
neighbors : personas(1,-1)  personas(1,0)  personas(1,1)
neighbors : personas(2,0)
initialvalue : 0
initialCellsValue : personas.val
localtransition : personas-rule

[personas-rule]
% Si termina la condena, desaparece
rule : 0 100 {(0,0)!2<=100}

% Reglas de movimiento si no hay enfrentamiento

% Reglas de moverme
rule : {
    [
        (0,-1)!0,
        randInt(3) + 1,
        (0,-1)!2 - 100,
        if((0,-1)!3 > 0, (0,-1)!3 - 1 , (0,-1)!3),
        if((0,-1)!4 > 0, (0,-1)!4 - 1 , (0,-1)!4)
    ]
} 100 {(0,0)=0 and (0,-1)!1=1 and (0,-1)!2>100}

rule : {
    [
        (-1,0)!0,
        randInt(3) + 1,
        (-1,0)!2 - 100,
        if((-1,0)!3 > 0, (-1,0)!3 - 1 , (-1,0)!3),
        if((-1,0)!4 > 0, (-1,0)!4 - 1 , (-1,0)!4)
    ]
} 100 {(0,0)=0 and (-1,0)!1=2 and (-1,0)!2>100}

rule : {
    [
        (0,1)!0,
        randInt(3) + 1,
        (0, 1)!2 - 100,
        if((0,1)!3 > 0, (0,1)!3 - 1 , (0,1)!3),
        if((0,1)!4 > 0, (0,1)!4 - 1 , (0,1)!4)
    ]
} 100 {(0,0)=0 and (0,1)!1=3 and (0,1)!2>100}

rule : {
    [
        (1,0)!0,
        randInt(3) + 1,
        (1, 0)!2 - 100,
        if((1,0)!3 > 0, (1,0)!3 - 1 , (1,0)!3),
        if((1,0)!4 > 0, (1,0)!4 - 1 , (1,0)!4)
    ]
} 100 {(0,0)=0 and (1,0)!1=4 and (1,0)!2>100}

% Reglas de eliminarme de la posicion anterior
rule : 0 100 {(0,0)!1=1 and (0,1)=0}
rule : 0 100 {(0,0)!1=2 and (1,0)=0 and (1,-1)!1!=1}
rule : 0 100 {(0,0)!1=3 and (0,-1)=0 and (0,-2)!1!=1 and (-1,-1)!1!=2}
rule : 0 100 {(0,0)!1=4 and (-1,0)=0 and (-1,-1)!1!=1 and (-2,0)!1!=2 and (-1,1)!1!=3}

% Si hay conflicto, se suma condena y se cambia la direccion de mirada
% Tiro una moneda para ver si se buchonean
% Si se buchonean, suma 100 de condena

% regla buchoneo 1
rule : {
    [
        (0,0)!0,
        randInt(3) + 1, % elijo nueva direccion
        (0,0)!2 + 100, % te buchonearon
        if(
            (0,1)!0 = 1, % es el oponente 1
            if((0,0)!3 = -1, randInt(4), min((0,0)!3, randInt(4))), % si ya me buchoneo (lo sepa o no)
            if((0,0)!3 > 0, (0,0)!3 - 1 , (0,0)!3) % pasa el tiempo
        ),
        if(
            (0,1)!0 = 2, % es el oponente 2
            if((0,0)!4 = -1, randInt(4), min((0,0)!4, randInt(4))), % si ya me buchoneo (lo sepa o no)
            if((0,0)!4 > 0, (0,0)!4 - 1 , (0,0)!4) % pasa el tiempo
        )
    ]
} 100 {
    (0,0)!1=1 and (0,1)!1=3 % me estoy mirando
    and
    (
        (
            (0,0)!0 = 1 % soy en 1
            and
            (0,1)!3 = 0 % obligatoriamente me buchonea porque ya se entero de que lo buchonee
        )
        or
        (
            (0,0)!0 = 2 % soy en 2
            and
            (0,1)!4 = 0 % obligatoriamente me buchonea porque ya se entero de que lo buchonee
        )
        or
        randInt(1) = 0 % siempre me puede buchonear
    )
}


rule : {
    [
        (0,0)!0,
        randInt(3) + 1, % elijo nueva direccion
        (0,0)!2 - 100, % te buchonearon
        if((0,0)!3 > 0, (0,0)!3 - 1 , (0,0)!3), % pasa el tiempo
        if((0,0)!4 > 0, (0,0)!4 - 1 , (0,0)!4) % pasa el tiempo
    ]
} 100 {
    (0,0)!1=1 and (0,1)!1=3 % me estoy mirando
    % si esta regla va despues de las regla buchoneo 1
    % si llegue aca (por el orden de las reglas), no me buchonearon
}

rule : {
    [
        (0,0)!0,
        randInt(3) + 1,
        (0,0)!2 + if(randInt(4)=0,-100,100),
        (0,0)!3,
        (0,0)!4
    ]
} 100 {(0,0)!1=3 and (0,-1)!1=1 }
rule : {
    [
        (0,0)!0,
        randInt(3) + 1,
        (0,0)!2 + if(randInt(4)=0,-100,100),
        (0,0)!3,
        (0,0)!4
    ]
} 100 {(0,0)!1=2 and (1,0)!1=4}
rule : {
    [
        (0,0)!0,
        randInt(3) + 1,
        (0,0)!2 + if(randInt(4)=0,-100,100),
        (0,0)!3,
        (0,0)!4
    ]
} 100 {(0,0)!1=4 and (-1,0)!1=2}

% regla default es que pasa el tiempo pero no se mueve
rule : 0 100 { (0,0) = 0 }
rule : {
    [
        (0,0)!0,
        (0,0)!1,
        (0,0)!2 - 100,
        if((0,0)!3 > 0, (0,0)!3 - 1, (0,0)!3),
        if((0,0)!4 > 0, (0,0)!4 - 1, (0,0)!4)
    ]
} 100 { t }
