---
title: ICO: Enhancing Semantic-Shift Jailbreaks via Iterative Context Optimization
url: http://arxiv.org/abs/2608.03210v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_06-48-17Z_ICO_EnhancingSemantic_ShiftJailbreaksviaIterativeC.md
generated_at: 2026-08-05 01:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the limited effectiveness of semantic‑shift jailbreaks and shows that they fail because contexts do not consistently induce the needed semantic shifts. By analyzing context capabilities, the authors introduce Iterative Context Optimization (ICO), a black‑box framework that iteratively refines contexts using model feedback to boost attack success rates. Their experiments on three datasets with eight foundation models demonstrate ICO outperforms all baselines, achieving an average success rate of 74.6%.

## Key Takeaways
- Contexts vary in their ability to trigger semantic shifts; stronger‑shift contexts guide models toward harmful meanings more reliably.
- The ICO framework systematically extracts these effective context characteristics and uses them iteratively with model feedback to improve jailbreak performance.
- On the evaluated datasets, ICO reaches an average attack success rate of 74.6%, surpassing eight state‑of‑the‑art baselines.

## Context
Semantic‑shift attacks exploit how foundation models interpret word meanings within surrounding text, making them a key vulnerability in large language systems. Understanding which contextual cues reliably induce harmful interpretations is essential for both security research and responsible model deployment.

## Implications
This work highlights the importance of context design in mitigating jailbreak vulnerabilities, offering practitioners a systematic method to strengthen safety mechanisms. For industry users, adopting ICO can lead to more robust models that resist semantic‑shift attacks without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03210v1)
