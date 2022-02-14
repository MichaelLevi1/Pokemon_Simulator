# Pokemon Type Simulator

This is an interactive Pokemon type simulator for determining the offensive and defensive stats of the 18 types. Three simulator tools are currently available; 'Attack Stats', 'Defend Stats' and 'Type Score'. This simulator is solely for a Pokemon's typing therefore it does not consider abilities such as Levitate, Dry Skin, Flash Fire etc.

![PokeSim](https://imgur.com/H7Bq4z5)

**Attack Stats**

Tells you the offensive stats of one type combined to the 18 types; whether an attack would be super effective, neutral, not very effective or have no effect. 

**Defend Stats** 

Tells you the defensive stats of any type combination allowing the ability to experiment with more than two types. This tells you what types your combination is weak, neutral, resisted, and immune to.

**Type Score**

Tells you how good a type combination is defensively using a type score, which is the summation of each type's effectiveness to the type combination. An immunity is equal to zero, a neutral attack is equal to one, and so forth for each stack of super effective and not very effective attacks. Also allows for typing combinator with any number of types.


## Required Packages

* pygame
* numpy
* moviepy.editor
