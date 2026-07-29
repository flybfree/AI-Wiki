# Summary: 2026-07-28_12-16-28Z_AIriskEval_eduDemo_AuditingofPedagogicalRisksinEdu.md
Saved: 2026-07-28 22:47
Source: 2026-07-28_12-16-28Z_AIriskEval_eduDemo_AuditingofPedagogicalRisksinEdu.md
Model: None

---

## Summary  
The paper introduces **AIriskEval‑edu Demo**, a platform that audits the pedagogical quality of instructional explanations by evaluating them against a rubric covering five dimensions—factual accuracy, depth and completeness, focus and relevance, student‑level appropriateness, and ideological bias. The system returns binary decisions with confidence scores for each dimension, offers natural‑language rationales, and (except for depth/completeness) supplies localized evidence spans. It operates in two modes: an “AI mode” that assesses six simulated teacher profiles representing distinct pedagogical behaviors, and a “human mode” that audits user‑written explanations in real time using a locally hosted evaluator.

## Key Contributions  
- Introduces **AIriskEval‑edu Demo**, a tool for auditing pedagogical quality of instructional explanations with binary decisions and confidence scores per five dimensions.  
- Develops a fine‑tuned **Llama 3.1 8B** evaluator that runs on consumer‑grade GPUs, outperforming GPT‑5.5 on most risk metrics.  
- Demonstrates the platform’s effectiveness through simulated teacher profiles and real‑time human auditing, showing practical deployment within institutional infrastructure.

## Methodology  
The authors built AIriskEval‑edu Demo by integrating **GPT‑5.5** via an external API and a self‑hosted **Llama 3.1 8B** evaluator. The local evaluator is fine‑tuned on the **AIriskEval‑edu** dataset, which contains K‑12 instructional explanations annotated for risk and explainability. Two modes are implemented: “AI mode” evaluates six simulated teacher profiles that embody different pedagogical behaviors; “human mode” audits user submissions in real time, delivering binary decisions, confidence scores, rationales, and evidence spans.

## Results  
Experiments show the local evaluator achieves higher accuracy on factual accuracy (92 % vs 85 %), depth/completeness (88 % vs 76 %), focus/relevance (84 % vs 70 %) and student‑level appropriateness (81 % vs 63%). Confidence scores align closely with human judgments, and the platform provides localized evidence spans for non‑depth/completeness risks, enabling targeted feedback.

## Significance  
This work matters because it offers educational institutions a privacy‑preserving, cost‑effective way to continuously monitor the pedagogical quality of AI‑generated explanations, reducing bias and ensuring learning outcomes stay aligned with curriculum goals. By operating locally, institutions avoid reliance on external APIs and maintain control over data.

## Related Concepts  
Pedagogical risk, explainability, rubric‑based evaluation, GPT‑5.5 API integration, local LLM deployment, fine‑tuned Llama 3.1, K‑12 instructional design, AI bias mitigation.
