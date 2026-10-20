---
title: Understanding When Reflective Prompt and Skill Optimization Helps on Locally Served Reasoning Models: A Two-Model Study of GEPA and SkillOpt
published: 2026-10-19T08:45:07Z
authors: Andrea Giummarra, Carmelo Baglieri, Antonio Di Maria, Andrea Farruggio, Michele Piatto, Giovanni Micale
url: http://arxiv.org/abs/2610.26020v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding When Reflective Prompt and Skill Optimization Helps on Locally Served Reasoning Models: A Two-Model Study of GEPA and SkillOpt

## Abstract
Reflective text-space optimizers such as GEPA and SkillOpt have reported large gains on frontier and mid-size models. We test replication across two reasoning-native target-serving configurations: DeepSeek V4 Flash through DwarfStar and Qwen3.8-27B through LM Studio. For each target, we evaluate the same held-out tasks and four conditions - minimal baseline, GEPA prompt, SkillOpt skill, and manually engineered prompt - on HotpotQA (n=500 per condition) and MATH-500 (n=250). In the primary Qwen v2 rerun under the same frozen protocol, GEPA selects the HotpotQA seed and exactly reproduces baseline behavior, whereas SkillOpt's validation gain reverses into held-out degradation. On MATH-500, GEPA raises exact match from 0.828 to 0.904 while reducing latency but increasing token consumption, so lower response time does not imply lower token cost. DeepSeek likewise shows its strongest GEPA effect on MATH-500 (0.852 to 0.908). Across both targets, GEPA's strongest gains occur on MATH-500, while neither optimizer improves the HotpotQA baseline. Optimization is therefore task- and method-dependent, and validation gains may reverse on held-out evaluation. An earlier Qwen run is retained as serving-sensitivity evidence. These results suggest that textual headroom for a model-task pair and the observed effect of a text-space optimizer are more informative when decomposed into content/reasoning, answer-realization/evaluator alignment, and serving-completion/reliability. The cross-benchmark pattern further suggests that optimization may benefit from low-ambiguity, actionable evaluation signals.

## Metadata
- **Published**: 2026-10-19T08:45:07Z
- **Authors**: Andrea Giummarra, Carmelo Baglieri, Antonio Di Maria, Andrea Farruggio, Michele Piatto, Giovanni Micale
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26020v1)