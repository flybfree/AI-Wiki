# Summary: 2026-07-29_08-06-43Z_OneRunIsNotanIdea_TheImplementationLotteryinAutoma.md
Saved: 2026-07-29 20:29
Source: 2026-07-29_08-06-43Z_OneRunIsNotanIdea_TheImplementationLotteryinAutoma.md
Model: None

---

## Summary  
Automated research platforms rely on single‑run scores to decide which ideas merit further study, but this creates an “implementation lottery” where the outcome depends on the particular implementation sampled rather than the underlying mechanism. The authors introduce the Idea Reliability Audit (IRA) to quantify how much a single run can mislead idea‑level conclusions and argue that evidence about mechanisms should come from multiple implementations, not just one. By systematically comparing runs across tasks and coding‑agent setups, they reveal that implementation variance dominates artifact utility and that winner selection is highly unstable. Their work provides a framework for evaluating the reliability of ideas before they guide branching, transfer, or memory in automated research.

## Key Contributions  
- [Finding 1] Implementation variance on tabular tasks was more than five‑fold larger than variance when re‑running the same artifact, and ten‑fold larger than variance across different implementations.  
- [Finding 2] The winner chosen from a single implementation draw differed from the winner under the other two mean implementations in 25.6 % of decisions for one coding‑agent setup and 43.6 % for another.  
- [Finding 3] Winner reversal persists even after applying card‑level filtering under two outcome‑blind review rules, indicating that a single run cannot reliably certify an idea.

## Methodology  
The authors designed the Idea Reliability Audit (IRA) to measure idea reliability by validating candidate cards, freezing them as artifacts, sampling fresh‑session implementations, and using outcome‑blind fidelity labels. They reran saved artifacts to check consistency and computed idea‑level intraclass correlation (ICC) and leave‑one‑implementation‑out (LOO) winner reversal rates across 312 assignments on 13 tabular tasks and two coding‑agent configurations.

## Results  
Across the experiments, implementation variance exceeded five times the same‑artifact rerun variance and ten times the variance from alternative implementations. The LOO analysis showed that a single implementation’s winner was inconsistent with the mean of the other two in 25.6 % and 43.6 % of cases respectively. Winner reversal remained observable after card filtering, confirming that a solitary run cannot robustly validate an idea.

## Significance  
These findings distinguish idea reliability from the utility of “best‑of‑N” artifact selection, highlighting that automated research systems risk propagating false ideas if they base decisions on isolated runs. The results underscore the need for multi‑implementation evidence before updating beliefs about mechanisms, which is crucial for reliable knowledge transfer and memory in AI research.

## Related Concepts  
idea reliability, implementation lottery, automated research, execution variance, outcome‑blind review, intraclass correlation (ICC), leave‑one‑out (LOO) analysis.
