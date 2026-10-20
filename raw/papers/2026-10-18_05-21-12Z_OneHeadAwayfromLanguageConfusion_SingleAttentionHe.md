---
title: One Head Away from Language Confusion: Single Attention Heads Across Model Families
published: 2026-10-18T05:21:12Z
authors: Jiwon Jeong, Anjelo Jann Laroza, Chaewoon Yoon, Arjun Pillai, Pranav Kokati, Christian Hoang, Seunghyeok Hong
url: http://arxiv.org/abs/2610.25026v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Head Away from Language Confusion: Single Attention Heads Across Model Families

## Abstract
Large language models sometimes reply in an unexpected language, a failure known as language confusion. We ablate individual attention heads in 12 model checkpoints spanning seven model series, using FLORES-200 continuations in five languages and Language Confusion Benchmark (LCB) chat replies. In ten models, zeroing one head causes substantially more departures from the expected language than zeroing any other head in its layer; its LCB pass-rate drop persists, though reduced, under mean ablation. Seven heads move 8.0 to 51.5 percent of all FLORES continuations out of the prompt's language, versus at most 1.4 percent for other same-layer heads; the other three mainly affect explicitly requested languages. These seven heads matter less in base models given plain text. In two models, replacing the values a head reads at the requested-language name with another language's mean makes replies fail and shifts some into that language, unlike a random change of equal size. Replacing a head's output with another language's mean redirects 84 to 99 percent of scored non-English monolingual LCB replies into that language in five models. Yet the requested language's mean improves crosslingual replies beyond every control head only in the two Gemma models, whose baselines are low. Code and results are available in the public repository at https://github.com/christian-hoang-04/anonymous-release.

## Metadata
- **Published**: 2026-10-18T05:21:12Z
- **Authors**: Jiwon Jeong, Anjelo Jann Laroza, Chaewoon Yoon, Arjun Pillai, Pranav Kokati, Christian Hoang, Seunghyeok Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25026v1)