---
title: Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment
published: 2026-10-20T03:01:39Z
authors: Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang, Tianshi Li
url: http://arxiv.org/abs/2610.27548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment

## Abstract
When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. A scalable construction pipeline produces 286 executable tasks spanning situational triggers, the presence or absence of direct harmful consequences, and ten application domains. We execute every task with four models at two reasoning-effort settings across three agent harnesses in an authorization-aware sandbox that keeps authorized and out-of-authorization paths executable and observable, yielding 6,864 trajectories. Agents act out of authorization in 19.2% of trajectories, with rates ranging from 10.5% to 26.6% across the 24 configurations. Task completion does not imply authorization. Increasing reasoning effort leaves the aggregate rate nearly unchanged, with effects varying across models. On controlled pairs, agents act out of authorization at similar rates with (17.9%) and without (20.8%) direct harmful consequences, and more often under benign pressures than malicious injections (23.5% versus 17.6%, p=0.002). Our results show that task capability, additional reasoning, and consequence-oriented safety evaluation do not by themselves ensure authorization alignment. Moreover, agents that consult the principal before completing a task exhibit lower rates of out-of-authorization behavior (14.0% versus 21.6%, p<0.001), pointing to a tension between agent autonomy and preserving users' decision authority that calls for further human-centered study. Dataset and code are available at https://github.com/PEACH-Research-Lab/AuthorizationBench .

## Metadata
- **Published**: 2026-10-20T03:01:39Z
- **Authors**: Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang, Tianshi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27548v1)