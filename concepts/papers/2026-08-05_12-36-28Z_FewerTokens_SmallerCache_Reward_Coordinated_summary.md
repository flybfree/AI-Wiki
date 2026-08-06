# Summary: 2026-08-05_12-36-28Z_FewerTokens_SmallerCache_Reward_CoordinatedEfficie.md
Saved: 2026-08-05 20:35
Source: 2026-08-05_12-36-28Z_FewerTokens_SmallerCache_Reward_CoordinatedEfficie.md
Model: None

---

## Summary  
Large Reasoning Models (LRMs) generate extensive chain‑of‑thought (CoT) steps that inflate inference cost, and their KV‑cache compression is typically applied uniformly without regard to the value of each step. This paper introduces ReCo, a reward‑coordinated framework that learns per‑step scores to jointly shrink the cache, penalize redundant tokens, and stop early when reasoning is reliable. By aligning cache deletion with process reward, ReCo reduces token usage and latency while preserving accuracy.

## Key Contributions  
- [Finding 1] High‑reward steps tolerate context loss better than low‑reward ones.  
- [Finding 2] Compression savings are offset by increased token generation caused by a smaller cache.  
- [Finding 3] A single process reward can coordinate both sides of the reasoning trajectory.

## Methodology  
The authors propose ReCo, a lightweight estimator that scores each completed step based on its reward. The score drives three mechanisms: (1) reward‑adaptive KV‑cache compression that shrinks retained cache aggressively at high‑reward steps and conservatively at low ones; (2) a banded penalty on reflection tokens to curb redundant generation; and (3) confidence‑based early stopping that triggers when the model’s reasoning is deemed reliable.

## Results  
Across three reasoning models and six benchmarks, ReCo reduces generated tokens by 37‑65% and shortens end‑to‑end latency by a factor of 2.08×–2.35× relative to full CoT, while accuracy changes remain below 1%. The compression is evaluated both in token count and runtime.

## Significance  
Efficient reasoning is essential for scaling large models; ReCo demonstrates that intelligent coordination between cache management and generation can achieve substantial savings without sacrificing performance, providing a template for future efficient inference pipelines.

## Related Concepts  
KV‑cache, chain‑of‑thought (CoT), process reward, token compression, early stopping, reflection tokens, confidence estimation.
