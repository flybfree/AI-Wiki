# Summary: 2026-11-02_16-53-29Z_OptimizetheHarness_NottheModel_FittingaMinimalAgen.md
Saved: 2026-11-05 21:47
Source: 2026-11-02_16-53-29Z_OptimizetheHarness_NottheModel_FittingaMinimalAgen.md
Model: None

---

## Summary
This paper introduces CLEO (Constrained Loop for Environment Optimization), a novel methodology designed to optimize the agent harness rather than the underlying Large Language Model (LLM) itself. The primary goal is to enable government intelligence teams to perform investigative analysis on large, messy evidence collections using self-hostable LLMs, thereby adhering to strict security and cost constraints that preclude the use of hosted frontier models. By systematically fitting a minimal agent harness—comprising only necessary tools, guardrails, memory policies, and loop components—to a fixed model, CLEO achieves high accuracy while maintaining auditability. The method demonstrates that significant performance gains can be derived from harness optimization rather than model scaling or proprietary API access.

## Key Contributions
- **Development of the CLEO Framework:** The authors propose a structured approach for "fitting" an agent to a fixed, self-hostable LLM by iteratively adding only those components (tools, guardrails, memory policies) that demonstrably improve accuracy on expert-validated datasets while remaining generalizable and auditable.
- **Performance Parity with Minimal Footprint:** The CLEO harness achieves an 83.8% pass rate on a held-out dataset, which is within 1.2 percentage points of the strongest out-of-the-box baseline using the Claude Code SDK. Crucially, this performance is achieved with a harness that is two orders of magnitude smaller than standard complex agent architectures.
- **Emphasis on Auditability and Security:** The paper highlights the critical importance of auditability in government intelligence contexts. By restricting the tool surface to only what is necessary and auditable, CLEO addresses security concerns associated with broad, opaque tool surfaces often found in commercial agent frameworks.

## Methodology
The authors approach the problem by treating the LLM as a fixed component and focusing optimization efforts on the surrounding "harness." The methodology involves starting with a minimal baseline agent and iteratively evaluating potential additions—such as specific tools for data retrieval, guardrails for safety compliance, memory policies for context management, and loop components for reasoning steps. Each addition is tested against an expert-validated dataset to determine if it improves accuracy without introducing unnecessary complexity or reducing auditability. The process ensures that only components that contribute positively to performance while maintaining generalizability are admitted into the final harness configuration. This contrasts with traditional approaches that might rely on larger models or more complex, less transparent toolchains.

## Results
The primary experimental result demonstrates that the CLEO-optimized harness achieves an 83.8% pass rate on a held-out investigative analysis dataset. This performance is statistically comparable to the strongest out-of-the-box baseline provided by the Claude Code SDK, falling short by only 1.2 percentage points. Despite this high level of accuracy, the CLEO harness is significantly more compact, being two orders of magnitude smaller than the baseline or typical complex agent setups. This result validates the hypothesis that optimizing the environment and interaction loop can yield near-frontier performance using self-hostable models, without the overhead associated with larger, more complex systems.

## Significance
This research is significant for organizations operating under strict security, privacy, and cost constraints, such as government intelligence agencies. It provides a viable pathway to leverage advanced LLM capabilities for sensitive investigative tasks without relying on hosted frontier models that may pose data sovereignty or security risks. By demonstrating that harness optimization can rival the performance of top-tier commercial baselines, the paper shifts the focus from model scale to system design efficiency. This approach enhances auditability and transparency, which are critical for high-stakes decision-making in public sector applications.

## Related Concepts
- Agent Harness Optimization
- Self-Hostable LLMs
- Investigative Analysis
- Auditability in AI Systems
- Constrained Loop for Environment Optimization (CLEO)
- Minimal Agent Architectures
- Government Intelligence Workflows
