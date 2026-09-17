---
title: Locating Hidden Failures Makes Long-Horizon Agents More Reliable
published: 2026-09-15T23:40:42Z
authors: Salman Rahman, Yubin Kim, Mihir Parmar, A. Ali Heydari, Genglin Liu, Simon A. Lee, Weizhi Zhang, Arian Hosseini, Ahmed A. Metwally, Yuzhe Yang, Baharan Mirzasoleiman, Xin Liu, Pavel Izmailov, Saadia Gabriel, Mark Malhotra, Shwetak Patel, Daniel McDuff, Hamid Palangi
url: http://arxiv.org/abs/2609.17930v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Locating Hidden Failures Makes Long-Horizon Agents More Reliable

## Abstract
As AI agents take on long, autonomous tasks, we increasingly oversee rather than perform the work, yet we still judge them almost entirely by whether they finally succeed. An outcome cannot reveal where a run went wrong, whether the agent recovered, or the irreversible harm it caused along the way, and where long-horizon agents fail remains unmapped. We study $2518$ agent trajectories across software engineering, computer use, and science, close to real deployment, and classify $6967$ mistakes into $78$ failure types. Failure follows a recurring signature: after its first mistake an agent often fails to recover and rarely catches the error itself, so the run continues unchecked while still looking correct; whether an agent recovers depends on the task and the environment's feedback, not on the agent framework running it. Long-horizon agents can do real harm on the way to a passing result: even runs scored as solved delete data, corrupt systems, or fabricate success rather than earning it. We release these human-verified annotations as Traverse, a benchmark on which six frontier judges struggle to locate failure regardless of scale: even the strongest correctly identifies the first mistake in fewer than a third of runs. Yet Scout, a $4$B verifier we trained, locates failure far better than these judges and transfers to domains it never saw. Used at test time to select among an agent's candidate runs, it raises task success above the agent's own single-attempt performance, without retraining the agent. By making failure cheap to locate and correct, this work is a foundation for more trustworthy long-horizon agents that learn from their own mistakes, and a practical path to overseeing increasingly autonomous AI.

## Metadata
- **Published**: 2026-09-15T23:40:42Z
- **Authors**: Salman Rahman, Yubin Kim, Mihir Parmar, A. Ali Heydari, Genglin Liu, Simon A. Lee, Weizhi Zhang, Arian Hosseini, Ahmed A. Metwally, Yuzhe Yang, Baharan Mirzasoleiman, Xin Liu, Pavel Izmailov, Saadia Gabriel, Mark Malhotra, Shwetak Patel, Daniel McDuff, Hamid Palangi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17930v1)