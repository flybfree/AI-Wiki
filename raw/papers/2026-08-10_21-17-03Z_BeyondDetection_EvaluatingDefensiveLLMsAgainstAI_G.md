---
title: Beyond Detection: Evaluating Defensive LLMs Against AI-Generated Social Engineering in Live Turn-by-Turn Interaction
published: 2026-08-10T21:17:03Z
authors: Yuqiao Xu, Osama Zafar, Alexander Nemecek, Erman Ayday
url: http://arxiv.org/abs/2608.10239v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Detection: Evaluating Defensive LLMs Against AI-Generated Social Engineering in Live Turn-by-Turn Interaction

## Abstract
Generative AI makes social-engineering attacks more fluent, adaptive, and scalable, increasing the need for LLM-based de- fenders that can protect users during ongoing interactions. We ask whether such defenders identify the structural source of risk or merely react to surface cues. We formalize trust-chain localization: identifying whether an interaction fails at actor authority, asset control, verification sufficiency, or transaction path. We construct a controlled 300-case online-housing corpus spanning 20 scenario families, legitimate cases, four structural failure modes, and three surface conditions. Five defender models are evaluated on the same corpus in state- ful turn-by-turn and one-shot static settings, yielding 1,500 model-case evaluations per protocol and 3,000 in total. No model produced explicit unsafe compliance, yet defensive effectiveness varied sharply: intervention rates ranged from 0% to 96.3%. Protective action and correct structural localization were frequently decoupled, with models sometimes intervening while identifying the wrong trust component or recognizing a structural failure without taking protective action. Asset-control failures were a major localization bottleneck, surface sensitivity varied across models, and live-static differences were model-dependent. These findings show that safe-looking behavior alone is insufficient; live scam resistance must separately measure intervention, timing, structural localization, and false-positive behavior.

## Metadata
- **Published**: 2026-08-10T21:17:03Z
- **Authors**: Yuqiao Xu, Osama Zafar, Alexander Nemecek, Erman Ayday
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10239v1)