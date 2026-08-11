# Summary: 2026-08-10_12-13-41Z_Buildit_Breakit_Repeat_BenchmarkingandimprovingLLM.md
Saved: 2026-08-11 00:07
Source: 2026-08-10_12-13-41Z_Buildit_Breakit_Repeat_BenchmarkingandimprovingLLM.md
Model: None

---

## Summary  
The paper introduces **Build it, Break it, Repeat (BiBiR)**, an iterative adversarial framework that continuously transforms social‑media disinformation posts to test the robustness of large language model (LLM) detectors. By repeatedly applying back‑translation and LLM persona‑based rewrites across five rounds, BiBiR reveals how detectors can be fooled while preserving original meaning, exposing weaknesses in static benchmarking. The study demonstrates that a dynamic triplet contrastive detector with anchor switching (DASS) outperforms prior baselines by 15 percentage points on the most resilient breakers’ attacks.

## Key Contributions  
- **Finding 1:** The most effective adversarial breakers combine back‑translation with LLM persona rewriting, achieving a 95 % label‑flip rate while maintaining semantic fidelity.  
- **Finding 2:** A DASS‑based triplet contrastive model reaches an average accuracy of 72.68 %, surpassing the fine‑tuned e5‑small‑LoRA baseline by fifteen points on the hardest breakers’ attacks.  
- **Finding 3:** Iterative BiBiR testing uncovers detector brittleness that static benchmarks miss, highlighting the need for repeated adversarial stress tests.

## Methodology  
The authors construct a controlled environment where each social‑media post is first generated as disinformation, then subjected to five iterative transformation stages. Each stage applies either back‑translation or LLM persona rewriting, alternating between them to simulate realistic evasion tactics. The detector’s label predictions are recorded after every round, and the resulting label flip rate (LFR) and accuracy are logged. This repeated testing allows the system to measure how quickly a model can be compromised and whether its performance degrades over successive rounds.

## Results  
Across all five iterations, the best‑performing detector achieved an average LFR of 95 % on the most robust breakers’ attacks, indicating that even high‑quality detectors can be systematically fooled. The DASS triplet model’s accuracy rose to 72.68 %, a clear improvement over the baseline (≈57.68 %). Sensitivity analysis shows that preserving original meaning reduces false positives, suggesting that semantic checks could improve detection reliability.

## Significance  
BiBiR provides a practical methodology for evaluating LLM‑based disinformation detectors under realistic adversarial conditions, moving beyond one‑off benchmark scores. By exposing iterative weaknesses, the framework guides developers to design more resilient models and informs policy on automated content moderation that must account for evolving evasion techniques.

## Related Concepts  
- Large language model (LLM) generation of disinformation  
- Back‑translation as an adversarial transformation  
- LLM persona rewriting for style mimicry  
- Triplet contrastive learning with dynamic anchor switching (DASS)  
- Label‑flip rate (LFR) and accuracy metrics in detection tasks
