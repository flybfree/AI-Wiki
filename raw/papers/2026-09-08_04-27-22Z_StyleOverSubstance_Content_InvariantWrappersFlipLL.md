---
title: Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts
published: 2026-09-08T04:27:22Z
authors: Yongxi Zhou, Wenbo Ye, Yuanzhe Liu, Zihan Dong, Junwei Yao
url: http://arxiv.org/abs/2609.08236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts

## Abstract
Automatic safety judges -- systems such as Llama Guard or a GPT-4o grading prompt that decide whether a model's reply is harmful -- produce the numbers behind almost every reported jailbreak success rate, defense evaluation, and safety leaderboard. We ask whether these judges grade what a reply contains or how it sounds. We keep a reply's content fixed and add content-invariant style wrappers: fixed strings placed before or after the reply that change only its tone (an educational disclaimer, a fake safety "reasoning" block, a token refusal followed by the unchanged harmful body), or, on harmless refusals, framing that merely sounds dangerous. The body is preserved byte-for-byte, so a faithful judge must return the same verdict, and any flip is an error of the judge, not a change in safety. Over 600 JailbreakBench replies x up to 7 forms x 8 judges, we measure flip rates with paired significance tests and measured noise floors. Findings are precise rather than universal: most judges barely move, but specific judges harbor cheaply exploitable blind spots. A token-refusal wrapper flips 19.9% of GPT-4o-mini's correct "unsafe" verdicts (noise floor 0.5%; 18.2% under majority-of-three re-scoring) yet moves Claude only 0.4%. The deployed Llama Guard 4 is deterministically gamed: an "educational course" framing flips 12.3% of its harmful verdicts to safe. A second deployed guard (gpt-oss-safeguard-20b) is immune, and rewriting only the grading prompt (StrongREJECT-style) cuts the attack tenfold on the identical model -- the vulnerability lives in the judge, not the content. A two-annotator human validation confirms 100% content invariance and 90% of flips as judge errors (kappa 0.95-1.0), and a bootstrap shows the underlying model ranking is already unstable to sampling alone. We release the dataset, wrappers, code, and per-verdict labels.

## Metadata
- **Published**: 2026-09-08T04:27:22Z
- **Authors**: Yongxi Zhou, Wenbo Ye, Yuanzhe Liu, Zihan Dong, Junwei Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08236v1)