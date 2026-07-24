# Summary: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
Saved: 2026-07-24 02:27
Source: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
Model: None

---

## Summary  
Tencent WorkBuddy Bench is a multi‑domain evaluation suite designed to test coding agents across four real‑world work areas—Code, Web, Office, and Security.  To avoid contamination from public issue text, each task is reverse‑engineered from actual commits or business scenarios into short, colloquial role‑play prompts that cannot be recovered by web search.  The dataset, including environment images, harnesses, tests and reference solutions, is released openly and versioned to guarantee reproducibility and third‑party auditing.  Evaluation runs on two agent harnesses (CodeBuddy Code and Claude Code) under a uniform protocol, with each domain using its own scoring instrument and no overall suite average.  

## Key Contributions  
- [Finding 1] Construction of contamination‑resistant tasks by reverse‑engineering real commits into unrecoverable role‑play prompts.  
- [Finding 2] A unified evaluation framework that spans four distinct work domains, each with its own verification style and scoring instrument.  
- [Finding 3] An open, versioned release enabling full reproducibility and third‑party auditability of the benchmark.  

## Methodology  
The authors reverse‑engineer genuine code commits or pull requests into concise, colloquial prompts that simulate a user’s request without exposing the underlying issue to external search engines.  These prompts are packaged in a consistent directory structure containing environment images, evaluation harnesses, test suites and reference solutions.  All tasks are executed under two agent harnesses—CodeBuddy Code and Claude Code—using a uniform execution protocol.  Each of the four subsets (Repository‑level engineering, Front‑end development, Office/business workflows, Red/Blue‑team security) employs its own verification method and scoring metric; consequently, scores cannot be aggregated across subsets.  

## Results  
The benchmark produces a cross‑model leaderboard that ranks several model families on each domain separately.  Performance varies significantly from one subset to another because of differing scoring instruments, but the open release allows any researcher to re‑run tasks and verify results independently.  No suite‑wide average is reported; instead, domain‑specific scores are presented to highlight strengths and weaknesses per task type.  

## Significance  
By eliminating contamination through reverse engineering and versioning, WorkBuddy Bench provides a trustworthy evaluation environment for coding agents that can be audited by the community.  The separation of scoring instruments prevents unfair comparison across domains, encouraging fairer assessment practices.  Its open nature supports reproducible research and facilitates benchmark adoption beyond Tencent’s internal use.  

## Related Concepts  
Coding‑agent evaluation, multi‑domain benchmarking, contamination resistance, reverse engineering prompts, uniform execution protocol, versioned dataset release, leaderboard ranking, reproducibility, open‑source benchmarking.
