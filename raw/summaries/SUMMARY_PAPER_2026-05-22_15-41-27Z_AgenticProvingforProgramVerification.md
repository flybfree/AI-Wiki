---

title: Agentic Proving for Program Verification
url: http://arxiv.org/abs/2605.23772v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-22_15-41-27Z_AgenticProvingforProgramVerification.md
generated_at: "2026-06-11 10:45"
model: nvidia/nemotron-3-nano-4b

---


## Summary  
This paper evaluates Claude Code within an agentic proving framework on the CLEVER benchmark to measure its ability to generate and verify verifiable code. The results show high success rates across specification generation, implementation certification, and end‑to‑end pipeline execution, indicating that agentic provers can currently handle many program verification tasks.

## Key Takeaways  
- Claude generates valid specifications for 98.8% of CLEVER problems, with 81.3% also receiving correct scores on the isomorphism‑based scoring system used by CLEVER.  
- The model certifies implementations against ground‑truth specifications for 87.5% of those problems and achieves a 98.1% success rate when the full generation‑verification pipeline is run with self‑consistent premises.  
- Manual review confirms that Claude provides detailed feedback on its own attempts, pinpointing causes of failure and lingering bugs in the dataset.

## Context  
Agentic AI systems are increasingly used to automate reasoning tasks such as theorem proving and code generation. This work demonstrates how similar architectures can be adapted for program verification, a domain where correctness is paramount. The study situates these capabilities within existing benchmark ecosystems that rely on isomorphism‑based scoring.

## Implications  
The findings suggest that compiler‑in‑the‑loop agentic paradigms are the most effective current approach for foundational program verification, potentially accelerating development of reliable software. For practitioners, this highlights a need to move beyond isomorphism‑based evaluation and adopt more robust, bug‑resilient assessment methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.23772v1)
