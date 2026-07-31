# Summary: 2026-07-30_08-53-05Z_AnEmpiricalStudyofCoordinationModeastheFirst_Class.md
Saved: 2026-07-30 20:31
Source: 2026-07-30_08-53-05Z_AnEmpiricalStudyofCoordinationModeastheFirst_Class.md
Model: None

---

## Summary  
The authors introduce MSEval, a benchmark that evaluates multi‑agent coding on real‑world full‑stack projects to measure how coordination modes affect speed, cost, and quality. By treating organizational topology as the first‑class citizen of from‑scratch multi‑agent development, they create a reproducible standard that moves beyond synthetic benchmarks. The study demonstrates that the same task and model can yield dramatically different outcomes when the collaboration structure changes. This work provides empirical evidence for the importance of coordination in practical software teams.

## Key Contributions  
- MSEval is a rigorous empirical benchmark for from‑scratch multi‑agent coding that uses real tasks, hierarchical requirements, and deterministic rubrics.  
- Organizational topology (collaboration topologies) rivals model capability in shaping the speed–cost–quality trade‑off; varying it shifts scores by over 30 points and doubles wall‑clock time.  
- Structured pipelines converge fastest with the highest quality, whereas heavy managerial oversight degrades performance.

## Methodology  
The authors built MSEval around ten authentic full‑stack projects spanning ten domains, each defined by a hierarchy of requirements. Their execution engine LegoGent tests ten collaboration topologies where agents synchronize at periodic intervals and deploy via native CI/CD pipelines. The automated grader TAgent probes implementations to jointly assess functional success, latency, and prefix‑cached token cost across 100 runs.

## Results  
Across the 100 runs, changing the topology produced score variations exceeding 30 points and doubled execution time. Structured pipelines achieved the fastest convergence and highest quality scores, while teams subjected to heavy managerial oversight showed degraded performance relative to self‑organizing groups.

## Significance  
MSEval establishes a rigorous, reproducible standard for measuring how multi‑agent teams actually build software, moving the field beyond synthetic or superficial benchmarks. The findings highlight that coordination mode is as critical as model capability and can be leveraged to optimize speed, cost, and quality in real collaborative coding environments.

## Related Concepts  
Multi‑agent vibe coding, from‑scratch evaluation, hierarchical requirements, deterministic rubrics, LegoGent execution engine, TAgent grader, CI/CD pipelines, collaboration topologies, functional success, latency, token cost, organizational topology, speed–cost–quality trade‑off.
