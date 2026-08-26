---
title: Investigating Knowledge Transfer Across Interactive Dialogue Games
published: 2026-08-25T01:47:31Z
authors: Filippo Momentè, Mir Nafis Sharear Shopnil, Andrea de Varda, Pavel Merinov, Raffaella Bernardi, Oswald Lanz, Alessandro Suglia, Alessandro Torcinovich
url: http://arxiv.org/abs/2608.23969v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Investigating Knowledge Transfer Across Interactive Dialogue Games

## Abstract
Dialogue games represent a challenging setting where complex cognitive skills are required to accomplish tasks while coordinating with other players. Considering that language represents an interface for both understanding the game rules and executing actions, it is reasonable to assume that training on a specific language game will enhance specific capabilities that might be relevant for other tasks as well. Motivated by this rationale, in this paper, we investigate how knowledge transfers across different dialogue games. We study transferability by finetuning LLM models on games from the clembench suite (Chalamalasetti et al., 2023) and performing two analyses: i) we derive a task-transferability graph using a binary integer optimization program from Zamir et al. (2018), using task performance as the main metric; and ii) we compute task vectors (Ilharco et al., 2022) for each game to study similarities across finetuned models and their task transferability. In our first analysis, we find that some games benefit more from transfer than finetuning, and that the visuospatial family (e.g., exploration games) transfers best. With our task vector analysis instead, we find that similarity-based approaches capture game-role relationships but almost no transferability patterns, suggesting that more complex metrics are required.

## Metadata
- **Published**: 2026-08-25T01:47:31Z
- **Authors**: Filippo Momentè, Mir Nafis Sharear Shopnil, Andrea de Varda, Pavel Merinov, Raffaella Bernardi, Oswald Lanz, Alessandro Suglia, Alessandro Torcinovich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23969v1)