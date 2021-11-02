# Simulación de Eventos Discretos - TP2

## Bajar repo con submodulos

Tenemos como submodulo el simulador, para clonar el repo con submodulos incluidos se puede correr:

```
git clone --recurse-submodules git@github.com:TobiasCarreira/sed-tp2.git
```

Si ya clonaste el repo y querés bajar los submodulos:

```
git submodule init
git submodule update
```

## Cambios para usar aleatoriedad

Para que funcione la aleatoriedad en CDPP, hay que entrar en `CDPP_ExtendedStates-codename-Santi/src/cd++/Makefile.defs` y comentar la linea `DEFINES_CPP += -DDEVS_NOTRANDOM`.

