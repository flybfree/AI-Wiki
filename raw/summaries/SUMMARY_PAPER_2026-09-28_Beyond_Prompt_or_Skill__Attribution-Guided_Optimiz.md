---
title: Beyond Prompt or Skill? Attribution-Guided Optimization of Modular LLM Programs
url: http://arxiv.org/abs/2609.32492v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_11-35-35Z_BeyondPromptorSkill_Attribution_GuidedOptimization.md
generated_at: 2026-09-28 20:47
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces SPARO, a unified framework that jointly optimizes task instructions, reusable skill blocks, and routing rules in large language model programs to address the limitations of existing methods that focus on isolated components. By employing controlled counterfactual evaluations to attribute failures probabilistically to specific modules, SPARO applies targeted mutations rather than global prompt rewriting. The approach consistently outperforms both prompt-centered and skill-centered baselines across multiple benchmarks, demonstrating that effective optimization requires not only discovering useful knowledge but also determining its storage location and activation timing.

## Key Takeaways
- SPARO utilizes a probabilistic responsibility distribution derived from controlled counterfactual evaluations to identify which component—prompt, skill, or routing rule—is most responsible for performance failures, enabling precise attribution rather than heuristic guessing.
- Unlike prior methods that treat prompts and skills as separate optimization targets, SPARO operates within a unified framework that simultaneously refines task instructions, modular skill blocks, and the policies governing their activation, leading to more coherent program improvements.
- Empirical results across five benchmarks and five worker models show that SPARO consistently surpasses existing bas

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32492v1)
