# Summary: 2026-08-03_11-48-39Z_HowMuchDoesaReasoningSummaryReveal_AnObservability.md
Saved: 2026-08-03 23:53
Source: 2026-08-03_11-48-39Z_HowMuchDoesaReasoningSummaryReveal_AnObservability.md
Model: None

---

## Summary  
This paper investigates how much information a reasoning summary reveals about the correctness of large language model answers when compared to the full trace and response alone. It introduces an observability ladder that isolates each component (response, self‑summary, trace, internal signals) as separate visibility levels. By training linear predictors on these access levels across multiple benchmarks and models, the authors quantify the incremental predictive power of each layer.

## Key Contributions  
- Finding 1: Summaries alone capture most of the trace’s ranking signal (mean AUROC 0.774 versus 0.813), providing a substantial improvement over response‑only (+0.156).  
- Finding 2: When the prompt is visible, the summary’s gain collapses to +0.019, indicating that the model already encodes its reasoning in the trace; only the full trace adds modest extra signal (+0.041).  
- Finding 3: The trace’s last words predict correctness as well as or slightly better than summaries and encode denser uncertainty cues, yet linear readers still rely heavily on length.

## Methodology  
The authors fix each run’s output (response, self‑summary, full trace) while varying only the information a reader can inspect. They create five access levels: response alone, response + prompt hidden, summary alone, summary + prompt hidden, and full trace alone (with/without prompt). Matched linear classifiers are trained on these levels using MMLU‑Pro and open‑weight Qwen3/gpt‑oss models to compute AUROC.

## Results  
On MMLU‑Pro with both correct and incorrect runs, linear readers are near chance without the prompt (0.503–0.545) but improve modestly with it (0.544–0.590). The trace alone yields a small advantage (+0.034) even when the prompt is hidden, outperforming summaries which plateau at +0.156 without the prompt. Length of traces correlates strongly with predictive power; shorter traces lose most signal.

## Significance  
The work clarifies that monitorability depends on both what is displayed and how it is read, challenging claims about faithfulness or correctness that ignore the reader’s perspective. It shows that summaries are valuable when the full trace is unavailable but become redundant if users already have access to the prompt; thus, any observability assessment must specify the display‑reader pair.

## Related Concepts  
- Observability ladder  
- Linear predictors for model evaluation  
- AUROC as a metric of discriminative power  
- Prompt‑aware vs. prompt‑withheld analysis
