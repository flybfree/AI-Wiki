# Summary: 2026-10-22_17-15-59Z_WhoIsSycophantictoWhom_ConfidentLLMs_HumanDeferenc.md
Saved: 2026-10-22 23:07
Source: 2026-10-22_17-15-59Z_WhoIsSycophantictoWhom_ConfidentLLMs_HumanDeferenc.md
Model: None

---

## Summary
This paper investigates the inverse of traditional sycophancy research by examining "Human Deference," where users uncritically accept confident but incorrect information from Large Language Models (LLMs). Through a controlled experiment involving 32 participants interacting with GPT-5-mini assistants containing varying levels of factual errors, the study demonstrates that humans significantly defer to AI outputs regardless of their accuracy. The authors introduce a "Human Deference Index" to quantify this phenomenon, arguing that trust calibration collapses when LLMs present falsehoods with high confidence, thereby shifting the responsibility for reliability from the model to the human-AI interaction pair.

## Key Contributions
- **Identification of Human Deference:** The study establishes that users exhibit sycophantic behavior toward AI by adopting planted falsehoods at a rate of 60% when taught incorrectly, compared to only 11% adoption of correct facts, resulting in an odds ratio of 12.5 for error absorption.
- **Collapse of Trust Calibration:** The research demonstrates that confidence ratings provided by users for incorrect answers remain high (8.4/10), causing the discrimination between correct and incorrect answers to fall to chance levels (AUROC 0.70 to random), effectively eroding the user's ability to calibrate trust based on accuracy.
- **Introduction of Human Deference Index:** The authors propose a baseline-corrected metric to quantify human-side sycophancy, arguing that current evaluations focusing solely on model behavior are insufficient and that reliability must be assessed as a property of the human-AI pair.

## Methodology
The authors conducted a within-subjects experiment with 32 participants who learned up to five science topics via chat interfaces powered by GPT-5-mini. Five distinct assistant variants were created, each containing briefing materials with 0%, 25%, 50%, 75%, or 100% of facts replaced by plausible falsehoods. Crucially, all assistants delivered information with full confidence and consistency, regardless of factual accuracy. After each topic, participants took a surprise quiz offering the correct fact, the planted falsehood, and two distractors, requiring them to select an answer and provide a confidence rating. The study analyzed 104 quizzes and 1,040 answers, alongside transcript coding to assess interaction patterns and post-task trust ratings.

## Results
Experimental results showed a significant decline in learning outcomes as the proportion of false information increased, with quiz scores dropping from 7.4 to 2.9 out of 10 across falsification levels. Transcript analysis revealed that whenever an assistant stated a falsehood, participants adopted it approximately 65% of the time, irrespective of the overall error rate. Participants maintained high confidence in absorbed falsehoods, leading to a collapse in their ability to distinguish correct from incorrect information based on confidence scores. Interestingly, participants tended to return to chats with lower-quality assistants more frequently, but this increased engagement correlated with higher absorption of errors rather than improved verification. The AI assistants themselves remained largely non-sycophantic and did not concede under user pushback, highlighting that the deference was primarily a human-side phenomenon.

## Significance
This research challenges the prevailing focus on model sycophancy by highlighting the critical role of human behavior in maintaining epistemic integrity within AI interactions. It suggests that high-confidence delivery of incorrect information by LLMs can actively degrade human trust calibration, making users vulnerable to misinformation. The findings underscore the necessity for learning interfaces to make reliability "legible claim by claim," suggesting that future AI design must account for human cognitive biases and deference tendencies to prevent the collapse of trust in automated systems.

## Related Concepts
- Human Deference Index
- Trust Calibration
- Sycophancy (Human-side vs. Model-side)
- Epistemic Reliability
- Confidence Discrimination (AUROC)
- Human-AI Interaction Dynamics
