# Summary: 2026-08-06_17-53-18Z_CalibForge_AdversarialSolverCalibrationforScalingL.md
Saved: 2026-08-06 22:25
Source: 2026-08-06_17-53-18Z_CalibForge_AdversarialSolverCalibrationforScalingL.md
Model: None

---

## Summary  
The paper introduces CalibForge, an autonomous system that synthesizes terminal tasks by calibrating them against verified solver behavior using adversarial feedback. It proposes two calibration strategies—multi‑solver and contrastive—that define a learnable zone of difficulty relative to each solver’s performance. By generating 5,431 calibrated tasks, CalibForge demonstrates how solver‑relative learning can be operationalized for training agents. The approach moves beyond simple validation toward task construction that directly aligns with the capabilities of diverse solvers.

## Key Contributions  
- [Finding 1] CalibForge autonomously creates executable terminal tasks whose difficulty is calibrated to the behavior of multiple solvers, producing a richer learning signal than authoring or manual validation alone.  
- [Finding 2] The system employs two distinct calibration paradigms: multi‑solver calibration that resolves disagreement across heterogeneous solvers and contrastive calibration that enforces a strong‑pass/weak‑fail relation to anchor a learnable zone of difficulty.  
- [Finding 3] CalibForge yields substantial performance gains on benchmark benchmarks, improving the base model by up to 30 percentage points on Doc2Repo and delivering 47.57% accuracy on Terminal‑Bench 2.0.

## Methodology  
CalibForge starts with a pool of candidate tasks that are verified as solvable by at least one solver. Using adversarial optimization, the system revises these tasks to match the desired difficulty profile defined by the calibration strategy. In multi‑solver calibration, each task is adjusted so that its performance lies between the weakest and strongest solvers in the pool; in contrastive calibration, tasks are tuned to satisfy a strong‑pass/weak‑fail relation for a designated strong solver while failing for weaker ones. The calibrated tasks are then used as training data for learning agents.

## Results  
The authors constructed 5,431 calibrated terminal tasks and evaluated them on three benchmark suites: Terminal‑Bench 2.0, SWE‑bench Pro, and Doc2Repo. Models trained on the full collection achieved 32.58% and 47.57% accuracy on Terminal‑Bench 2.0, respectively, with the largest improvements over baseline models reaching 24.71 percentage points on Terminal‑Bench 2.0, 27.68 points on SWE‑bench Pro, and 30.04 points on Doc2Repo.

## Significance  
CalibForge demonstrates that solver‑relative learnability—making tasks challenging precisely for the solvers they will be trained with—is a practical target for generating high‑quality training data. By aligning task difficulty with solver capabilities, the system reduces overfitting and improves transfer performance across diverse benchmarks.

## Related Concepts  
- Terminal tasks (executable, verifiable problems)  
- Adversarial calibration / optimization  
- Multi‑solver vs. contrastive calibration strategies  
- Solver‑relative learning zone  
- Verifiable task synthesis  
- Benchmark suites: Terminal‑Bench 2.0, SWE‑bench Pro, Doc2Repo
