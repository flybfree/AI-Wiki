# Summary: 2026-08-05_08-00-54Z_ThePersonalizationMirage_HowLLMsFabricateUserProfi.md
Saved: 2026-08-05 20:31
Source: 2026-08-05_08-00-54Z_ThePersonalizationMirage_HowLLMsFabricateUserProfi.md
Model: None

---

## Summary  
This paper investigates the phenomenon of over‑inference, where large language models (LLMs) generate user attributes that are not supported by any evidence in their training data or conversation history. The authors introduce MirageBench, a benchmark that evaluates 12 personalization models across diverse persona types and tasks, revealing that every model fabricates a substantial proportion of its claims. A key finding is the “Self‑Monitoring Inversion,” showing that models’ self‑reported confidence in their over‑inference is negatively correlated with actual judge scores, indicating that self‑monitoring is unreliable for trustworthy personalization.

## Key Contributions  
- **Finding 1:** Over‑inference rates are pervasive across all evaluated models, ranging from 35 % to 49 % of generated claims.  
- **Finding 2:** The self‑assessed over‑inference scores exhibit a strong negative rank correlation (ρ = –0.60, p = .044) with independent judge measurements, meaning the models that claim low fabrication actually produce the most inflated outputs.  
- **Finding 3:** Over‑inference is task‑dependent and accumulates linearly over multi‑turn interactions, suggesting a cumulative “fabrication budget” rather than random errors.

## Methodology  
The authors constructed MirageBench with 150 personas spanning stereotypical, counter‑stereotypical, and neutral profiles. They performed six personalization tasks organized along an imagination gradient, each judged by human annotators using a four‑way faithfulness taxonomy (validated by Cohen’s kappa = .863 for four classes). The dataset comprises 143 616 claims across 12 models from seven families, enabling systematic comparison of over‑inference behavior.

## Results  
Across the full evaluation, every model over‑infers between 35 % and 49 % of its claims (cross‑model mean 41.6 %). The self‑monitoring inversion is statistically significant: models with higher self‑reported low OI rank lower on judge‑measured OI (ρ = –0.60, p = .044). Task analysis shows over‑inference varies from 27 % to 59 %, and multi‑turn inference grows roughly linearly without substantial revision.

## Significance  
These results expose a critical flaw in current personalization systems: models generate plausible‑sounding user profiles that lack evidential grounding, undermining trust. The self‑monitoring inversion further reveals that relying on model confidence is misleading; external verification remains the only robust metric for assessing faithfulness.

## Related Concepts  
- Over‑inference (OI) – generation of unsupported attributes.  
- Personalization with persistent memory.  
- Self‑assessment and confidence reporting.  
- Human evaluation via human‑in‑the‑loop (HITL).  
- Cohesive faithfulness taxonomy.
