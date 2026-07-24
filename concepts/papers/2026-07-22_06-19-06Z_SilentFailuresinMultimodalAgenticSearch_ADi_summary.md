# Summary: 2026-07-22_06-19-06Z_SilentFailuresinMultimodalAgenticSearch_ADiagnosti.md
Saved: 2026-07-24 01:27
Source: 2026-07-22_06-19-06Z_SilentFailuresinMultimodalAgenticSearch_ADiagnosti.md
Model: None

---

## Summary  
This paper investigates “silent failures” that occur when multimodal agentic search systems produce correct answers despite flawed or misleading intermediate steps, leading to a mismatch between surface accuracy and true trajectory‑level reliability. The authors introduce a diagnostic taxonomy of six failure modes—modality shortcuts, phantom grounding, wrong‑evidence‑right‑answer cases, over‑retrieval laundering, cross‑modal contradiction, and provenance hallucination—and build a unified ReAct‑style pipeline to evaluate both answer correctness and evidence grounding across MMSearch‑Plus trajectories. Experiments on four frontier multimodal models reveal that surface accuracy systematically overestimates the genuine reliability of the search process, indicating hidden failures are pervasive yet often undetected by standard benchmarks.

## Key Contributions  
- [Finding 1] A six‑category taxonomy that captures all known silent failure patterns in multimodal agentic search.  
- [Finding 2] A trajectory‑level diagnostic pipeline that jointly assesses answer correctness and evidence grounding under a ReAct scaffold.  
- [Finding 3] Empirical evidence that surface accuracy overestimates true trajectory‑level correctness, and that these silent failures are capability‑dependent and tend to shift rather than disappear.

## Methodology  
The authors collect MMSearch‑Plus trajectories from four state‑of‑the‑art multimodal models. Each trajectory is examined through the diagnostic pipeline: first, the final answer is checked for factual accuracy; second, evidence grounding quality is evaluated using the taxonomy categories. Cross‑judge validation compares model predictions across judges, while blank‑image stress tests and tool ablations isolate failures to specific components (e.g., vision encoder or retrieval module). This multi‑modal approach ensures that silent failures are not masked by surface‑level correctness.

## Results  
Surface accuracy consistently overestimates true trajectory‑level correctness; for example, models that hallucinate provenance often still receive correct answers but with low evidence quality. Cross‑judge analysis shows a systematic shift in failure patterns across models, indicating capability dependence. Tool ablations reveal that failures are not uniformly eliminated by disabling any single component, suggesting they arise from interactions between modalities.

## Significance  
Standard evaluation metrics ignore hidden reliability issues, leading to false confidence in agentic search systems. By diagnosing silent failures and quantifying their prevalence, this work provides a roadmap for more robust, trustworthy multimodal agents that can be reliably deployed in knowledge‑intensive tasks.

## Related Concepts  
multimodal agentic search, ReAct scaffold, silent failures, modality shortcuts, phantom grounding, wrong‑evidence‑right‑answer cases, over‑retrieval laundering, cross‑modal contradiction, provenance hallucination, trajectory‑level evaluation, blind‑image stress test, tool ablations, cross‑judge validation.
