# Summary: 2026-07-31_16-46-19Z_ExposedbyDesign_ADynamicSecurityAssessmentofIntern.md
Saved: 2026-08-03 20:15
Source: 2026-07-31_16-46-19Z_ExposedbyDesign_ADynamicSecurityAssessmentofIntern.md
Model: None

---

## Summary  
The paper presents the first systematic, dynamic security assessment of Model Context Protocol (MCP) servers that are publicly reachable on the internet. By combining passive discovery across eleven data sources with active testing using a purpose‑built framework, it uncovers 68 reportable vulnerabilities and reveals rapid deployment cycles among MCP services. The study demonstrates that many of these servers lack essential security controls such as OAuth authentication and fail to persist beyond three days between measurement runs. This work contributes both a vulnerability taxonomy for MCP and an open‑source testing tool (Corvus) to help the community evaluate and harden internet‑facing MCP deployments.

## Key Contributions  
- 640 production MCP servers were identified, of which 414 were dynamically audited and yielded 68 reportable vulnerabilities.  
- 91.8 % of the audited servers lack OAuth authentication, exposing them to unauthenticated attacks.  
- Approximately 41.6 % of confirmed servers disappear within three days between consecutive measurement runs, indicating a fast deployment cycle without security review.

## Methodology  
The authors employed a two‑phase approach: first, they gathered passive data from eleven sources (crt.sh, HuggingFace, GitHub, npm, Smithery, PyPI, Censys, FOFA, Shodan, glama.ai, pulsemcp.com) to locate all internet‑facing MCP instances; second, they ran four measurement cycles using the Corvus framework, which implements 34 test modules that target ten distinct MCP vulnerability classes. This combination allowed both discovery and active probing at scale.

## Results  
The audit uncovered several critical flaws: SQL injection in input handling, SSRF attacks targeting cloud metadata services, prompt template injection that manipulates model instructions, and path traversal via cursor manipulation. Additionally, 687 tool instances exposed shell execution capabilities without any access controls. The rapid disappearance of servers between runs highlighted the absence of a formal security review process.

## Significance  
These findings expose a systemic weakness in the rapidly expanding MCP ecosystem: services are deployed quickly but rarely subjected to automated or manual security testing, leading to widespread exposure to known attack vectors. By providing an open‑source framework and clear vulnerability taxonomy, the paper offers a concrete path for organizations to evaluate their MCP deployments proactively.

## Related Concepts  
- Model Context Protocol (MCP) – a real‑time data exchange protocol for AI models.  
- Dynamic security testing – continuous assessment of services as they evolve.  
- Vulnerability classification – grouping attacks into ten MCP‑specific classes.  
- Rapid deployment cycles – short lifespans between measurement runs.  
- OAuth authentication – standard access control mechanism.  
- SSRF (Server‑Side Request Forgery) – technique for reaching internal services via external requests.  
- Prompt template injection – manipulation of model prompts to alter behavior.
