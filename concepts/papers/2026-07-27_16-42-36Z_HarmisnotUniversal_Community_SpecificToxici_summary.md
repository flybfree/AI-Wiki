# Summary: 2026-07-27_16-42-36Z_HarmisnotUniversal_Community_SpecificToxicityDetec.md
Saved: 2026-07-28 22:22
Source: 2026-07-27_16-42-36Z_HarmisnotUniversal_Community_SpecificToxicityDetec.md
Model: None

---

## Summary  
The paper argues that current, one‑size‑fits‑all toxicity detectors for text‑to‑image generation are harmful to marginalized communities and propose a community‑specific approach (CTD). It shows that these universal models mislabel roughly 35 % of images that are safe for dwarfism or blind/low‑vision users as harmful, with zero‑shot F1 scores below random guessing. The authors demonstrate that prompt‑based adaptation (ICL, VQA) and lightweight fine‑tuning improve detection but still fall short of the high performance achieved by general‑purpose detectors.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- Finding 1: Universal toxicity detectors mislabel about one‑third of images that are safe for disability communities.  
- Finding 2: Zero‑shot evaluation yields F1 scores of 0.32 and 0.37, essentially random guessing.  
- Finding 3: Prompt adaptation (GPT‑4o) reaches F1 = 0.50/0.78; parameter‑efficient fine‑tuning on small models reaches 0.48/0.59, yet remains below the ≈0.9 benchmark.

## Methodology  
The authors collaborated with disability experts to craft safety guidelines for dwarfism and blind/low‑vision users, then assembled a dataset of 2 400 T2I images annotated according to those community‑specific rules. They evaluated large vision‑language models and generic toxicity detectors in zero‑shot settings, while also testing prompt‑based adaptation (ICL, VQA) and parameter‑efficient fine‑tuning with ≤100 demonstration examples.

## Results  
Universal detectors achieve F1 = 0.32 for dwarfism and 0.37 for blind/low vision. GPT‑4o with ICL improves to 0.50 and VQA to 0.78, whereas fine‑tuned 0.5b–0.7b models reach 0.48 and 0.59 respectively. All results are far below the ≈0.9 F1 typical of general‑purpose toxicity detectors.

## Significance  
The findings underscore that marginalized groups remain unprotected by existing safety systems, exposing a critical gap in AI ethics. By highlighting the failure of universal approaches, the paper urges sustained research into community‑specific detection to ensure equitable and effective content moderation.

## Related Concepts  
Toxicity detection, text‑to‑image generation, zero‑shot learning, prompt adaptation (ICL, VQA), parameter‑efficient fine‑tuning, F1 score, marginalization, dwarfism, blind/low vision.
