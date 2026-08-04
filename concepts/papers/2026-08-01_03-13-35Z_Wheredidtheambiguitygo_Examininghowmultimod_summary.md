# Summary: 2026-08-01_03-13-35Z_Wheredidtheambiguitygo_Examininghowmultimodalmodel.md
Saved: 2026-08-03 20:21
Source: 2026-08-01_03-13-35Z_Wheredidtheambiguitygo_Examininghowmultimodalmodel.md
Model: None

---

## Summary  
This paper investigates how large multimodal foundation models handle polysemous (multiple‑meaning) words when the meaning is not fixed by surrounding context, a problem that remains largely unexplored beyond text. By comparing 17 text‑to‑image and 15 text‑generation models across a set of common polysemous terms such as “bank” or “palm,” the authors quantify the diversity of meanings each model produces in both modalities. Their analysis reveals a pronounced multimodal gap: generated images exhibit far lower semantic variability than sentences, while human intuition predicts even higher diversity. Moreover, when models are asked to predict how often they would generate each sense, their predictions diverge from actual output distributions, indicating a misalignment between internal reasoning and observable behavior.

## Key Contributions  
- [Finding 1] A consistent multimodal gap exists across all model families: normalized entropy of image outputs is ~0.10 versus ~0.25 for sentence outputs, both below the human‑imagined entropy of ~0.47.  
- [Finding 2] Text‑to‑image models generate far fewer distinct senses than their textual counterparts, suggesting a loss of polysemy in visual representation.  
- [Finding 3] The models’ self‑predicted frequency distributions for each sense are more diverse than the actual output space, exposing a discrepancy between internal reasoning and external behavior.

## Methodology  
The authors selected 17 text‑to‑image diffusion models (e.g., Stable Diffusion variants) and 15 pure language generators (e.g., GPT‑4, Claude). For each model they chose a polysemous word with no contextual cues. Over many independent prompts, the system was asked to generate outputs that could correspond to any of the word’s senses. The diversity of generated meanings was measured using normalized entropy, which quantifies how spread out the output distribution is. Additionally, models were prompted to list how often they would produce each sense, and these predictions were compared to the empirical frequencies observed in the actual outputs.

## Results  
Across all models, image‑based polysemy showed significantly lower entropy (0.10) than text‑based entropy (0.25), both underrepresenting human intuition (0.47). The most extreme disparity occurred with “bank,” where images consistently produced only one of two meanings while sentences produced a balanced mix. When models were asked to predict sense frequencies, they overestimated the diversity of possible outputs, indicating an internal belief that does not match reality.

## Significance  
These findings highlight a critical limitation in current foundation models: their ability to convey and interpret polysemy is unevenly distributed across modalities, potentially leading to misaligned user experiences or downstream tasks. Understanding this gap is essential for developing more robust multimodal systems that faithfully represent human language semantics in both text and image spaces.

## Related Concepts  
- Polysemy (multiple meanings of a single word)  
- Normalized entropy as a measure of output diversity  
- Multimodal foundation models (text‑to‑image, text generation)  
- Contextual disambiguation vs. polysemous ambiguity  
- Semantic representation in diffusion and language models
