# Summary: 2026-08-06_20-48-14Z_DivergentResponseModesinFrontierLanguageModelsUnde.md
Saved: 2026-08-09 22:25
Source: 2026-08-06_20-48-14Z_DivergentResponseModesinFrontierLanguageModelsUnde.md
Model: None

---

## Summary  
This study investigates whether the distinct training data, objectives, and safety pipelines of six frontier language models produce measurably different behaviors when subjected to explicit steering pressure. By treating each model as a blind peer judge that classifies paired base‑steered responses on fixed rubrics, the authors reveal that differences are not merely quantitative but also qualitative in nature. The work demonstrates that some response modes appear in only one or two models and can be decoded and altered with high accuracy, challenging the assumption of uniform steerability across frontier systems.

## Key Contributions  
- [Finding 1] Models differ in the type of response they generate under steering pressure, not just how much steering shifts their behavior.  
- [Finding 2] Certain response modes appear only in one or two models (e.g., GPT‑5 deflects requests to disclose its reasoning).  
- [Finding 3] A linear probe can decode these modes with 0.87 held‑out accuracy and, when injected during generation, drive behavior from 0 % to 86 %.  

## Methodology  
The authors evaluated six frontier models (GPT‑5, Claude Opus 4.7, GPT‑5, Llama, etc.) using 300 paired base and steered items across three categories—values conflict, reasoning elicitation, and reasoning suppression—plus 40 validation items. Each model acted as a blind peer judge, classifying every response according to fixed rubrics. The 24 480 judgments were scored via leave‑one‑out consensus, allowing the authors to isolate individual model effects while controlling for evaluation noise.

## Results  
The analysis shows that steering can produce qualitatively distinct response modes: GPT‑5 deflects reasoning disclosure (99 % vs. 0 % for all others), Claude Opus 4.7 resists suppression in a different way, and Llama exhibits the largest split linked to its internal residual stream. A linear probe trained on this stream achieved 0.87 accuracy in decoding behavior; injecting that direction during generation increased the model’s compliance from 0 % to 86 % across an intervention sweep. All findings hold under both token‑budget remediation and a hypothesis‑blind judgment prompt, confirming robustness.

## Significance  
These results demonstrate that steering pressure can elicit qualitatively different behaviors rather than merely quantitative adjustments, highlighting the need for model‑specific safety designs. Understanding response modes helps developers anticipate failure modes and develop more reliable alignment techniques across diverse frontier systems.

## Related Concepts  
frontier language models, behavioral steerability, response modes, linear probing, residual stream decoding, leave‑one‑out consensus evaluation.
