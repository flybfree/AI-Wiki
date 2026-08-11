# Summary: 2026-08-09_15-49-00Z_OmnilingualGAIA2_EvaluatingtheMultilingualGapinFro.md
Saved: 2026-08-10 23:24
Source: 2026-08-09_15-49-00Z_OmnilingualGAIA2_EvaluatingtheMultilingualGapinFro.md
Model: None

---

## Summary  
The paper introduces **OmnilingualGAIA2**, a machine‑translated expansion of the English‑only GAIA2 agentic benchmark that covers ten languages across five writing systems, together with a locally calibrated multilingual verifier. Its goal is to quantify whether the competence observed in English translates to other linguistic contexts and to identify why frontier AI agents underperform when deployed globally. By evaluating seven open‑weight agents on this expanded set, the authors reveal a persistent cross‑lingual gap that persists despite model scale and argues for multilingual evaluation as a standard reporting practice.

## Key Contributions  
- **Finding 1:** A universal cross‑lingual gap of 8.8–18.4 pass@3 points exists across all ten languages, indicating that agentic performance does not uniformly transfer.  
- **Finding 2:** The gap is larger for tool‑orchestration tasks than for quantitative reasoning and does not close with increasing model size, suggesting architectural or data‑related constraints rather than pure scaling limits.  
- **Finding 3:** Error analysis shows that roughly 55 % of failures are model‑driven while only a minimal 6.4 % can be attributed to translation contamination; human linguistic review uncovers morphological cue loss and amplified ambiguity as primary failure mechanisms in non‑Latin scripts.

## Methodology  
The authors created OmnilingualGAIA2 by translating the original English scenarios into ten target languages, with partial human expert validation to preserve task intent. A multilingual verifier was calibrated locally for each language to score agentic behavior consistently. Seven frontier AI agents (open‑weight) were run on this expanded benchmark, and their pass@3 scores were compared across languages. Errors were stratified using a decomposition framework that attributes failures to model capacity versus translation artifacts.

## Results  
The experimental results demonstrate a consistent performance shortfall of 8.8–18.4 points at pass@3 for all agents in every language. The gap is agent‑asymmetric, meaning some models suffer more than others regardless of scale. Tool‑orchestration tasks exhibit the widest variance, while pure reasoning shows smaller differences. Stratified error attribution reveals that 55 % of errors stem from the model’s inability to handle complex planning, whereas translation contamination accounts for only 6.4 % of scenario‑language pairs. Human analysis confirms that non‑Latin scripts lose morphological cues and experience heightened ambiguity, leading to misinterpretations.

## Significance  
These findings underscore a critical gap in current AI research: benchmarks measuring agentic competence are almost exclusively English‑centric, obscuring real‑world deployment outcomes for multilingual users. By quantifying this cross‑lingual disparity and pinpointing its sources, the work calls for standardizing multilingual evaluation as an essential component of any AI agent’s reporting protocol.

## Related Concepts  
- Agentic benchmarks  
- GAIA2 (agentic task suite)  
- Frontier AI agents  
- Multilingual gap / cross‑lingual performance disparity  
- Tool‑orchestration vs. quantitative reasoning  
- Model scale effects  
- Translation contamination  
- Morphological cue loss  
- Ambiguity amplification  
- Error attribution (stratified analysis)
