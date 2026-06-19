---

title: Multi-Agent LLM-based Metamorphic Testing for REST APIs
url: http://arxiv.org/abs/2605.28321v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-27_11-24-46Z_Multi_AgentLLM_basedMetamorphicTestingforRESTAPIs.md
generated_at: "2026-06-11 10:48"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces ARMeta, a tool that employs an LLM‑driven multi‑agent workflow to perform metamorphic testing of REST APIs defined in OpenAPI. The agents generate test scenarios in Given‑When‑Then format, which are then turned into executable tests and run against the target system. Evaluation on two public web applications shows that ARMeta uncovers additional behaviors complementary to conventional scenario‑based testing.

## Key Takeaways
- ARMeta uses an LLM‑based multi‑agent system to create metamorphic test scenarios without explicit oracles, addressing the test oracle problem in REST API validation.
- The generated scenarios are automatically translated into executable tests that can be executed against the system under test, enabling systematic exploration of hidden behaviors.
- Results demonstrate that ARMeta complements existing scenario‑based approaches by exploring new response patterns not covered by traditional tests.

## Context
Metamorphic testing is gaining traction in AI research as it allows systems to verify correctness through relational properties rather than fixed outputs. Integrating large language models into multi‑agent workflows exemplifies the trend of leveraging generative AI for automated test generation and exploration, enhancing coverage while reducing manual effort.

## Implications
For practitioners, ARMeta offers a scalable way to validate REST APIs without maintaining extensive test oracles, lowering maintenance costs. In industry, this approach can improve software quality assurance pipelines, making it easier to detect subtle bugs in dynamic API responses as systems evolve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.28321v1)
