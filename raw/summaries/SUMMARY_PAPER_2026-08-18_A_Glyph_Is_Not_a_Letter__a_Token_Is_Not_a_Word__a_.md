---
title: A Glyph Is Not a Letter, a Token Is Not a Word, a Space Is Not a Space: What the Units of Voynichese Are Not
url: http://arxiv.org/abs/2608.17096v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_20-05-12Z_AGlyphIsNotaLetter_aTokenIsNotaWord_aSpaceIsNotaSp.md
generated_at: 2026-08-18 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper challenges the common assumptions that Voynichese glyphs correspond to letters, tokens correspond to words, and blanks are simple spaces. Using a Zandbergen-Landini transliteration with matched controls, it finds none of these mappings hold, revealing instead a quire‑stable scale of multi‑symbol units.

## Key Takeaways
- The conditional entropy of glyph regularity is 2.7 bits versus about 3.5 for Latin, Italian and English, indicating glyphs are not simple one‑to‑one substitutes but part of larger recurring units.
- Token order has under 1% entropy, lower than any matched control (2–10%), showing tokens form a plausible vocabulary yet the identity of each token strongly predicts the next.
- Blanks behave like internal junctures: they are physically narrower on the page and are crossed by learned units even when spaces are erased, forming an open, hapax‑rich vocabulary with 70% singleton types.

## Context
This study matters for AI research because it demonstrates that linguistic modeling often rests on untested structural assumptions; without empirical validation such models may misinterpret data. The findings highlight the need for quantitative checks of tokenization and glyph semantics in historical or encoded texts, a principle increasingly relevant as machine learning approaches are applied to ancient scripts.

## Implications
For practitioners working with unknown alphabets, this research underscores that any translation pipeline must first measure entropy and mutual information rather than assume correspondence. The results suggest developing models that respect quire‑level units and edge‑glyph coupling, which could improve accuracy in deciphering similarly anomalous corpora.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17096v1)
