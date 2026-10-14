---
title: The Curse of Knowledge in Role-Playing Language Models
url: http://arxiv.org/abs/2610.17327v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_19-37-03Z_TheCurseofKnowledgeinRole_PlayingLanguageModels.md
generated_at: 2026-10-14 01:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether role-playing language models respect the information boundaries assigned to characters in game and agent simulations, testing 480 scenes across 11 open-weight models and 6 proprietary models. The central finding is that open-weight models leak knowledge they should not possess—content from speech they cannot understand or hear—at rates 67 to 72 percentage points above a counterfactual baseline, a phenomenon the author terms a "curse of knowledge." However, the leak is highly sensitive to input formatting, and providing models only the observations available to the character effectively eliminates the leakage without restricting what the character may report.

## Key Takeaways
- Open-weight models exhibit severe knowledge leakage: across 480 test scenes, characters reference information from speech they cannot perceive at 67–72 percentage points above a carefully constructed counterfactual baseline, even though most models can correctly state what the character perceives when asked directly. The leak extends beyond spoken dialogue to hidden actions, private messages, and even influences where characters choose to search for information.
- Compliance is fragile and format-dependent: changing only the scene layout or character description raises leakage in two otherwise compliant open-weight models from under 10 to over 60 percentage points, and combined changes push two proprietary models from near zero to 13 and 21 percentage points. Five of six proprietary models show minimal leakage, but this compliance is not robust to presentation changes.
- The framing of the prompt matters enormously: writing the same line as the "scene's author" leaks nearly as much as explicit role-play, and chain-of-thought thinking rarely helps reduce leakage. The effective mitigation is architectural—restricting the model's input to only what the character can observe—which stops the leak without hiding information the character might legitimately report.

## Context
This work sits at the intersection of language model evaluation, agent simulation, and narrative AI systems, where role-playing models are increasingly deployed in interactive fiction, multi-agent game simulations, and social reasoning benchmarks. The "curse of knowledge" concept, borrowed from cognitive psychology, is here operationalized as a measurable failure mode in which a model's global training knowledge contaminates a character's supposedly limited perspective. As multi-agent LLM systems proliferate in research and industry, ensuring that agents do not exploit privileged information becomes critical for valid simulation outcomes and fair benchmarking.

## Implications
For practitioners building role-playing agents, game simulations, or multi-agent systems, this paper demonstrates that prompt formatting alone is an unreliable safeguard against knowledge leakage; instead, information must be architecturally restricted at the input level to match the character's perceptual boundaries. The finding that proprietary models are more compliant but still vulnerable to layout changes suggests that current alignment techniques are brittle and that evaluation harnesses must test robustness across presentation formats. For benchmark designers, the counterfactual-twin methodology offers a rigorous template for measuring whether an agent's outputs reflect genuine in-character reasoning or leaked global knowledge, which is essential for trustworthy evaluation of role-playing and agent-based language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17327v1)
