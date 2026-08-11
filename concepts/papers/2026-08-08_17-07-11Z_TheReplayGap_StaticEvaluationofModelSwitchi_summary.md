# Summary: 2026-08-08_17-07-11Z_TheReplayGap_StaticEvaluationofModelSwitchinginLLM.md
Saved: 2026-08-10 23:04
Source: 2026-08-08_17-07-11Z_TheReplayGap_StaticEvaluationofModelSwitchinginLLM.md
Model: None

---

## Summary  
The paper demonstrates that static evaluation of model switching in LLM agents using replay scoring produces misleading results because it assumes the environment remains unchanged after a router swaps models, whereas real‑world forks cause substantial divergence. By forking live SWE‑bench agent trajectories and continuing each branch with different models, the authors expose how many post‑fork actions are rewritten and how often early swaps diverge at the first step. Their analysis also reveals that replay evaluators mispredict every success‑relevant outcome call and generate patches of near‑zero similarity to reality. The study therefore provides a reproducible harness to reveal these hidden issues in agentic routing.

## Key Contributions  
- [Finding 1] Replay‑based evaluation of model switches in LLM agents yields inflated performance gains because it ignores environment changes caused by forks.  
- [Finding 2] A significant fraction (61‑94 %) of actions after forks are altered, with early swaps diverging at the first post‑fork action in 74‑77 % of cases versus only 6‑35 % for controls.  
- [Finding 3] Replay evaluators mispredict every success‑relevant outcome call and produce patch similarity scores between 0.00 and 0.11, indicating they score the wrong world.

## Methodology  
The authors fork live SWE‑bench agent trajectories at controlled points, rebuild the environment for each fork, and continue each branch with a different model (router). They compare these “swap” branches against same‑model control branches that isolate sampling noise. Six paired runs (~900 rollouts) are executed to measure normalized edit distance and outcome flips.

## Results  
Swaps exceed matched controls by +0.25 to +0.66 normalized edit distance, rewriting 61‑94 % of post‑fork actions; early swaps diverge at the first action in 74‑77 %, versus 6‑35 % for controls, leaving only 3 % of replayed states valid. Outcome flips occur only in swap arms: upgrades rescue unsolved instances while downgrades lose the sole solve; zero flips appear across 359 control forks. Replay evaluators mispredict every success‑relevant call and have patch similarity 0.00‑0.11. Temperature‑0 determinism shows FP8‑served controls diverge on >90 % of forks, whereas AWQ‑served ones remain near identical; under tight budgets the stronger model often exhausts its steps without submitting.

## Significance  
This work shows that static replay benchmarks score the wrong world, undermining confidence in claims about router efficiency. It provides a reproducible harness to detect hidden divergence and highlights the need for more realistic evaluation of agentic routing.

## Related Concepts  
LLM agents, model switching, agentic routing, SWE‑bench, normalized edit distance, outcome flips, replay evaluator, temperature‑0 determinism, environment rebuild.
