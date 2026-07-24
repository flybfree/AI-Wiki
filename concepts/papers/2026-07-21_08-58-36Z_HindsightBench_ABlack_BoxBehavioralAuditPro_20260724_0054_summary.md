# Summary: 2026-07-21_08-58-36Z_HindsightBench_ABlack_BoxBehavioralAuditProtocolfo.md
Saved: 2026-07-24 00:54
Source: 2026-07-21_08-58-36Z_HindsightBench_ABlack_BoxBehavioralAuditProtocolfo.md
Model: None

---

## Summary  
HindsightBench is a black‑box behavioral audit protocol designed to profile parametric hindsight in any time‑indexed LLM decision task without requiring backtests, logprobs, or corpus access. It achieves this by chaining a four‑arm date‑manipulation matrix with dual memory probes (date recovery and outcome recall) that generate six per‑model metrics at probe‑level cost. The protocol is applied to 15 models from seven vendors on a vintage‑correct macro panel, revealing three headline patterns that suggest the existence of hidden parametric leakage.  

## Key Contributions  
- [Finding 1] The date‑trigger reflex tracks training generation rather than model scale: it is absent across open‑weight generations up to 70 B, appears only in 2026‑generation models, and switches on within a single vendor lineage (Qwen3 → Qwen3.6) at a fixed MoE architecture with 3 B active parameters.  
- [Finding 2] Effective knowledge cutoffs span roughly 22 months across vendors and precede vendor‑reported dates by up to eight months, invalidating calendar‑window placebo designs that assume a fixed cutoff.  
- [Finding 3] Audit results are not invariant to serving: BF16 serving of an FP8‑referenced model breaks the trigger estimate’s stability, whereas AWQ‑INT4 preserves it; a provider‑locked reasoning regime makes one probe non‑convergent, highlighting that operational choices can alter audit outcomes.  

## Methodology  
HindsightBench constructs a four‑arm date‑manipulation matrix (revealed/date‑only/masked/transplanted) and pairs it with two memory probes: one for date recovery and another for outcome recall. The protocol measures six metrics per model—trigger strength, transplant effect, post‑cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and a recall‑accuracy dissociation coefficient—while inserting explicit gates where identifiability depends on the data. To make the audit operational, the authors prescribe pinning quantization (e.g., BF16 serving) and a “thinking regime” that disables provider‑locked reasoning; they also disclose the parser implementation and sampling policy. The entire pipeline can be reproduced with a single command, returning frozen preregistrations, per‑model audit rows, measured dollar costs, transcripts, and one‑command regeneration of results.  

## Results  
The study evaluated 15 models across seven vendors on a 258‑node vintage‑correct macro panel. The three headline patterns identified are: (i) the date‑trigger reflex is generation‑specific, not scale‑dependent; (ii) effective cutoffs vary widely and lag vendor dates by up to eight months; (iii) serving configurations dramatically affect metric stability, with BF16‑served FP8 models showing unstable trigger estimates while AWQ‑INT4 retains them. The protocol’s operational requirements—pinning quantization and a thinking regime—are essential for reproducible findings. Dollar costs per model are reported, along with full transcripts that illustrate the probe interactions.  

## Significance  
HindsightBench provides a cheap, black‑box method to audit parametric hindsight in time‑indexed LLM decision tasks, enabling practitioners to detect hidden leakage without costly backtesting or logprob computation. The findings expose how training generation, vendor reporting, and serving choices interact, offering actionable insights for model design and deployment that can mitigate unintended bias.  

## Related Concepts  
parametric hindsight, time‑indexed decision tasks, black‑box audit protocol, date‑manipulation matrix, dual memory probes (date recovery, outcome recall), MoE architecture, quantization serving (BF16/FP8/AWQ‑INT4), knowledge cutoff, recall‑accuracy dissociation coefficient.
