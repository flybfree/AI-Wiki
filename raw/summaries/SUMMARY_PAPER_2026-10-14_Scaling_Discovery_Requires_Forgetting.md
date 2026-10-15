---
title: Scaling Discovery Requires Forgetting
url: http://arxiv.org/abs/2610.20563v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_17-49-37Z_ScalingDiscoveryRequiresForgetting.md
generated_at: 2026-10-14 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how LLM-based research agents plateau when scaling automated discovery through longer iteration, parallel execution, or inter-agent communication, all of which suffer from agents becoming anchored to their accumulated history. The authors demonstrate that periodically discarding search state—sessions, candidate histories, and agent memory—and restarting from the best candidate found so far effectively unblocks the search process, yielding up to 15% improvement over parallel agents and up to 39% over a single agent across heuristic programming, kernel optimization, and model training tasks.

## Key Takeaways
- All three conventional scaling strategies for automated research agents—extended single-agent iteration, parallel independent agents, and communicating parallel agents—eventually plateau because each agent becomes anchored to its own past attempts, progressively making fewer and smaller edits, meaning additional compute budget yields diminishing returns.
- The proposed "forgetting" mechanism involves periodically discarding the entire search state, including every agent's session context and the full candidate history, then restarting the search from only the single best candidate discovered so far, which resets the agents' anchoring bias and allows them to explore novel edit directions they would otherwise avoid.
- The forgetting strategy was implemented within a team of communicating agents and evaluated across four distinct tasks spanning heuristic programming, kernel optimization, and model training, demonstrating consistent gains of up to 15% over parallel-agent baselines and up to 39% over single-agent baselines, suggesting that memory management is as critical as compute allocation for open-ended discovery.

## Context
This work sits at the intersection of automated scientific discovery, LLM agent systems, and search optimization, addressing a fundamental question in the growing field of AI-driven research automation. As LLM agents increasingly serve as autonomous researchers capable of iterative refinement and scored verification, understanding the limits of scaling these systems becomes critical for both theoretical and practical progress. The paper contributes a counterintuitive insight—that strategic forgetting outperforms strategic remembering—that challenges the prevailing assumption that more context and longer histories always improve agent performance.

## Implications
For practitioners building agentic research pipelines, this finding suggests that memory architecture design is a first-class concern alongside model capability and compute budget, and that periodic state resets should be considered a standard component of any multi-agent discovery system. For the broader AI research community, it implies that open-ended discovery tasks require fundamentally different scaling strategies than closed-form optimization, and that the field must develop principled forgetting mechanisms rather than simply accumulating context. Industry applications in automated code generation, hyperparameter search, and scientific hypothesis generation could benefit directly from incorporating forgetting protocols into their agent orchestration frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20563v1)
