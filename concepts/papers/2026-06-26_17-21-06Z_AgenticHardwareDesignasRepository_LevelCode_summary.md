title: "Summary: 2026-06-26_17-21-06Z_AgenticHardwareDesignasRepository_LevelCodeEvoluti.md"
# Summary: 2026-06-26_17-21-06Z_AgenticHardwareDesignasRepository_LevelCodeEvoluti.md
Saved: 2026-06-28 21:01
Source: 2026-06-26_17-21-06Z_AgenticHardwareDesignasRepository_LevelCodeEvoluti.md
Model: None

---


## Summary  
The authors introduce HORIZON, a self‑evolving agent framework that treats hardware design as repository‑level code evolution. By converting a Markdown harness into a project pack that bundles domain knowledge, an evaluator, acceptance predicates, and a git/runtime policy, the system runs a hands‑free loop that evolves an isolated git worktree using only repository operations for state management, tracing, and replay. The approach achieves 100 % completion across multiple hardware‑design benchmarks, demonstrating the feasibility of fully autonomous design iteration. However, the authors clarify that this is not a claim of solving chip design but rather a controlled experiment on proxy problems.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 5 title terms overlap; 121 backlinks; 13 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 17 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, acceptance predicates, and a git/runtime policy to serve as a repository‑level codebase for hardware design.  
- [Finding 2] The framework implements a hands‑free agent loop that evolves an isolated git worktree using only repository operations (commit, fetch, branch, etc.) for state management, tracing, and replay.  
- [Finding 3] HORIZON attains 100 % benchmark completion across ChipBench, RTLLM, Verilog‑Eval, and nine CVDP categories in a fully autonomous loop.

## Methodology  
The authors approached the problem by modeling hardware design artifacts as code that can be versioned with git. A Markdown‑based harness encodes the domain knowledge required for each task, while an evaluator checks whether generated designs satisfy acceptance predicates. The runtime policy defines how the agent interacts with the repository—what operations are allowed and when. During evaluation, the agent operates on a separate worktree, committing incremental changes that trace back to the original harness; replay of these commits allows debugging or re‑experimentation without manual intervention.

## Results  
The experimental results show that HORIZON completes all benchmarks in its test suite with no human input: ChipBench (a suite of chip design tasks), RTLLM (reinforcement‑learning‑based layout generation), Verilog‑Eval (Verilog synthesis validation), and nine categories of CVDP (circuit verification and performance). The agent’s evolution is fully traceable via git logs, and the system can be replayed to reproduce intermediate states. These outcomes demonstrate that repository‑level self‑evolution can scale to hardware artifacts.

## Significance  
This work extends prior research on self‑evolving EDA software systems by applying them directly to hardware‑design artifacts, opening a pathway for AI agents to autonomously iterate design space without human oversight. It highlights the potential of treating low‑level engineering processes as versioned code, which could accelerate prototyping and reduce iteration time. However, the authors note that these benchmarks are controlled proxies; real chip design involves many more constraints, physical laws, and safety considerations that remain unsolved.

## Related Concepts  
- Repository‑level code evolution  
- Self‑evolving agents  
- Git worktree isolation  
- Markdown harness as domain specification  
- Executable evaluator and acceptance predicates  
- ChipBench, RTLLM, Verilog‑Eval benchmarks  
- CVDP categories (circuit verification & performance)
