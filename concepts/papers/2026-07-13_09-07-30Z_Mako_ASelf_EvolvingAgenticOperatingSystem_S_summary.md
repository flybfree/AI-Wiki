# Summary: 2026-07-13_09-07-30Z_Mako_ASelf_EvolvingAgenticOperatingSystem_SE_AOS_f.md
Saved: 2026-07-23 23:41
Source: 2026-07-13_09-07-30Z_Mako_ASelf_EvolvingAgenticOperatingSystem_SE_AOS_f.md
Model: None

---

## Summary  
This paper introduces Mako, a self-evolving agentic operating system (SE-AOS) designed to autonomously exploit web applications by continuously discovering and integrating new exploit capabilities into its own kernel. Unlike traditional tools that rely on static rule sets or human-curated exploits, Mako dynamically evolves through observation, synthesis, and verification, treating each discovered capability as a versioned module that can be hot-loaded back into the system. The authors claim to have achieved full-suite coverage across 104 CTF-style web applications using this self-improving architecture, demonstrating that once a vulnerability class is discoverable, exploitation becomes trivial regardless of difficulty. This work represents a paradigm shift from static security testing to adaptive, agent-driven offensive research.

## Key Contributions  
- [Finding 1] Mako introduces the concept of SE-AOS—a runtime-extendable kernel where exploit capabilities are treated as mutable modules that can be synthesized, verified, and hot-loaded without restarting the system. This enables continuous self-improvement based on real-world failure analysis.  
- [Finding 2] The system achieves full-suite coverage across 104 containerized web applications spanning multiple vulnerability classes, with each target generating a unique cryptographic flag to ensure results are non-memorised and verifiable.  
- [Finding 3] Mako implements a gated self-evolution loop that evaluates fitness of new capabilities against live targets; if degradation is detected, the system discards or refines the change, maintaining long-term effectiveness.

## Methodology  
The authors approached the problem by modeling exploit discovery as an evolutionary process within a self-contained operating system. Mako observes failures in its current state, synthesizes potential new exploits from observed patterns, and tests them against live targets using a verification regime that prevents memorisation or fabrication of results. Each successful capability is integrated into the kernel via hot-loading, allowing immediate use without rebooting. The evolution loop ensures only improvements are committed, preserving system stability and relevance.

## Results  
Mako successfully drove every one of 104 web applications to emit a per-build cryptographic flag, confirming full coverage across all vulnerability classes. Crucially, the system demonstrated that difficulty in exploitation is not inherent but stems from the scarcity of discoverable capabilities—not reasoning or logic. The self-evolution loop maintained performance over time without regression, validating the long-term viability of the SE-AOS framework.

## Significance  
This research marks a significant advancement in autonomous security testing by shifting control to an adaptive agent that continuously improves its own capabilities. By formalising exploit discovery as a runtime process, Mako reduces reliance on human intervention and static rule bases, enabling faster, more comprehensive offensive testing. The paper’s contribution lies not only in the technical innovation but also in its ethical stance: while publishing the scientific framework, it withholds operational details to prevent dual-use concerns.

## Related Concepts  
- Autonomous agents  
- Self-evolving systems  
- Kernel-level capability injection  
- Continuous security testing  
- CTF-style web exploitation  
- Cryptographic verification  
- Dual-use research of concern
