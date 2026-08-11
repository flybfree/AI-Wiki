# Summary: 2026-08-10_00-42-51Z_HowCanRhetoricReward_HackAIReviewers_DissectingRhe.md
Saved: 2026-08-10 23:32
Source: 2026-08-10_00-42-51Z_HowCanRhetoricReward_HackAIReviewers_DissectingRhe.md
Model: None

---

## Summary  
This paper investigates a form of reward‑hacking in AI‑based peer review, asking how rhetorical choices affect the scores that large language models assign to scientific manuscripts while preserving the original content. By systematically altering six rhetorical dimensions across 4 200 full papers and having five LLM reviewers evaluate both the original and rewritten versions under standard and strict protocols, the authors uncover a structured hierarchy of rhetorical sensitivity rather than uniform effects. Their contribution is a detailed analysis that links specific rhetorical patterns—evidence framing, novelty stance, and scope framing—to measurable changes in AI‑generated objective assessments.

## Key Contributions  
- [Finding 1] Rhetorical sensitivity is not uniform; evidence framing and novelty stance generate the strongest positive‑negative contrasts, while scope framing forms a weaker secondary tier.  
- [Finding 2] The magnitude and sign of score changes depend on the AI reviewer’s original score: lower scores tend to rise, higher scores fall, with clearest effects in middle ranges.  
- [Finding 3] Joint rewriting is rewriter‑dependent, reviewer guidance does not consistently outperform an unguided second pass, and repeated rewriting yields diminishing, configuration‑specific returns.

## Methodology  
The authors constructed a controlled corpus of 4 200 full‑paper manuscripts derived from 120 anonymized ICLR 2026 submissions. Two LLM rewriters were programmed to transform six rhetorical dimensions in opposing directions (e.g., evidence framing vs. omission). Five LLM reviewers then evaluated each set of variants under both standard and strict review protocols, also testing joint, recursive, and reviewer‑guided rewriting workflows.

## Results  
Evidence framing and novelty stance produce the largest positive‑negative contrasts across all conditions, whereas scope framing yields a weaker effect. The remaining dimensions have smaller or less stable impacts. This hierarchy holds true when human experts assess quality levels, but AI score movement is contingent on the reviewer’s original rating: lower scores increase, higher scores decrease, with the strongest divergence in middle ranges. More elaborate workflows (joint/recursive/reviewer‑guided) do not reliably produce larger gains; joint rewriting is heavily influenced by which rewriter was used, and reviewer guidance often adds little beyond an unguided second pass. Repeated rewriting yields diminishing returns that vary with the configuration of dimensions altered.

## Significance  
These findings identify when rhetorical presentation influences AI scientific review and underscore the need for evaluation systems robust to content‑preserving variation in scholarly writing, thereby mitigating potential reward‑hacking vulnerabilities.

## Related Concepts  
reward hacking, rhetorical sensitivity, large language model reviewers, peer review, objective assessment (OA), ICLR submissions, evidence framing, novelty stance, scope framing, hierarchical effects, diminishing returns, joint rewriting.
