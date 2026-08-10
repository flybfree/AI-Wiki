# Summary: 2026-08-07_14-44-19Z_GrammarEngineeringMeetsLLMs_DevelopmentofCantonese.md
Saved: 2026-08-09 23:05
Source: 2026-08-07_14-44-19Z_GrammarEngineeringMeetsLLMs_DevelopmentofCantonese.md
Model: None

---

## Summary
The paper aims to develop parallel treebanks for Cantonese and Irish within the Parallel Grammar (ParGram) Project, integrating grammar engineering with large language model (LLM) assistance. It evaluates how multilingual LLMs can support abstract syntactic generation and translation tasks across these languages. The study highlights both opportunities and constraints of using LLMs in collaborative linguistic analysis.

## Key Contributions
- [Finding 1] The authors created parallel treebanks that preserve functional equivalence between Cantonese and Irish syntax while respecting each language's morphological and phonological features.
- [Finding 2] Evaluation shows that OpenAI’s gpt‑oss‑120b model fails to produce reliable translations, with performance independent of prompt language, indicating limited translation capability for grammar engineering.
- [Finding 3] Although the LLM can generate syntactically plausible structures, its ability to capture cross‑linguistic abstraction is weak, underscoring the need for expert verification.

## Methodology
The authors built two parallel treebanks by aligning syntactic trees of comparable sentences in Cantonese and Irish, using a functional grammar specification. They then fed these aligned examples into gpt‑oss‑120b via prompt engineering to generate new tree structures and translation outputs, measuring quality through human evaluation and automated metrics.

## Results
Translation attempts yielded low BLEU scores and frequent mistranslations, confirming the model’s poor multilingual translation ability. Syntactic generation produced some structurally coherent trees but many violated cross‑linguistic constraints, as measured by expert annotation of predicate‑argument relations.

## Significance
These findings demonstrate that while LLMs can offer heuristic suggestions in grammar engineering, they cannot replace human expertise for accurate, linguistically faithful analysis. The work contributes to understanding LLM utility limits and guides future research on hybrid human‑AI workflows.

## Related Concepts
Parallel Grammar (ParGram), treebank construction, functional linguistic modeling, multilingual large language models, predicate‑argument relations, grammar engineering, cross‑linguistic abstraction.
