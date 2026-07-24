# Summary: 2026-07-22_06-19-06Z_SilentFailuresinMultimodalAgenticSearch_ADiagnosti.md
Saved: 2026-07-24 01:37
Source: 2026-07-22_06-19-06Z_SilentFailuresinMultimodalAgenticSearch_ADiagnosti.md
Model: None

---

## Summary  
The paper investigates silent failures in multimodal agentic search, where surface‑level accuracy masks hidden reliability issues that can cause agents to produce correct answers despite flawed reasoning. By introducing a diagnostic taxonomy and evaluating trajectory‑level correctness across multiple models, the authors reveal systematic blind spots that degrade performance beyond final‑answer metrics.

## Key Contributions  
- Introduce a six‑category taxonomy covering modality shortcuts, phantom grounding, wrong‑evidence‑right‑answer cases, over‑retrieval laundering, cross‑modal contradiction, and provenance hallucination.  
- Build a trajectory‑level diagnostic pipeline that assesses both answer correctness and evidence‑grounding quality under a unified ReAct scaffold.  
- Demonstrate via experiments on MMSearch‑Plus trajectories that surface accuracy consistently overestimates true trajectory‑level correctness; silent failures are capability‑dependent and often shift rather than disappear.

## Methodology  
The authors collected MMSearch‑Plus trajectories, applied the taxonomy to each step of the search process, and used a unified ReAct framework to evaluate both final answers and intermediate evidence. They performed cross‑judge validation, blank‑image stress tests, and tool ablations to isolate failure modes and ensure robustness across models.

## Results  
Surface accuracy consistently overestimates true trajectory‑level correctness; silent failures appear as modality shortcuts and provenance hallucination in some models. Error rates shift across models, and tool ablations show that certain failures disappear when tools are disabled, confirming their conditional nature.

## Significance  
The work highlights the limitation of focusing only on final answer accuracy for multimodal agents, urging evaluation at intermediate stages to improve robustness and reliability. It provides a diagnostic taxonomy that can guide future research on safer agentic search systems.

## Related Concepts  
Multimodal agentic search, ReAct paradigm, trajectory‑level evaluation, silent failure taxonomy, evidence grounding, cross‑judge validation.
