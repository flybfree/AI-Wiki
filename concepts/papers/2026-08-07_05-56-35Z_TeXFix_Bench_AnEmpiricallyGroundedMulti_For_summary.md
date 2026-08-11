# Summary: 2026-08-07_05-56-35Z_TeXFix_Bench_AnEmpiricallyGroundedMulti_FormatBenc.md
Saved: 2026-08-10 22:37
Source: 2026-08-07_05-56-35Z_TeXFix_Bench_AnEmpiricallyGroundedMulti_FormatBenc.md
Model: None

---

## Summary  
TeXFix‑Bench is an empirically grounded benchmark that evaluates large language models (LLMs) on repairing LaTeX, Typst, and Markdown documents by fixing a curated set of “hard‑crash” faults. The authors develop the DocMut taxonomy—a 48‑operator, AST‑aware fault model derived from 168 verified errors—and generate 10 437 repair instances across three markup formats to test LLM performance under a zero‑shot protocol with provider‑pinned routing.

## Key Contributions  
- The authors construct **TeXFix‑Bench**, a multi‑format dataset of 10 437 repair instances built from 743 openly licensed seeds, enabling systematic evaluation across LaTeX, Typst, and Markdown.  
- They introduce the **DocMut taxonomy** of 48 AST‑aware operators that capture localized hard‑crash faults mined from Stack Exchange, GitHub commits, and package documentation (κ = 0.34).  
- Empirical results show that LLM repairs exhibit compile success rates ranging from 56.7 % to 84.2 % (intention‑to‑treat) while restoration ranks diverge, revealing that compile success alone overstates repair quality.

## Methodology  
The authors first mined a fault taxonomy by collecting 168 verified hard‑crash LaTeX faults from three sources and applying grounded theory to produce DocMut. Using this taxonomy, they generated synthetic repair instances by applying the 48 operators to each seed document. Evaluation involved seven LLMs deployed under a fixed zero‑shot protocol with provider‑pinned routing; each attempt was logged, and compile outcomes as well as restoration quality were measured via an oracle that restores the original text.

## Results  
Compile success across the intention‑to‑treat group averaged 70.9 % (56.7–84.2 %). Restoration rank does not correlate with compile rank: the model with the lowest compile rate restored content best among its successes. Over 28 129 compiling repairs, 13.6–18.5 % materially altered the document text, indicating that many successful compiles produce low‑quality restorations. The benchmark also demonstrates Typst is markedly harder than LaTeX and Markdown.

## Significance  
TeXFix‑Bench provides a rigorous, multi‑format testbed for assessing LLM‑based document repair beyond compile pass rates, highlighting the need for content‑preservation metrics such as restoration rank and fidelity. By exposing the gap between compile success and true repair quality, it guides future research toward more reliable, human‑centric evaluation protocols.

## Related Concepts  
LaTeX, Typst, Markdown pipelines; AST‑aware operators; fault taxonomy (DocMut); zero‑shot prompting with provider‑pinned routing; compilation, restoration oracle; intention‑to‑treat analysis; repair quality metrics.
