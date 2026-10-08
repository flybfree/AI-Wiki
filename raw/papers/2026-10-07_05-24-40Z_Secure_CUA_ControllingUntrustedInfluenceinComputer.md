---
title: Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents
published: 2026-10-07T05:24:40Z
authors: Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda, Somesh Jha, Tongxin Li, Damien Octeau
url: http://arxiv.org/abs/2610.09469v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents

## Abstract
Computer-use agents (CUAs) perform tasks across applications (such as desktops, mobile apps, and web browsers) by observing graphical interfaces and issuing commands such as clicks and keystrokes. These interfaces combine trusted controls and content with untrusted content needed for legitimate tasks. An adversary controlling this untrusted content can embed instructions or misleading visual cues to change the agent's intended action or redirect its commands to the wrong interface target. We formalize security requirements for both the agent's decisions and their execution through GUI commands. In an ideal execution model, we show that enforcing both requirements at each step protects execution traces.   We instantiate this model in Secure-CUA, our system for secure CUA execution. Its key idea is to commit to an explicit per-action program, called an $\textit{action transaction}$, before accessing untrusted content. Each transaction fixes its queries to untrusted content and the permitted uses of their responses. The system masks untrusted regions and evaluates each transaction to produce the next action, using an isolated query model to answer its queries. It then locates the intended interface target using the masked interface. Under the model's assumptions, Secure-CUA is secure by design, while generating a new transaction at each step helps maintain high task utility by adapting to changing interfaces.   We evaluate Secure-CUA under benign conditions on 400 WebArena tasks using three frontier models across $5$ seeds, yielding $6,000$ execution traces. Secure-CUA achieves an average task success rate of $53.55\%$, compared with $55.12\%$ for Vanilla-CUA and $13.17\%$ for CaMeL-CUA.

## Metadata
- **Published**: 2026-10-07T05:24:40Z
- **Authors**: Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda, Somesh Jha, Tongxin Li, Damien Octeau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09469v1)