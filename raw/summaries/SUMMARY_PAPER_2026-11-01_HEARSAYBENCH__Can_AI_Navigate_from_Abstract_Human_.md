---
title: HEARSAYBENCH: Can AI Navigate from Abstract Human Rights to Lived Lives?
url: http://arxiv.org/abs/2610.39062v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-28_23-49-28Z_HEARSAYBENCH_CanAINavigatefromAbstractHumanRightst.md
generated_at: 2026-11-01 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HEARSAYBENCH introduces a 400-case human-authored benchmark grounded in United Nations and human rights reports to test whether large language models can move beyond recognizing structural constraints on people's lives and actually provide actionable advice to users whose agency is limited by war, displacement, statelessness, and other systemic barriers. The study evaluates 14 proprietary and open-weight models and finds that every model infers a constrained user's situation more accurately than it advises on it, revealing a persistent gap between understanding lived hardship and generating guidance that a person can actually follow.

## Key Takeaways
- Existing AI benchmarks implicitly assume users possess the freedom to act—leaving a situation, filing a report, seeking help, or appealing a decision—yet millions of users face structural conditions such as armed conflict, statelessness, and displacement that strip away those options. HEARSAYBENCH deliberately constructs scenarios where these barriers stand between a person and the exercise of their rights, spanning over 80 regions and covering social, environmental, and personal constraints, with in-region human verification to ensure authenticity.
- Drawing on Nobel laureate Amartya Sen's Capabilities Approach, the benchmark tests whether models can distinguish what a person is formally entitled to do under human rights frameworks from what they are actually able to do given their circumstances. This distinction is critical because models increasingly shaped by normative frameworks like Constitutional AI may default to rights-based recommendations that are legally correct but practically unusable for constrained users.
- Across all 14 models tested, a consistent pattern emerges: models are better at inferring a user's constrained situation than at advising on it. While stronger models narrow this inference-to-advice gap, their recommendations remain unsafe to follow in practice. The authors frame this as a "hearsay" failure—models may understand lives shaped by constraint, but that knowledge does not translate into guidance people can act on, and these constrained users are not alignment's long tail but among those for whom good guidance matters most.

## Context
This paper addresses a growing tension in AI alignment and evaluation research: as large language models are deployed globally for personal counseling and advisory roles, the benchmarks used to assess their quality often encode assumptions about user agency that do not hold for the most vulnerable populations. By grounding its evaluation in real human rights documentation and applying Sen's Capabilities Approach, HEARSAYBENCH challenges the field to move beyond abstract normative reasoning and confront whether model outputs are genuinely actionable for people living under structural constraint.

## Implications
For AI developers and alignment researchers, HEARSAYBENCH provides a measurable diagnostic for a failure mode that existing benchmarks miss: the gap between understanding constrained lives and producing advice those lives can actually use. For practitioners deploying LLMs in counseling, humanitarian aid, or public-service contexts, the findings signal that higher model capability does not automatically yield safer or more actionable guidance for users facing war, displacement, or statelessness. The benchmark pushes the field toward systems that serve the world as it is rather than as assumed, with direct consequences for how evaluation suites, safety testing, and model fine-tuning are designed for global deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.39062v1)
