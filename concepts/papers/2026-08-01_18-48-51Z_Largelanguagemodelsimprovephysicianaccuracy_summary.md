# Summary: 2026-08-01_18-48-51Z_Largelanguagemodelsimprovephysicianaccuracybutlead.md
Saved: 2026-08-03 20:31
Source: 2026-08-01_18-48-51Z_Largelanguagemodelsimprovephysicianaccuracybutlead.md
Model: None

---

## Summary  
The paper investigates how retrieval‑augmented large language models (LLMs) that provide source‑linked clinical support affect physicians’ decision‑making. By introducing CORA, an agentic LLM that can cite relevant literature, the authors show that while accuracy improves, clinicians may develop a false sense of safety when incorrect information is presented with citations. The study demonstrates a trade‑off between enhanced diagnostic performance and a grounding‑dependent risk to clinician judgment.

## Key Contributions  
- [Finding 1] CORA maintains benchmark LLM performance and yields larger gains on cases published after the model’s training data cutoff, indicating effective retrieval‑augmented assistance.  
- [Finding 2] Source‑linked citations increase physicians’ adoption of correct advice from 34 % to 76.9 %, showing that explicit source attribution can boost confidence in LLM recommendations.  
- [Finding 3] When an incorrect answer is citation‑supported, physician resistance drops dramatically (from 92 % to 34.8 %), revealing a safety risk tied to the perceived legitimacy of citations.

## Methodology  
The authors developed CORA—a retrieval‑augmented LLM that can retrieve and cite relevant clinical sources at query time. In a controlled study, they recruited 46 physicians who were presented with diagnostic questions either unaided or with CORA’s citation‑enabled responses. The researchers measured physician accuracy, the proportion of correct answers predicted by citations, perceived support for advice, and resistance to incorrect advice.

## Results  
- Accuracy rose from 70.8 % (unaided) to 82.6 % when using CORA.  
- Citations correctly predicted answers in 87.7 % of cases versus 65.5 % without citations.  
- Perceived support for correct advice increased from 34 % to 76.9 %.  
- Resistance to incorrect, citation‑supported advice fell from 92 % to 34.8 %.

## Significance  
These findings highlight that source‑linked LLM assistance can genuinely improve physician diagnostic accuracy while simultaneously creating a safety concern: clinicians may overestimate the reliability of information presented with citations, potentially leading to false reliance on erroneous outputs. The work underscores the need for mechanisms that maintain confidence only when evidence is truly correct.

## Related Concepts  
- Retrieval‑augmented large language models (LLMs)  
- Agentic LLMs capable of ground‑truth citation retrieval  
- Source‑linking in clinical AI support  
- Physician decision‑making and cognitive bias  
- Grounding‑dependent safety risk in AI‑assisted medicine
