# Summary: 2026-07-30_17-44-31Z_Change2Task_FromRepositoryChangestoExecutableCodin.md
Saved: 2026-07-30 22:23
Source: 2026-07-30_17-44-31Z_Change2Task_FromRepositoryChangestoExecutableCodin.md
Model: None

---

## Summary  
Change2Task is a system that transforms merged pull‑request events into verified, executable coding‑agent tasks and environments by leveraging repository history. It reconstructs task states through three strategies—Patch Reversal, Code Mapping, or Agent Reconstruction—while preserving a healthy base version of the same repository. The approach supplies multiple tasks for training and evaluation without repeatedly setting up storage or environment infrastructure. Evaluation across five common task families demonstrates high success rates and efficiency gains.

## Key Contributions  
- [Finding 1] Change2Task converts merged pull requests into verified executable coding‑agent tasks using patch reversal, code mapping, or agent reconstruction.  
- [Finding 2] It constructs up to 79.6 % of tasks from a pool of 1,130 eligible source changes across five task families.  
- [Finding 3] Historical and reconstructed cases achieve up to 98.0 % matched outcome agreement under agent evaluation.

## Methodology  
The authors treat repository history as a rich evidence source for coding‑agent tasks. They apply three reconstruction techniques—Patch Reversal, Code Mapping, and Agent Reconstruction—to map a healthy base revision to the task state, ensuring that all required development tools are present. The lifecycle is validated from the clean base to the task state and back, guaranteeing reproducibility.

## Results  
Across Bug Fix, Feature Addition, Test Generation, API Migration, and Security Repair, Change2Task achieved 79.6 % verified‑task construction success, recovering 29.2 % more tasks than a baseline that uses only pull requests. Historical and reconstructed cases matched up to 98.0 % under agent evaluation, and the full pipeline reduces storage and setup expenditure by 10.8 %.

## Significance  
By providing scalable, reproducible executable data directly from repository changes, Change2Task eases manual environment management for coding‑agent pipelines. The work proves that historical source modifications can be reliably transformed into tasks, supporting continuous learning without repeated resource consumption.

## Related Concepts  
Repository history; Pull Requests; Patch Reversal; Code Mapping; Agent Reconstruction; Verified Task Construction; Execution Environments; Coding Agents; Continuous Evaluation; Baseline PR construction.
