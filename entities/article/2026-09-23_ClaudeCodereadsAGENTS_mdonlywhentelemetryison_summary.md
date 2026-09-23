# Summary: 2026-09-23_ClaudeCodereadsAGENTS_mdonlywhentelemetryison.md
Saved: 2026-09-23 08:17
Source: 2026-09-23_ClaudeCodereadsAGENTS_mdonlywhentelemetryison.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Claude Code 2.1.277 introduced support for AGENTS.md, a file intended to provide project-specific instructions when no CLAUDE.md exists. However, this feature only activates when telemetry is enabled and relies on a remote server-side flag (tengu_agents_md_mod), which remains false by default. When telemetry is disabled or the environment variables DISABLE_TELEMETRY and CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC are set, AGENTS.md is never read, despite being present locally. The article demonstrates that this design forces users to maintain a CLAUDE.md file with an @path import workaround to bypass the gate.

## Key Takeaways  
- [Critical point 1] AGENTS.md is only loaded when telemetry is active and the remote feature flag is true, making it inaccessible in privacy-focused or offline environments.  
- [Critical point 2] The system cannot be enabled locally without telemetry, even if users set environment variables to zero, due to a hardcoded false fallback.  
- [Critical point 3] Third-party AI platforms like Bedrock and Vertex share the same issue because they depend on unresolved remote flags.

## Context  
This situation reflects broader trends in AI tooling where features are gated behind telemetry or server-side configurations, prioritizing data collection over user autonomy. The reliance on cloud-based feature flags undermines local control and raises concerns about transparency and privacy in AI workflows. It also highlights a design flaw: the only input needed for AGENTS.md is already available locally, making remote dependency unnecessary.

## Implications  
For developers and users, this means that even basic project instructions can be silently ignored due to technical constraints rather than user choice. The workaround introduces an extra file per repository, negating the original goal of reducing overhead. In an industry where trust in AI systems is paramount, such gatekeeping mechanisms risk eroding confidence if not clearly communicated. This issue underscores a need for more transparent, user-centric design in AI tooling—where local files should be accessible without requiring telemetry or cloud coordination.
