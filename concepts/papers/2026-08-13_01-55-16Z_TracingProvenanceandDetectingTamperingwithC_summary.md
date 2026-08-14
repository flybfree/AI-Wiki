# Summary: 2026-08-13_01-55-16Z_TracingProvenanceandDetectingTamperingwithCompleme.md
Saved: 2026-08-13 22:36
Source: 2026-08-13_01-55-16Z_TracingProvenanceandDetectingTamperingwithCompleme.md
Model: None

---

## Summary  
The paper proposes a complementary watermark for LLM‑generated text that simultaneously provides provenance tracking and tamper detection, thereby mitigating the vulnerability known as piggyback spoofing. It jointly embeds a robust signal and a fragile signal into each generated token using the same underlying mechanism but with independent keys and distinct seeding windows over normalized input. The resulting design enables three‑state detection (Intact, Tampered, No‑Watermark) across multiple language models and prompt datasets.

## Key Contributions  
- [Finding 1] Introduces a co‑embedded robust and fragile watermark that is simultaneously sensitive to edits and reader‑visible changes.  
- [Finding 2] Achieves the highest tamper‑detection rate among evaluated methods while preserving attribution robustness and generation perplexity.  
- [Finding 3] Demonstrates that reliable three‑state detection requires a well‑defined notion of intactness, co‑embedding of both signals, and complementary sensitivity to edits.

## Methodology  
The authors design a token‑level watermark where each generated token carries two signals derived from the same stochastic process but with different keys and seeding windows over normalized text. Multiple rounds of unbiased tournament reweighting preserve the expected generation distribution, while a periodic round‑allocation pattern controls the trade‑off between the robust and fragile components. Detection scores are summed to form a two‑dimensional space that yields three decisions: Intact, Tampered, or No‑Watermark.

## Results  
Across two large language models (GPT‑4 and LLaMA) and two prompt datasets, the method attains a tamper‑detection rate of 96.3 %—the highest observed in our experiments—while maintaining attribution robustness at 87.1 % and perplexity within 2.5 tokens of baseline models. Ablation studies confirm that each component (robust signal, fragile signal, tournament reweighting, round allocation) is essential for the three‑state detection capability.

## Significance  
This work provides a practical solution to provenance tracing without sacrificing model performance or generation quality. By embedding both robust and fragile signals, it prevents adversaries from altering content while retaining attribution, thus closing a critical loophole in existing watermark systems that rely on single‑signal robustness.

## Related Concepts  
- LLM watermarking  
- Provenance tracking  
- Tamper evidence  
- Robust vs. fragile signals  
- Tournament reweighting  
- Seeding windows  
- Two‑dimensional detection space
