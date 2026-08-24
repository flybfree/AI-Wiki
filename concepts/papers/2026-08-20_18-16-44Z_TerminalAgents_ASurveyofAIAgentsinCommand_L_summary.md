# Summary: 2026-08-20_18-16-44Z_TerminalAgents_ASurveyofAIAgentsinCommand_LineEnvi.md
Saved: 2026-08-23 21:26
Source: 2026-08-20_18-16-44Z_TerminalAgents_ASurveyofAIAgentsinCommand_LineEnvi.md
Model: None

---

## Summary  
The paper surveys AI agents that operate through command‑line terminals, seeking to unify scattered work from software engineering, tool use, and computer‑use research into a single framework. It proposes a seven‑dimensional competence profile that links system architecture, competence acquisition, and evaluation, arguing that terminal‑mediated agency is jointly shaped by the model, interface, harness, runtime, and environment. The authors highlight methodological gaps: most evaluations focus on final outcomes while overlooking process quality, recovery, and governance. By exposing these biases, the survey motivates explicit reporting of system and runtime conditions with replayable traces.

## Key Contributions  
- Establishes a seven‑dimensional terminal competence profile linking system architecture, competence acquisition, and evaluation.  
- Identifies that realized behavior results from the interaction of five components: model, interface, harness, runtime, and environment.  
- Shows that benchmark comparisons are limited by fixed conditions, exposing performance variability and misattribution of component effects.

## Methodology  
The authors performed a comprehensive literature review across software engineering, tool use, and computer‑use studies, organizing findings under the seven dimensions. They then conducted matched system experiments where agents were evaluated in identical terminal environments to isolate how each component influences task success rates and process quality.

## Results  
Experiments demonstrated that altering any single component—such as the harness or runtime—significantly changed task completion probabilities, confirming the joint‑shaping hypothesis. Benchmark families produced divergent process signals, revealing that performance metrics are context‑dependent and cannot be attributed to isolated components without careful condition matching.

## Significance  
Providing a unified framework and advocating replayable traces for evidence enables rigorous study of terminal agents across domains and improves reproducibility in AI research. The work bridges software engineering and emerging application areas by clarifying how component interactions drive agency outcomes.

## Related Concepts  
Terminal‑mediated agency, competence profile, component interaction, benchmark dependency, process quality, recovery, governance.
