---
title: SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models
url: http://arxiv.org/abs/2610.17727v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_05-03-43Z_SkillScreen_High_RecallScreeningofMaliciousAgentSk.md
generated_at: 2026-10-14 00:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillScreen introduces a compact decision model designed to directly score the maliciousness of agent skill definitions (SKILL.md files) in a single forward pass, addressing the challenge that legitimate automation instructions and malicious agent behaviors can appear deceptively similar. The model achieves 99% recall on unseen attack families while flagging only 20-25% of benign skills, substantially outperforming word-level classifiers and prompted LLM judges in both detection accuracy and review burden reduction.

## Key Takeaways
- SkillScreen demonstrates that a task-trained decision model can achieve 99% recall on unseen attack families while maintaining a manageable false-positive rate of 20-25% on benign skills, significantly outperforming both word-level classifiers and prompted LLM judges tested under the same evaluation protocol on MaliciousSkillBench.
- Under identical training protocols, SkillScreen generalizes better to unseen sources than a fully fine-tuned encoder, suggesting that purpose-built decision models trained specifically for the screening task can outperform general-purpose fine-tuned architectures in transfer robustness.
- A critical limitation emerges: while the model recognizes new attack patterns effectively, unfamiliar benign sources sharply increase false positives, revealing that high recall on novel attacks does not guarantee reliable screening when the benign distribution shifts, highlighting a fundamental distributional sensitivity in skill screening systems.

## Context
As AI agent ecosystems expand, agent skills that convert natural-language instructions into executable actions have become a primary attack surface for security threats. The ambiguity between legitimate automation and adversarial behavior makes traditional keyword-based or heuristic screening inadequate, while prompted LLM judges introduce latency and cost overheads impractical for production pipelines. This paper sits at the intersection of AI safety, adversarial robustness, and practical security engineering, addressing a gap where existing detection methods either miss attacks or overwhelm human reviewers with false alarms.

## Implications
For practitioners deploying agent frameworks at scale, SkillScreen demonstrates that compact, task-specific decision models can serve as high-recall first-pass filters that dramatically reduce the human review burden without sacrificing detection coverage, making security screening feasible in production environments. However, the sharp increase in false positives on unfamiliar benign sources signals that organizations must invest in distribution-aware training data and ongoing calibration rather than treating a single screening model as a universal solution, underscoring the need for continuous monitoring and adaptive retraining strategies in evolving agent ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17727v1)
