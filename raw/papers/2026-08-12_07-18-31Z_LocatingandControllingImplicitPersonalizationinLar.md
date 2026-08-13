---
title: Locating and Controlling Implicit Personalization in Large Language Models
published: 2026-08-12T07:18:31Z
authors: Yueru Yan, Siqi Wu, Thai Le
url: http://arxiv.org/abs/2608.11735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Locating and Controlling Implicit Personalization in Large Language Models

## Abstract
Large language models (LLMs) often shift their outputs in response to implicit demographic cues even when users never state a demographic identity. Previous work has documented this behavior, but the connection between these behavioral changes and the model's internal activations remains unclear. Using matched cued and neutral conversations across five LLMs, we establish that a localized internal activation signal tracks changes in recommendations, with correlations up to r=0.87. When multiple cues appear together, their internal signals largely combine, but the changes in output do not simply add up. We further show that removing the internal signal associated with one cue can suppress its influence, often more effectively than asking the model to ignore demographics via prompting, while largely preserving general benchmark performance. However, the ability to selectively remove one dimension's influence while leaving co-present dimensions intact remains highly model- and attribute-specific. These results connect implicit personalization behavior to an internal signal that can be analyzed and causally controlled.

## Metadata
- **Published**: 2026-08-12T07:18:31Z
- **Authors**: Yueru Yan, Siqi Wu, Thai Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11735v1)