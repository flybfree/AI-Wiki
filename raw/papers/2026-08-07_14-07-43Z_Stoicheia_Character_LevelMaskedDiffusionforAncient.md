---
title: Stoicheia: Character-Level Masked Diffusion for Ancient Greek Textual Restoration, Parsing, and Metrical Scansion
published: 2026-08-07T14:07:43Z
authors: Eric Cullhed, Albin Thörn Cleland
url: http://arxiv.org/abs/2608.07249v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stoicheia: Character-Level Masked Diffusion for Ancient Greek Textual Restoration, Parsing, and Metrical Scansion

## Abstract
We introduce Stoicheia, a 405M-parameter character-level masked-diffusion encoder for Ancient Greek whose input factors into five aligned, independently maskable planes: letters, word and sentence boundaries, diacritics, capitalization, and punctuation. A single backbone can therefore restore lacunae, re-segment, accentuate, and punctuate unspaced text without task-specific retokenization. We pretrain it on an open, revision-pinned corpus of 380M words and release eleven checkpoints: ten rotated, decontaminated folds, guaranteeing that for any given literary passage at least one released model has never seen its text, and one with no exposure to documentary texts. Three experiments - reconstruction of damaged inscriptions and papyri, morphosyntactic tagging and dependency parsing, and macronization with metrical scansion - each carry a matched random-initialization control, isolating what character-level diffusion pretraining contributes: 5.6 CER points on inscription reconstruction, 12.9 LAS on parsing, and 6.0 points of balanced accuracy on macronization. On Ithaca's own test split, with identical frozen samples and strict scoring, Stoicheia reduces character error relative to both prior state-of-the-art systems, from 24.6 (Ithaca) and 23.5 (its 2025 Aeneas-framework successor) to 15.5, and raises top-1 accuracy from 63.0 and 64.0 to 74.5.

## Metadata
- **Published**: 2026-08-07T14:07:43Z
- **Authors**: Eric Cullhed, Albin Thörn Cleland
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07249v1)