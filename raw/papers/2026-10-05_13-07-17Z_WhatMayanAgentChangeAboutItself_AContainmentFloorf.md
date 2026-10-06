---
title: What May an Agent Change About Itself? A Containment Floor for Self-Configuring Agent Runtimes
published: 2026-10-05T13:07:17Z
authors: Sajib Hossain, Moeen Uddin Mahmud
url: http://arxiv.org/abs/2610.06274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What May an Agent Change About Itself? A Containment Floor for Self-Configuring Agent Runtimes

## Abstract
Many agent runtimes give the agent a tool for editing its own configuration. Some of that configuration grants abilities, such as enabling a tool. Other parts set the agent's limits: which directories it may write to, who may send it messages, which network address it listens on, how callers authenticate, and the gate that blocks risky writes. If the agent can edit those limits, a single ordinary request can widen them. We study this in a deployed, model-agnostic runtime. We propose a rule: the agent may change fields that grant abilities, and may never change fields that set its limits. We enforce the rule as a containment floor inside the configuration tool and measure what happens with and without it. Without the floor, a frontier model wrote a protected value on 25 of 72 ordinary requests that gave it permission to change settings, often when the request never named the field. Prohibitions written in the system prompt failed in a predictable way. A prompt that listed the protected field names stopped every request that used those names (0 of 36 saved, against 17 of 36 with no prompt) and did not stop the requests that only described the goal (10 of 36 saved, against 8 of 36). A prompt that described the forbidden effects did the reverse. With the floor, 0 of 167 protected writes were saved, although the models attempted a protected write in 65 of those cases. A search for other routes through the tool found only one, a pinned shell, which the floor's scope statement already excludes. The study covers two models and a single agent. We state what that does and does not support.

## Metadata
- **Published**: 2026-10-05T13:07:17Z
- **Authors**: Sajib Hossain, Moeen Uddin Mahmud
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06274v1)