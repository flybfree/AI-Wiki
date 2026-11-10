---
title: Safer for Whom? A Systematic Exploration of AI Safety in Eating Disorder Interactions
url: http://arxiv.org/abs/2611.10488v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-07_05-30-37Z_SaferforWhom_ASystematicExplorationofAISafetyinEat.md
generated_at: 2026-11-09 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper systematically evaluates how three open-weight large language models respond to questions drawn from a real online pro-anorexia community, assessing whether AI assistants recognize implicit vulnerability in natural language interactions and provide safe guidance related to diet, exercise, and weight. The authors construct a clinically informed grading framework extending a seven-dimensional taxonomy of eating disorder harms and test matched conditions varying user demographics and explicit vulnerability signals. They find that safety varies substantially across models, that high-risk responses are roughly twice as frequent when demographic context is absent, and that explicit signals of ED vulnerability improve safety by 10–14 points, while responses differ significantly by race, gender, and BMI.

## Key Takeaways
- High-risk AI responses are approximately twice as frequent when questions lack accompanying demographic bios, indicating that current models do not consistently infer vulnerability from language cues alone and rely heavily on explicit signals to trigger protective behavior.
- Explicit signals of eating disorder vulnerability improve safety scores by 10–14 points across all three evaluated models, suggesting that user self-disclosure functions as a critical safety mechanism but also places the burden of protection on the user rather than the system.
- Responses differ significantly by race, gender, and body mass index, with body size producing the largest disparities in safety outcomes. These patterns align with a stereotypical assumption that eating disorders primarily affect thin, White women, potentially leaving users outside that profile—such as individuals with higher BMI or non-White users—receiving less protective and potentially harmful guidance.

## Context
Most existing AI safety evaluations in health-related domains focus on diagnostic accuracy, overtly harmful prompts, or synthetic test scenarios, which fail to capture how models behave in the ambiguous, emotionally nuanced interactions typical of real users seeking diet or exercise advice. This paper fills that gap by grounding its evaluation in authentic community-sourced questions and a clinically informed harm taxonomy, shifting the assessment from whether models can detect obvious harm to whether they can recognize implicit vulnerability in natural conversational contexts. This approach matters because eating disorder harms—such as worsening dietary restriction, compulsive exercise, and body dissatisfaction—are often subtle and cumulative rather than acute, making them poorly captured by conventional safety benchmarks.

## Implications
For AI developers and safety practitioners, these findings underscore that demographic-blind safety testing can mask significant disparities in model behavior, and that deploying AI health assistants without explicit vulnerability detection mechanisms may systematically disadvantage users who do not fit the stereotypical eating disorder profile. Industry teams building conversational health tools should consider incorporating implicit vulnerability detection, demographic-aware safety guardrails, and community-sourced evaluation datasets rather than relying solely on synthetic prompts. For clinicians and public health advocates, the results highlight a growing risk that AI-mediated dietary and exercise guidance could inadvertently reinforce harmful body-size stereotypes and widen health disparities for populations already underserved in eating disorder research and treatment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10488v1)
