---
title: LOCI: A Locator-Critic with Refinement Loop
url: http://arxiv.org/abs/2608.30959v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_15-26-00Z_LOCI_ALocator_CriticwithRefinementLoop.md
generated_at: 2026-08-31 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Locator-Critic (LOCI), a training-free framework that separates visual search from evidence verification in vision-language models. By using an iterative refinement loop between a locator agent and a critic, LOCI improves the quality of retrieved image details, leading to state‑of‑the‑art gains on several complex benchmarks.

## Key Takeaways
- LOCI decouples visual search (Locator) from evidence evaluation (Critic), allowing each component to operate independently without retraining.  
- The iterative refinement loop progressively enhances the candidate evidence until it is sufficient for answering a question, reducing reliance on flawed perceptual grounding.  
- Results show significant accuracy improvements: Open‑weight models gain +12.1 on V*, +5.8 on HR‑Bench and +11.2 on VisualProbe‑Hard, while Gemini 2.5 Pro gains +8.9 on V* and comparable boosts on other tasks.

## Context
Vision‑language models often produce plausible but incorrect reasoning because they cannot pinpoint the exact visual information needed for a task. Traditional approaches treat search and verification as coupled steps, limiting flexibility and performance. LOCI’s architecture addresses this by providing a modular, self‑correcting pipeline that can be applied to any existing model.

## Implications
For researchers, LOCI offers a practical way to boost VQA capabilities without extensive fine‑tuning, encouraging more modular research designs. For industry practitioners, the framework translates into higher accuracy in real‑world applications such as medical imaging analysis and autonomous navigation where precise visual grounding is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30959v1)
