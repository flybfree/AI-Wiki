# Summary: 2026-08-31_22-46-48Z_mimeo_CompilingPublicExpertCorporaintoAgentSkillsa.md
Saved: 2026-09-01 21:44
Source: 2026-08-31_22-46-48Z_mimeo_CompilingPublicExpertCorporaintoAgentSkillsa.md
Model: None
Canonical original paper: [http://arxiv.org/abs/2609.00453v1](http://arxiv.org/abs/2609.00453v1)

---

## Summary  
The paper introduces **mimeo**, an open‑source tool that compiles publicly available expert corpora into structured agent skills and rigorously tests whether the resulting knowledge or persona transfers to a coding agent. It evaluates four distinct claims: (1) providing hard‑to‑find material, (2) creating a recognizable persona, (3) changing the agent’s decisions, and (4) transferring judgment. The study finds that mimeo dramatically improves knowledge access but offers only limited evidence for genuine persona or judgment transfer.

## Key Contributions  
- **mimeo compiles public expert corpora into agent skills with source verification**, producing inspectable reference files.  
- **Knowledge access is markedly enhanced**: mimeo answered all 20 obscure, quotation‑heavy questions, whereas a closed‑book condition succeeded on ≤10 and keyword search (BM25) achieved only 15–17 answers.  
- **Personas written from model memory misstate documented positions** on 1–4 of the 20 answers under every grader, indicating that persona creation can distort expert output.

## Methodology  
The authors gathered public work, extracted quotations, cached the original source text, and built agent‑loadable files. Eight builds were logged to measure model calls (averaging 38) and rejection rates (13.2%). Four expert files were tested with a coding‑agent harness under four conditions: closed‑book retrieval, keyword search (BM25), mimeo’s compiled file, and a plain agent. Accuracy was measured across the same questions, identification of personas on short prompts, and grounding in engineering tasks. Judgment transfer was assessed by evaluating how many pre‑planted problems were solved and how well new application scenarios performed.

## Results  
- **Knowledge access**: mimeo answered every obscure question; closed‑book ≤10, BM25 15–17.  
- **Grounding**: persona misstatements occurred on 1–4 answers under each grader; identification dropped 18–23 points when task material was added.  
- **Mimeo vs memory profile**: indistinguishable on short open prompts, suggesting no strong persona effect.  
- **Judgment transfer ceiling**: both conditions solved 94–97% of planted engineering problems and scored 94–100% on 16 new scenarios; AI‑judged “sounds like the expert” scores varied between judges.

## Significance  
The evidence supports mimeo as a compact, inspectable reference for an individual’s knowledge but does not demonstrate reliable transfer of their judgment. It cautions against relying on a single AI judge and highlights a gap between persona creation and genuine skill transfer.

## Related Concepts  
- Agent skills  
- Public expert corpora  
- Grounding  
- Persona distortion  
- Benchmarking  
- AI‑judged similarity  
- Skill compilation
