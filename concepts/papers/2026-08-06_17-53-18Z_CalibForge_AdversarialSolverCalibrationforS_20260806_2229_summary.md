# Summary: 2026-08-06_17-53-18Z_CalibForge_AdversarialSolverCalibrationforScalingL.md
Saved: 2026-08-06 22:29
Source: 2026-08-06_17-53-18Z_CalibForge_AdversarialSolverCalibrationforScalingL.md
Model: None

---

## Summary  
CalibForge is an autonomous system for synthesizing terminal tasks that are both executable and appropriately challenging for learning agents. It leverages verified solver behavior to perform adversarial calibration, thereby refining candidate tasks so they lie within a learnable zone relative to diverse solvers. The approach addresses the gap between simple validation and deeper understanding of task difficulty across heterogeneous solvers. By generating a large collection of calibrated tasks, CalibForge enables scalable training data for terminal agents.

## Key Contributions  
- [CalibForge autonomously synthesizes terminal tasks using adversarial solver calibration to improve supervision over authoring and validation alone.]  
- [Two calibration strategies—multi‑solver disagreement targeting and contrastive strong‑pass/weak‑fail relations—provide more effective feedback than single‑solver methods.]  
- [The full dataset of 5,431 calibrated tasks yields large gains on benchmark benchmarks, with up to 27.68 percentage points improvement on SWE‑bench Pro.]

## Methodology  
The authors first generate a pool of candidate terminal tasks that are executable by multiple solvers. They then apply adversarial calibration: for multi‑solver calibration, they identify tasks where solver outputs disagree, and revise the task to align with the intended difficulty; for contrastive calibration, they create pairs where one solver passes while another fails, forcing the task to sit in a learnable zone between pass and fail. This iterative process produces calibrated tasks that are suitable for training agents across heterogeneous solvers.

## Results  
CalibForge constructs 5,431 calibrated terminal tasks. Models trained on this full collection achieve 32.58 % and 47.57 % on Terminal‑Bench 2.0. Compared with the base model, improvements reach 24.71 percentage points on Terminal‑Bench 2.0, 27.68 points on SWE‑bench Pro, and 30.04 points on Doc2Repo. These gains demonstrate that adversarial calibration significantly boosts performance.

## Significance  
The work establishes solver‑relative learnability as a practical target for constructing effective, transferable training data. By calibrating tasks to the relative behavior of solvers, CalibForge bridges the gap between mere executability and meaningful difficulty, enabling agents to learn from tasks that are both feasible and appropriately challenging.

## Related Concepts  
- Terminal agents  
- Executable validation  
- Adversarial calibration  
- Solver‑relative learnability  
- Terminal‑task synthesis  
- Benchmark benchmarks (Terminal‑Bench 2.0, SWE‑bench Pro, Doc2Repo)
