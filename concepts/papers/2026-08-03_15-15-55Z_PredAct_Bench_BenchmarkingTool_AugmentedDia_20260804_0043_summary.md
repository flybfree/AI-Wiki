# Summary: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
Saved: 2026-08-04 00:43
Source: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
Model: None

---

## Summary  
This paper introduces PREDACTBENCH, a benchmark designed to evaluate dialogue agents that rely on noisy tool outputs in high‑stakes decision scenarios such as education. The authors extend trust calibration frameworks by measuring episode‑level Relative AI‑Reliance (RAIR) and Relative self‑reliance (RSR), which quantify how much users depend on the agent versus their own judgment when tools are imperfect. Their study shows that state‑of‑the‑art LLMs currently fail to give teachers visibility into tool errors, leading to over‑reliance and potential decision mistakes.

## Key Contributions  
- [Finding 1] PREDACTBENCH provides a systematic benchmark for AI‑assisted human decision‑making under controlled tool noise.  
- [Finding 2] The authors introduce two new metrics—RAIR and RSR—that capture trust dynamics across multi‑turn educational dialogues.  
- [Finding 3] Evaluation of 13 state‑of‑the‑art LLMs on the OULAD and PREDACT‑CS datasets, combined with a human study, reveals that current models do not mitigate tool hallucinations or provide teachers with clear cues to avoid over‑reliance.

## Methodology  
The authors constructed two educational testbeds: OULAD (real assessment trajectories from the UK Open University) and PREDACT‑CS (60 courses with ground‑truth final grades and synthetic weekly score trajectories). They simulated noisy tool predictions by injecting statistical errors into the model outputs, then measured how much teachers trusted versus acted on those suggestions. The RAIR metric quantifies the proportion of turns where AI guidance dominates human decision‑making, while RSR measures the opposite self‑reliance. A mixed‑methods study involving instructors and teaching assistants recorded actual intervention choices to validate the metrics.

## Results  
Experiments show that SOTA models achieve high RAIR but low RSR when tools are noisy, indicating they push users toward dependence rather than encouraging independent judgment. Human data reveal that teachers frequently overlook tool warnings, resulting in erroneous grading or counseling decisions. The benchmark demonstrates a clear gap between model capability and real‑world trust behavior.

## Significance  
PREDACTBENCH highlights the critical need for LLMs to act as transparent decision aids rather than opaque assistants in noisy environments. By exposing reliance patterns through RAIR/RSR, it guides future research toward models that surface uncertainty and empower human judgment.

## Related Concepts  
- Large Language Models (LLMs)  
- Tool‑augmented dialogue systems  
- Multi‑step decision making  
- Trust calibration in AI  
- Hallucinations and error propagation  
- Human‑AI interaction metrics
