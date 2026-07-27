# Summary: 2026-07-24_11-37-19Z_WhyLargeLanguageModelsandHumansConvergeandDivergei.md
Saved: 2026-07-26 21:49
Source: 2026-07-24_11-37-19Z_WhyLargeLanguageModelsandHumansConvergeandDivergei.md
Model: None

---

## Summary  
This paper investigates why large language models (LLMs) sometimes agree with human judgments of creativity and other times do not. By analyzing three experiments that compare LLM assessments to those of real people, the authors uncover that alignment depends on which aspects of creativity are emphasized and on the evaluation standards each model adopts. The study demonstrates that LLMs converge most strongly with humans on novelty‑focused criteria but diverge when contextual information—such as social or market relevance—is required. These findings clarify the mixed evidence about LLM‑human agreement and suggest that selecting an evaluator is a strategic choice.

## Key Contributions  
- [Finding 1] LLMs generally rely on a narrower subset of human creativity evaluation standards, showing strongest convergence in novelty but clear divergence in contextual dimensions.  
- [Finding 2] The correlation between LLM and human evaluations is moderate; models with broader standards are better at distinguishing ideas that humans rate as more versus less creative.  
- [Finding 3] LLMs are less sensitive to contextual information: changes in context alter human creativity ratings but leave LLM ratings largely unchanged.

## Methodology  
The authors conducted three studies using widely used idea prompts and six different LLMs. In Study 1, they compared the dimensions (novelty vs. contextual relevance) that each model emphasized when ranking ideas. Study 2 evaluated 1,103 ideas with human judges and LLM evaluators to measure correlation and discrimination ability across models. Study 3 examined 1,195 ideas where context was varied; it measured how much the added contextual cues affected human versus LLM ratings.

## Results  
Study 1 revealed that novelty‑centric standards align best, while contextual standards cause divergence. Study 2 found moderate overall correlation (r≈0.4) between human and LLM scores, with models using broader criteria performing better at separating highly creative from lowly creative ideas. Study 3 showed that adding context increased human ratings by up to 15 points but had negligible impact on LLM outputs, confirming the model’s insensitivity to contextual cues.

## Significance  
Understanding these patterns matters because it informs practical deployment of LLMs as creativity assessors—e.g., choosing a model whose standards match the evaluation context. The research also highlights that alignment is not universal; it hinges on which dimensions are salient and how models interpret them, guiding developers to mitigate bias in automated judgments.

## Related Concepts  
- Creativity evaluation standards (novelty, contextual relevance)  
- Convergence vs. divergence of human‑LLM judgments  
- Model‑specific evaluation criteria  
- Novelty dimension versus contextual dimension
