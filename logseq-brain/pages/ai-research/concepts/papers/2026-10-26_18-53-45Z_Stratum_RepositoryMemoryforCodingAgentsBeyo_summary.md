# Summary: 2026-10-26_18-53-45Z_Stratum_RepositoryMemoryforCodingAgentsBeyondtheCo.md
Saved: 2026-10-27 21:13
Source: 2026-10-26_18-53-45Z_Stratum_RepositoryMemoryforCodingAgentsBeyondtheCo.md
Model: None

---

## Summary
This paper addresses a critical limitation in current coding agents: the inability to retain persistent memory across sessions, leading to redundant work and forgotten root causes despite large context windows. The authors propose that this is not merely a context-length issue but a fundamental memory-architecture problem requiring persistent, experience-aware repository memory. They introduce "Stratum," a tiered memory system designed to live alongside repositories and serve agents through page-safe tools that explicitly track retrieval costs and completeness. By shifting from transient context windows to indexed external storage, the system aims to enable knowledge survival across sessions, significantly improving efficiency and accuracy in multi-session coding tasks.

## Key Contributions
- **Identification of Memory Architecture Flaws:** The authors demonstrate that storing knowledge in a model’s key-value (KV) cache is prohibitively expensive ($10^4$ to $10^5$ times more bytes than indexed text) and inefficient for mid-size projects, which often exceed production context limits.
- **Analysis of Repository Structure and Selection Bottlenecks:** Through an analysis of 752 real bug-fix commits, the study reveals that fixes typically involve a small subset of files (<10% of the repository), highlighting that the primary challenge is efficient selection rather than raw capacity. Furthermore, they show that structural connectivity (imports/tests) fails to capture 47% of co-edited file pairs, proving that historical experience mining is essential for accurate context retrieval.
- **Development and Validation of Stratum:** The paper presents Stratum, a tiered memory architecture with page-safe tools that provide transparency on what was retrieved and what remains. It demonstrates high performance (1.7 ms median retrieval time) and superior efficacy in multi-session experiments compared to retrieval-only baselines.

## Methodology
The authors approached the problem by first conducting empirical measurements on real repositories to quantify the limitations of current context-window-based approaches. They analyzed storage costs, file edit patterns in bug fixes, and structural connectivity gaps to justify the need for an external memory system. Based on these findings, they designed Stratum as a tiered memory system that integrates with the repository itself. The methodology involved implementing page-safe tools that explicitly state retrieval status and costs. Finally, they evaluated the system using a multi-session experiment involving eight real bugs, comparing agents that inherited prior session memory against a baseline retrieval-only approach to measure success rates and token efficiency.

## Results
The experimental results demonstrate significant improvements in both accuracy and cost-efficiency. In a controlled multi-session experiment, an agent utilizing Stratum’s persistent memory identified the root-cause file in 21 out of 24 trials, compared to only 6 out of 24 for a retrieval-only baseline, with a statistically significant difference (Fisher $p<10^{-4}$). Additionally, the Stratum-based approach achieved these results at 4.5 times lower median token cost. The system also showed robust scalability, maintaining an 8/8 success rate when notes from all eight investigations were pooled into a single store, and demonstrated fast retrieval speeds with a median time of 1.7 ms for a store containing one million nodes.

## Significance
This research is significant because it challenges the prevailing assumption that larger context windows are sufficient for complex coding tasks. By proving that persistent, experience-aware memory is necessary for efficient and accurate bug fixing, the paper shifts the focus from model capacity to architectural design. The ability to inherit knowledge across sessions reduces redundant work, lowers computational costs, and improves the reliability of autonomous coding agents. This has profound implications for the development of long-running, autonomous software engineering assistants that can maintain context over extended periods without incurring prohibitive token costs or losing track of previously established facts.

## Related Concepts
- Persistent Repository Memory
- Context Window Limitations
- Key-Value (KV) Cache Costs
- Experience-Aware Retrieval
- Page-Safe Tools
- Multi-Session Agent Learning
- Structural Connectivity vs. Historical Co-editing

## Original research paper

[Canonical original paper: http://arxiv.org/abs/2610.36153v1](http://arxiv.org/abs/2610.36153v1)
