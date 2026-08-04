# Summary: 2026-08-02_05-00-44Z_JudgingIsNotEnumerating_SilentOmissionsinLLM_Autho.md
Saved: 2026-08-03 20:37
Source: 2026-08-02_05-00-44Z_JudgingIsNotEnumerating_SilentOmissionsinLLM_Autho.md
Model: None

---

## Summary  
This paper investigates the discrepancy between language models’ ability to generate correct test suites and their capacity to evaluate them, revealing that LLMs often produce incomplete acceptable sets due to silent omissions. The authors construct four reference problem families—two with exhaustive truth tables, one executable code suite, and a lexical WordNet set—to measure judgment versus authoring performance across a 24‑parameter range. They find systematic gaps where models judge far better than they create the correct answer keys. Their analysis shows that omissions are more damaging than over‑inclusions and cannot be audited by reviewers.  

## Key Contributions  
- Finding 1: The gap between judging and authoring persists across parameter sizes, up to +0.34 F1 on incompleteness‑proof algorithmic tasks.  
- Finding 2: Models detect planted over‑inclusions six to seven times more often than omissions, indicating a bias toward inclusion.  
- Finding 3: Deploying the authored key in RLVR incurs a 1.9‑point accuracy loss and an 18.5 WordNet‑relative error across seeds.  

## Methodology  
The authors built reference constructions for algorithmic, executable, and lexical tasks, then evaluated two LLM capabilities: (1) authoring the test suite and (2) judging whether a candidate belongs to that suite. They measured F1 scores for both processes, compared detection rates of over‑inclusions versus omissions, computed RLVR scoring cost, and repaired suites by rewriting expected values to match oracle outputs.  

## Results  
Incomplete algorithmic suites show a 0.29–0.34 F1 advantage for judges; the executable code suite admits only ~19–42 % of oracle‑correct solutions when authored. Over‑inclusion detection occurs at a rate six to seven times higher than omission detection, and a production deployment of 43,227 items fails omission‑first at a ratio of 10:1. Repairing each wrong expected value raises yield by 3.3–10.6× across four author families.  

## Significance  
These findings demonstrate that LLMs cannot reliably produce exhaustive, auditable test suites, which threatens automated testing pipelines and the fairness of AI‑generated evaluations. The silent omission problem is a critical flaw in current model‑driven grading systems.  

## Related Concepts  
- Language model authoring  
- Test suite generation  
- F1 metric  
- Omission vs over‑inclusion bias  
- RLVR scoring  
- Lexical reference (WordNet)  
- Oracle correctness
