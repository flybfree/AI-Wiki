---
title: ToolRosetta: Surface-Form Invariance of Tool-Call Guards
url: http://arxiv.org/abs/2610.24055v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_17-14-13Z_ToolRosetta_Surface_FormInvarianceofTool_CallGuard.md
generated_at: 2026-10-19 20:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ToolRosetta is a benchmarking methodology that re-renders tool-call actions from TS-Bench's AgentDojo and AgentHarm splits into alternative surface forms—Python function calls, shell commands, and rationale-free variants—while keeping the underlying request, history, label, and action effect fixed. The study evaluates eleven step-level guards across these renderings and finds that frontier and strong open-weight guards remain stable (error shifts under 3.4 points), but four of five specialized agent guards degrade severely under shell-form rendering, with false-positive rates rising 21 to 47 points and blocking between one-third and nine-tenths of benign actions.

## Key Takeaways
- Specialized agent guards such as TS-Guard and others suffer dramatic false-positive spikes (21–47 points on AgentDojo, 38 points on TS-Guard's own benchmark) when tool calls are presented as shell commands rather than tidy JSON, meaning they block a third to nine-tenths of benign actions in realistic code-acting agent deployments.
- Frontier and strong open-weight guards show robustness to surface-form changes, with no error-rate shift exceeding 3.4 points, suggesting that general-purpose safety training transfers across rendering formats while narrow, task-specific guard training does not.
- Removing the agent's rationale from the guard input shifts most guards in guard-specific directions, and a request-blind control demonstrates that the rationale field is where intent is actually parsed; a parser that restores the canonical JSON call before the guard eliminates the effect by construction, confirming the vulnerability is purely a surface-form artifact.
- Benchmark accuracy measured on JSON-formatted tool calls does not predict a guard's operating point when deployed behind a code-acting agent that uses execute_bash or execute_code tools, exposing a critical evaluation gap.

## Context
This work sits at the intersection of AI agent safety evaluation and the practical reality that deployed coding agents operate through string-payload tools like execute_bash and execute_code rather than structured JSON tool calls. As agentic coding assistants become ubiquitous in software engineering workflows, the guards that gate their actions are increasingly deployed in production, yet the safety literature has predominantly benchmarked these guards on clean, structured inputs. ToolRosetta bridges this gap by systematically perturbing only the surface form while holding semantics constant, revealing that the safety community's evaluation protocols may be measuring a regime that does not match deployment conditions.

## Implications
For practitioners deploying tool-using agents, this finding means that a guard validated on JSON benchmarks may silently over-block benign actions in production when the agent acts through shell or code execution, creating both safety regressions and usability failures. For the research community, it signals that guard evaluation must incorporate surface-form invariance testing and that training guards on narrow, format-specific data risks brittle deployment behavior. Industry teams building agent platforms should treat the rendering format as a first-class safety variable and consider parser-normalization layers as a mitigation, while benchmark designers should adopt multi-form evaluation suites like ToolRosetta to avoid overestimating guard robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24055v1)
