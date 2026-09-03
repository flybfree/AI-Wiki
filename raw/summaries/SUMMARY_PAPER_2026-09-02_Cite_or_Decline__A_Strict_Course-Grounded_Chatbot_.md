---
title: Cite or Decline: A Strict Course-Grounded Chatbot for STEM Lecture Videos
url: http://arxiv.org/abs/2609.01846v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_20-27-47Z_CiteorDecline_AStrictCourse_GroundedChatbotforSTEM.md
generated_at: 2026-09-02 21:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VideoPoints, a semester‑long deployment of a retrieval‑augmented chatbot that answers course‑specific questions from lecture videos and provides timestamped citations. Across 833 messages, 70.5 % included citations and none crossed the course boundary, while the system declined when no evidence matched. Compared with dense‑only retrieval, its design boosted correct‑lecture retrieval by six point three percentage points on EduVidQA. The platform also supports practice‑question generation, which remains an unmet request.

## Key Takeaways
- Students used it for quick lookups and exam review, and 70.5 % of messages included timestamped citations that never referenced outside material.  
- The chatbot’s retrieval accuracy improved by six point three percentage points over dense‑only methods on the EduVidQA benchmark.  
- When no lecture evidence matched a query, the system declined rather than answered, preserving factual integrity.

## Context
In AI research, retrieval‑augmented generation is a key strategy for grounding large language models in external knowledge. This work demonstrates how course isolation and citation mechanisms can improve factual accuracy in educational settings, showing that grounding systems must respect domain boundaries to be effective.

## Implications
For educators and developers, the findings suggest that chatbots must be tightly coupled to specific curricula and provide verifiable references to build trust. Aligning AI tools with actual study habits like exam review can drive adoption and impact learning outcomes across STEM education.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01846v1)
