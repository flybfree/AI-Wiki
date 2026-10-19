---
title: HardEval: An Execution-Verified Benchmark for AI-Driven Security Hardening and Compliance Remediation
url: http://arxiv.org/abs/2610.23685v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_16-14-58Z_HardEval_AnExecution_VerifiedBenchmarkforAI_Driven.md
generated_at: 2026-10-18 22:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HardEval introduces an execution-verified benchmark designed to evaluate whether large language models can correctly implement Security Technical Implementation Guide (STIG) controls on live operating systems. The benchmark tasks models with producing Bash scripts that remediate failing security configurations on Red Hat Enterprise Linux 8, grading outputs against hidden OpenSCAP/OVAL compliance checks rather than superficial code review. Evaluation across fourteen frontier and open-weight model configurations reveals substantial and uneven capability gaps across security domains, with a dominant failure mode being plausible-looking security code that fails to satisfy the precise compliance condition required.

## Key Takeaways
- HardEval addresses a critical gap in existing evaluation infrastructure: code benchmarks test isolated programs without persistent system state, and agent benchmarks focus on application-level tasks rather than operating-system configuration. HardEval instead requires models to produce executable Bash scripts that modify live system state across SSH configuration, authentication policy, audit rules, and kernel parameters, with grading performed by running the corresponding OpenSCAP/OVAL compliance check on a live virtual machine.
- The benchmark uses a hidden ground-truth design where expert-written reference remediations and OVAL checks are never shown to the model. Each task states only the required security outcome while withholding the implementation details, forcing models to independently reason about how to achieve compliance rather than pattern-matching against known solutions.
- Testing fourteen frontier and open-weight model configurations exposed large and uneven capability differences across security domains. A recurring failure mode is the generation of plausible security code that appears correct but does not satisfy the exact compliance condition enforced by the OVAL check. For four open-weight configurations, multi-run Wilson confidence intervals were used to confirm that the observed performance ordering is statistically robust rather than a single-run artifact.

## Context
This paper sits at the intersection of AI safety evaluation, operating-system security administration, and compliance automation. As organizations increasingly rely on language models to automate infrastructure tasks, the ability to correctly configure security controls on production systems becomes a high-stakes capability. Existing benchmarks such as SWE-bench or agent evaluation suites measure code generation or application-level reasoning but do not test whether a model can produce persistent, system-level configuration changes that pass formal compliance audits. HardEval fills this gap by grounding evaluation in the actual compliance-checking infrastructure used by government and enterprise security programs, making it directly relevant to the growing field of AI-assisted DevSecOps and automated compliance remediation.

## Implications
For practitioners in government and regulated industries who depend on STIG compliance, HardEval provides a concrete, reproducible way to assess whether AI-assisted security hardening tools can be trusted to produce correct remediations without human review. The finding that models frequently generate plausible but non-compliant code underscores the need for execution-verified evaluation pipelines rather than relying on model self-assessment or superficial code inspection. For the broader AI research community, the benchmark demonstrates that domain-specific, stateful evaluation is necessary to expose capability gaps that static code benchmarks miss, and its public availability enables reproducible comparison across future model releases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23685v1)
