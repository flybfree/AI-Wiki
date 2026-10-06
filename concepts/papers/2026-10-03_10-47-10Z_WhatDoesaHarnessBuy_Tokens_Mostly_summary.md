# Summary: 2026-10-03_10-47-10Z_WhatDoesaHarnessBuy_Tokens_Mostly.md
Saved: 2026-10-05 22:15
Source: 2026-10-03_10-47-10Z_WhatDoesaHarnessBuy_Tokens_Mostly.md
Model: None

---

## Summary
This paper investigates the actual impact of coding agent harnesses—defined as the system prompts, tool sets, and context management wrapping a language model—on performance metrics like SWE-bench Verified scores. The authors challenge the industry assumption that harness changes significantly improve model performance by conducting rigorous experiments holding the underlying model fixed while swapping harnesses. They find that for most models and tasks, different production harnesses yield statistically equivalent performance, with the primary measurable effect being a significant increase in computational cost rather than accuracy gains. The study provides critical calibration data on the statistical noise inherent in agent evaluations, offering a framework for determining the sample size required to detect genuine harness improvements.

## Key Contributions
- **Performance Equivalence:** The study demonstrates that heavy and light harnesses (e.g., Claude Code vs. mini-SWE-agent) are statistically equivalent within a five-point margin on large benchmarks, suggesting that harness architecture does not inherently boost pass rates for fixed models.
- **Cost Disparity:** The primary differentiator between harnesses is economic; cost per task can vary by up to 3x due to differences in system prompt preambles, tool schema overhead, and step counts, rather than algorithmic efficiency.
- **Statistical Calibration:** The authors quantify the "noise floor" of agent evaluations, showing that standard benchmark sizes (like 45 tasks) lack the statistical power to reliably detect small performance gains, thereby exposing potential overstatement in vendor-reported improvements.

## Methodology
The researchers conducted a controlled experiment using five distinct language models across three production-grade coding agent harnesses: Claude Code, mini-SWE-agent, and OpenCode. They evaluated these configurations on the SWE-bench Verified dataset, comprising 447 tasks, and a harder subset of 45 tasks. To distinguish genuine harness effects from stochastic variance, the authors performed repeated runs of identical configurations to calibrate the baseline noise level. This approach allowed them to isolate the specific contribution of the harness wrapper from the inherent variability of the language model's output.

## Results
The experiments revealed that swapping harnesses produced task flips at a rate of 13%, which was identical to the variance observed when simply rerunning the same harness, indicating no systematic performance gain from harness selection. While OpenCode showed a performance deficit of up to 9 points, this was largely attributed to output caps truncating runs rather than superior logic in other harnesses. In terms of cost, the analysis showed that the initial system prompt and tool schemas sent at the first call were the dominant factors driving cost differences, with per-step growth and tool output volume playing minor roles. Statistically, the data indicated that 45-task benchmarks have insufficient power to detect 13-point gaps, while 447-task benchmarks can only resolve differences as small as 5 points.

## Significance
This research is significant for the AI development community as it debunks the marketing narrative that sophisticated harness engineering directly translates to higher accuracy. It highlights that "harness engineering" is primarily an optimization of cost and token usage rather than a method for improving problem-solving capability. By providing empirical data on the statistical noise of agent benchmarks, the paper urges the community to adopt more rigorous evaluation standards and larger sample sizes before claiming performance improvements from harness updates. It shifts the focus from chasing marginal accuracy gains to understanding the economic and operational trade-offs of different agent architectures.

## Related Concepts
- Coding Agent Harnesses
- SWE-bench Verified
- Statistical Power and Noise Calibration
- Token Cost Optimization
- System Prompt Overhead
- Benchmark Variance
