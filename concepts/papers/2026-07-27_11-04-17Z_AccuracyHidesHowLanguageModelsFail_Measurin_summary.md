# Summary: 2026-07-27_11-04-17Z_AccuracyHidesHowLanguageModelsFail_MeasuringFailur.md
Saved: 2026-07-27 22:56
Source: 2026-07-27_11-04-17Z_AccuracyHidesHowLanguageModelsFail_MeasuringFailur.md
Model: None

---

## Summary  
The paper argues that language‑model benchmarks conflate two distinct measurement questions—whether a response reaches an evaluable state and whether its answer is judged correct—into a single accuracy score, which obscures the true nature of failures. To address this, it introduces a two‑layer evaluation framework that separates scorer‑independent execution evidence (termination, answer exposure, parseability, completion length) from scorer‑dependent correctness, demonstrating that matching output token budgets produce markedly different failure patterns across models.

## Key Contributions  
- [Finding 1] Execution mixtures differ sharply under matched token limits; e.g., Qwen MATH outputs terminate without a final answer in 49 of 450 cases versus only 5 of 300 DeepSeek MATH outputs.  
- [Finding 2] At the longer limit (8,192 tokens) no missing‑final length termination is observed for DeepSeek MATH, indicating that longer contexts mitigate this failure mode.  
- [Finding 3] Candidate‑selection and aggregation policies can substantially alter comparative accuracy estimates, showing that policy choices heavily influence reported scores.

## Methodology  
The authors collected 2,550 outputs from five fixed Qwen and DeepSeek configurations on MATH and ARC‑Challenge. They applied a two‑layer evaluation framework that records scorer‑independent execution evidence (termination, answer exposure, parseability, completion length) and scorer‑dependent correctness. A coverage‑audited targeted verification study was also performed to assess how candidate‑selection and aggregation policies affect accuracy estimates.

## Results  
Under the 2,048‑token limit, Qwen MATH exhibits a high failure rate (49/450 outputs terminate without an answer), while DeepSeek MATH shows a lower but non‑zero rate (5/300). ARC‑Challenge yields none. At the 8,192‑token limit, DeepSeek eliminates missing‑final termination entirely. Coverage audits reveal that policy‑driven candidate selection and aggregation can cause large variance in comparative accuracy, confirming that reported scores depend heavily on execution states and verification coverage.

## Significance  
This work reveals that reported accuracy hides underlying execution failures and is contingent on evaluation policies, prompting a shift toward transparent reporting of pre‑intervention execution states, verification coverage, and scorer provenance alongside any accuracy metric. Understanding these factors is essential for reliable model assessment and debugging.

## Related Concepts  
- Two‑layer evaluation framework  
- Execution evidence vs correctness  
- Matched output budgets  
- Termination without answer (missing final length)  
- Candidate selection policy  
- Aggregation policy  
- Verification coverage  
- Scorer independence
