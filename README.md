# NosDamage

NosDamage is a damage calculator (and much more to come in the future) for the
MMORPG NosTale.  
The project is based on [this](https://forum.vendettagn.com/index.php?/topic/2749-formula-damage/)
formula (you can find the original thread on the Italian forum
[here](https://board.it.nostale.gameforge.com/index.php/Thread/88530-Formula-del-Danno-Aggiornata-e-ancora-in-fase-di-aggiornamento/)).
Please note that the formula is only 98~99% accurate in PvE, mainly due to things like
hidden monster stats. This could possibly affect calculations offsetting high
elemental damage (usually when it's higher than 20k) by few hundreds (100-200
compared to 20k+ damage is fairly negligible, in my opinion, for the purposes of
this calculator).

## Currently implemented features
The graphical user interface is not pretty at the moment; it's been created with the sole
purpose of easily manage the calculator and its features, which at the moment, are:

- Damage calculator (normal/crit/soft/softcrit/average)
- Editor to handily create and manage your attackers/defenders

There also an sp build optimizer that at the moment is only available through
command line interface. It will take the stats of the character you input as
attacker and brute-force against one or more defenders to find the build with
the highest (average) damage output. You can specify job/up oof your sp and your SLs.

## Upcoming features
- SP build damage output optimizer (just needs to be added to the GUI)
- Option to calculate average damage against multiple defenders (as above, just
  TBA to the GUI)
- Total HP calculation based on SP build/bonuses/pp, accessories, etc.
- HP recovery calculation based on base recovery, skills, accessories, etc.
- More sample attacker/defender files (I was planning to add all the most common
  mobs like act 6 and LoD ones)
- UI/UX improvements
- Error checking
- Unit testing
- And much more!  
