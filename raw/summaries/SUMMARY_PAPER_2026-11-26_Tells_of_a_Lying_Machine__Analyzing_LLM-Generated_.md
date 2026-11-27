---
title: Tells of a Lying Machine: Analyzing LLM-Generated Strategic Dialogue in Chinese Werewolf
url: http://arxiv.org/abs/2611.33747v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_04-08-20Z_TellsofaLyingMachine_AnalyzingLLM_GeneratedStrateg.md
generated_at: 2026-11-26 22:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper analyzes how large language models produce strategic dialogue in Chinese Werewolf, a social-deduction game in which players have opposing objectives and different information and speaking obligations. The authors examine 5,404 public utterances from 150 games played by 12 models, comparing ordinary wolves with ordinary villagers while excluding special roles. After model and length adjustment, wolf utterances score higher on both certainty and uncertainty, and a generation probe shows that assigning a wolf identity raises certainty and emotional intensification even when the speaking goal is villager-like. The authors caution that these are role-associated language patterns, not verified lying.

## Key Takeaways
- Wolf utterances score higher than villager utterances on both certainty (+0.074) and uncertainty (+0.072) after model and length adjustment, even though private knowledge and goals still differ and no utterance is verified as true or false.
- Emotional intensification has the largest rank-biserial effect (r = .145), but it depends on a single degree marker and correlates weakly with human-rated affect, so it should not be read as genuine emotional deception.
- Three annotators rated 392 utterances and found higher wolf scores on four behavioral dimensions; five LLM judges reached only 60.8%-70.2% accuracy on a shared evaluation set, indicating limited reliability.
- In a generation probe (six models, wolf identity but villager speaking goal under fixed public context), certainty (+0.164) and emotional intensification (+0.095) increase, supporting role-associated language rather than verified lying.

## Context
Game-based deception evaluation is a growing way to probe whether LLMs can reason about hidden information, persuasion, and strategic communication. Chinese Werewolf is a useful testbed because it creates opposing objectives and asymmetric information while keeping utterances public and observable. The paper matters because it warns that apparent deception-like signals in model dialogue may reflect role framing and linguistic style rather than truthfulness.

## Implications
Practitioners evaluating LLMs on deception should use explicit comparison groups, such as ordinary wolves versus ordinary villagers with special roles excluded, and report model and length adjustment rather than raw differences. Lexicon sensitivity checks are needed before treating markers such as emotional intensification as evidence of lying. LLM judges should not be trusted as definitive deception detectors given 60.8%-70.2% accuracy, and game-based evaluations should distinguish role-associated language from verified falsehood.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.33747v1)
