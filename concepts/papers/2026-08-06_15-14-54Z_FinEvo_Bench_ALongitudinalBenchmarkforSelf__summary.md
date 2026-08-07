# Summary: 2026-08-06_15-14-54Z_FinEvo_Bench_ALongitudinalBenchmarkforSelf_Evolvin.md
Saved: 2026-08-06 20:46
Source: 2026-08-06_15-14-54Z_FinEvo_Bench_ALongitudinalBenchmarkforSelf_Evolvin.md
Model: None

---

**## Summary**  
FinEvo‑Bench is a longitudinal benchmark designed to evaluate how self‑evolving agents improve over time within real professional financial workflows. It provides 120 ground‑truth tasks across six domains and twenty business scenes, each with manually reviewed rubrics for quality and compliance. The study compares four self‑evolution scaffolds using the Qwen3.7‑Max backbone while interleaving task streams to isolate experience transfer. By measuring both evolved scores and compliance issues, FinEvo‑Bench quantifies the ability of agents to turn prior experience into later performance gains.

**## Key Contributions**  
- Letta achieves the highest evolved score (91.65) with the fewest compliance issues (0.09 per task).  
- Codex demonstrates the largest self‑evolution gain (+19.37 points) compared to non‑evolving controls.  
- Skill‑only evolution in Claude Code yields higher task quality and fewer compliance problems than memory‑only or combined memory‑skill evolution.

**## Methodology**  
The authors constructed a longitudinal dataset where each scene contains six distinct cases sharing a professional procedure and a rubric for evaluation. Eligible tasks are sourced from institution‑provided procedures and publicly documented cases. Four self‑evolution scaffolds (Letta, Codex, Memory‑Only, Combined) were evaluated on the same Qwen3.7‑Max model with three independently shuffled task streams. Paired non‑evolving controls estimate each scaffold’s retained experience, while an independent Claude Code scoring agent backed by Opus 4.6 evaluates all outputs for compliance and quality.

**## Results**  
Across scaffolds, the evolving condition raises scores by 9.33–19.37 points and reduces compliance issues by 0.12–0.44 per task. Paired score gains at within‑scene ranks 4‑6 exceed those at ranks 1‑3 by 6.10–8.70 points. In Claude Code, skill‑only evolution outperforms memory‑only and combined memory‑skill evolution in both quality and compliance.

**## Significance**  
FinEvo‑Bench bridges the gap between independent task evaluation and real‑world workflow learning, offering a rigorous measure of how agents benefit from accumulated experience. It highlights that structured self‑evolution can significantly boost professional performance while maintaining regulatory compliance, informing future research on adaptive AI in finance.

**## Related Concepts**  
- Self‑evolving agents  
- Longitudinal benchmarking  
- Financial workflow automation  
- Task quality rubrics and compliance monitoring  
- Memory vs. skill evolution strategies  
- Interleaved task streams for experience transfer
