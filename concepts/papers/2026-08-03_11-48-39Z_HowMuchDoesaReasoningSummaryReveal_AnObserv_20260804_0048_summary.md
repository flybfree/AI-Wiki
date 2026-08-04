# Summary: 2026-08-03_11-48-39Z_HowMuchDoesaReasoningSummaryReveal_AnObservability.md
Saved: 2026-08-04 00:48
Source: 2026-08-03_11-48-39Z_HowMuchDoesaReasoningSummaryReveal_AnObservability.md
Model: None

---

## Summary  
The paper investigates how much a reasoning summary reveals about the correctness of large language model outputs by constructing an “observability ladder” that isolates each component—response only, self‑written summary, full trace, and internal signals—and evaluates them under two conditions: with the original prompt visible to the reader or hidden. Using linear classifiers trained on matched data across three benchmarks and five open‑weight models (Qwen3 and gpt‑oss), the authors quantify the incremental signal each component provides for correctness prediction. Their experiments show that summaries alone capture most of the trace’s predictive power, but this benefit erodes when the prompt is visible, while the full trace still offers a modest advantage. The findings highlight that monitorability depends jointly on what is displayed and how it is read.

## Key Contributions  
- **Observability ladder**: A systematic framework that measures the contribution of response, summary, trace, and internal signals to correctness prediction.  
- **Summaries’ dominant signal**: When the prompt is hidden, summaries carry most of the trace’s ranking signal (mean AUROC 0.774 vs 0.813 for responses) and improve linear readers by +0.156.  
- **Trace superiority in uncertainty cues**: The full trace provides dense self‑correction and last‑word predictions that are as predictive as summaries, with a small +0.034 advantage over summaries.

## Methodology  
The authors fix each model run (prompt, response, summary, trace) and vary only the information presented to a linear predictor. They train five matched predictors on three benchmark datasets (including MMLU‑Pro) for both open‑weight Qwen3 and gpt‑oss models under two prompt conditions: visible and withheld. AUROC is reported per access level to compare signal strength.

## Results  
Without the prompt, summaries improve linear readers by +0.156 (AUROC 0.774 vs 0.813), while traces add only +0.041. With the prompt visible, summary gain collapses to +0.019 and trace adds +0.041; trace’s last words predict correctness as well as summaries, slightly better. On MMLU‑Pro (prompt withheld) linear readers are near chance: response 0.503–0.545, summary 0.544–0.590, trace 0.544–0.590. A GPT‑5‑mini reader recovers more signal from both summaries and traces on gpt‑oss‑20b, yet the trace retains a modest +0.034 edge. Length of the trace also correlates with predictive power.

## Significance  
These results demonstrate that monitorability is not inherent to a model’s output but depends on the combination of displayed content and reader capability. Claims about faithfulness must specify both the observability level (summary vs. full trace) and the readership context, because linear readers can be near chance even when the full trace is available.

## Related Concepts  
- Observability ladder  
- Linear correctness predictors  
- AUROC as a metric of discriminative power  
- Self‑generated summaries in LLM responses  
- Trace signals and self‑correction cues  
- Monitorability (joint property of display and reader)
