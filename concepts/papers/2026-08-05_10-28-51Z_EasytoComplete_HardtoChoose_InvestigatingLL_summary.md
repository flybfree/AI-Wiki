# Summary: 2026-08-05_10-28-51Z_EasytoComplete_HardtoChoose_InvestigatingLLMPerfor.md
Saved: 2026-08-05 20:33
Source: 2026-08-05_10-28-51Z_EasytoComplete_HardtoChoose_InvestigatingLLMPerfor.md
Model: None

---

## Summary  
The paper introduces ProverbIT, an Italian benchmark of 100 multiple‑choice questions that test Large Language Models’ ability to complete proverbs, and evaluates 13 frontier models across three tasks: direct completion, MC selection with the correct answer present, and MC selection without a correct answer. The authors find that while nearly all models succeed at completing proverbs, performance collapses dramatically when the correct ending is absent from the options, especially for reasoning‑oriented LLMs. A detailed Chain‑of‑Thought analysis reveals a systematic bias toward literal synonyms and statements about missing endings, indicating reliance on memorized patterns rather than genuine semantic understanding of figurative language. This work highlights a critical gap between LLM capability in generation tasks and their reasoning performance on culturally embedded expressions.

## Key Contributions  
- [Finding 1] Near‑universal success on proverb completion but severe degradation when answering multiple‑choice questions that lack the correct answer.  
- [Finding 2] Chain‑of‑Thought analysis shows models select literal synonyms and mention correct endings even though those endings are not among the options, revealing a pattern bias.  
- [Finding 3] The observed gap suggests current LLMs depend on memorized patterns rather than deeper semantic comprehension of proverbs.

## Methodology  
The authors constructed ProverbIT with 100 Italian proverb items, each providing one correct completion and three distractors. They measured performance of 13 frontier models—including Large Reasoning Models (LRMs) and traditional LLMs—on the three tasks: direct completion, MC selection with a correct answer present, and MC selection without a correct answer. To uncover reasoning processes, they extracted Chain‑of‑Thought traces via prompting and analyzed the generated text for literal synonyms and statements about missing endings.

## Results  
All models completed proverbs correctly in the generation task (≈90 %+ accuracy). In tasks where the correct ending was absent, performance fell below 50 %, with LRMs dropping to roughly 30 %. The bias analysis identified frequent literal synonyms and explicit mentions of “the correct ending is not among the options,” confirming that models treat the task as a pattern‑matching exercise. Statistical bootstrapping confirmed these drops were significant across all evaluated models.

## Significance  
This study demonstrates that LLMs, despite excelling at generating completed proverbs, cannot reliably reason over culturally embedded figurative language when the answer is hidden among distractors. The findings underscore limitations in current reasoning architectures for tasks requiring inference beyond memorized patterns, which is crucial for applications involving idiomatic or metaphorical understanding.

## Related Concepts  
- Large Language Models (LLMs)  
- ProverbIT benchmark  
- Multiple‑choice question generation  
- Chain‑of‑Thought prompting  
- Figurative language comprehension  
- Cultural embedding in language
