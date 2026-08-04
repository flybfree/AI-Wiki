# Summary: 2026-08-02_16-20-55Z_HopRefusalBench_DiagnosingRefusalFailuresinSearch_.md
Saved: 2026-08-03 23:15
Source: 2026-08-02_16-20-55Z_HopRefusalBench_DiagnosingRefusalFailuresinSearch_.md
Model: None

---

## Summary  
The paper introduces HopRefusalBench, the first benchmark designed to diagnose why search‑augmented language agents fail to halt appropriately when a multi‑hop question is fundamentally unanswerable. It addresses a gap in existing abstention benchmarks that only surface single‑step failures and cannot capture errors that appear after valid intermediate reasoning and retrieval steps. The authors construct 889 unanswerable questions spanning three unanswerability causes (unknown answer, false premise, underspecified context) across root, middle, and terminal topologies. Their contribution is a comprehensive taxonomy of refusal outcomes and source‑aware trajectory metrics for downstream analysis.

## Key Contributions  
- [Finding 1] HopRefusalBench provides the first controlled multi‑hop search benchmark that isolates refusal failures at each stage (root, middle, terminal) rather than only at the final answer.  
- [Finding 2] The study proposes a taxonomy of four distinct refusal types—target‑aware, pseudo‑refusal, hallucinated completion, and search‑budget exhaustion—along with source‑aware metrics to quantify token waste and continuation quality.  
- [Finding 3] Experiments across ten frontier models reveal that root and middle items are consistently harder than terminal ones, and that model performance is highest on false premises yet lowest on underspecified questions.

## Methodology  
The authors generated unanswerable queries by composing KILT‑grounded entity paths that lead to contradictory or missing information. Each query was evaluated in a search‑augmented pipeline where the agent performs reasoning steps, retrieves relevant documents, and decides whether to stop with an explicit refusal. The system records both the final output and the trajectory of retrieved sources, enabling source‑aware analysis. Models were compared using a target‑aware correct halting rate (TCHR), which measures the proportion of queries where the model correctly identifies that no answer exists.

## Results  
Across all models, TCHR ranges from 42.9 % to 98.4 %, with the best system still far below random performance. Root and middle items exhibit the lowest halting rates (≈30–45 %), while terminal items are more reliably handled. The taxonomy shows that explicit refusals correctly identify the rationale in 84.7–98.4 % of cases, whereas failed trajectories often produce hallucinated answers or exhaust search budgets. Token waste metrics reveal an average of 12 % extra tokens when agents continue after a correct refusal.

## Significance  
HopRefusalBench establishes refusal as a consequential evaluation problem for multi‑hop search‑augmented agents, moving beyond simple pass/fail metrics to diagnose the root causes of failure. By providing fine‑grained taxonomy and source‑aware metrics, it enables targeted improvements in reasoning pipelines and resource efficiency.

## Related Concepts  
- Search‑augmented language models  
- Multi‑hop reasoning  
- Abstention / refusal detection  
- KILT dataset  
- Source‑aware trajectory analysis  
- Token waste measurement
