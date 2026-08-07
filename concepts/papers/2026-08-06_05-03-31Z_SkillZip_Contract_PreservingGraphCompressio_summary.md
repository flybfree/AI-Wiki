# Summary: 2026-08-06_05-03-31Z_SkillZip_Contract_PreservingGraphCompressionforSca.md
Saved: 2026-08-06 20:32
Source: 2026-08-06_05-03-31Z_SkillZip_Contract_PreservingGraphCompressionforSca.md
Model: None

---

## Summary  
The paper addresses the challenge of compressing large agent skill libraries while preserving procedural contracts and enabling scalable reuse in Large Language Model agents. SkillZip introduces a contract‑preserving compression framework that operates on section‑level execution graphs, rewriting recurring motifs into reversible ported macros without losing boundary signatures or dependencies. The system hydrates a compact context at inference time and expands macros only when necessary, allowing efficient skill library expansion. Experiments demonstrate up to 12.2‑point gains over baselines with a 3.46× compression ratio while maintaining high dependency preservation and verifier reachability.

## Key Contributions  
- [Finding 1] SkillZip achieves a 3.46× compression ratio on skill libraries ranging from 200 to 100 K skills, outperforming existing methods that compress entire packages.  
- [Finding 2] The framework preserves procedural contracts by converting recurring motifs into reversible ported macros, ensuring boundary signatures and dependency closure remain intact.  
- [Finding 3] ReZip integrates new skills and revises risky macros using execution evidence, providing a dynamic update mechanism for evolving libraries.

## Methodology  
SkillZip treats each skill as a section‑level graph with explicit contracts. The authors first identify recurring contract‑valid motifs across the library, then rewrite these motifs into portable macro definitions that are reversible at runtime. Macro expansion is deferred until the specific invocation occurs, allowing the compressed context to remain dependency‑closed and verifier reachable. ReZip builds on this by monitoring execution traces of newly added skills and applying evidence‑driven updates to any macros that might become unsafe.

## Results  
On technical and embodied agent benchmarks, SkillZip consistently outperforms the strongest baseline by up to 12.2 points. The compression ratio is 3.46×, with 99.2% of dependencies preserved and 98.7% verifier reachability maintained. Scaling analyses confirm robust retrieval across libraries of varying sizes, validating that the framework scales from small to very large skill collections.

## Significance  
By enabling compact, contract‑preserving skill representations, SkillZip reduces inference latency and memory usage for LLMs that rely on procedural knowledge. Its ability to safely update skill libraries without re‑compressing the entire set is crucial for long‑lived agent systems where skills evolve over time.

## Related Concepts  
- Graph compression  
- Procedural abstraction  
- Contract preservation  
- Macro expansion at runtime  
- Dependency closure  
- Verifier reachability
