title: "Summary: 2026-06-29_17-50-54Z_ScalingtheHorizon_NottheParameters_ReachingTrillio.md"
# Summary: 2026-06-29_17-50-54Z_ScalingtheHorizon_NottheParameters_ReachingTrillio.md
Saved: 2026-06-30 01:01
Source: 2026-06-29_17-50-54Z_ScalingtheHorizon_NottheParameters_ReachingTrillio.md
Model: None

---


## Summary  
The paper introduces Agents‑A1, a 35B Mixture‑of‑Experts agentic model that reaches trillion‑parameter performance by scaling the agent horizon rather than increasing model size. It achieves this through long‑horizon trajectories of average 45K tokens and a three‑stage training recipe combining full‑domain fine‑tuning, domain‑level teacher models, and multi‑teacher domain‑routed distillation. Agents‑A1 outperforms several trillion‑parameter benchmarks across multiple long‑horizon tasks. The work offers a practical path for scaling horizons with a 35B agent that can match or exceed the performance of 1T models.

## Key Contributions  
- Finding 1: Long‑horizon trajectories of average 45K tokens enable agents to encode extensive knowledge and reasoning.  
- Finding 2: A three‑stage training pipeline (full‑domain fine‑tuning, domain teacher models, multi‑teacher domain‑routed distillation) efficiently unifies six heterogeneous domains into a single deployable student model.  
- Finding 3: Agents‑A1 achieves leading scores on SEAL‑0 (56.4), IFBench (80.6), HiPhO (46.4), FrontierScience‑Olympiad (79.0), MolBench‑Bind (56.8) and remains competitive on SciCode (44.3), HLE (47.6) and BrowseComp (75.5).

## Methodology  
The authors approached the problem by first constructing a knowledge‑action infrastructure that links external knowledge sources, executable actions, observations, and verifier outcomes to generate long agentic trajectories. They then trained Agents‑A1 in three stages: (1) full‑domain supervised fine‑tuning of a 35B base model to align it with broad agentic behaviors; (2) creation of domain‑specific teacher models that capture specialized expertise; and (3) on‑policy distillation where the student receives knowledge from multiple teachers via salient vocabulary alignment, enabling efficient cross‑domain knowledge transfer.

## Results  
Agents‑A1 achieves leading scores across long‑horizon benchmarks: SEAL‑0 56.4, IFBench 80.6, HiPhO 46.4, FrontierScience‑Olympiad 79.0, MolBench‑Bind 56.8; it remains highly competitive on SciCode (44.3), HLE (47.6) and BrowseComp (75.5). These results demonstrate that a 35B agent can rival or surpass performance of trillion‑parameter models such as Kimi‑K2.6 and DeepSeek‑V4‑pro on long‑horizon tasks.

## Significance  
This work proves that scaling the agent horizon—through longer trajectories and heterogeneous abilities—can deliver performance comparable to massive model parameters, offering a more resource‑efficient path for deploying powerful agents. It highlights the importance of trajectory length as a design variable beyond raw model size, potentially reshaping future AI research on agentic capabilities.

## Related Concepts  
- Mixture-of-Experts (MoE) architectures  
- Agentic modeling and long‑horizon trajectories  
- On‑policy distillation with domain routing  
- Knowledge‑action infrastructure
