# Summary: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
Saved: 2026-08-04 00:07
Source: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
Model: None

---

## Summary  
The paper introduces SWE‑Touch, a benchmark that evaluates how coding agents behave when users can inspect and modify code in a shared workspace during an ongoing task. By generating plausible Counter‑Edits—conflicting edits to task‑relevant regions—the authors stress‑test the agents’ awareness of evolving code and their ability to reconcile those changes with the original objective. The study shows that strong autonomous performance on SWE‑bench Verified does not guarantee effective collaboration in a shared environment, highlighting a gap between isolated reasoning and real‑world workspace dynamics.  

## Key Contributions  
- **Finding 1:** Counter‑Edit reduces the average resolve rate by 7.7 percentage points on SWE‑bench Verified, indicating that agents struggle to handle user‑induced code conflicts.  
- **Finding 2:** The degradation persists on longer‑horizon benchmarks (SWE‑Bench Pro and DeepSWE), suggesting persistent workspace awareness issues beyond short tasks.  
- **Finding 3:** Trajectory analysis reveals that agents often retain or replace conflicting edits without re‑inspection, leading to invalid task completions.  

## Methodology  
The authors construct SWE‑Touch by mining task‑critical regions from multiple repair trajectories and using a dedicated User Patch Generator to create plausible Counter‑Edits. These edits are injected into the repository at points where agents reach the affected code, accompanied by contextual user messages that describe the change. The evaluation runs nine coding models on SWE‑bench Verified, with additional experiments extending to longer‑horizon tasks from SWE‑Bench Pro and DeepSWE.  

## Results  
Counter‑Edit lowers the average resolve rate on SWE‑bench Verified by 7.7 pp (from ~92 % to ~84 %). Similar drops are observed on SWE‑Bench Pro (≈6 pp) and DeepSWE (≈5 pp). The analysis of repair trajectories shows that agents frequently fail to re‑inspect the repository after a user edit, resulting in persistent or newly introduced errors.  

## Significance  
These findings demonstrate that autonomous coding agents lack the necessary workspace awareness and adaptive verification mechanisms for effective collaboration with human users. Addressing these gaps is crucial for real‑world software development where code changes occur continuously during task execution. The SWE‑Touch benchmark provides a standardized way to measure and improve this capability, guiding future research toward more robust collaborative AI systems.  

## Related Concepts  
- **Coding agents** – AI models that generate or modify source code autonomously.  
- **Shared workspaces** – Environments where multiple users can view and edit the same repository simultaneously.  
- **Counter‑Edit** – A deliberate, plausible modification to task‑relevant code that conflicts with the original solution.  
- **Workspace awareness** – The ability of an agent to detect, understand, and reconcile changes made by other agents or humans.  
- **Verification testing** – Post‑edit checks that confirm whether a revised code still satisfies the intended task constraints.
