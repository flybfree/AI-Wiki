---
title: Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild
published: 2026-10-04T04:03:10Z
authors: Yifan Xiong, Jingyi Ge, Zhenpeng Chen, Yiling Lou
url: http://arxiv.org/abs/2610.04921v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild

## Abstract
LLM-based agentic systems are emerging as a new software paradigm. Modern agents are typically composed of backbone LLMs and a surrounding harness that serves as the operational software infrastructure for agent execution. As agent harnesses grow increasingly complex, agents suffer from diverse harness implementation bugs, raising substantial reliability concerns. In this work, we conduct the first empirical study to systematically investigate the test adequacy of harness in real-world agentic systems. Our analysis reveals that agent harness remains substantially undertested. In particular, LLM-dependent harness (LDH) code, despite its critical role in processing LLM outputs and governing agent behavior, receives limited testing attention, with less than half of its lines and branches covered by existing tests. Motivated by these findings, we further propose HarnessTester, the first harness-oriented test generation technique that incorporates explicit agent-harness contract support to construct contract-faithful test setups and extensively exercise LDH code. Our evaluation shows that HarnessTester substantially outperforms state-of-the-art general-purpose test generation techniques in achieving 75.95%/84.76% larger line/branch coverage gains and 69.89% larger mutation-score gains. Furthermore, HarnessTester detects 122 real-world harness bugs in widely-used agentic systems (e.g., OpenClaw), among which, 88 bugs are previously-unknown bugs and 69 bugs have been confirmed by agent developers. These results highlight the practical effectiveness of HarnessTester in improving test adequacy and assuring the reliability of real-world agentic systems.

## Metadata
- **Published**: 2026-10-04T04:03:10Z
- **Authors**: Yifan Xiong, Jingyi Ge, Zhenpeng Chen, Yiling Lou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04921v1)