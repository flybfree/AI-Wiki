# Summary: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
Saved: 2026-07-24 02:30
Source: 2026-07-23_04-34-06Z_TencentWorkBuddyBench_AMulti_DomainCoding_AgentBen.md
Model: None

---

## Summary  
Tencent WorkBuddy Bench is a multi-domain evaluation suite designed to assess coding agents across four distinct work environments: Code, Web, Office, and Security. The benchmark’s primary contribution lies in its contamination-resistant task construction, where every prompt is reverse-engineered from real commit or business scenarios and rewritten as an original, colloquial role-played request, ensuring that the underlying issue cannot be recovered via web search. This approach eliminates reliance on external knowledge to maintain evaluation integrity while enabling open, reproducible benchmarking.

## Key Contributions  
- [Finding 1] The Tencent WorkBuddy Bench introduces a contamination-resistant dataset where tasks are constructed from real commit or pull request threads and rewritten as original prompts, preventing external recovery of the source material.  
- [Finding 2] The benchmark is structured around four work domains—Code, Web, Office, and Security—each with its own verification style and scoring protocol, avoiding cross-subset score comparability.  
- [Finding 3] The full dataset, including task directories, environment images, evaluation harnesses, tests, and reference solutions, is released openly to ensure end-to-end reproducibility and third-party auditing.

## Methodology  
The authors approached the problem by designing a unified framework for constructing distribution-informed coding tasks across four real-world work domains. Instead of using public issue text, each task was reverse-engineered from actual commit or business scenarios and rewritten as a short, colloquial role-played request. This ensures that the prompt is not recoverable via web search, thus resisting contamination. The dataset is organized into four subsets: repository-level engineering, front-end development, office and business workflows, and red-/blue-team security tasks. All tasks are packaged in a uniform task-directory format and evaluated under a consistent protocol on two agent harnesses—CodeBuddy Code and Claude Code. Dataset versioning and open release ensure reproducibility and auditability.

## Results  
The benchmark evaluates several model families across the four domains, with each subset using its own scoring instrument to prevent cross-subset comparison. The full open release allows third parties to re-run tasks and inspect content, enabling independent verification. While no suite-wide average is reported due to domain-specific scoring, the leaderboard demonstrates varying performance across models and domains, highlighting strengths and weaknesses in different contexts.

## Significance  
This work matters because it addresses a critical flaw in existing coding-agent benchmarks: contamination from external knowledge. By constructing tasks from real commit or business scenarios and rewriting them as original prompts, Tencent WorkBuddy Bench ensures that evaluation reflects the agent’s ability to generate correct code based on its own understanding, not on internet searches. The open, reproducible design fosters trust in benchmark results and enables broader research.

## Related Concepts  
- Contamination-resistant task construction  
- Coding-agent evaluation  
- Multi-domain benchmarking  
- Reproducible machine learning benchmarks  
- Cross-model leaderboards  
- Reverse-engineered prompts
