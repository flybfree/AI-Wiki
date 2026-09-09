---
title: FramingQA: Does the Question Shape the Answer? Measuring the Compositional Framing Effect
published: 2026-09-07T12:56:44Z
authors: Hazel H. Kim, Andrew M. Bean, Guilherme Affonso Ferreira de Camargo, Shanyu Chauhan, Felix Drinkall, Jade Kosché, Chenyang Ma, Glory Nwaugbala, Nabeel Seedat, Bradley Max Segal, Samuel Recht, Hinrich Schütze, Philip H. S. Torr
url: http://arxiv.org/abs/2609.07448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FramingQA: Does the Question Shape the Answer? Measuring the Compositional Framing Effect

## Abstract
We introduce FramingQA, a benchmark that measures the model sensitivity to question framing across law, medicine, finance, and robotic simulations. Large language models (LLMs) often change their responses to subtle rephrasings that align with an implied stance by users. This can leave users with advice tainted by how they happened to phrase a question rather than by the underlying facts, and the consequences are highly costly in high-stakes domains. Because in the realistic scenarios, both expert practitioners and non-expert users frequently ask LLMs questions containing incomplete or misleading assumptions, models are highly susceptible to those framings. To test this, we inject the framing bias across three nested levels: a framing-biased question phrasing (root), an injected framing-biased premise prepended to a neutral question (propositional), and a premise paired with a framing-biased question (global). Evaluating nine open models (3.8B-70B) across four families, we find that strong per-variant accuracy does not guarantee the robustness across differently phrased questions under the fixed factual information.

## Metadata
- **Published**: 2026-09-07T12:56:44Z
- **Authors**: Hazel H. Kim, Andrew M. Bean, Guilherme Affonso Ferreira de Camargo, Shanyu Chauhan, Felix Drinkall, Jade Kosché, Chenyang Ma, Glory Nwaugbala, Nabeel Seedat, Bradley Max Segal, Samuel Recht, Hinrich Schütze, Philip H. S. Torr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07448v1)