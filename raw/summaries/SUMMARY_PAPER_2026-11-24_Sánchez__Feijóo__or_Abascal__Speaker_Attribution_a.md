---
title: Sánchez, Feijóo, or Abascal? Speaker Attribution and Ideological Congruence in LLM Personas Reading Posts on X of the Leaders of the Three Main Parties of the 29N General Election in Spain
url: http://arxiv.org/abs/2611.29765v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-22_20-55-14Z_Sánchez_Feijóo_orAbascal_SpeakerAttributionandIdeo.md
generated_at: 2026-11-24 22:09
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether LLM personas respond to who speaks in political communication, not only to what is said, using Spain's 29 November 2026 general election as a testbed. It ran a speaker-attribution experiment with 1,075 anonymised X posts by PSOE, PP and VOX leaders across four topics (economy and employment, household costs, immigration, corruption), assigned to 791 value-grounded LLM personas (150 Inglehart-Welzel cultural map, 150 Moral Foundations Theory) under four conditions (no author, Sánchez, Feijóo, Abascal), yielding 322,470 complete persona-post quartets. Naming any leader lowered support for identical text, with the penalty for Abascal nearly twice as large as those for Sánchez and Feijóo; the penalty followed the persona's elicited left-right self-placement (left personas spared Sánchez, right personas spared Feijóo) even though ideology was never in the message-evaluation prompt.

## Key Takeaways
- Speaker attribution matters independently of content: naming any leader reduced support for identical text, demonstrating that personas respond to source cues rather than only to the message itself.
- The penalty is ideologically structured: left personas spared Sánchez and right personas spared Feijóo, and the Abascal penalty was nearly twice that of Sánchez and Feijóo, despite ideology never appearing in the message-evaluation prompt.
- Topic and leader effects interact: corruption posts were penalised under every name, whereas on the other topics the ideologically closest leader generally produced little or no penalty.
- Alignment with public opinion is ordinal, not quantitative: the leader order matched public opinion in 48 CIS barometers (2022-2026) in all three groups and the sign of all twelve differences, but fit barometers before the model's 2024 knowledge cutoff better than recent ones.

## Context
Political communication research increasingly uses LLM personas as synthetic audiences to study message reception, yet prior reception studies have not tested whether personas respond to the speaker rather than only to the content. This study matters because it probes source effects in a high-stakes, real-world political setting, asking whether value-grounded LLM personas reproduce human-like attribution patterns and can serve as controlled proxies for human audiences in election contexts.

## Implications
The findings show that LLM personas evaluate political speakers through systematic, value-congruent priors, making them useful for controlled source-effect experiments and for stress-testing how attribution changes reception. However, because their alignment with survey barometers is ordinal rather than quantitative and degrades after the model's 2024 knowledge cutoff, they should not be treated as substitutes for empirical public opinion surveys; practitioners should use them for controlled comparisons and hypothesis generation, not as stand-ins for measured public opinion.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.29765v1)
