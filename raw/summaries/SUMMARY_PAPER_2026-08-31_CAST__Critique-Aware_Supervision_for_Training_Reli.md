---
title: CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents
url: http://arxiv.org/abs/2608.30147v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_01-59-51Z_CAST_Critique_AwareSupervisionforTrainingReliableL.md
generated_at: 2026-08-31 21:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CAST, a critique‑aware training framework that turns sparse task outcomes into action‑level supervision for learning reliable long‑horizon tool‑calling agents. By analyzing agent trajectories to generate structured rationales about action validity, CAST improves reliability across domains and outperforms GPT‑OSS‑120B by over 10 % on Retail tasks while adding a further 9 % gain in Telehealth.

## Key Takeaways
- CAST converts task outcomes into detailed critiques that explain why specific actions are valid or invalid, providing supervision for both learning and policy optimization.  
- The framework uses structured rationales to handle partial observability and long intertwined trajectories typical of real‑world agent behavior.  
- Fine‑tuning Qwen3 models on dynamic tool‑calling benchmarks with CAST yields measurable reliability improvements that exceed prior state‑of‑the‑art methods.

## Context
Current LLM agents often fail to produce reliable, interpretable actions in long, interactive environments where a single error can cascade. Existing approaches rely on prompt‑based critiques or lack systematic verification rationales, limiting robustness and explainability.

## Implications
CAST demonstrates that critique‑aware training can substantially boost the robustness of deployed LLM agents, offering industry practitioners a practical path to safer autonomous tools. This could reduce costly errors in high‑stakes applications such as telehealth and retail operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30147v1)
