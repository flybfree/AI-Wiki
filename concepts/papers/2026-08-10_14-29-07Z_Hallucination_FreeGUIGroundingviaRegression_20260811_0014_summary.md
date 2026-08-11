# Summary: 2026-08-10_14-29-07Z_Hallucination_FreeGUIGroundingviaRegression_FreeLa.md
Saved: 2026-08-11 00:14
Source: 2026-08-10_14-29-07Z_Hallucination_FreeGUIGroundingviaRegression_FreeLa.md
Model: None

---

## Summary  
The paper tackles the persistent problem of hallucinated coordinate grounding in GUI interaction, where abstract user instructions are translated into precise element locations. It introduces a regression‑free framework that separates instruction understanding from layout‑aware localization, eliminating the need for fine‑tuned coordinate regressors. By freezing a multimodal language model to generate rich visual descriptions and using only binary Text/Icon labels for grounding, the method avoids expensive fine‑tuning while suppressing hallucinations. The core contribution is a decoupled architecture that improves accuracy without learning any regression parameters.

## Key Contributions  
- [Finding 1] A frozen MLLM produces structured visual descriptions from abstract instructions, providing layout cues independent of coordinate computation.  
- [Finding 2] A dedicated grounding model performs regression‑free localization by matching against layout‑prior candidates using only Text/Icon binary labels.  
- [Finding 3] The architecture eliminates fine‑tuning of coordinate regressors and reduces hallucinations, leading to measurable gains on benchmark datasets.

## Methodology  
The authors adopt a two‑stage pipeline: first, the frozen MLLM parses user instructions into a detailed visual description enriched with layout information. This description is then fed to a Layout‑Aware GUI Grounding Model that does not learn any regression parameters. Instead, it learns to match candidate element coordinates against the generated description using binary Text/Icon labels, effectively performing a regression‑free matching operation. The method thus separates perception (instruction parsing) from localization (matching), avoiding the need for costly fine‑tuning of coordinate regressors.

## Results  
On ScreenSpot‑Pro, the proposed framework improves grounding accuracy by over 20% compared with end‑to‑end MLLM baselines. On Mind2Web, it raises both success rate and element selection rate by more than 15%. These gains demonstrate that the regression‑free matching approach yields superior performance while being computationally lighter.

## Significance  
By decoupling instruction understanding from layout‑aware localization, the method directly addresses the root causes of hallucinated coordinates—deficient fine‑grained perception and reliance on learned regressions. This separation simplifies training, reduces model complexity, and makes GUI grounding more robust for real‑world applications where precise element selection is critical.

## Related Concepts  
GUI grounding, multimodal large language models (MLLMs), regression‑free matching, layout‑aware models, binary Text/Icon labels, coordinate hallucination, fine‑tuning of regressors.
