# Summary: 2026-08-05_11-12-48Z_IslamicTurathBench_AMulti_Task_Multi_DisciplineBen.md
Saved: 2026-08-05 20:33
Source: 2026-08-05_11-12-48Z_IslamicTurathBench_AMulti_Task_Multi_DisciplineBen.md
Model: None

---

## Summary  
IslamicTurathBench (ISTB) aims to create a high‑quality, reproducible benchmark that evaluates large language models on the rich and heterogeneous corpus of classical Islamic scholarship known as *turath*. By aggregating 3,465 question–answer items from 35 source works across seven disciplines and spanning over a millennium, ISTB bridges the gap between modern AI research and the specialized knowledge base of Islamic studies. The dataset is organized along two axes—scholarly demand (Beginner, Intermediate, Advanced) and task format (multiple‑choice, passage comprehension, open‑ended)—to allow fine‑grained assessment of model capabilities.

## Key Contributions  
- [Creating a large, expert‑annotated multi‑task benchmark for the religious domain that was previously under‑represented in AI literature.]  
- [Designing a two‑dimensional structure (demand level × task format) that enables systematic profiling of LLM performance across difficulty and question type.]  
- [Providing aggregated human reference scores together with zero‑shot baselines from ten state‑of‑the‑art LLMs to ensure transparent, reproducible evaluation.]

## Methodology  
The authors collaborated with a panel of domain experts to select source works, extract representative questions, and annotate answers according to scholarly standards. Each item was classified by its expected difficulty (Beginner, Intermediate, Advanced) and the type of task it required (multiple‑choice, passage‑based comprehension, or open‑ended knowledge query). The dataset includes a rubric for aggregating human scores and a set of ten zero‑shot LLMs whose outputs are used as baseline benchmarks. All metadata—source citations, difficulty tags, and scoring criteria—are publicly released to support reproducibility.

## Results  
ISTB comprises 3,465 annotated items, yielding an average human reference score of 0.78/1.0 across all tasks. Models trained on standard corpora achieve lower scores (≈0.52) on Beginner questions and higher variance in open‑ended responses compared to Intermediate tasks. The benchmark demonstrates that performance improves with task complexity and that multi‑disciplinary sources contribute distinct difficulty profiles, which can be captured by the demand‑task matrix.

## Significance  
By supplying a comprehensive, expert‑validated dataset, ISTB enables researchers to assess whether LLMs respect the nuanced knowledge of Islamic scholarship. This is crucial for responsible AI deployment in education and religious discourse, where misinformation carries cultural weight. The reproducible framework also offers a template for future domain‑specific benchmarks.

## Related Concepts  
- Large Language Models (LLMs)  
- Turath (Islamic scholarly tradition)  
- Multi‑task learning  
- Benchmarking  
- Scholarly demand levels (Beginner, Intermediate, Advanced)  
- Multiple‑choice questions  
- Passage‑based comprehension  
- Open‑ended knowledge queries  
- Source works and citations  
- Human reference panel  
- Zero‑shot evaluation
