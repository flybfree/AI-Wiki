# Summary: 2026-07-26_07-38-11Z_AuditingAlignmentControllabilityinLLMsviaPolitical.md
Saved: 2026-07-27 20:18
Source: 2026-07-26_07-38-11Z_AuditingAlignmentControllabilityinLLMsviaPolitical.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) can be steered across the political spectrum by varying system prompts, rather than merely mapping each model to a single point on a political compass. It demonstrates that controllability is not a uniform property but varies dramatically among models and prompt conditions, producing a dispersion of responses that depends on instruction framing, model identity, and saturation limits. The authors introduce a “political‑axes” audit framework that reports both the magnitude and direction of steering, as well as geometric properties such as symmetry and refusal floors. By releasing prompts, benchmark data, and code, they provide an open tool for systematic alignment‑controllability evaluation.

## Key Contributions  
- **Finding 1:** Prompt‑driven controllability explains 88–93 % of variance on the economic axis and < 3 % on the societal axis, showing that model identity is a minor factor compared with instruction framing.  
- **Finding 2:** Different LLMs exhibit distinct steering behaviors: some shift markedly under extreme prompts while others saturate or refuse, indicating non‑uniform alignment across models.  
- **Finding 3:** The effect of prompts is geometric rather than differential compliance; displacement and proximity to the baseline differ, so prior audits that assumed centered baselines misinterpreted results.

## Methodology  
The authors conducted a dispersion‑first stress test using 12 ideological personas (political compass positions) plus an unsteered baseline. They generated 70 Political Compass items across ten replicates for seven leading LLMs (GPT‑5, Claude, Grok, Gemini, DeepSeek, Kimi, Qwen), producing 63,700 responses. The system prompt was varied to simulate personalization layers; each response was scored on both axes and compared to the baseline.

## Results  
Responses were highly adjustable: contextual framing explained most of the variance, while model identity contributed negligibly. Some models moved far from the baseline under extreme prompts, others plateaued or refused altogether. The dispersion across models formed a geometric pattern rather than a uniform shift, confirming that controllability is not a single metric but a set of observable properties.

## Significance  
This work moves beyond static political‑compass audits to a dynamic, steerability‑focused evaluation that can inform responsible deployment by quantifying how far and in which directions an LLM can be nudged. By exposing saturation and refusal floors, it helps developers design safeguards against unintended ideological drift.

## Related Concepts  
- Political compass (economic vs. societal axes)  
- System prompt / personalization layer  
- Alignment controllability  
- Dispersion‑first analysis  
- Saturation and refusal thresholds
