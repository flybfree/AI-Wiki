# Summary: 2026-05-25_17-56-46Z_BeyondSummaries_Structure_AwareLabelingofCodeChang.md
Saved: 2026-05-26 00:00
Source: 2026-05-25_17-56-46Z_BeyondSummaries_Structure_AwareLabelingofCodeChang.md
Model: None

---


## Summary  
The paper proposes a taxonomy‑aware labeling system for code changes that leverages large language models to move beyond simple summarization toward capturing structural attributes of patches. It introduces a two‑stage pipeline: the first stage assigns coarse labels to each diff hunk, while the second refines those labels with relational metadata such as rename propagation and type changes. The approach is built on few‑shot prompting, making it language‑agnostic and customizable without the engineering overhead of traditional static‑analysis tools.

## Key Contributions  
- [Finding 1] The study demonstrates that LLMs can achieve high recall (up to 84 %) and precision (81 %) on manually curated code patches.  
- [Finding 2] The two‑stage pipeline captures structural relationships such as rename propagation and type changes, providing richer metadata than single‑hunk labeling.  
- [Finding 3] Few‑shot prompting enables language‑agnostic label generation without the need for engineering static‑analysis pipelines.

## Methodology  
The authors evaluate four LLMs (e.g., GPT‑4, Claude, Gemini, Llama) across multiple context configurations on a benchmark of natural and synthetic patches. They employ few‑shot prompts to generate initial labels for each diff hunk, then refine those labels using relational reasoning that links hunks together and extracts semantic attributes. The pipeline is modular, allowing customizable label schemas and easy integration with downstream tools.

## Results  
The best configuration yields 84 % recall and 81 % precision, with high accuracy in extracting both relational metadata (e.g., “rename‑propagated”) and attribute metadata (e.g., “type‑changed”). Compared to baseline static analysis alone, the LLM‑based labeling provides a substantial improvement in coverage of change types while requiring minimal manual annotation.

## Significance  
This work shows that LLM‑driven labeling can automate code review workflows, support multilingual projects, and supply structured data for downstream automation. By delivering fine‑grained, relational labels, it reduces the burden on human reviewers and enables more efficient prioritization of patches across diverse codebases.

## Related Concepts  
code diff hunk, taxonomy labeling, few‑shot prompting, static analysis, semantic attributes, rename propagation, type changes, relational metadata.

[[Beyond Summaries: Structure-Aware Labeling of Code Changes with Large Language Models]]