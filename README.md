# Blazebadge
Generative roleplaying game taking inspiration from Blaseball, Fire Emblem, and Final Fantasy Tactics. Starting to build this as a simple "generate characters/children similar to Fire Emblem" toy, I became inspired with the stories that organically grew out of Blaseball's automated systems, and the sense of fandom/possessiveness over these randomly generated characters and games in which players have no agency.

This is early early development work, and no actual game is yet built. See the roadmap for future plans.

## Goals
A player goes to the Blazebadge site, and sees their collection of characters. They can send these characters out on missions (automatically generated and performed) where they will gain experience, level up, and grow closer to their comrades. Multiple characters would then be able to have a child whose skills are weighted towards their parent's strengths.


## Roadmap
1. Figure out character generation and settle on stats. <-- We are here
2. Determine leveling curves and stat scaling.
3. Determine job relationships. Someone high in Black Magic will likely meet with someone with high Apothecary over someone with high Sword skill. Preferably find in-universe explanations like "big beefy tank naturally spends more time with the cook".
4. Build missions for sending characters out on.
5. Build out-of-mission goals, such as townbuilding levels. Build out specified buildings to provide stat boosts?

## Running
Do `python char.py` to generate two parents and their child.

## Credits
Utilizes some data from [Copora](https://github.com/dariusk/corpora), notably first names and last names. It's a fantastic project, so check it out.