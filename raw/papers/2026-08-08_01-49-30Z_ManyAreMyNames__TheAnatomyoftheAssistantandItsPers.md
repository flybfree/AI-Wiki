---
title: "Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders
published: 2026-08-08T01:49:30Z
authors: Adelaide Danilov, Aria Nourbakhsh, Oleksandr Marchenko Breneur, Salima Lamsiyah
url: http://arxiv.org/abs/2608.07852v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# "Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders

## Abstract
How a language model internally represents who is speaking, the Assistant, an assigned roleplay persona, or a narrated story character, remains underexplored. We study speaker representations using a dataset of user-expressed emotional text and corresponding model responses. We decompose three generation settings (Assistant, Roleplay, and Story) into sparse autoencoder features extracted at turn-boundary and pronoun-token positions and selected through a filtering pipeline for different depths. We characterize each surviving feature through its steering effects and activation distribution. Our main finding is that the Assistant and roleplay personas are not independent alternatives: personas retain the Assistant-associated feature core while progressively differentiating from it across layers, starting from operational machinery towards behavioral and stylistic features. Meanwhile, generated story characters lack the Assistant-associated core. Both Story and Roleplay can be distinguished from the Assistant with Immersive Simulation Mode. However, the Assistant can sometimes enter or slowly drift into it even in the default setting.

## Metadata
- **Published**: 2026-08-08T01:49:30Z
- **Authors**: Adelaide Danilov, Aria Nourbakhsh, Oleksandr Marchenko Breneur, Salima Lamsiyah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07852v1)