---
title: When Charts Deceive Web Agents: A Paired Benchmark for Misleading Visualization-Grounded Tasks
url: http://arxiv.org/abs/2610.12823v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_00-03-13Z_WhenChartsDeceiveWebAgents_APairedBenchmarkforMisl.md
generated_at: 2026-10-11 22:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MisVisAgentBench, the first paired executable benchmark designed to evaluate how misleading visualizations (charts and dashboards) affect Web Agent task execution. The authors construct 280 task instances in matched clean-versus-misleading pairs that differ only in the chart evidence presented, and they test thirteen vision-language Web Agents across these tasks. The central finding is that replacing clean charts with misleading counterparts reduces average task success rates by more than 34 percentage points, and these failures follow targeted misleading action branches rather than occurring randomly, indicating that deceptive charts systematically redirect agent decision-making.

## Key Takeaways
- MisVisAgentBench is the first benchmark specifically designed to isolate the effect of misleading visual evidence on Web Agent execution, using 280 matched task pairs where the only variable is whether the chart is clean or misleading. This paired design allows researchers to attribute failures directly to visual deception rather than to inherent task difficulty, addressing a gap left by prior chart question-answering benchmarks.
- Across thirteen vision-language Web Agents, misleading charts cause a greater than 34-percentage-point drop in task success rates. Critically, the diagnostic framework separates misleading-induced failures from baseline difficulty and captures execution-level effects such as extra browsing steps and decision hesitation, revealing that misleading evidence does not merely confuse agents but actively redirects their downstream actions along the targeted misleading branch.
- The failures are systematic rather than random: agents consistently follow the misleading action branch suggested by the deceptive chart, meaning that visualization robustness is not a peripheral concern but a core reliability risk for Web Agents that treat charts as intermediate evidence feeding into concrete downstream actions.

## Context
Web Agents are increasingly deployed in realistic workflows where they browse, interpret, and act on web content autonomously, including dashboards, financial charts, and data visualizations. Prior research on chart understanding has focused on static question-answering tasks, but Web Agents consume charts as intermediate evidence whose misinterpretation propagates into concrete actions such as navigation decisions, form submissions, or data extraction. This paper addresses a critical gap in the AI safety and reliability literature by formalizing how visual deception in web content can silently corrupt agent behavior without any explicit malicious instruction, a risk that existing benchmarks and evaluation frameworks have largely overlooked.

## Implications
For practitioners deploying Web Agents in production environments—such as automated data analysis, financial decision support, or web-based research assistants—these findings signal that visualization robustness must be treated as a first-class safety requirement alongside prompt injection and hallucination defenses. Industry teams building agentic systems should incorporate misleading-visualization stress tests into their evaluation pipelines, and benchmark designers should adopt paired clean-misleading task structures to accurately measure agent resilience. The systematic nature of the failures also suggests that targeted counter-deception training or chart-verification modules could meaningfully improve agent reliability in real-world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.12823v1)
