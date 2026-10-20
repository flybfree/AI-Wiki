---
title: SPIDES: Information-Flow Control for Browser Agents
published: 2026-10-16T22:12:45Z
authors: Egor Zverev, Juhee Kim, Leon Trampert, Boris Köpf, Aashish Kolluri, Shruti Tople, Santiago Zanella-Béguelin
url: http://arxiv.org/abs/2610.24277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPIDES: Information-Flow Control for Browser Agents

## Abstract
Browser agents automate complex workflows by reading and acting on arbitrary page content, but this flexibility exposes them to prompt injection attacks and unintended data exfiltration. Recent work argues that LLM-driven browser agents erode traditional web security boundaries such as the Same-Origin Policy (SOP) by acting across origins with the user's authority and no built-in isolation. We argue that restoring SOP is neither sufficient (a same-origin public sink can leak private data) nor necessary (legitimate tasks require authorized cross-origin flows) for protecting the security of users. We propose SPIDES, which instead enforces information-flow control by gating primitive browser actions such as typing, clicking and navigating on labels propagated from element-level HTML confidentiality and integrity annotations. Untrusted and confidential content is masked from the agent's context, while policies block unauthorized flows, providing security guarantees against both prompt injection and data exfiltration that hold independently of the model driving the agent. To evaluate SPIDES and baseline defenses under a common threat model, we build MicroNet, a closed ecosystem of 28 interlinked websites with element-level ground-truth labels and paired benign/adversarial tasks. SPIDES achieves 0% attack success rate by design while retaining high task completion rate and autonomy. Our findings demonstrate that information-flow control is an effective technique to extend web security to browser agents, gaining on autonomy and utility against state-of-the-art baselines. The source code and data are openly accessible at https://github.com/microsoft/SPIDES.

## Metadata
- **Published**: 2026-10-16T22:12:45Z
- **Authors**: Egor Zverev, Juhee Kim, Leon Trampert, Boris Köpf, Aashish Kolluri, Shruti Tople, Santiago Zanella-Béguelin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24277v1)