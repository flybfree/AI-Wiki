# Summary: 2026-08-03_04-01-02Z_StyleWins_SubstanceLoses_ADiagnosisofLLM_as_Judgei.md
Saved: 2026-08-03 23:19
Source: 2026-08-03_04-01-02Z_StyleWins_SubstanceLoses_ADiagnosisofLLM_as_Judgei.md
Model: None

---

## Summary  
The paper investigates whether LLM‑based idea judges evaluate scientific substance or are swayed by superficial style, proposing a new benchmark called SciStyleBench to diagnose and mitigate stylistic bias in idea evaluation. It introduces a three‑component framework that combines controlled stylistic perturbations across multiple contexts with quantitative metrics and an extraction module. Experiments show that direct LLMs remain highly sensitive to writing style while the extraction approach reduces bias and improves substance detection. The contribution is a systematic method for identifying, quantifying, and mitigating stylistic bias in scientific idea evaluation.

## Key Contributions  
- [Finding 1] Direct LLM judges exhibit a high Style Bias Index (SBI) indicating strong sensitivity to writing style.  
- [Finding 2] SciStyleExtractor significantly lowers SBI while boosting Substance Recognition Rate (SRR) and Adversarial Win Rate (AWR), demonstrating improved discrimination of scientific substance.  
- [Finding 3] The three‑stage evaluation environment (SciStyleStage) systematically varies stylistic presentation across no‑context, fixed‑domain, and open‑domain retrieval contexts to capture bias under different conditions.

## Methodology  
The authors designed SciStyleBench comprising SciStyleStage, SciStyleMetrics, and SciStyleExtractor. SciStyleStage generates 600 scientific ideas with 15 style variants applied in three evaluation settings (no context, fixed‑domain, open‑domain), each containing 9,000 instances. SciStyleMetrics define SBI (stylistic bias), SRR (substance recognition rate), and AWR (adversarial win rate) to quantify how stylistic variation affects scoring stability, substance discrimination, and ranking robustness. SciStyleExtractor predicts style type and deviation before evaluation, enabling separation of content from style so that style‑conditioned judgments can be assessed.

## Results  
Experiments on SciStyleBench show SBI reduced from 0.566 to 0.501 after extraction; SRR increased to 0.759 and AWR rose to 0.899. These improvements indicate that extracting style reduces bias while preserving or enhancing substance detection.

## Significance  
Robust idea evaluation is critical for scientific AI, yet current LLMs fail due to style bias. This work provides a benchmark and mitigation strategy, enabling more reliable, fair evaluations that prioritize scientific merit over superficial presentation.

## Related Concepts  
- Style Bias Index (SBI)  
- Substance Recognition Rate (SRR)  
- Adversarial Win Rate (AWR)  
- SciStyleBench  
- LLM‑as‑Judge bias  
- Prompt engineering for style invariance
