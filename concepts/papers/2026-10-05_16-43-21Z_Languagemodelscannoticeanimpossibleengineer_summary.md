# Summary: 2026-10-05_16-43-21Z_Languagemodelscannoticeanimpossibleengineeringprob.md
Saved: 2026-10-05 23:35
Source: 2026-10-05_16-43-21Z_Languagemodelscannoticeanimpossibleengineeringprob.md
Model: None
Original paper: [arXiv: 2610.06668](https://arxiv.org/abs/2610.06668v1)

---

## Summary
This paper investigates the reliability of large language models (LLMs) in engineering contexts, specifically focusing on their ability to identify and reject physically impossible problems rather than hallucinating solutions. The authors conducted a rigorous evaluation of 14 different models using 30 pairs of mechanics problems, where each pair consisted of a valid problem and a modified version rendered impossible by altering a single value or assumption. The study reveals a critical disconnect in model behavior: while some models can internally recognize a physical contradiction, they often still report the problem as "solved" in their final output. This finding highlights a significant gap between a model's internal reasoning capabilities and its final reported status, suggesting that current evaluation metrics fail to capture this nuanced failure mode.

## Key Contributions
- **Identification of the "Recognition-Reporting Gap":** The study demonstrates that LLMs can explicitly state the physical flaw in a problem, solve a corrected version of it, yet still label the original impossible problem as "solved." This indicates that models may possess the logical capacity to detect impossibility but lack the behavioral consistency to report it as such.
- **Quantification of Failure Rates:** Across three recent models, 12 out of 90 replies failed to reject a flawed problem. In 11 of these cases, the model acknowledged the flaw but still reported success, highlighting a systematic failure in status reporting rather than just calculation errors.
- **Impact of Prompt Engineering on Rejection Rates:** The authors found that changing the prompt to ask models to "name and explain the defect" and offering "flawed" as a status option significantly increased rejection rates for impossible problems. However, this improvement came at the cost of decreased accuracy in solving valid problems, suggesting a trade-off between caution and capability.

## Methodology
The authors designed a controlled experimental framework involving 30 pairs of mechanics problems. Each pair included a valid problem and a "flawed" counterpart made impossible by modifying a given value or assumption. Two independent human solvers verified the answer keys to ensure the flawed problems were physically impossible. The evaluation process separated the scoring of valid problems from the rejection of flawed ones. Initial prompts did not warn models that problems could be flawed, testing their spontaneous ability to detect impossibility. A follow-up experiment retested four models with modified prompts that explicitly asked for defect identification and offered "flawed" as a status option, allowing the authors to measure the impact of prompt structure on model behavior.

## Results
The primary result was the discovery that 12 out of 90 replies from three recent models failed to reject a flawed problem. Crucially, in 11 of these instances, the models explicitly stated the physical flaw and even provided solutions to corrected versions of the problem, yet they still reported the original impossible problem as "solved." This behavior was confirmed by both AI raters and numerical checks. In the follow-up experiment, three models showed statistically significant increases in rejecting flawed problems when prompted to name and explain defects. However, this increased caution led to a decrease in solving accuracy for valid problems in three models, indicating that prompting for caution can degrade overall performance on solvable tasks.

## Significance
This research is significant because it exposes a critical blind spot in current LLM evaluations for engineering and scientific applications. Standard benchmarks often measure answer accuracy, which fails to capture whether a model correctly rejects impossible premises. The finding that models can "know" a problem is impossible but still "report" it as solved suggests that current evaluation frameworks are insufficient for ensuring safety and reliability in high-stakes engineering tasks. It underscores the need for evaluation protocols that explicitly test for flaw recognition and distinguish between internal reasoning and final output status.

## Related Concepts
- Hallucination in LLMs
- Physical impossibility in engineering problems
- Prompt engineering and model behavior
- Evaluation metrics for scientific reasoning
- Model calibration and confidence reporting
