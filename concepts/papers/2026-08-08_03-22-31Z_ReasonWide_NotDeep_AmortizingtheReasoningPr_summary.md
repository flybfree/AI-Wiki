# Summary: 2026-08-08_03-22-31Z_ReasonWide_NotDeep_AmortizingtheReasoningPremiumin.md
Saved: 2026-08-10 22:48
Source: 2026-08-08_03-22-31Z_ReasonWide_NotDeep_AmortizingtheReasoningPremiumin.md
Model: None

---

## Summary  
This paper addresses the high computational cost of reasoning in large language models by identifying that multi-step agentic tasks incur a significant token overhead due to redundant procedural derivations across episodes. The authors propose amortizing this "reasoning premium" through skill distillation, where compact natural-language procedures are extracted from existing task trajectories and injected into non-reasoning models as system prompts. By doing so, they reduce output tokens by 2.7–6x while eliminating reasoning traces entirely. Their approach enables non-reasoning models to recover up to 100% of the performance gap of reasoning-capable models on several benchmarks, surpassing them in two cases.

## Key Contributions  
- [Finding 1] The "reasoning premium" — a 3–6x increase in output tokens per episode due to repeated procedural re-derivation across episodes — is identified as the primary bottleneck limiting reasoning efficiency.  
- [Finding 2] A skill distillation method extracts and injects compact natural-language procedures from task trajectories, amortizing this cost into a one-time deployment cost rather than per-episode computation.  
- [Finding 3] The distilled skills recover 55–100%+ of the reasoning gap for GPT-5.4-mini on held-out tasks across four benchmarks, with zero reasoning tokens used at inference time.

## Methodology  
The authors approached the problem by analyzing existing task trajectories from training splits to identify recurring procedural knowledge. They compiled these into distilled natural-language skills and tested them in non-reasoning models via system prompt injection. The method was evaluated across four agentic benchmarks: ALFWorld, tau$^2$-bench telecom and retail, and SpreadsheetBench-Verified. Crucially, they compared skills distilled from reasoning-only trajectories versus paired reasoning/non-reasoning corpora to understand domain-specific effectiveness.

## Results  
The main results show that skill distillation reduces output tokens by 2.7–6x and eliminates reasoning traces entirely. The distilled skills recover 55% to over 100% of the performance gap for GPT-5.4-mini on held-out tasks across all four benchmarks, with gains exceeding those seen in pure reasoning modes on two of them. Notably, no reasoning tokens are generated at inference time — only distilled skill prompts are used. The residual gaps observed in telecom and SpreadsheetBench-Verified domains suggest that some tasks genuinely require per-instance deep search.

## Significance  
This work fundamentally shifts the paradigm from costly, repeated reasoning to efficient, pre-compiled procedural knowledge. By amortizing the reasoning premium into a one-time distillation step, it enables non-reasoning models to achieve near-reasoning performance at significantly lower computational cost. This is especially impactful for resource-constrained or real-time applications where token efficiency and latency matter.

## Related Concepts  
- Reasoning mode vs. distilled skills  
- Amortization of computational overhead  
- Task trajectory analysis  
- System prompt injection  
- Deep search vs. wide search in AI inference
