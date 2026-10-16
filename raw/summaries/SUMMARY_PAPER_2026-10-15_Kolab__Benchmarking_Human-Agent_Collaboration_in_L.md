---
title: Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows
url: http://arxiv.org/abs/2610.21109v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_02-13-36Z_Kolab_BenchmarkingHuman_AgentCollaborationinLong_H.md
generated_at: 2026-10-15 22:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Kolab, a benchmark dataset comprising over 115 hours of screen recordings capturing 50 professionals across 40 occupations as they collaborate with AI agents on realistic, long-horizon tasks. The authors find that frontier models, both agentic and non-agentic, systematically overestimate the quality of their collaboration with human experts and fail to distinguish between high- and low-quality collaborative interactions, revealing a critical gap in current AI systems' ability to understand and evaluate long-horizon human-agent workflows.

## Key Takeaways
- Kolab operationalizes two capabilities that no existing automation benchmark tests: (1) forecasting whether professionals will adopt, modify, or reject an agent's contribution after it leaves the chat window, and (2) verifying professionals' own judgments of collaboration satisfaction and output quality from the unfolding workflow without constant expert feedback. These capabilities are essential because real professional workflows involve interdependent steps where ongoing interaction—such as revising plans—matters far more than a single-attempt task completion.
- The dataset includes not only screen recordings but also participants' explicit collaboration and output quality judgments, enabling rigorous evaluation of whether AI agents can accurately assess their own collaborative performance. Analysis of the recordings reveals diverse collaboration patterns, emphasizing that the timing and manner of coordination between professionals and agents are critical factors that current benchmarks ignore entirely.
- Empirical findings demonstrate that frontier models consistently overestimate their collaborative effectiveness with experts and cannot reliably differentiate between high-quality and low-quality collaboration. Furthermore, providing longer workflow context does not consistently improve these predictions, suggesting that simply extending context windows is insufficient for building agents that genuinely understand long-horizon collaborative dynamics.

## Context
The AI research landscape has been dominated by agentic benchmarks that measure task completion accuracy, tool use, and autonomous execution—essentially treating agents as solo performers. This paper challenges that paradigm by arguing that strong benchmark scores do not translate into effective real-world collaboration, where humans and agents must coordinate across interdependent professional workflows over extended time horizons. By grounding evaluation in authentic professional settings spanning 40 occupations, Kolab shifts the field's focus from automation metrics to the nuanced, interactive, and judgment-laden reality of human-agent teamwork, addressing a fundamental blind spot in how AI capabilities are assessed.

## Implications
For AI developers and researchers, these findings signal that current frontier models are not yet equipped to function as reliable collaborative partners in professional settings, as they cannot accurately gauge whether their contributions will be accepted or rejected by human experts. Industry practitioners deploying AI agents in complex workflows should be cautious about assuming that high benchmark performance translates into productive collaboration, and should prioritize systems that can assess collaboration quality from unfolding interactions rather than relying on single-shot task completion. The dataset itself provides a foundation for future research into building agents that truly understand when, how, and whether their contributions serve human collaborators effectively.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21109v1)
