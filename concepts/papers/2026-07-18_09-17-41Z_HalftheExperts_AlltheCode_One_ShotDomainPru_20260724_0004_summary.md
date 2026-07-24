# Summary: 2026-07-18_09-17-41Z_HalftheExperts_AlltheCode_One_ShotDomainPruningofM.md
Saved: 2026-07-24 00:04
Source: 2026-07-18_09-17-41Z_HalftheExperts_AlltheCode_One_ShotDomainPruningofM.md
Model: None

---

## Summary  
The paper investigates how many sub‑networks (experts) can be removed from large, open‑weight mixture‑of‑experts language models while preserving their ability to generate correct code. By pruning two distinct MoE families—Qwen3.6‑35B‑A3B and Gemma‑4‑26B‑A4B—under five selection strategies, the authors demonstrate that half of the experts can be eliminated with no measurable drop in coding performance, while the loss is confined to non‑coding capabilities. The study also shows that standard compression metrics such as perplexity are misleading for this task and that a lightweight fine‑tune can partially recover what aggressive pruning loses. Overall, the work establishes that expert pruning is feasible but must be validated against the specific downstream coding task it will serve.

## Key Contributions  
- Finding 1: Half of the experts in both Qwen3.6‑35B‑A3B and Gemma‑4‑26B‑A4B can be removed without a statistically detectable loss on the primary code benchmark, indicating that many expert capacities are irrelevant to coding tasks.  
- Finding 2: The optimal pruning strategy differs between the two models; a recipe validated for one family does not generalize to the other, highlighting the need for model‑specific validation.  
- Finding 3: Standard compression metrics like perplexity overestimate damage, and a single‑shot repair process can fully eliminate the penalty of aggressive pruning when evaluated with task‑specific feedback.

## Methodology  
The authors selected two open‑weight MoE models from different architectural families and applied five expert‑pruning strategies: random removal, half‑expert removal, guided selection based on importance scores, causal expert importance (which respects token generation order), failure attribution (identifying which experts cause errors), and an agentic evaluation where each model repairs its own failures after execution. After pruning, they measured coding correctness on a benchmark, perplexity, memory usage, and compared the results with equivalent quantization levels.

## Results  
Aggressive pruning that removes half of the experts leaves coding accuracy unchanged while reducing memory consumption by roughly 50 %. Perplexity scores rise only slightly, suggesting that the metric is not sensitive to this specific compression. A lightweight fine‑tune recovers about half of the lost performance, indicating that a modest post‑pruning adjustment can mitigate degradation. When the full model is quantized to match the pruned memory footprint, the two approaches are comparable; however, aggressive pruning only outperforms quantization when the per‑weight bit depth drops below three bits.

## Significance  
This research proves that large MoE models can be significantly compressed for coding assistance without harming their core function, offering a path to make these models runnable on consumer hardware. It also warns against relying solely on perplexity as an evaluation metric and underscores the importance of task‑specific validation when pruning or quantizing language models.

## Related Concepts  
- Mixture‑of‑Experts (MoE) architectures that activate a subset of subnetworks per token.  
- One‑shot domain pruning, which removes experts without retraining.  
- Quantization techniques that reduce weight precision to save memory.  
- Fine‑tuning as a lightweight recovery method after aggressive compression.
