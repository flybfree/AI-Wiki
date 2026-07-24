# Summary: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
Saved: 2026-07-24 02:47
Source: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
Model: None

---

## Summary  
The paper introduces RegretBench, a multi‑turn benchmark that evaluates clarification policies of LLMs as sequential decision problems rather than isolated question quality. It measures regret relative to a reference policy to capture value loss from ambiguous requests. Experiments show that models can have similar accuracy yet differ in efficiency and stopping behavior. The work argues that effective clarification requires timely, appropriate questions.

## Key Contributions  
- [Finding 1] RegretBench frames clarification as a sequential decision problem with hidden‑intent formulation.  
- [Finding 2] It introduces a regret‑based objective measuring value loss relative to a reference policy.  
- [Finding 3] Experiments reveal that final success alone is insufficient; models vary in interaction cost, robustness, and stopping decisions.

## Methodology  
The authors designed RegretBench by simulating open‑domain QA and product recommendation dialogues where users issue ambiguous requests. The system tracks semantic state across turns, records model clarification actions (asking questions, answering), and computes regret as the difference between user satisfaction under reference policy and actual policy. Evaluation focuses on intent resolution, interaction cost, ineffective clarifications, and stopping decisions.

## Results  
Experiments show that models with high accuracy still incur higher regret when they ask irrelevant or delayed questions, leading to longer interactions and lower user satisfaction. Some models stop prematurely, missing clarification opportunities; others over‑clarify, incurring unnecessary costs. The regret metric correlates strongly with overall dialogue efficiency and robustness.

## Significance  
By shifting evaluation from static accuracy to dynamic regret, RegretBench provides a more holistic view of LLM performance in real conversational settings. It guides research toward policies that balance clarity, timeliness, and user effort, aligning AI behavior with human expectations for efficient communication.

## Related Concepts  
- Sequential decision theory  
- Hidden intent modeling  
- Regret minimization  
- Multi‑turn dialogue systems  
- Semantic state tracking
