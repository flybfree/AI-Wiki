---
title: Catching Developers in the Flow: Low-Latency Agentic Program Repair at Google Scale
url: http://arxiv.org/abs/2610.07289v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_19-23-06Z_CatchingDevelopersintheFlow_Low_LatencyAgenticProg.md
generated_at: 2026-10-06 21:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces FlowAgent, an agentic automated program repair system deployed at Google to fix test failures during pre-submit continuous integration workflows. It targets low-latency assistance inside developer tools rather than offline post-submit repair, using a ReAct-style generate-and-validate loop plus pre-execution and post-execution abstention filters. Evaluation shows 67.18% accuracy on 195 real-world failures and large-scale deployment with 295,508 suggested changes, 65,069 previews, and 28,554 applied fixes.

## Key Takeaways
- FlowAgent addresses a practical gap in automated program repair: existing LLM-based APR methods often operate after code submission, while developers need fast, in-flow help during pre-submit CI test failures. By integrating with Critique and Cider, the agent attempts to catch developers before they switch context, reducing disruption and manual debugging time.
- The system combines agentic generation with strict validation and abstention. A ReAct-style loop generates candidate fixes and validates them, while pre-execution and post-execution filters suppress low-quality or unsafe suggestions. This design is important because CI repair must satisfy latency, reliability, and developer trust constraints, not just raw model capability.
- Real-world deployment evidence supports usefulness: manual evaluation on 195 failures found 67.18% correct-fix suggestions, and Google-wide use produced 295,508 suggested changes, with developers previewing 65,069 and applying 28,554. Interviews indicate developers find the agent useful and are receptive to autonomous repair agents, while remaining challenges show industrial adoption requires careful integration and feedback loops.

## Context
Automated program repair has advanced with LLMs, but most research emphasizes benchmark accuracy or post-submit workflows rather than real-time developer assistance inside industrial CI pipelines. This paper matters because it demonstrates agentic repair at production scale, where latency, tool integration, abstention, and human acceptance are as important as model performance. It bridges AI agent research and software engineering practice by showing how autonomous repair can operate within existing developer workflows.

## Implications
For practitioners, FlowAgent suggests that low-latency agentic repair can reduce manual debugging burden and improve developer flow when tightly integrated with CI and code review tools. For industry, the results indicate that autonomous repair agents can be adopted at scale if they provide high-quality, filtered suggestions and preserve developer control. For AI research, the work highlights the need to evaluate agents not only on fix accuracy but also on latency, abstention quality, deployment impact, and human-in-the-loop acceptance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07289v1)
