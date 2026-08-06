# Summary: 2026-08-05_07-58-09Z_STRIVE_ProbingReasoningLimitsinGradedPlausibilityG.md
Saved: 2026-08-05 22:25
Source: 2026-08-05_07-58-09Z_STRIVE_ProbingReasoningLimitsinGradedPlausibilityG.md
Model: None

---

## Summary  
The paper introduces **STRIVE**, an LLM‑based framework that automatically creates controlled event sets for graded plausibility judgments in psycholinguistics, thereby eliminating the labor‑intensive manual construction of such sets. By probing how models generate plausible versus implausible events across easy and hard difficulty levels, STRIVE reveals the reasoning limits that underlie human‑evaluator agreement. The work both offers a scalable pipeline for event‑set generation/evaluation and provides empirical insights into where current LLMs still struggle.

## Key Contributions  
- **Automated generation of controlled event sets**: The framework varies a single slot while fixing all other features, producing plausible vs. implausible events across four difficulty conditions (plausible‑easy, plausible‑hard, implausible‑easy, implausible‑hard).  
- **Improved generation success with reasoning steps**: Adding a global reasoning scratchpad and evaluator‑guided refinement raises the generation success rate from 16.7 % to 75.0 % across six models (including GPT‑5.1).  
- **Persistent difficulty at the plausibility boundary**: Human disagreement is highest for events near the plausibility threshold, and even the best evaluator reaches only 57 % accuracy on the implausible‑hard condition.

## Methodology  
STRIVE builds an event frame per verb and generates one event for each of the four conditions by altering a single slot while holding all other features constant. The baseline generation prompt is first used; if performance is low, the system inserts a global reasoning scratchpad where the model can iteratively refine its output. An evaluator then scores each generated event, and the process repeats until a higher success rate is achieved. Experiments were conducted on six LLM models across 60 verbs.

## Results  
The baseline generation prompt succeeded only 16.7 % of the time. After incorporating reasoning steps, the success rate climbed to 75.0 %. Human‑evaluator agreement improved with more reasoning effort. Evaluator accuracy on the implausible‑hard condition was modest at 57 %, indicating that events just outside the plausibility boundary remain challenging for both models and humans.

## Significance  
STRIVE reduces manual labor in psycholinguistic studies, enabling researchers to collect large, standardized event sets quickly. It also highlights a fundamental limitation of current LLMs: they can generate high‑quality event frames but still falter near the plausibility boundary, where human judgment is most variable and evaluation accuracy drops sharply.

## Related Concepts  
- Graded plausibility judgments  
- Event frames  
- LLM reasoning (global scratchpad)  
- Human evaluator agreement  
- Plausibility boundary  
- Event slot variation  
- Psycholinguistic data generation
