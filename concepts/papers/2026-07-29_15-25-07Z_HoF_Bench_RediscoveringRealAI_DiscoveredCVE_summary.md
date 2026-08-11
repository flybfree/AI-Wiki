# Summary: 2026-07-29_15-25-07Z_HoF_Bench_RediscoveringRealAI_DiscoveredCVEsWithou.md
Saved: 2026-07-29 20:39
Source: 2026-07-29_15-25-07Z_HoF_Bench_RediscoveringRealAI_DiscoveredCVEsWithou.md
Model: None

---

## Summary  
HoF‑Bench is a benchmark designed to evaluate the ability of LLM‑based vulnerability scanners to rediscover real AI‑discovered CVEs without relying on frontier models. The authors construct a dataset of 95 publicly reported vulnerabilities across eight open‑source repositories, then test ten detector backbones (five open‑weight and five proprietary) under a strict protocol that only rewards findings matching the exact code path, root cause, attack condition, and impact. The study shows that no frontier model can perform detection on the benchmark, yet several smaller models recover up to 65 of the 95 CVEs, highlighting the limits of current AI‑driven scanning tools.

## Semantic links
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 5 title terms overlap; 12 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- **Benchmark Construction**: HoF‑Bench provides a compact, reproducible test set derived from AISLE’s Hall of Fame, enabling fair comparison across scanners.  
- **Strict Evaluation Protocol**: The protocol eliminates CVE identifiers and fixes, forcing detectors to rely solely on code‑path matching, which isolates detection quality from external metadata.  
- **Model Diversity Insight**: Results reveal that open‑weight models (21B–284B parameters) achieve comparable performance to proprietary “flash” models, while all models miss CVE‑heavy C infrastructure code.

## Methodology  
The authors assembled 95 CVEs from eight repositories, each pinned at a vulnerable commit. Detectors were given only the source and target file scopes; they could not see CVE IDs or descriptions. A frontier‑model judge was used to define the correct answer (identifying the exact code path, root cause, attack condition, impact). Each detector ran four repeated passes through a scaffold that includes an optional generated‑context stage and a replayable multi‑round triage phase, accumulating 7,600 model–CVE pass records. Difficulty was stratified by programming language.

## Results  
No frontier model detected any CVE on HoF‑Bench. Among the ten models tested, the best open‑weight detector recovered 65 of the 95 CVEs (≈68% recall). The proportion of missed CVEs is heavily concentrated in C code, where detection is most challenging. Repeated runs showed stable performance across passes, confirming reliability.

## Significance  
HoF‑Bench demonstrates that AI‑driven vulnerability scanners can rediscover real vulnerabilities without the need for frontier models, yet they still struggle with certain codebases and languages. This work provides a practical benchmark to guide future research on model efficiency, robustness, and language‑specific performance in security analysis.

## Related Concepts  
- LLM‑based vulnerability detection  
- Frontier models vs. small/flash models  
- Hall of Fame (AISLE)  
- CVE identification accuracy  
- Multi‑round triage evaluation framework
