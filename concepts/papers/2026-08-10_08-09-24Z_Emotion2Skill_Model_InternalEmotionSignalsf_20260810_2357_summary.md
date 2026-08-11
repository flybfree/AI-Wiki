# Summary: 2026-08-10_08-09-24Z_Emotion2Skill_Model_InternalEmotionSignalsforAdapt.md
Saved: 2026-08-10 23:57
Source: 2026-08-10_08-09-24Z_Emotion2Skill_Model_InternalEmotionSignalsforAdapt.md
Model: None

---

## Summary  
The paper introduces **Emotion2Skill**, a framework that leverages model‑internal emotion signals to guide adaptive skill selection and evolution in large language models (LLMs). By extracting a 27‑dimensional emotion vector from the residual stream, the authors map this internal state onto a confidence‑gated summary that is injected into the routing prompt at each decision step. This approach moves beyond post‑hoc interpretability to influence actual agent behavior during complex task execution. Experiments on WebShop and ALFWorld demonstrate measurable gains in success rates over zero‑shot baselines.

## Key Contributions  
- [Finding 1] LLM internal emotion representations exist as linear vectors that causally affect behavior, providing a new decision‑level signal for skill orchestration.  
- [Finding 2] Emotion2Skill extracts these vectors and integrates them into both online skill selection and offline skill evolution via confidence‑gated summaries injected into the routing prompt.  
- [Finding 3] Co‑activation analysis reveals semantically coherent emotion–skill pairings, confirming that improvements stem from meaningful internal signals rather than random correlations.

## Methodology  
The authors approached the problem by first analyzing the residual stream of Qwen3 models to capture a compact 27‑dimensional emotion state. This vector is transformed into a confidence‑gated summary that is appended to the routing prompt, allowing the model to weigh skill options according to its internal emotional state. For online selection, the same summary guides which stored procedure is invoked; for offline analysis, trajectory changes are examined to identify abrupt internal shifts that may indicate problematic skill invocations, prompting targeted SOP rewriting.

## Results  
On the WebShop benchmark, Emotion2Skill with Qwen3‑8B boosts success rate by **+26.9 %** relative to a zero‑shot baseline and lifts average success by **+25.5 %**. On ALFWorld, it achieves similar gains, outperforming all existing baselines consistently. The advantage persists on the larger Qwen3‑14B model, confirming scalability.

## Significance  
This work establishes LLM‑internal emotion vectors as a practical decision‑level signal for orchestrating skill systems, extending their utility beyond interpretability and output steering. By enabling adaptive selection and evolution, Emotion2Skill can improve agent reliability and performance in complex, multi‑step tasks where external cues are insufficient.

## Related Concepts  
LLM internal representation, emotion vectors, residual stream extraction, confidence‑gated summary, skill selection, skill evolution, co‑activation analysis, routing prompt injection.
