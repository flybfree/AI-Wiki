# Summary: 2026-08-02_07-00-49Z_DecoyImagesAmplifyCaption_MediatedDefensesAgainstE.md
Saved: 2026-08-03 21:34
Source: 2026-08-02_07-00-49Z_DecoyImagesAmplifyCaption_MediatedDefensesAgainstE.md
Model: None

---

## Summary  
The paper investigates an unexpected interaction between image inputs and black‑box defenses on Vision–Language Models (VLMs). By pairing a jailbreak prompt with an unrelated decoy image, the authors show that caption‑mediated defenses can dramatically reduce attack success rates. The effect is not due to changes in the model’s internal logic but rather to how the defense pipeline handles the presence of an image versus text alone. This work advances understanding of how external inputs influence safety mechanisms without exposing vendor internals.

## Key Contributions  
- [Finding 1] Caption‑mediated defenses (ECSO) drop attack success rates by up to 73 pp when a content‑free decoy image is attached, while text‑only attacks remain largely unaffected.  
- [Finding 2] The effect persists across five frontier VLMs, two encoded‑attack families, and three black‑box defenses, confirming its generality under the black‑box threat model.  
- [Finding 3] Attaching a decoy unconditionally inflates benign refusals by 10–67 pp, whereas gating the attachment with an encoded‑input detector preserves safety gains without harming refusal rates.

## Methodology  
The authors evaluated five state‑of‑the‑art VLMs (e.g., CLIP, Flamingo) using two families of encoded jailbreak prompts and three black‑box defenses that operate solely on model outputs. They introduced a caption‑mediated defense (ECSO) that re‑examines the input image before applying the original safety check. To isolate variables, they used three decoy types: blank canvas, natural photographs, and random noise images, each paired with or without the encoded prompt. A lightweight detector was trained to identify encoded inputs, enabling conditional attachment of the decoy only when the detector fires.

## Results  
Exact McNemar tests revealed that every non‑saturated contrast is significant (p < 0.05). The ECSO pipeline reduced ASR from ~30 % to ≤27 % for encoded attacks, a 73 pp drop. Blank‑canvas and natural‑photo decoys reproduced the effect on all models, indicating image presence rather than content drives the outcome. When the decoder flagged an encoded prompt, attaching the decoy caused benign refusals to rise by 10–67 pp; however, gating attachment only when detection succeeded kept refusal rates near baseline while preserving safety gains. Adaptive attacks targeting ECSO showed modest degradation but did not eliminate the benefit.

## Significance  
This study uncovers a critical interaction point between image inputs and safety pipelines that can be exploited to bypass black‑box defenses without altering model weights or training data. By showing that simple image manipulation—when gated intelligently—can amplify caption‑mediated defenses, it offers practical guidance for developers seeking to harden VLMs against prompt injection attacks while minimizing false positives.

## Related Concepts  
- Vision–Language Models (VLMs)  
- Black‑box defenses  
- Encoded jailbreak prompts  
- Caption‑mediated defense (ECSO)  
- Decoy images and content‑free visual perturbations  
- Lightweight encoded‑input detectors
