---
title: Post-Training Language Models for Gold-Medal Performance in Coding Competitions
url: http://arxiv.org/abs/2609.02849v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_17-33-37Z_Post_TrainingLanguageModelsforGold_MedalPerformanc.md
generated_at: 2026-09-02 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a post‑training pipeline that combines large‑scale problem curation, synthetic reasoning traces, supervised fine‑tuning and reinforcement learning to achieve gold‑medal performance in competitive programming. Using 22 000 curated problems, the authors train two models—Nemotron‑3‑Nano‑CC (30B) with SFT+RL and Nemotron‑3‑Ultra‑CC (550B) with SFT alone—and evaluate them on IOI 2025. The Nano‑CC model reaches 468 points after GenCorrect, surpassing the gold threshold of 438.3, while Ultra‑CC scores 535.4 out of 600, exceeding both the gold and top human score.

## Key Takeaways
- Post‑training fine‑tuning combined with reinforcement learning enables Nano‑CC to exceed the IOI 2025 gold threshold by a large margin.
- The GenCorrect test‑time compute strategy iteratively generates and refines diverse solutions, delivering substantial gains over baseline post‑training models.
- An AI system has surpassed the highest‑scoring human contestant on an IOI problem set, demonstrating that LLM reasoning can outperform elite programmers.

## Context
Competitive programming remains a benchmark for large language model reasoning, yet previous work focused mainly on pre‑training or limited fine‑tuning. This study shows that systematic post‑training and test‑time compute strategies can push models beyond human performance under realistic competition constraints such as internet access and submission limits.

## Implications
The results suggest that specialized LLM pipelines can be deployed in real‑world coding competitions, offering a new benchmark for model capability. Industry practitioners may adopt similar approaches to create domain‑specific AI assistants that rival top human competitors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02849v1)
