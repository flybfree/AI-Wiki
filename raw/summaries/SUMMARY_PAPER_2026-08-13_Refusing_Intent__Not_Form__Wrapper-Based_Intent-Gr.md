---
title: Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety
url: http://arxiv.org/abs/2608.13304v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_14-33-15Z_RefusingIntent_NotForm_Wrapper_BasedIntent_GroupSu.md
generated_at: 2026-08-13 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Wrapper-Based Intent-Group Supervision (WIFA) to address surface‑form shortcuts in LLM safety tuning where harmless prompts wrapped with the same structure are over‑refused while harmful ones slip through. The authors demonstrate that WIFA, combined with two fine‑tuning routes—WIFA-Boost and Anchored Group‑Consistent Refusal Training (A‑GCRT)—achieves stronger transformed‑harmful refusals and lower benign over‑refusal than baseline methods in Qwen and Llama settings.

## Key Takeaways
- WIFA automatically pairs wrapped harmful examples with structurally matched benign counterexamples without requiring external teacher labels or manual per‑wrapper intent annotations.  
- A‑GCRT regularizes refusal/compliance scores across same‑intent wrappers, placing harmful and benign groups on opposite sides of a margin to improve consistency.  
- In Qwen, WIFA-Boost yields the highest transformed‑harmful refusal rate, while A‑GCRT reduces OR‑Bench over‑refusal from 25.7 % to 17.4 %, surpassing reproduced baselines.

## Context
Current safety fine‑tuning often relies on human‑labeled data or surface cues that can lead to unintended behavior when prompts are wrapped, causing benign queries to be incorrectly flagged as unsafe. This creates a trade‑off between harmful refusal and benign over‑refusal, limiting the reliability of deployed models.

## Implications
The findings suggest that grouping intent by wrapper structure can guide model updates more effectively than treating each prompt independently, offering a scalable approach for safety tuning across diverse LLM deployments. Practitioners may adopt WIFA to balance safety improvements with reduced false positives in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13304v1)
