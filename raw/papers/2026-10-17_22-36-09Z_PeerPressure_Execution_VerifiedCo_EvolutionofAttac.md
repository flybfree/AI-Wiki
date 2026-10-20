---
title: Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security
published: 2026-10-17T22:36:09Z
authors: Khushbu Pahwa, Yubin Ge, Daniele Bonadiman, Xiaofei Ma, Yi Zhang
url: http://arxiv.org/abs/2610.24896v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security

## Abstract
LLM code agents increasingly ship code with little oversight, yet defenders trained on static vulnerability datasets fall behind adapting adversaries. We co-train attacker and defender instead, and let execution decide every reward: an attacker (Red) edits a real repository and earns nothing unless its patch applies, builds, passes the tests, completes its development task and reproduces a real exploit in an isolated container, whose path also labels the entry point, the critical operation and the trace between them.   Peer-Relative Policy Optimization (PRPO) makes both sides populations of LoRA adapters over one frozen base and credits each against same-role peers that faced an identical condition, placing the population inside the policy-gradient baseline rather than the opponent pool, with a tournament preserving diversity. Matching cancels the condition's difficulty: at equal coverage it is worth 2.3 points of balanced accuracy over a baseline computed on other conditions, and it matches a within-policy control at half the verifier spend.   PRPO's 7B diff reviewer reaches 64.8% balanced accuracy on four unseen applications in three untrained languages, 5.5 points above supervised security fine-tuning and 4.4 above a frozen frontier reviewer (Claude Opus 4.8), which it leads by 15.8 on the application it trains on. Its 9B repository agent recovers 23 of 172 held-out VulnGym advisories, against 10 after supervised fine-tuning and 7 for the same backbone untrained under the same scaffold, and locates 17 of 43 reachable entry points against 13 for mini-swe-agent with GLM-5.2. Run unchanged on jailbreak defense, the same algorithm matches or exceeds WildGuard's static F1 at equal corpus and model size. Under a judge distinct from its training oracle it cuts attack success from 36.0% to 4.6%, against WildGuard's 8.9%.

## Metadata
- **Published**: 2026-10-17T22:36:09Z
- **Authors**: Khushbu Pahwa, Yubin Ge, Daniele Bonadiman, Xiaofei Ma, Yi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24896v1)