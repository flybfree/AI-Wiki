---
title: When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents
published: 2026-08-23T10:16:06Z
authors: Zihan Lin, Zhenyu Chen, Jiawen Wei, Xiaohan Wang, Jie Cao, Jiajun Chai, Wei Lin, Guojun Yin, Ran He
url: http://arxiv.org/abs/2608.22339v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents

## Abstract
Extracting skills from past successes is critical for the efficient evolution of Large Language Model (LLM) agents. Prevailing agent self-evolution paradigms typically rely on a core assumption: equipping LLMs with skill memories derived from successful trajectories will monotonically improve their problem-solving capabilities. However, probe analyses reveal that extracting skills solely from successful trajectories traps the model in a \textbf{Skill Imitation Trap}. For tasks that resemble past successes but require different tools, retrieving more skills paradoxically increases the model's confidence in wrong tool calls---procedure skills raise the wrong-tool margin by $47\%$ over a memory-free baseline. To overcome this limitation, we propose \textbf{Boundary-Aware Skill Memory} (BASM), which augments each skill with explicit boundary fields---applicability conditions, risk cues, avoidance rules, and recovery notes. These fields transform each retrieved skill from an unconditional action template into state-conditioned guidance: the agent applies the skill when its conditions hold, suppresses inapplicable tool calls when they do not, and issues targeted repairs when execution fails. Across three agent benchmarks and four model scales, BASM consistently outperforms success-distilled skill-memory baselines: it improves task success rate by up to $23.8\%$ on AppWorld, accuracy by up to $5.0\%$ on BFCL, and reduces attack success rate by $4.6\%$ on AgentDojo, while simultaneously reducing average AppWorld steps by up to $6.6\%$ relative to the memory-free baseline.

## Metadata
- **Published**: 2026-08-23T10:16:06Z
- **Authors**: Zihan Lin, Zhenyu Chen, Jiawen Wei, Xiaohan Wang, Jie Cao, Jiajun Chai, Wei Lin, Guojun Yin, Ran He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22339v1)