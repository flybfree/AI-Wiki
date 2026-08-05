# Summary: 2026-07-23_14-37-23Z_Evaluationdesignconditionstheexpert_vs_autoMeSHgap.md
Saved: 2026-07-26 21:28
Source: 2026-07-23_14-37-23Z_Evaluationdesignconditionstheexpert_vs_autoMeSHgap.md
Model: None

---

## Summary  
The paper investigates how evaluation design influences the apparent gap between expert‑assigned MeSH terms and automatic MeSH features in classification tasks, using a controlled comparison of bag‑of‑words logistic regression versus BiomedBERT on the Cohen drug‑class benchmark across three topics. It demonstrates that the size of the expert‑vs‑auto gap varies with cross‑validation scheme and corpus allocation, challenging assumptions about feature source importance. The study also reveals token truncation constraints as a possible contributor to transformer performance differences. Overall, it argues that evaluation methodology can substantially reshape conclusions drawn from benchmark results.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 12 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- Finding 1: The expert‑vs‑auto MeSH gap on the Statins topic is +0.096 WSS@95% under full‑corpus 5‑fold design but shrinks to near zero in 10‑fold CV or when matched to smaller topics.  
- Finding 2: BiomedBERT’s performance matches bag‑of‑words results under the 10‑fold cross‑validation design, suggesting that evaluation scheme can mask underlying feature differences.  
- Finding 3: 15.1% of Statins inputs exceed BiomedBERT’s 512‑token limit when expert MeSH terms are appended, indicating token truncation may limit transformer capacity.

## Methodology  
The authors employed the Cohen et al. (2006) drug‑class benchmark across three topics, training a bag‑of‑words logistic regression classifier with seven random seeds and BiomedBERT with five seeds. They compared outcomes under two evaluation designs: canonical 5‑fold full‑corpus split and 10‑fold cross‑validation at full size, while also matching the corpus to smaller topics (n = 803). Feature asymmetry was quantified by counting tokens beyond the transformer limit.

## Results  
Under the canonical design, bag‑of‑words yields a +0.096 WSS@95% gap for Statins; 10‑fold CV reduces it to +0.021 (CI excludes zero), and matching small topics drives the gap to +0.033 (CI includes zero). BiomedBERT’s canonical result is +0.020, within sampling noise of the 10‑fold bag‑of‑words outcome. Power analysis shows that a non‑zero Statins effect would be undetectable on Opioids or ADHD due to small sample sizes.

## Significance  
The findings demonstrate that evaluation design—particularly cross‑validation scheme and corpus allocation—can dramatically alter perceived feature source effects, undermining the reliability of benchmark conclusions about expert versus automatic MeSH contributions. This matters for screening pipelines where transformer models are standard but may be misinterpreted as superior due to favorable designs.

## Related Concepts  
MeSH (Medical Subject Headings), bag‑of‑words classification, logistic regression, cross‑validation, WSS@95%, token truncation limits, transformer models, Cohen benchmark, feature asymmetry.
