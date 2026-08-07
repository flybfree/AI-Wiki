# Summary: 2026-08-06_09-43-04Z_WhenSelf_EvolutionBackfires_Pre_CommitGatingagains.md
Saved: 2026-08-06 20:35
Source: 2026-08-06_09-43-04Z_WhenSelf_EvolutionBackfires_Pre_CommitGatingagains.md
Model: None

---

## Summary  
Self‑evolving language model agents improve by distilling reusable skills from their execution histories, yet the authors discover that this process is not monotonic: after a certain pool size new skills actually degrade performance. They formalize a capability‑contamination phase transition caused by defective skills contaminating later ones through cross‑round reference material, showing that such contamination is structurally irreversible. To mitigate this, they introduce Verifier‑as‑Gatekeeper (VaG), a progressive trust hierarchy with three heterogeneous critics that pre‑commit skill admission and a marginal‑gain subset selector that eliminates the worst offenders before runtime. The study demonstrates on Terminal‑Bench 2 that unconditional accumulation peaks then drops, while VaG consistently improves, achieving 72 % pass@1 with a much smaller pool.

## Key Contributions  
- [Finding 1] A capability‑contamination phase transition occurs when the skill pool exceeds a critical size, causing newly added skills to degrade overall performance.  
- [Finding 2] The contamination is structurally irreversible; removing a source skill after its descendants have been distilled cannot fully recover lost performance.  
- [Finding 3] Verifier‑as‑Gatekeeper (VaG) mitigates the issue via a three‑criteria trust hierarchy and marginal‑gain subset selection, yielding consistently higher performance across benchmarks.

## Methodology  
The authors first simulate self‑evolving agents on Terminal‑Bench 2, accumulating skills round‑by‑round while tracking performance. They then introduce VaG: each skill passes through three critics—structural validity (syntactic correctness), behavioral harmlessness (no harmful side effects), and semantic consistency (logical coherence)—before being added to the runtime context. A marginal‑gain subset selector removes a minimal set of skills that cause the largest performance drop, ensuring only beneficial skills reach execution.

## Results  
Unconditional skill accumulation on Terminal‑Bench 2 peaks at ~80 % pass@1 and then declines sharply as the pool grows, with post‑hoc removal of culprit skills recovering only ~5 % of the loss. VaG eliminates this degradation, achieving a stable 72 % pass@1 with a pool roughly five times smaller. Ablation studies confirm that each critic intercepts distinct classes of harmful skills, and the frozen skill set transfers positively to four additional backbones and a second benchmark without re‑evolution.

## Significance  
Understanding the irreversible nature of skill contamination provides a theoretical foundation for designing safer self‑evolving agents. VaG’s pre‑commit gating strategy offers a practical framework that can be applied across diverse LLM applications, reducing risk while preserving capability gains.

## Related Concepts  
- Self‑evolution in LLMs  
- Skill distillation and reuse  
- Capability contamination / phase transition  
- Irreversible skill inheritance  
- Verifier‑as‑Gatekeeper (VaG) hierarchy  
- Marginal‑gain subset selection  
- Structural validity, behavioral harmlessness, semantic consistency  

These sections collectively illustrate the problem, its root cause, and a robust solution that safeguards agent performance.
