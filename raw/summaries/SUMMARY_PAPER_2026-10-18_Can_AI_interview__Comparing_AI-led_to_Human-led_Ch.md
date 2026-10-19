---
title: Can AI interview? Comparing AI-led to Human-led Chat Interviews
url: http://arxiv.org/abs/2610.23149v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_08-43-18Z_CanAIinterview_ComparingAI_ledtoHuman_ledChatInter.md
generated_at: 2026-10-18 20:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents the first direct empirical comparison of data quality between AI-led and human-led qualitative interviews, using a randomized experiment with 41 university students conducted via synchronous text chat. The study finds that AI-interviewers asked more than twice as many questions and elicited roughly 65 percent more respondent text per interview compared to trained non-expert human interviewers, while responses remained on-topic in both conditions and no meaningful difference in specificity was detected. These results support the viability of AI-interviewing as a tool for large-N qualitative data collection in social science research.

## Key Takeaways
- AI-interviewers demonstrated substantially higher throughput: they asked more than twice as many questions per interview and elicited approximately 65 percent more respondent text per interview than human interviewers, while median interview duration remained similar across conditions. This suggests AI can extract more data per unit of time, which is critical for scaling qualitative research.
- Per-question responses were longer when human interviewers were used, but this difference did not survive multiple-testing correction, and only AI-condition participants skipped questions. Responses were almost uniformly on-topic in both conditions, and no statistically significant difference in specificity was detected, though the study design could not rule out a difference of up to three-quarters of a point.
- The experiment used a locally hosted open-weight model with only 7 billion parameters, directly addressing practical concerns around data security, GDPR compliance, and scientific reproducibility that often limit the adoption of commercial AI APIs in academic research settings.

## Context
Social science has long faced a fundamental methodological tension: surveys offer breadth and statistical power but lack the depth of qualitative interviews, while interviews provide rich, contextual understanding but are prohibitively expensive and time-consuming to scale. Large language model chatbots have been proposed as a potential bridge across this divide, yet until this paper, no direct empirical comparison of data quality between AI-led and human-led interviews had been conducted. This study fills that gap by providing a controlled, randomized experimental design that evaluates concrete quality metrics—exposure, specificity, and relevance—rather than relying on anecdotal or theoretical arguments about AI's suitability as an interviewer.

## Implications
For social science researchers and practitioners, these findings suggest that AI-led interviewing is a viable and potentially scalable alternative for collecting qualitative data at larger sample sizes, particularly when using locally hosted models that satisfy data protection and reproducibility requirements. For industry and policy applications, the ability to conduct structured qualitative interviews at scale could transform market research, public opinion gathering, and organizational assessment workflows. However, the small sample size (N=41) and the inability to exclude moderate specificity differences mean that further replication with larger samples and more capable models is necessary before AI-interviewing can be broadly adopted as a standard research method.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23149v1)
