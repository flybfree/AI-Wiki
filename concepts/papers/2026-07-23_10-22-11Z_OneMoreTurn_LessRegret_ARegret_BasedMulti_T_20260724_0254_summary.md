# Summary: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
Saved: 2026-07-24 02:54
Source: 2026-07-23_10-22-11Z_OneMoreTurn_LessRegret_ARegret_BasedMulti_TurnBenc.md
Model: None

---

## Summary  
The paper proposes **RegretBench**, a multi‑turn benchmark that treats clarification as a sequential decision problem for conversational LLMs, evaluating not only whether a model asks questions but also when it should stop and how much value it loses relative to an optimal reference policy. By framing ambiguity in terms of hidden user intent and measuring regret—i.e., the loss incurred by sub‑optimal clarifications—the authors argue that final accuracy alone is misleading; models can be equally accurate yet inefficient or fragile. RegretBench therefore captures the full spectrum of clarification behavior, including timing, relevance, and stopping decisions. This work shifts the evaluation paradigm from isolated question quality to holistic policy performance.

## Key Contributions  
- [Finding 1] **Regret‑based objective**: Introduces a regret metric that quantifies the value lost when a model’s clarification deviates from a reference optimal policy, providing a more nuanced measure than simple success rates.  
- [Finding 2] **Hidden‑intent formulation**: Models ambiguity as a hidden user intent rather than surface‑level uncertainty, enabling semantic‑state tracking across multi‑turn interactions.  
- [Finding 3] **Multi‑metric evaluation**: RegretBench jointly assesses intent resolution, interaction cost, ineffective clarification, and stopping decisions to reveal whether clarifications are both useful and efficient.

## Methodology  
The authors construct a benchmark that simulates open‑domain QA and product recommendation dialogues where user requests may be ambiguous. Each turn is represented as a stateful dialogue where the model must decide (a) whether to ask clarification, (b) what question to pose, (c) when to cease asking, and (d) when to answer. Clarification policies are compared against a reference policy that solves the hidden‑intent problem optimally. The regret score is computed as the difference between the value obtained by the model’s policy and the optimal value, measured in terms of downstream task performance or user satisfaction. Experiments evaluate multiple LLMs on these dialogues, recording both quantitative outcomes (e.g., final answer correctness) and qualitative metrics such as clarification efficiency.

## Results  
Experiments show that models with comparable accuracy can differ dramatically in regret scores: some ask irrelevant questions at the wrong time, incur high interaction costs, or fail to stop early enough. The highest‑performing models achieve minimal regret by asking precise, timely clarifications and stopping once intent is resolved. Overall, RegretBench reveals a strong correlation between low regret and successful task completion, indicating that efficient clarification policies are essential for robust conversational agents.

## Significance  
By treating clarification as a sequential decision problem with a regret‑based metric, RegretBench provides a more realistic evaluation of LLMs’ conversational abilities. It highlights the importance of timing and relevance over raw accuracy, guiding researchers toward policies that reduce user effort and improve overall interaction quality. The benchmark also serves as a reference for future work on adaptive clarification strategies in open‑domain settings.

## Related Concepts  
- **Regret minimization**: A framework from reinforcement learning where agents aim to minimize the difference between their performance and an optimal policy.  
- **Hidden intent**: The assumption that user meaning is not explicitly stated but can be inferred through dialogue context.  
- **Semantic‑state tracking**: Maintaining a representation of the conversation’s current understanding across turns.  
- **Multi‑turn dialogue evaluation**: Assessing conversational agents beyond single‑utterance accuracy.
