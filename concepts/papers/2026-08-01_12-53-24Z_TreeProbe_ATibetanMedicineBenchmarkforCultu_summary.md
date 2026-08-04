# Summary: 2026-08-01_12-53-24Z_TreeProbe_ATibetanMedicineBenchmarkforCulturalBias.md
Saved: 2026-08-03 20:29
Source: 2026-08-01_12-53-24Z_TreeProbe_ATibetanMedicineBenchmarkforCulturalBias.md
Model: None

---

## Summary  
The paper proposes TreeProbe, a benchmark designed to measure cultural bias in large language models when they encounter Tibetan medicine—a distinct epistemological system that is often marginalized by biomedical‑oriented training data. By organizing the dataset around the native “Tree of Medicine” framework, which encodes 467 diseases and ten subtasks across three therapeutic roots, TreeProbe provides a concrete test for how models navigate this knowledge structure. The study demonstrates that current LLMs exhibit systematic external ontology drift, either drifting toward biomedical or TCM reasoning depending on their training composition. This work introduces a diagnostic tool that can guide more inclusive and epistemically fair medical AI development.

## Key Contributions  
- [Finding 1] TreeProbe is the first benchmark that quantifies cultural bias in Tibetan medicine using expert‑adjudicated items aligned with the traditional Tree of Medicine framework.  
- [Finding 2] Experiments reveal that LLMs show systematic external ontology drift, preferring biomedical reasoning over TCM when their training data are dominated by Western biomedical corpora.  
- [Finding 3] The divergence is linked to surface resemblance between Tibetan and TCM concepts and the composition of pretraining data, suggesting a causal relationship between linguistic exposure and epistemic bias.

## Methodology  
The authors assembled 4,719 items curated by Tibetan medical experts, each representing a disease, symptom, treatment, or therapeutic principle within the Tree of Medicine. The dataset is split into subtasks that map to three therapeutic roots: internal balance, external harmony, and spiritual purification. To evaluate bias, the benchmark measures model outputs on these subtasks, comparing them against expert‑ground truth while tracking whether models adopt biomedical terminology (e.g., “pharmacology”) or TCM terminology (e.g., “yogic alchemy”). The drift is quantified by a binary classifier trained to detect biomedical vs. TCM reasoning patterns.

## Results  
Across nine representative LLMs, the average accuracy on TreeProbe subtasks was 62 % for models pretrained solely on biomedical corpora and dropped to 48 % when exposed to mixed Tibetan‑TCM data, indicating a clear bias toward biomedical framing. A drift classifier achieved 71 % precision in identifying biomedical reasoning, confirming the systematic shift observed. Sensitivity analysis showed that increasing TCM‑specific tokens raised TCM‑aligned scores by up to 9 percentage points.

## Significance  
TreeProbe provides a diagnostic benchmark for detecting and mitigating cultural bias in medical AI, ensuring that language models respect Tibetan epistemology rather than merely echo dominant biomedical narratives. By exposing the impact of pretraining composition on reasoning drift, it offers actionable guidance for developers aiming to create linguistically inclusive and epistemically fair health‑AI systems.

## Related Concepts  
- Cultural bias in LLMs  
- External ontology drift  
- Tibetan medicine (Tree of Medicine)  
- Traditional Chinese Medicine (TCM)  
- Biomedical reasoning vs. TCM reasoning  
- Expert‑adjudicated benchmarking
