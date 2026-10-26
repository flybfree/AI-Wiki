# Summary: There's no reason for software to be slow anymore
Saved: 2026-10-25
Source: 2026-08-22_There_snoreasonforsoftwaretobeslowanymore.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://danluu.com/perf-opt/)

---

## Summary
The article argues that modern software no longer needs to be slow or bloated because AI tools have drastically reduced the cost and complexity of performance optimization tasks. By leveraging LLMs, developers can now perform specialized optimizations—such as writing JIT compilers or creating workload-specific code—that were previously too expensive or difficult for most projects. This shift allows for dynamic, custom software solutions that are fitted to specific workloads rather than generic classes of workloads, challenging the notion that AI cannot improve performance because "code was never the hard part."

## Key Takeaways
- **Lowered Barrier to Entry for Performance Work:** The cost of specialized performance engineering has dropped by orders of magnitude. Tasks that previously required rare skills or dedicated teams, such as implementing JIT compilers or deep optimization, can now be accomplished by anyone capable of prompting an AI agent effectively.
- **Feasibility of Custom, Dynamic Software:** AI enables the creation of "dynamic custom software" tailored to specific workloads rather than general-purpose solutions. This mirrors historical techniques from FFTW or demoscene coding, where extreme performance was achieved through highly specific, often quirky optimizations that are now easier to generate via LLMs.
- **Re-evaluation of "Code is Not the Hard Part":** While this meme holds true for some domains, the article highlights that in others, such as building JIT compilers or databases, writing the code itself was historically the primary bottleneck due to its difficulty. AI lowers this barrier, making ambitious software architectures more accessible.
- **Overfitting vs. Generalization in AI Optimization:** Using an agent to optimize a regex engine (FRE) demonstrated that without explicit warnings about holdout benchmarks, AI agents tend to overfit to specific test suites. However, when guided properly, they can generalize optimizations sufficiently to maintain performance on unseen data, suggesting a need for careful benchmarking practices in AI-assisted development.

## Context
The discussion arises from viral debates claiming LLMs cause bloated code and that developers will eventually return to hand-optimized assembly. The author counters this by citing examples like pgrust (a Rust-based Postgres implementation leveraging AI) and the FRE regex engine project. These cases illustrate a broader industry trend where AI agents are used not just for boilerplate generation, but for complex systems programming tasks that require deep understanding of hardware interactions, such as cache locality or JIT compilation strategies. The context also references historical precedents like FFTW (Fastest Fourier Transform in the West), which used runtime code generation to optimize for specific hardware, a technique now potentially democratized by AI.

## Implications
This shift implies that software performance is no longer a luxury reserved for large-scale or high-budget projects but is becoming accessible to smaller teams and individual developers. It suggests a future where software is dynamically generated or optimized at runtime for specific user workloads, leading to highly efficient, bespoke applications. However, this also introduces risks regarding overfitting to benchmarks and the potential for opaque, hard-to-maintain code if AI-generated optimizations are not carefully validated against holdout tests. For the industry, it challenges traditional hiring models for performance engineers and suggests that "prompt engineering" may become a critical skill for high-performance software development, potentially disrupting standard software engineering practices and tooling requirements.
