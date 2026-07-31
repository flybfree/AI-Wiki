# Summary: 2026-07-30_17-14-07Z_ORCA_bench_HowReadyAreLanguageModelAgentsforOncall.md
Saved: 2026-07-30 22:22
Source: 2026-07-30_17-14-07Z_ORCA_bench_HowReadyAreLanguageModelAgentsforOncall.md
Model: None

---

## Summary  
The paper introduces ORCA‑bench, a benchmark that evaluates general‑purpose language model agents on realistic root‑cause analysis (RCA) tasks in a production‑fidelity setting. It pairs six days of OpenTelemetry‑instrumented telemetry with expertly curated incident reports and full source‑code access to simulate the noisy, ambiguous nature of oncall RCA. The study measures how well frontier coding agents can infer accurate root causes despite limited information. The results show that even state‑of‑the‑art models achieve only modest accuracy (≈25 % for medium tasks) and are prone to hallucinations.

## Key Contributions  
- [Finding 1] The best RCA Accuracy among five frontier agents is 25.3 % on Medium‑difficulty tasks, indicating a significant gap from human performance.  
- [Finding 2] The Hard‑difficulty accuracy drops to only 10.0 %, and this gap persists even when using Claude Fable 5, suggesting that current models are not yet reliable for the most challenging incidents.  
- [Finding 3] Removing source‑code access degrades every metric, and the weakest model hallucinates an implausible root cause in about 40 % of reports.

## Methodology  
The authors built a production‑like testbed using OpenTelemetry‑instrumented microservice telemetry (Prometheus, Jaeger, OpenSearch via Grafana) and full source‑code access. They generated 1,079 RCA tasks that vary in report specificity, time‑to‑detection, and co‑occurring fault scenarios. Ground‑truth symptoms were curated by expert SREs and independently re‑scored by humans with Cohen’s κ = 0.90. The LLM‑as‑judge was evaluated on these tasks to produce the reported accuracies.

## Results  
Across five frontier agents, Medium‑difficulty RCA Accuracy reaches 25.3 % while Hard‑difficulty Accuracy is 10.0 %. The weakest model hallucinates in roughly 40 % of incidents when source‑code access is absent. All metrics improve noticeably with source‑code inclusion, underscoring its importance for reliable RCA.

## Significance  
These findings establish a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability. The gap between human and model performance highlights that current LLMs are still far from sufficient for real‑world oncall RCA, prompting further research into better reasoning, grounding, and safety mechanisms.

## Related Concepts  
- Oncall root cause analysis (RCA)  
- Language model agents / coding assistants  
- OpenTelemetry telemetry (Prometheus, Jaeger, OpenSearch)  
- LLM‑as‑judge evaluation with human re‑scoring (Cohen’s κ)  
- Hallucination in LLMs  
- Source‑code grounding for reasoning tasks
