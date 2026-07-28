# Summary: 2026-07-24_18-03-21Z_AgenticAutoresearchforCTReconstruction.md
Saved: 2026-07-27 23:23
Source: 2026-07-24_18-03-21Z_AgenticAutoresearchforCTReconstruction.md
Model: None

---

## Summary  
The paper proposes an “agentic autoresearch” framework that lets a large‑language‑model (LLM) agent autonomously design, tune, and benchmark 26 different CT reconstruction solvers without human intervention. By iteratively editing the solver code, launching short GPU jobs, reading a single frozen metric, and revising based on feedback, the agent discovers a compact 969‑parameter solver that ties for first place in a low‑dose breast task while using only 0.4 % of the champion’s parameters. The study also shows that rankings derived from idealized (noise‑free) data are unreliable under realistic conditions: noise can invert the leaderboard, and the best method collapses to zero performance on noisy inputs.  

## Key Contributions  
- [Finding 1] An LLM agent can independently implement, tune, and benchmark all 26 CT reconstruction methods using a closed‑loop workflow that requires only a single frozen metric (headroom score).  
- [Finding 2] Ideal‑data leaderboards do not predict robustness; severe input noise flips the ranking and causes the best noiseless method to perform poorly.  
- [Finding 3] Retraining on matched noisy data restores much of the original ranking, as measured by a Spearman correlation that improves from 0.04 to 0.61.  

## Methodology  
The authors built an agentic loop: the LLM edits a reconstruction solver, runs a short cluster job to produce reconstructions, reads one calibrated headroom score (difference between the method’s result and the FBP baseline within the field of view), and revises its code accordingly. The same differentiable fan‑beam projector is used for all methods, ensuring fair comparison. Benchmarking involved 26 solvers on two datasets: the noisy Mayo low‑dose CT dataset and a 128‑view sparse‑view breast task from the noiseless DL‑Sparse‑View Challenge. Validation‑selected iterations were scored on a held‑out test set, then re‑scored on I₀ = 10⁵ photons without retraining, and finally retrained on matched noise levels.  

## Results  
The agent produced a compact solver with 969 parameters that tied the top tier at the 1 % level while using only 0.4 % of the champion’s parameter count. On noisy inputs, the noiseless champion (supervised image denoiser, HR = 0.89) dropped to a score of 0.00, whereas a learned primal‑dual method improved from 0.72 to 0.93. When retrained on matched noise, Spearman’s rho rose from 0.04 to 0.61, indicating that the original ranking was largely a transfer effect rather than a permanent deficit. The study also notes that no single factor (e.g., beam hardening, scatter, anatomy) can certify generality across all realistic challenges.  

## Significance  
This work demonstrates that AI agents can perform full‑cycle CT reconstruction research autonomously and efficiently, reducing human labor and parameter waste. It also reveals a critical flaw in current benchmarking practices: idealized leaderboards mask real‑world performance degradation under noise and other factors. By showing that retraining restores rankings, the study underscores the importance of multi‑factor robustness testing for reliable AI‑driven medical imaging solutions.  

## Related Concepts  
- Large language model (LLM) agent  
- CT reconstruction methods  
- Headroom score as a calibration metric  
- Differentiable fan‑beam projector  
- Sparse‑view breast imaging challenge  
- Transfer effect in AI performance  
- Parameter efficiency and sparsity  
- Robustness to input noise, beam hardening, scatter, anatomy
