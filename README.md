![HnS Logo](HnS_Logo.png)

# Pokémon 2 : Version Améthyste 
Romhack Française basée sur PokeHnS Expansion (Pokémon Crystal sur GBA) proposant une nouvelle approche : si Pokémon n'était pas devenu une franchise et soit resté sur le projet Pokémon 2 tout en sortant sur GBA plutôt que GBC pour aller au bout de leurs idées.

La branche **hns_2_fr** est la traduction de **Pokémon Heart and Soul 2.0** sans ajouts spécifiques mise à part l'adaptation aux spécificités françaises et à un peu plus coller au ton du jeu original.

# About `pokemonHnS-expansion`

<!-- If you want to re-record or change these gifs, here are some notes that I used: https://files.catbox.moe/05001g.md -->
<!-- TODO: Actually change these gifs, and generally update contents to convey HnS-specific information -->
![HnS Collage](HnS_Collage_YourAdventure.png)

**`pokemonHnS-expansion`**, aka Pokémon Heart and Soul 2.0, is a GBA ROM hack that is both a remake of GSC and demake of HGSS, with added quality-of-life, customization, and more.  
Originally built on top of [resetes12's **`Modern Emerald`**](https://github.com/resetes12/pokeemerald).  
Now additionally built on top of [RHH's **`pokeemerald-expansion`**](https://github.com/rh-hideout/pokeemerald-expansion) GBA ROM hack base.  
Finally, all of these projects are built on top of [pret's **`pokeemerald`**](https://github.com/pret/pokeemerald) decompilation project.

> Pokémon Heart & Soul brings the classic Johto Region and its iconic story to the world of modern GBA decomp hacking. Built on Modern Emerald and pokeemerald-expansion, this project offers a fresh take on the GSC/HGSS experience, blending key aspects of the Gen 2 and Gen 4 games, while incorporating many modern QoL features, as well as some familiar mechanics from Gen 3 to Gen 9. Not only is Heart & Soul (HnS) a first-of-its-kind, fully completed, playtested, and largely faithful GSC remake / HGSS demake, it's also completely open source, and is intended to be a base for a new generation of Johto rom hacks.
> 
# [Features](FEATURES.md)

**`pokemonHnS-expansion`** includes a mix of vanilla Emerald/FRLG features, re/de-made implementations of GSC/HGSS features, custom **`Modern Emerald`** features, and both features from [core series Pokémon games](https://bulbapedia.bulbagarden.net/wiki/Core_series) and popular QOL enhancements made available by **`pokeemerald-expansion`**.  
A full list of the features present in Pokémon Heart & Soul 2.0 can be found in [`FEATURES.md`](FEATURES.md)
A full list of the features made available by **`pokeemerald-expansion`** can be found in [`AVAILABLE_FEATURES.md`](AVAILABLE_FEATURES.md).

# Documentation

En cas de question ou de soucis, n'hésitez pas à passer sur [Discord](https://discord.gg/ZatqJRXzCm).

# [Credits](CREDITS.md)

- [Pokemon Heart and Soul](https://github.com/PokemonHnS-Development/pokehns-expansion) pour leur rom incroyable ! [Crédits complets](CREDITS.md)
- [Remylenain](https://github.com/Remylenain) : traduction de la plupart du contenu et adaptation des textes pour coller au jeu original
- [qigast](https://github.com/qigast) : traduction de [pokeemeraude-expansion](https://github.com/pokehacking-fr/pokeemeraude-expansion) qui nous sert de base pour notre traduction
- [DaftHunk](https://github.com/DaftHunk?tab=repositories) : traduction et adaptation de divers contenus

# **`pokemonHnS-expansion`** multiplayer compatibility

- **`pokemonHnS-expansion`** supports trade and link battle multiplayer functionality, which *should* extend to forks built on **`pokemonHnS-expansion`** but cannot be guaranteed.
- **`pokemonHnS-expansion`** is not compatible with official Pokémon games, **`pokemonHnS 1.X`**, **`Modern Emerald`**, or other **`pokeemerald-expansion`** projects.

# AI Disclosure
Since this is a controversial topic at the moment, we'd like to be transparent about use of AI for this project.

Every line of code written for the game is either hand-written or manually reviewed by a member of the team. However, it is still important to point out that LLMs like Claude Code and GitHub Copilot have been used for some tasks.

Here is what AI has been used for:
- Code Reviews of hand-written code
- Debugging more complex scenarios
- Auto Completion (stuff like repeating lists, DebugPrints, etc.)
- Creating Python Scripts for I/O procedures (like downloading/writing list data, I/O data with Excel, etc. namely for documentation)

AI has not been used for:
- Generating assets of any kind; Art or Music
