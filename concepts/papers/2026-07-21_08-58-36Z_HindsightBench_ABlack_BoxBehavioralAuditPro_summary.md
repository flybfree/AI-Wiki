# Summary: 2026-07-21_08-58-36Z_HindsightBench_ABlack_BoxBehavioralAuditProtocolfo.md
Saved: 2026-07-24 00:37
Source: 2026-07-21_08-58-36Z_HindsightBench_ABlack_BoxBehavioralAuditProtocolfo.md
Model: None

---

## Summary  
The paper introduces **HindsightBench**, a black‑box audit protocol that lets researchers evaluate parametric hindsight leakage in time‑indexed LLM decision tasks without needing backtests, log probabilities, or corpus access. It does so by manipulating dates across four arms and probing memory recall while measuring six per‑model metrics to detect behavioral leakage. The authors apply the method to 15 models on a vintage‑correct macro panel, revealing three distinct patterns of hindsight behavior. This work provides a cheap, operational audit that can be reproduced with one command.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Date‑trigger reflex correlates with training generation rather than model scale; it appears only in the latest 2026‑generation models and switches on within a single vendor lineage.  
- [Finding 2] Effective knowledge cutoffs span about 22 months across vendors, often preceding official release dates by up to eight months, undermining calendar‑window placebo designs.  
- [Finding 3] Audit results are not invariant to serving configuration; BF16 serving of an FP8‑referenced model destabilizes trigger estimates while AWQ‑INT4 preserves them, and provider‑locked reasoning regimes cause probe non‑convergence.

## Methodology  
The authors built HindsightBench by constructing a four‑arm date‑manipulation matrix (revealed/date‑only/masked/transplanted) that feeds time‑indexed decision tasks to LLMs. Two memory probes are used: one recovers dates, the other recalls outcomes. Six per‑model metrics—trigger strength, transplant effect, post‑cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and recall‑accuracy dissociation coefficient—are measured. Identifiability is gated where data dependence matters. The protocol requires operational settings such as pin quantization, thinking regime, parser disclosure, and sampling policy.

## Results  
Applied to 15 models from seven vendors on a 258‑node vintage‑correct macro panel, the audit produced three headline patterns described above. Dollar costs per model were measured; transcripts and one‑command regeneration scripts are released. The protocol requires only probe‑level cost, no backtests or corpus access.

## Significance  
Hindsight leakage can bias financial decisions by leaking realized outcomes into historical data; detecting it cheaply is crucial for trust in LLM deployments. This audit enables systematic monitoring across models and vendors without expensive infrastructure.

## Related Concepts  
parametric hindsight, time‑indexed decision tasks, black‑box auditing, date manipulation matrix, memory probes, knowledge cutoff inference, serving configuration effects, MoE architecture influence.
