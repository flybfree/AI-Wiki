---
title: "You" Is Not Toxic: How LLM Labelers Rewrite the Web's Conversation Laws
url: http://arxiv.org/abs/2610.23446v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_13-29-30Z_You_IsNotToxic_HowLLMLabelersRewritetheWeb_sConver.md
generated_at: 2026-10-18 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that large language model labelers systematically conflate second-person address ("you") with toxicity, producing spurious statistical laws about online conversation that human crowd labels do not support. The authors show that on 1.25 million news comments, Claude Haiku flags 51% of non-toxic comments containing four or more instances of "you" versus 10% flagged by a single human rater, and that this single bias manufactures a false rising-toxicity-with-thread-depth law. They propose Threadsafe, a method that certifies the statistical law rather than the labeler, achieving unbiased linear-law estimation regardless of the labeler's systematic errors.

## Key Takeaways
- LLM labelers across all seven models tested systematically over-flag comments containing second-person pronouns as toxic. Claude Haiku flags 12% of non-toxic comments with no "you" but 51% of those with four or more, compared to 6% and 10% for a single crowd rater. This is not a calibration issue solvable by threshold tuning: flagging only as many comments as the crowd does not remove the bias, and showing the parent comment to the model actually enlarges it.
- The "you" bias manufactures a false law that toxicity rises with reply depth (+0.93 percentage points per level under Haiku) while human crowd labels show a slight decline (-0.12). Rewriting "you" in third person removes two-thirds of the false rise, and at the crowd's flag rate without parent context, any false rise vanishes at a fixed number of second-person words. The bias also replicates on Reddit, Gab, and Wikipedia talk pages.
- Agreement metrics like Cohen's kappa do not reveal this bias because a fixed kappa leaves the derived law nearly unconstrained. Threadsafe instead certifies the law directly: it uses the labeler's scores to select which comments human raters label and to predict the rest, then corrects predictions with human labels. In simulated audits, Threadsafe achieves nominal coverage from 250 labels onward where uniform-sample methods like PPI++ fall short, and at 1,000 to 8,000 labels produces intervals 0.75 times as wide as design-based supervised learning. A thousand human labels suffice to rule out Haiku's rising law.

## Context
As Google's Perspective API shuts down, the web research community faces a transition to LLM-based toxicity measurement for studying conversation dynamics across news sites, social platforms, and collaborative encyclopedias. Prior findings about toxicity increasing in longer threads were largely established through Perspective API measurements, and the field now needs to determine whether those conclusions survive the switch to LLM labelers. This paper sits at the intersection of measurement validity, algorithmic fairness, and causal inference in computational social science, addressing a critical methodological gap before the field's foundational assumptions are silently corrupted by a new tool.

## Implications
For researchers studying online discourse, this work warns that adopting LLM labelers without auditing for second-person bias will silently reproduce and amplify false conclusions about how toxicity propagates through threaded conversations, potentially reshaping platform moderation policies and public understanding of online hostility. For practitioners deploying LLMs as annotation tools at scale, the paper provides a concrete corrective protocol—Threadsafe—that requires only a modest number of human labels (as few as 1,000) to validate or refute any derived statistical law, offering a practical path to trustworthy measurement without abandoning LLM efficiency. The finding that agreement metrics fail to detect the bias also challenges standard quality-assurance practices in AI-assisted annotation pipelines across all domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23446v1)
