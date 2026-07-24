# Summary: 2026-07-21_09-56-58Z_ReasoningErrorfromKnownFact_Step_LevelSelf_Consist.md
Saved: 2026-07-24 00:58
Source: 2026-07-21_09-56-58Z_ReasoningErrorfromKnownFact_Step_LevelSelf_Consist.md
Model: None

---

## Summary  
The paper investigates factual hallucinations that arise in long reasoning traces of LLMs, focusing on context‑sensitive errors where the model knows the fact but misapplies it due to contextual interference. It proposes SSC‑GRPO, a step‑level self‑consistency group relative policy optimization method that assigns rewards based on self‑consistency scores across multiple rollouts. The approach improves detection and mitigation of these hallucinations while maintaining reasoning performance.

## Key Contributions  
- [Finding 1] Hallucinations in LLM reasoning are often context‑sensitive factual errors rather than pure knowledge gaps.  
- [Finding 2] Step‑level reward design using self‑consistency scores across multiple rollouts effectively captures error propagation.  
- [Finding 3] SSC‑GRPO achieves state‑of‑the‑art results on both math reasoning benchmarks and hallucination leaderboards.

## Methodology  
The authors conduct a fine‑grained analysis of LLM reasoning traces to identify where factual errors originate, then design an optimization framework that treats each reasoning step as a policy component. Self‑consistency scores are computed by comparing outputs across multiple rollouts for each step, and these scores feed into relative policy gradients to update the model’s reasoning behavior.

## Results  
Experimental results show SSC‑GRPO outperforms baselines on MATH and GSM8K math benchmarks and reduces hallucination rates on the Hallucination Leaderboard by 12.3 % compared to previous methods. The improvement is consistent across diverse models and prompt lengths.

## Significance  
By pinpointing context‑sensitive factual errors at the step level, SSC‑GRPO offers a principled way to align LLM reasoning with external knowledge, potentially leading to safer and more reliable AI assistants that minimize hallucinations without sacrificing performance.

## Related Concepts  
- Large Language Models (LLMs)  
- Reasoning traces  
- Hallucination detection  
- Self‑consistency scoring  
- Policy optimization  
- Context‑sensitive errors
