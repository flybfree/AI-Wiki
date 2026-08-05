# Summary: 2026-07-29_18-52-44Z_FunL2O_LLM_GuidedFeatureFunctionDesignforLearningt.md
Saved: 2026-07-30 21:36
Source: 2026-07-29_18-52-44Z_FunL2O_LLM_GuidedFeatureFunctionDesignforLearningt.md
Model: None

---

## Summary  
Learning‑to‑optimize (L2O) aims to train models that predict useful information such as optimal solutions or warm‑start points for repeated optimization problems. Existing L2O pipelines rely on manually designed feature functions, which limit flexibility across domains. The authors introduce **FunL2O**, the first unified framework that automates this representation design using large language model (LLM)–guided program evolution within a FunSearch‑style loop. By iteratively generating executable feature functions and re‑training the original L2O model on their outputs, FunL2O replaces handcrafted features with dynamically evolving ones.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-08-04_09-31-44Z_LLM_DerivedPriorsforThompsonSamplinginCold__summary.md|Summary: 2026-08-04_09-31-44Z_LLM_DerivedPriorsforThompsonSamplinginCold_StartCo.md]] — 4 title terms overlap; 1 backlink; 7 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 2 title terms overlap; 121 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- **Finding 1:** A unified framework called FunL2O that automates feature function design for learning‑to‑optimize via LLM‑driven program evolution.  
- **Finding 2:** An iterative loop where an LLM proposes executable feature functions, a fixed evaluation process retrains the original L2O model, and performance is measured on downstream optimization tasks.  
- **Finding 3:** Evolved features consistently outperform hand‑crafted representations across continuous/discrete optimization problems and four different LLMs.

## Methodology  
The authors adopt a FunSearch‑style meta‑learning loop: the LLM receives problem instances and generates candidate feature functions that are compiled into executable code. A fixed evaluation pipeline then re‑trains the original L2O model on these generated features, computes optimization metrics (e.g., solution quality, warm‑start accuracy), and feeds the results back to the LLM for further proposals. This cycle repeats until convergence or a predefined budget is reached. The framework is applied uniformly across various optimization tasks without domain‑specific feature engineering.

## Results  
Experiments on linear and quadratic programming tasks involving solution prediction and warm‑starting, as well as mixed‑integer optimization using GNN‑guided backdoor branching and Predict‑and‑Search, demonstrate that features evolved by FunL2O achieve higher optimization performance than manually designed alternatives. The improvements are observed for both continuous (e.g., linear/quadratic) and discrete problems, and across four LLMs (GPT‑4, Claude, Llama 3, and Mixtral). Statistical analysis confirms the superiority of LLM‑generated features in a wide range of scenarios.

## Significance  
By decoupling representation design from expert heuristics, FunL2O opens a scalable path to improve learning‑to‑optimize systems across diverse problem spaces. The work shows that LLMs can act as creative designers of feature functions, reducing the need for manual engineering and enabling rapid adaptation to new domains.

## Related Concepts  
Learning‑to‑optimize (L2O), feature functions, LLM‑driven program evolution, FunSearch meta‑learning loop, GNN‑guided backdoor branching, Predict‑and‑Search, linear programming, quadratic programming, mixed‑integer optimization.
