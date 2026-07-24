# Summary: 2026-07-23_01-41-17Z_REFACT_AdaptiveFactRestatementforCompactandFaithfu.md
Saved: 2026-07-24 02:21
Source: 2026-07-23_01-41-17Z_REFACT_AdaptiveFactRestatementforCompactandFaithfu.md
Model: None

---

## Summary  
The paper REFACT addresses the problem of long‑form reasoning in large language models, where traces may drift into unsupported inferences due to sparse, noisy, or conflicting evidence. It proposes an adaptive fact‑restatement citation framework that decides both when a reasoning step needs grounding and at what granularity source facts should be restated, thereby avoiding both unsupported inference and indiscriminate copying. This approach reduces token consumption while preserving answer‑bearing evidence in the trace.

## Key Contributions  
- REFACT introduces an adaptive fact‑restatement mechanism that dynamically decides when to ground reasoning steps.  
- The two‑stage SFT‑to‑RL training optimizes citation utility, rewarding well‑formed, source‑traceable, and answer‑sufficient facts.  
- Experiments on LongBench, LV‑Eval, and ConFiQA show improved long‑context QA, higher counterfactual faithfulness scores, and a substantial reduction in token usage.

## Methodology  
The authors train a model to generate reasoning traces that include citations. First, supervised fine‑tuning aligns generation with factual correctness. Second, reinforcement learning refines the trace by rewarding citation‑utility: citing facts that are useful for local inference and answer generation while penalizing redundant or unsupported restatements. The framework restates facts only when they support a specific inference step, producing denser traces without sacrificing faithfulness.

## Results  
On LongBench, REFACT cuts token consumption by roughly 30 % while maintaining or improving accuracy scores; on LV‑Eval it raises counterfactual faithfulness metrics; and on ConFiQA it yields reasoning traces with fewer restated facts but higher answer coverage. Ablation studies confirm that the citation‑utility reward is essential for achieving these gains.

## Significance  
By making citations purposeful and compact, REFACT advances the efficiency of chain‑of‑thought reasoning, enabling models to produce traceable yet concise explanations—critical for scalable LLM deployment where token limits are a practical constraint. The method bridges the gap between faithfulness and brevity in long‑context tasks.

## Related Concepts  
Chain‑of‑thought prompting, fact grounding, reinforcement learning from human feedback (RLHF), citation‑utility reward, adaptive restatement, long‑context QA evaluation benchmarks.
