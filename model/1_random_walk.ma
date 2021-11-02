[Top]
components : personas

[personas]
type : cell
dim : (10,10)
delay : transport
defaultDelayTime  : 0
border : wrapped
neighbors : personas(-1,0)
neighbors : personas(0,-1)  personas(0,0)  personas(0,1)
neighbors : personas(1,0)
initialvalue : 0
initialrowvalue :  5     1000000000
%initialCellsValue : personas.val
localtransition : personas-rule

[personas-rule]
% Comportamiento de las personas
rule : 0 100 {(0,0)=1 and (0,1)=0}
rule : {randInt(3) + 1} 100 {(0,0)=0 and (0,-1)=1}
rule : 0 100 {(0,0)=2 and (1,0)=0}
rule : {randInt(3) + 1} 100 {(0,0)=0 and (-1,0)=2}
rule : 0 100 {(0,0)=3 and (0,-1)=0}
rule : {randInt(3) + 1} 100 {(0,0)=0 and (0,1)=3}
rule : 0 100 {(0,0)=4 and (-1,0)=0}
rule : {randInt(3) + 1} 100 {(0,0)=0 and (1,0)=4}

rule : {(0,0)} 0 { t }
