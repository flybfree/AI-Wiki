# Summary: 2026-07-30_17-59-11Z_AskChem_Claim_CenteredInfrastructureforChemistryLi.md
Saved: 2026-07-30 22:24
Source: 2026-07-30_17-59-11Z_AskChem_Claim_CenteredInfrastructureforChemistryLi.md
Model: None

---

## Summary  
Chemistry literature synthesis traditionally relies on manually assembling findings from disparate papers, which is inefficient for both human researchers and AI agents. The authors propose AskChem, a claim‑centered infrastructure that treats each paper as a set of atomic, typed claims grounded by DOIs and verbatim evidence. By storing these claims in a shared repository, AskChem enables automated retrieval, verification, and synthesis without the need for manual curation. This shift from document ranking to provenance‑driven retrieval is intended to streamline cross‑paper chemistry search.

## Key Contributions  
- Finding 1: Converting entire papers into atomic, typed claims that are anchored by a DOI and an explicit evidence locator.  
- Finding 2: Building an evidence graph that links related claims through semantic relations, allowing traceable provenance across multiple sources.  
- Finding 3: Introducing a stabilized faceted taxonomy for hierarchical retrieval and browsing, as well as a living taxonomy that situates papers under scientific principles.

## Methodology  
The authors first parse each chemistry publication into individual claims using natural language processing pipelines. Each claim is tagged with its source DOI and either a verbatim quote or an evidence locator (e.g., a figure reference). These claims are then stored in a centralized, version‑controlled store. From this store, AskChem exposes three complementary structures: a faceted taxonomy for stable hierarchical queries, an evidence graph for relational linking, and an exploratory living taxonomy that maps papers onto overarching scientific concepts.

## Results  
On the AskChem‑Bench benchmark, grounding a GPT‑5.5 reader in AskChem yields 100 % resolvable DOIs, compared with 88.3 % without retrieval, and it achieves the highest citation density among five competing systems. The infrastructure currently indexes 2.4 million claims derived from 147 k papers.

## Significance  
AskChem eliminates the manual curation bottleneck that hampers literature synthesis, enabling AI agents to locate, verify, and combine evidence automatically while preserving provenance. This not only accelerates research but also improves the reliability of synthesized answers by providing traceable sources.

## Related Concepts  
- Claim‑centered retrieval  
- Provenance‑carrying claims  
- Evidence graph linking claims through relations  
- Faceted taxonomy for hierarchical browsing  
- Living taxonomy situating papers under scientific principles  
- DOI grounding of evidence  
- Cross‑paper chemistry synthesis  
- AskChem‑Bench benchmarking framework
