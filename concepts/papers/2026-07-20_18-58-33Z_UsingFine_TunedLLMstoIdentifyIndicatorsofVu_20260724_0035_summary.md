# Summary: 2026-07-20_18-58-33Z_UsingFine_TunedLLMstoIdentifyIndicatorsofVulnerabi.md
Saved: 2026-07-24 00:35
Source: 2026-07-20_18-58-33Z_UsingFine_TunedLLMstoIdentifyIndicatorsofVulnerabi.md
Model: None

---

## Summary  
The paper investigates whether fine‑tuned large language models can be used to detect four vulnerability indicators—mental ill health, substance misuse, alcohol dependence and homelessness—in UK police incident narratives. It adapts an open‑source US LLM pipeline to run locally on sensitive data, producing prevalence estimates that could guide policing resources and training. While the model can generate meaningful outputs at scale, its results are unreliable without human review and statistical correction. The authors contribute a methodological framework for obtaining defensible LLM‑based measurements in operational policing.

## Key Contributions  
- Finding 1: LLMs can identify mental ill health indicators in approximately one in five incidents.  
- Finding 2: Single‑pass classifications are unstable; aggregated outputs over‑assign indicators relative to human judgment.  
- Finding 3: Defensible prevalence estimates require substantial human input and statistical adjustment, leaving considerable uncertainty.

## Methodology  
The authors built a multi‑stage pipeline that combines repeated model inference on de‑identified incident logs, label aggregation from multiple passes, structured human review of the aggregated results, and statistical correction to address systematic biases. The entire system runs on a locally hosted open‑weight LLM, ensuring data stays within secure police environments while preserving privacy.

## Results  
Analysis of nearly 3,000 de‑identified logs showed mental ill health indicators present in about 20 % of incidents, with lower prevalence for substance misuse, alcohol dependence and homelessness. Naïve single‑pass deployments produced high false‑positive rates and systematically over‑estimated indicator prevalence compared to human annotators. After applying the correction steps, estimates remained uncertain, indicating that operational use requires additional validation.

## Significance  
The work demonstrates that LLMs can extract actionable information from unstructured police data at scale, informing resourcing and training decisions. However, it also warns against treating raw model outputs as valid measurements; without human‑in‑the‑loop oversight and statistical adjustments, the estimates remain unreliable for individual or policy‑level actions.

## Related Concepts  
fine‑tuned LLMs, vulnerability indicators, police incident logs, multi‑agency response planning, statistical correction, human‑in‑the‑loop review, open‑weight models, privacy‑preserving AI, operational policing.
