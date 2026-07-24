# Summary: 2026-07-18_09-02-19Z_DS_GTARCateRisk2026_HybridMulti_AgentLLMSystemwith.md
Saved: 2026-07-24 00:04
Source: 2026-07-18_09-02-19Z_DS_GTARCateRisk2026_HybridMulti_AgentLLMSystemwith.md
Model: None

---

## Summary  
The paper presents DS@GT’s entry in the eRisk 2026 Task 1 challenge, which requires a conversational depression‑screening system that interviews LLM personas and outputs a Beck Depression Inventory II (BDI‑II) score together with four key symptoms for each persona. To achieve this, the authors built a hybrid multi‑agent architecture that replaces the proprietary GPT‑5‑nano interviewer with the open‑source Gemma 27B model while adding three algorithmic components: a precomputed dialogue tree, a reliability‑weighted consensus aggregator inspired by the Weaver framework, and a cluster‑based imputation step for unprobed symptoms. The system was evaluated across all 20 personas using fully automated runs, with the hybrid configuration achieving higher performance than the paid baseline at a markedly lower API cost. This work demonstrates that algorithmic supervision can enable a weaker open‑source model to compete effectively with a stronger proprietary one in conversational mental‑health screening.

## Key Contributions  
- [Finding 1] The hybrid Run 3 achieved an ADODL of 0.9063, ranking third among all complete submissions and second overall out of the 21 teams.  
- [Finding 2] Hybrid Run 3 outperformed the paid baseline Run 1 (ADODL 0.8841) while using roughly one‑quarter of the per‑persona API cost.  
- [Finding 3] The three algorithmic components—precomputed dialogue tree, reliability‑weighted consensus aggregation, and cluster‑based imputation—enable a weaker open‑source model to compensate for its limited reasoning and instruction‑following abilities.

## Methodology  
The authors evolved the system through three stages: (1) a monolithic single‑model prototype that handled both interviewing and scoring; (2) a baseline multi‑agent architecture separating conversational interviewing from BDI‑II scoring under an orchestration layer; and (3) a final hybrid configuration that substitutes GPT‑5‑nano with the open‑source Gemma 27B. To mitigate Gemma’s weaker reasoning, they introduced: a precomputed dialogue tree standardizing interview openers and follow‑ups; a reliability‑weighted consensus aggregator modeled on the Weaver framework to combine multiple agent outputs; and a cluster‑based imputation step that fills in unprobed symptoms using statistical clustering of symptom patterns. All components are executed automatically across the 20 personas.

## Results  
The experimental results show that Run 3’s ADODL (0.9063) is higher than the baseline’s 0.8841, placing DS@GT among the top performers despite using a free model. The hybrid system also reduced per‑persona API usage to about 25 % of the cost associated with the proprietary GPT‑5‑nano interviewer, delivering comparable or better clinical scores at lower expense. These quantitative gains validate the hypothesis that algorithmic supervision can offset model weaknesses.

## Significance  
This research highlights a practical pathway for deploying cost‑effective AI in mental‑health screening: by pairing a weaker open‑source model with structured algorithmic guidance, organizations can achieve high diagnostic accuracy without expensive proprietary services. The findings suggest broader applicability to other low‑resource conversational tasks where human‑like interaction is needed but resources are limited.

## Related Concepts  
- Multi‑agent LLM systems  
- Structured algorithmic guidance  
- Beck Depression Inventory II (BDI‑II)  
- Weaver framework for consensus aggregation  
- Cluster‑based imputation  
- Conversational depression screening  
- Open‑source versus proprietary large language models
