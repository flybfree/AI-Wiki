# Summary: 2026-08-06_15-58-32Z_WhatCurrentAIBenchmarksLeaveUnmeasured_Modality_Se.md
Saved: 2026-08-06 20:47
Source: 2026-08-06_15-58-32Z_WhatCurrentAIBenchmarksLeaveUnmeasured_Modality_Se.md
Model: None

---

## Summary  
The authors critique the dominant practice of evaluating large language models (LLMs) with a single access modality, a single run per prompt, and accuracy as the sole metric, arguing that such assessments miss crucial factors—modality, web search conditions, citation grounding, and response‑level variability—that are vital for AI safety. By auditing two widely used benchmarks (BBQ and SafetyBench) across ChatGPT’s UI and OpenAI API with and without search, they demonstrate that current benchmark reports can obscure important behavioral differences in deployed systems.

## Key Contributions  
- **Finding 1:** The chat‑UI modality is less accurate than the API modality when web search is disabled on both benchmarks.  
- **Finding 2:** Enabling web search reduces accuracy by up to eight percentage points and even reverses the performance trend for one benchmark, showing that search can degrade or improve model behavior depending on context.  
- **Finding 3:** Repeated runs of the same prompt produce inconsistent responses in up to 21 % of cases, highlighting a lack of multi‑run consistency.

## Methodology  
The authors audited assumptions underlying LLM benchmarking by constructing a stratified total sample of 401 prompts drawn from BBQ and SafetyBench. Each prompt was evaluated three times (three repeated runs) across two modalities: ChatGPT’s chat UI and OpenAI’s API, with web search toggled on and off. This design captures modality effects, search influence, citation grounding, and response‑level behaviors.

## Results  
Chat UI responses were consistently less accurate than API responses when search was disabled (p < 0.05). With search enabled, accuracy dropped up to 8 pp for ChatGPT and increased for OpenAI on one benchmark, indicating a reversal of the modality trend. Of the 4,812 total responses, 21 % exhibited output inconsistency across runs, meaning the same prompt yielded different answers. Additionally, each modality grounded its answers in distinct citation sets, and abstention behavior varied between modalities.

## Significance  
These findings reveal that safety evaluations relying solely on accuracy metrics can misrepresent how models behave in real‑world deployment scenarios where access methods, search capabilities, and repeated queries occur. Accounting for modality, multi‑run consistency, search conditions, and response‑level behaviors will lead to more reliable AI safety assessments.

## Related Concepts  
- LLM benchmarks (BBQ, SafetyBench)  
- AI safety evaluation frameworks  
- Modality effects in model access  
- Web search integration with LLMs  
- Citation grounding and factuality  
- Response consistency and abstention behavior
