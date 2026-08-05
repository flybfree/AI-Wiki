# Summary: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
Saved: 2026-08-04 01:00
Source: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
Model: None

---

## Summary  
The paper introduces PREDACTBENCH, a benchmark for evaluating AI‑assisted human decision‑making when tools provide noisy predictions in high‑stakes domains such as education. It extends trust calibration to multi‑turn dialogue and measures both the reliance on AI (RAIR) and self‑reliance of humans (RSR). The authors evaluate 13 state‑of‑the‑art LLMs on two real educational datasets, OULAD and PREDACT‑CS, alongside a human study with instructors. The main finding is that current models fail to provide useful visibility when tools are unreliable.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 13 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- The creation of PREDACTBENCH, a benchmark that simulates noisy tool outputs while preserving ground‑truth outcomes for education tasks.  
- Definition of two new metrics: Relative AI‑Reliance (RAIR) and Relative Self‑Reliance (RSR), which quantify how much each participant depends on the AI across dialogue turns.  
- Empirical evidence that top LLMs do not mitigate over‑reliance on hallucinated tool predictions, leading to increased error propagation.

## Methodology  
The authors built a controlled experiment where an LLM generates weekly score forecasts for 60 courses using synthetic but imperfect trajectories. Human participants (teachers and teaching assistants) receive these noisy scores as decision support and make final grade decisions. The system records each turn’s AI output, human response, and the eventual outcome to compute RAIR and RSR. Two datasets—OULAD with real assessment paths and PREDACT‑CS with synthetic weekly trajectories—were used for comparison across models.

## Results  
Experiments showed that even SOTA LLMs produced high‑confidence but often incorrect predictions, which teachers frequently accepted without questioning. RAIR values were consistently above 0.7, indicating strong reliance, while RSR remained low, suggesting limited self‑trust. Model performance dropped when tools were noisy, confirming the need for better transparency.

## Significance  
PREDACTBENCH highlights a critical gap: AI decision support must be trustworthy and transparent to avoid harming educational outcomes. By exposing this failure, it pushes research toward models that can surface uncertainty and encourage human oversight.

## Related Concepts  
- Large Language Models (LLMs)  
- Tool‑augmented dialogue systems  
- Trust calibration metrics  
- Hallucination in AI predictions  
- Human‑AI collaboration in education
