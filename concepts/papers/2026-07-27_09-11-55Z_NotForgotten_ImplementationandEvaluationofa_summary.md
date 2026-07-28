# Summary: 2026-07-27_09-11-55Z_NotForgotten_ImplementationandEvaluationofaPersona.md
Saved: 2026-07-27 22:55
Source: 2026-07-27_09-11-55Z_NotForgotten_ImplementationandEvaluationofaPersona.md
Model: None

---

## Summary  
The paper introduces a lightweight episodic‑memory module for the humanoid robot head Kim that enables the system to retain and retrieve past conversational episodes using vector‑based semantic retrieval combined with an LLM‑controlled dialogue pipeline. By integrating cosine similarity with a learned memory‑strength metric, the module injects contextually relevant snippets into the generation prompt, thereby addressing the well‑known problem of short‑term memory in social robots. The authors demonstrate that this personalized recall improves human perception of sociability and trustworthiness without provoking negative affective responses such as privacy discomfort or uncanny‑valley feelings.

## Key Contributions  
- A hybrid scoring function that combines cosine similarity with a memory‑strength metric to retrieve the most relevant past interactions for each dialogue turn.  
- Empirical evidence that episodic memory significantly raises perceived sociability (d = 0.60, p < .001), trustworthiness (d = 0.62) and warmth (d = 0.56) in a within‑subjects video study.  
- No increase in perceived disturbance or privacy discomfort was observed, indicating that the implementation is socially acceptable.

## Methodology  
The authors built an episodic memory module that stores each completed interaction as a dense vector embedding and maintains a relevance score for each stored episode. At the start of a new conversation, the system computes cosine similarity between the current LLM prompt (or generated token) and all stored embeddings, then applies the learned strength metric to weight the most pertinent memories. The top‑k retrieved snippets are concatenated into the generation prompt, allowing the LLM to “remember” earlier exchanges. The design is lightweight enough to run on the robot’s head hardware while preserving real‑time performance.

## Results  
In a within‑subjects experiment with 43 participants (Video‑Based Online Study), the HRIES questionnaire was administered before and after exposure to the episodic‑memory system. Mean differences were: sociability = 0.60, trustworthiness = 0.62, warmth = 0.56; all statistically significant (p < .001). The perceived disturbance score remained unchanged at d = 0.00, confirming that the memory feature did not trigger negative affective reactions. Retrieval success rates were high (≈85 % of sessions produced at least one relevant snippet), and participants reported the system felt “more present” during dialogue.

## Significance  
These findings show that episodic memory can act as a social lubricant in embodied human‑robot interaction, enhancing relational quality without eliciting uncanny‑valley or privacy‑related discomfort. The work provides a practical template for integrating persistent recall into LLM‑driven chatbots and robotics platforms, potentially improving long‑term user engagement and trust.

## Related Concepts  
- Episodic memory (personalized recall of past events)  
- Vector‑based semantic retrieval  
- Cosine similarity as a similarity measure  
- Hybrid scoring functions combining similarity and relevance weighting  
- LLM‑controlled dialogue generation  
- Human‑Robot Interaction Evaluation Scale (HRIES)  
- Personalization in AI systems  
- Memory strength metric for episodic recall
