# Summary: 2026-08-21_13-47-51Z_ClawSentry_AProgressiveMulti_TierSecurityMonitorfo.md
Saved: 2026-08-23 21:40
Source: 2026-08-21_13-47-51Z_ClawSentry_AProgressiveMulti_TierSecurityMonitorfo.md
Model: None

---

## Summary  
The paper introduces ClawSentry, a framework‑agnostic security supervision gateway designed to protect autonomous LLM agents from the progressive risk of malicious skill injection across four distinct control loops: skill admission, invocation‑time intent, execution‑time effect, and post‑action consequence. By moving beyond single‑boundary defenses, ClawSentry employs a multi‑tier decision engine that audits skill packages before use, reviews ambiguous runtime actions, and captures high‑severity evidence after actions without retroactively altering prior decisions. The system also includes an anti‑bypass mechanism that detects tool‑switching or rephrased retries to close evasion paths. An abstracted Agent Harness Protocol (AHP) lets the same policy be applied uniformly across multiple agent runtimes such as Codex, Claude Code, Kimi CLI, and Gemini CLI without modifying their internals.

## Key Contributions  
- [Finding 1] The threat model is progressive: malicious intent can appear at any of four loci in the agent control loop, necessitating a security monitor that spans the entire lifecycle rather than being confined to one call.  
- [Finding 2] ClawSentry implements a three‑tier decision engine (deterministic L1, rule‑anchored semantic reviewer L2, read‑only evidence‑seeking agent L3) and an anti‑bypass system that catches tool‑switching or rephrased retries, while also performing First‑use Skill Package Review (FSPR).  
- [Finding 3] The Agent Harness Protocol abstracts policy across multiple agents, achieving a contextual ASR reduction from 39.55 % to 2.61 % and lowering overall ASR on the SkillsSafety benchmark from 33.5–49.7 % to 9.09–15.03 %, while keeping clean‑skill TSR at 98.7 %.

## Methodology  
ClawSentry is built as a framework‑agnostic security supervision gateway that sits between the LLM agent and its external skill ecosystem. The authors designed a progressive decision engine: the first tier (L1) performs deterministic checks on skill packages, the second tier (L2) applies rule‑anchored semantic review to resolve remaining ambiguities, and the third tier (L3) conducts read‑only evidence gathering after actions without altering prior decisions. An anti‑bypass mechanism monitors for tool switching or rephrased retries at runtime. Skill packages undergo First‑use Skill Package Review (FSPR), which audits them under a deterministic evidence floor before execution. The Agent Harness Protocol abstracts these policies so they can be applied uniformly across different agent runtimes without code changes.

## Results  
Experimental evaluation on the SkillsSafety benchmark with five Work Agents shows that ClawSentry reduces contextual ASR from 39.55 % to 2.61 % and lowers overall ASR on the test set from 33.5–49.7 % to 9.09–15.03 %. The aggregate true‑skill rate (TSR) for clean skills remains high at 98.7 %, indicating that legitimate skill usage is unaffected while malicious attempts are effectively suppressed.

## Significance  
By addressing the progressive nature of agentic risk across multiple lifecycle boundaries, ClawSentry offers a robust defense against data exfiltration, privilege escalation, and cascading compromise that could arise from compromised skills. Its framework‑agnostic design enables rapid deployment across diverse LLM agents, reducing reliance on per‑agent customizations and accelerating security integration.

## Related Concepts  
skill admission, invocation‑time intent, execution‑time effect, post‑action consequence, tool‑switching, rephrased retries, evidence floor, read‑only review, progressive decision engine, First‑use Skill Package Review (FSPR), Agent Harness Protocol (AHP).

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21101v1)
