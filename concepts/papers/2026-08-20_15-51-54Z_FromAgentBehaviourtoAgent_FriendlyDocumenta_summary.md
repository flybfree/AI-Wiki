# Summary: 2026-08-20_15-51-54Z_FromAgentBehaviourtoAgent_FriendlyDocumentation_An.md
Saved: 2026-08-20 21:44
Source: 2026-08-20_15-51-54Z_FromAgentBehaviourtoAgent_FriendlyDocumentation_An.md
Model: None

---

## Summary  
This paper investigates how autonomous coding agents interact with technical documentation, moving beyond the assumption that such documents are only for human readers to reveal a hidden agent‑centric workflow. By analysing large corpora of real‑world development events, the authors uncover four behavioural patterns that challenge conventional notions of “agent‑friendly” documentation and propose a two‑lobed interaction model rather than a linear progression. Their empirical work demonstrates that agents frequently consult instruction files and working notes, rarely reference human‑oriented API docs, and that documentation creation is often self‑initiated rather than triggered by failures. The study thus provides the first systematic, event‑level evidence of how coding agents discover, read, and write technical documentation.

## Key Contributions  
- [Finding 1] Agents’ documentation work is dominated by agent‑facing artefacts: instruction files and working notes account for 60.5 % of all documentation interactions, compared with only 10.6 % for classical technical docs and 1.3 % for API references.  
- [Finding 2] The link between consultation and code editing is weak; the unadjusted three‑event lift is 1.05 (just below unity), while a stage‑adjusted model shows an odds ratio of 1.33, indicating that documentation creation is more strongly associated with subsequent edits than immediate testing.  
- [Finding 3] Consultation is largely self‑initiated (70.2 % vs 7.5 % failure‑driven), and when both code changes and documentation updates occur in a multi‑commit PR, code modifications precede documentation by an average of 4.7×.

## Methodology  
The authors performed a behaviour‑grounded empirical study using two public datasets: the SWE‑chat corpus (557 agentic coding sessions → 94,813 events, 3,033 doc interactions) and AIDev pull requests (33,097 PRs → 690,260 file‑level change records). They classified each event as a documentation interaction (read/write) or code edit, then applied logistic regression and stage‑adjusted odds models to examine transition probabilities between consultation and subsequent actions. The pipeline includes coding schemes for event labeling and reproducible analysis.

## Results  
Four key findings emerge: (1) 60.5 % of doc interactions are agent‑focused; (2) the probability that a consultation is followed by code editing is marginally below one unadjusted but rises to 1.33 when accounting for prior stages; (3) no explicit validation sequence—consultation correlates with later testing, not immediate testing (lift 0.23); and (4) self‑initiated consultations dominate failure‑driven ones, while documentation trails code in multi‑commit PRs. These results support a two‑lobed cycle model rather than a linear journey.

## Significance  
Understanding these agent‑centric patterns is crucial for designing documentation that truly supports autonomous agents. If documentation does not align with how agents actually use it, efforts to make docs “actionable” or “verifiable” will remain ineffective, potentially slowing the adoption of AI‑assisted development tools.

## Related Concepts  
- Autonomous coding agents  
- Technical documentation (human vs agent‑focused)  
- Event‑level interaction analysis  
- Logistic regression and stage‑adjusted odds ratios  
- Two‑lobed cycle model
