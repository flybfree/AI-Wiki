# Summary: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
Saved: 2026-07-24 02:38
Source: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
Model: None

---

## Summary  
The paper proposes **RegretBench**, a multi‑turn benchmark that treats clarification as a sequential decision problem for conversational LLMs, measuring not only the quality of questions but also when they are asked and when the conversation ends. By framing ambiguity in terms of hidden user intent and using a regret‑based objective that compares a model’s policy to a reference one, RegretBench captures how much value a model loses relative to an optimal clarification strategy. The authors argue that effective clarification depends on asking the right question at the right time and stopping once the user’s meaning is clear, rather than merely generating plausible queries.

## Key Contributions  
- [Finding 1] RegretBench introduces a regret‑based multi‑turn benchmark that evaluates clarification as policy behavior, moving beyond isolated question quality to capture decision timing and stopping criteria.  
- [Finding 2] The hidden‑intent formulation of ambiguity enables free‑form interaction grounded in semantic‑state tracking, allowing the system to model evolving user meaning across turns.  
- [Finding 3] Effective clarification requires models to ask the right question at the right time and halt once the intended meaning is resolved; final success alone does not guarantee good performance.

## Methodology  
The authors designed RegretBench by first defining a hidden‑intent representation of ambiguous user requests, which guides the generation of clarification questions. The benchmark supports multi‑turn dialogue where each turn updates a semantic state that tracks the user’s evolving intent. Clarification is scored using a regret objective: for every model policy π and reference policy π\*, the loss is the expected value lost by deviating from π*. Experiments evaluate two domains—open‑domain QA and product recommendation—where models generate clarification turns, resolve intent, incur interaction cost, or fail to clarify. The benchmark jointly measures intent resolution, interaction cost, ineffective clarification, and regret.

## Results  
Experiments show that while some LLMs achieve comparable accuracy on final answers, their clarification policies differ markedly in efficiency, robustness to user behavior, and stopping decisions. Models that ask clarifying questions too early or too late incur higher regret, leading to longer interactions and lower utility. The benchmark reveals systematic trade‑offs: a model may be accurate but still suffer from high regret due to suboptimal timing. Overall, RegretBench demonstrates that clarification effectiveness is not captured by accuracy alone.

## Significance  
RegretBench clarifies that clarification in conversational AI is a sequential decision problem where the cost of asking or not asking a question matters as much as the answer itself. By exposing these hidden costs, it guides researchers toward policies that balance user intent resolution with interaction efficiency and respectful stopping points. This insight can improve real‑world deployments where long dialogues and variable user behavior are common.

## Related Concepts  
- Regret minimization in reinforcement learning  
- Multi‑turn dialogue systems  
- Semantic state tracking  
- Hidden‑intent representation of ambiguity  
- Clarification policies  
- Interactive QA and product recommendation scenarios
