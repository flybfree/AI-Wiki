# Summary: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
Saved: 2026-07-24 02:38
Source: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
Model: None

---

## Summary  
The Tencent WorkBuddy Bench is a multi‑domain coding‑agent evaluation suite that creates tasks by reverse‑engineering real code commits, pull requests, and business scenarios into short, colloquial role‑play prompts, ensuring the dataset cannot be contaminated through web‑searching. It provides four distinct work domains—Code, Web, Office, and Security—each with its own verification style, packaged in a uniform task directory format for reproducible execution on two agent harnesses (CodeBuddy Code and Claude Code). The benchmark’s contribution lies not only in the construction methodology but also in releasing all components openly so that any third party can audit and rerun each task. By separating scoring instruments per subset and avoiding suite‑wide averages, it enables fair cross‑model comparison across model families.

## Key Contributions  
- [Finding 1] A contamination‑resistant dataset built by reverse‑engineering real commits into unrecoverable prompts, eliminating reliance on public issue text.  
- [Finding 2] Four domain‑specific subsets (Code, Web, Office, Security) each with unique verification styles and scoring instruments to probe complementary facets of real work.  
- [Finding 3] An open, reproducible benchmark framework that releases task directories, environment images, evaluation harnesses, tests, and reference solutions for full auditability.

## Methodology  
The authors approached the problem by first selecting a set of authentic code commits, pull requests, and business scenarios from Tencent’s internal repositories. Each item was rewritten as a short, colloquial request that mirrors how a human would ask an agent to perform a task in a real work context, ensuring the original source is not recoverable via search. The rewritten prompts were organized into four domain folders—Code, Web, Office, and Security—each containing tests, reference solutions, and environment images. A uniform evaluation harness (CodeBuddy Code) and a second agent harness (Claude Code) were used to execute tasks under identical protocols. All artifacts are versioned and publicly released on GitHub, allowing independent re‑runs and inspection.

## Results  
The benchmark was evaluated across several state‑of‑the‑art model families, including open‑source LLMs such as CodeBuddy, Claude, and other proprietary models. Performance is reported per domain subset with its own scoring metric; no overall suite average is provided to avoid bias from differing evaluation scales. The leaderboard shows that certain models excel in security tasks while others dominate code generation, highlighting the value of domain‑specific testing.

## Significance  
This work matters because it introduces a realistic, contamination‑resistant benchmark for coding agents that can be independently audited and extended by the community. By separating scoring per subset, it prevents artificial inflation of overall scores and provides actionable insights into model strengths across different real‑world work contexts.

## Related Concepts  
- Coding‑agent evaluation  
- Contamination resistance in datasets  
- Multi‑domain benchmarking  
- Reverse engineering tasks from commits  
- Open‑source benchmark reproducibility
