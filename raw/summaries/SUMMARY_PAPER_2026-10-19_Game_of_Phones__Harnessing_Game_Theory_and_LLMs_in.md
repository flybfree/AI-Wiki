---
title: Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams
url: http://arxiv.org/abs/2610.26781v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_17-35-02Z_GameofPhones_HarnessingGameTheoryandLLMsin_BotWars.md
generated_at: 2026-10-19 23:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a game-theoretic framework that enables large language models to learn adaptive counter-strategies for scam-baiting interactions without requiring fine-tuning. By modeling scammer-baiter interactions as a two-player game with empirically grounded strategies and utility functions, the authors demonstrate that adaptive strategy selection achieves 28.9–79.7% closer alignment to Nash equilibrium compared to non-adaptive baselines across 300 simulated dialogues and three LLM architectures.

## Key Takeaways
- The framework addresses a critical gap in existing anti-scam countermeasures, which impose no resource cost on perpetrators, by proposing strategic scam-baiting where automated agents actively engage scammers to deplete their operational capacity, requiring dynamic strategy adaptation that static rule-based systems cannot provide.
- The game-theoretic model formalizes scammer-baiter interactions using Nash equilibrium as a benchmark for evaluating learned behaviour, allowing LLMs to learn effective counter-strategies purely through in-context experience rather than costly fine-tuning processes, making the approach scalable and accessible.
- The authors release an annotated dataset of 300 dialogues with turn-level strategy labels and utility scores, providing a reproducible benchmark for evaluating adaptive strategy selection across multiple LLM architectures, with results showing consistent improvements in equilibrium alignment across all tested models.

## Context
This work sits at the intersection of computational game theory and applied LLM reasoning, addressing a real-world adversarial problem where phone scams impose substantial and growing costs on individuals and financial systems worldwide. The paper contributes to the broader research direction of using LLMs as strategic agents in competitive environments, demonstrating that in-context learning can substitute for expensive model fine-tuning when the task structure can be formalized as a game with well-defined utility functions and strategy spaces.

## Implications
For practitioners in telecommunications security and fraud prevention, this framework offers a deployable approach to automatically adapt baiting strategies against evolving scam tactics without retraining models, reducing operational costs while increasing effectiveness. For the AI research community, the released dataset and game-theoretic evaluation methodology provide a template for benchmarking strategic reasoning in LLMs, potentially extending to other adversarial domains such as negotiation, cybersecurity, and automated negotiation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26781v1)
