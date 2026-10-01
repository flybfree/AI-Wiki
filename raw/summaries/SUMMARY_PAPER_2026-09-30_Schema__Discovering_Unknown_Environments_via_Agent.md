---
title: Schema: Discovering Unknown Environments via Agentic Program Induction
url: http://arxiv.org/abs/2609.39140v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_07-08-31Z_Schema_DiscoveringUnknownEnvironmentsviaAgenticPro.md
generated_at: 2026-09-30 20:53
model: qwen3.6-35b-a3b
---

## Summary
Schema is an agent harness that addresses the challenge of LLM agents operating in unfamiliar environments with unknown rules by leveraging interactive program induction to organize learning and action. Instead of relying on prose-based records, the agent encodes its evolving understanding as executable programs within a persistent workspace, enabling verification against interaction history and step-by-step execution planning. This approach significantly enhances performance, raising ARC-AGI-3 RHAE from 58.7% to 99.2%, solving all DiG-bench games, and achieving median human-level performance on MazeBench using the same base model.

## Key Takeaways
- Schema replaces traditional prose-based documentation with executable programs, allowing the LLM agent to express its hypothesis about environmental rules as testable code. This structured representation facilitates compact and explicit modeling of unknown mechanisms, enabling the system to check predictions against interaction history and refine its understanding iteratively through a persistent program workspace.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39140v1)
