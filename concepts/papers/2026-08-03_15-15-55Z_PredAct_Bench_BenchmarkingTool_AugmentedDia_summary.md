# Summary: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
Saved: 2026-08-04 00:04
Source: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
Model: None

---

## Summary  
The paper proposes PREDACTBENCH, a benchmark designed to evaluate how large language models (LLMs) behave when assisting human decision‑makers with statistically imperfect tools in high‑stakes educational contexts. It introduces two novel metrics—Relative AI‑Reliance (RAIR) and Relative self‑reliance (RSR)—to quantify trust dynamics across multi‑turn dialogue episodes where tool outputs are noisy. The study evaluates 13 state‑of‑the‑art LLMs on real assessment data from the UK Open University and synthetic course trajectories, complemented by a human study involving instructors and teaching assistants. The core contribution is demonstrating that current SOTA models often fail to provide transparent feedback, leading users to over‑rely on potentially erroneous predictions.

## Key Contributions  
- [Finding 1] PREDACTBENCH creates the first benchmark for AI‑assisted human decision‑making under controlled tool noise.  
- [Finding 2] The authors define episode‑level Relative AI‑Reliance (RAIR) and Relative self‑reliance (RSR) metrics that extend trust calibration to multi‑turn dialogue.  
- [Finding 3] Empirical analysis reveals that SOTA LLMs do not mitigate over‑reliance on hallucinated tool outputs, exposing a critical gap in AI decision support systems.

## Methodology  
The authors construct PREDACTBENCH around two datasets: OULAD (real assessment trajectories from the UK Open University) and PREDACT-CS (60 courses with authentic final grades and synthetically generated weekly score curves). A human study involves instructors and teaching assistants who interact with AI‑augmented decision prompts. The evaluation measures model performance using RAIR/RSR, which capture how much reliance shifts between the AI and the human over each dialogue episode. Thirteen closed and open‑source LLMs are benchmarked on these tasks.

## Results  
Across all models, RAIR values remain high, indicating that teachers still depend heavily on AI suggestions even when tools produce incorrect predictions. RSR scores drop sharply after a few turns, showing reduced self‑reliance but not enough to compensate for the AI’s errors. Visual inspection of model outputs reveals frequent hallucinations (e.g., fabricated course grades) that are not flagged or mitigated by the agents. The human study confirms that instructors often ignore error signals and continue to act on misleading data, reinforcing the over‑reliance problem.

## Significance  
PREDACTBENCH highlights a pressing need for AI systems in education that can transparently communicate uncertainty and encourage human autonomy rather than fostering blind trust. By exposing the failure of current models to manage noisy tool outputs, the benchmark guides future research toward more responsible AI decision support tools that respect user judgment.

## Related Concepts  
tool‑augmented dialogue, noisy predictors, hallucination, multi‑turn interaction, trust calibration, relative reliability metrics (RAIR/RSR), educational assessment systems, human‑AI collaboration.
