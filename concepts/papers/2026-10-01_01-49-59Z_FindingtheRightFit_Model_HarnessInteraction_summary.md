# Summary: 2026-10-01_01-49-59Z_FindingtheRightFit_Model_HarnessInteractionsacross.md
Saved: 2026-10-01 21:46
Source: 2026-10-01_01-49-59Z_FindingtheRightFit_Model_HarnessInteractionsacross.md
Model: None

---

## Summary
This research paper investigates the critical yet often overlooked interaction between large language models (LLMs) and agent harnesses, challenging the assumption that stronger models inherently yield better performance regardless of the execution environment. The authors systematically evaluate 66 distinct configurations by pairing five different LLMs with four configurable open-source harnesses alongside native vendor pairings across three rigorous benchmark suites: TUA-Bench, ALE-CLI, and Terminal-Bench 4. Their primary goal is to determine whether model rankings remain stable when the underlying harness changes or if specific model-harness "fits" dictate success more than raw model capability. The study concludes that evaluating models in isolation is insufficient, as the choice of harness can dramatically reverse performance hierarchies and significantly impact cost-efficiency.

## Key Contributions
- **Performance Reversals Across Harnesses**: The study reveals that model rankings are not static; for instance, on Terminal-Bench 4, Claude leads GPT by nearly 8 points in OpenHands but trails it by over 30 points when paired with the PI harness, demonstrating that harness choice can completely invert perceived model superiority.
- **Vendor Harnesses Are Not Optimal**: Contrary to common industry practices, a model’s native vendor harness is not reliably its best performing option. The research shows that third-party or alternative harnesses often outperform official implementations, suggesting that users should not default to proprietary pairings without empirical validation.
- **Cost-Performance Decoupling**: Higher costs do not guarantee higher scores. The authors demonstrate instances where cheaper configurations outperform expensive ones; specifically, GPT achieved higher scores under the PI harness than under DeepSeek Harness (DSH) at less than a quarter of the cost per task, highlighting significant opportunities for optimization.

## Methodology
The authors adopted a comprehensive empirical approach by constructing 66 unique experimental configurations. They selected five distinct LLMs and paired them with four configurable open-source harnesses: OpenHands, DeepSeek Harness (DSH), PI, and openJiuwen. Additionally, they included native vendor pairings such as Codex-GPT and Claude Code-Claude for baseline comparison. These configurations were tested across three standardized agent benchmarks designed to evaluate terminal and tool-use capabilities: TUA-Bench, ALE-CLI, and Terminal-Bench 4. To understand the underlying reasons for performance variations, the researchers conducted a qualitative analysis of matched trajectories, examining how failures were handled and whether harnesses provided feedback in formats that models could effectively utilize for self-repair.

## Results
The experimental results indicate that while some pairings remain robust across tasks (such as openJiuwen consistently boosting Kimi’s performance), most model-harness interactions are task-specific. For four of the five models evaluated, the optimal harness changed depending on which benchmark was used. The analysis of trajectories showed that since models initiate almost all repair attempts themselves, the critical factor is whether the harness returns failure information in a usable format. GPT performed best with PI’s lean scaffold, whereas Kimi, prone to malformed tool calls, benefited most from openJiuwen’s handling mechanisms.

## Significance
This work is significant because it shifts the paradigm of agent evaluation from model-centric to system-centric. It provides actionable insights for practitioners who need to optimize both performance and cost in real-world deployments. By releasing 6,204 scored trajectories and evaluation code, the authors enable further research into harness design and model adaptation, fostering a more nuanced understanding of AI agent ecosystems.

## Related Concepts
- Large Language Model (LLM) Agents
- Agent Harnesses and Frameworks
- Benchmark Evaluation (TUA-Bench, ALE-CLI, Terminal-Bench 4)
- Model-Harness Interactions
- Cost-Efficiency in AI Deployment
- Trajectory Analysis
