---
title: </think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination
url: http://arxiv.org/abs/2609.03633v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_10-25-23Z_think_Doesn_tStopReasoning_AnalysisofSpuriousCoTTe.md
generated_at: 2026-09-03 20:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates a phenomenon called spurious CoT termination that occurs when an end‑of‑think token (EoT) is injected to force a reasoning‑to‑answering transition in large language models. It shows that the EoT does not always cleanly separate the two phases, and that additional reasoning can continue into the answer segment, lengthening it. The authors propose Exit‑token Attention Biasing (EAB) as an intervention that reduces this issue.

## Key Takeaways
- Spurious CoT termination happens when the model continues reasoning after the EoT is injected, causing a longer answering phase than intended.  
- Insufficient attention to the injected EoT token allows the model’s internal mechanisms to keep generating reasoning tokens into what should be the answer block.  
- Attention‑biasing toward the EoT significantly reduces spurious termination and shortens the answering span across multiple models and benchmarks.

## Context
Chain‑of‑thought prompting has become a standard technique for improving large language model performance on complex tasks, but training‑free early‑exit methods aim to make reasoning more efficient. These methods often rely on inserting markers like EoT to signal when to stop generating thoughts and start producing answers, yet their effectiveness is limited by the observed spurious continuation.

## Implications
For practitioners developing automated reasoning systems, this research highlights that simply adding a token does not guarantee desired behavior; attention mechanisms must be tuned accordingly. The findings suggest that future early‑exit strategies should incorporate bias toward termination tokens to ensure clean transitions and avoid unnecessary computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03633v1)
