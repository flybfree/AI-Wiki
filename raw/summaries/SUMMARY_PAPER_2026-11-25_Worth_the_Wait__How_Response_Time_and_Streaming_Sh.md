---
title: Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement
url: http://arxiv.org/abs/2611.33050v1
type: paper-summary
date: 2026-11-25
source_paper: 2026-11-24_17-57-00Z_WorththeWait_HowResponseTimeandStreamingShapeJudgm.md
generated_at: 2026-11-25 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the speed and delivery format of generative AI responses—streamed word-by-word versus displayed all at once—shape user judgments in blind preference voting systems. Through three naturalistic experiments involving a French government chatbot arena, provider congestion data, and millions of WildChat interactions, the authors find that streaming the same text significantly increases its chance of winning a preference vote, while slower delivery reduces user engagement through fewer follow-up questions. The findings directly contradict the assumption held by arena designers that faster answers would be preferred.

## Key Takeaways
- In the comparIA French government chatbot arena, replaying a stored answer all at once instead of streaming it as it was generated lowered the answer's chance of winning a decisive blind vote by 25.8 percentage points. The identical text won 57% of decisive votes when streamed but only 29% when replayed, and voters rated the replayed version as less complete, more superficial, and more often incorrect—demonstrating that delivery format fundamentally alters perceived quality independent of content.
- Provider congestion that slowed streamed answers produced no detectable net credit in preference votes across 324,029 conversations, but a slower first exchange made visitors significantly less likely to ask a follow-up question. This reveals a hidden cost of latency that preference leaderboards cannot capture because both competing answers are equally slow.
- Analysis of 4,378,514 WildChat replies from everyday ChatGPT use confirmed that congestion-induced delays reduced user continuation, showing that waiting costs engagement in ways that head-to-head comparisons between two slow answers cannot register. Delivery effects moved blind votes in the direction opposite to what the arena's designers expected.

## Context
This research sits at the intersection of human-computer interaction, behavioral economics, and AI evaluation methodology. As large language model providers increasingly deploy reasoning models that deliberate before answering and caching systems that return stored responses instantly, the speed and format of delivery have become design choices that directly influence user perception. The paper challenges the foundational assumption underlying popular model leaderboards such as Chatbot Arena, which treat blind preference votes as pure judgments of textual quality while ignoring how the presentation medium shapes those judgments.

## Implications
For AI service providers, these findings suggest that streaming answers word-by-word is not merely a technical implementation detail but a strategic lever that can shift perceived quality by tens of percentage points, while aggressive caching or instant-display strategies may inadvertently degrade user trust and engagement. For the field of model evaluation, preference leaderboards must account for delivery format as a confounding variable, and providers should reconsider how they budget latency, since the hidden cost of slow responses manifests in reduced user continuation rather than in vote outcomes. Practitioners designing chatbot products should treat streaming as a user-experience feature with measurable effects on perceived completeness and correctness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.33050v1)
