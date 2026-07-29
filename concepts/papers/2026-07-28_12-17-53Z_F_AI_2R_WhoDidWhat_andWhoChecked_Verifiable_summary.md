# Summary: 2026-07-28_12-17-53Z_F_AI_2R_WhoDidWhat_andWhoChecked_VerifiableAIProve.md
Saved: 2026-07-28 20:29
Source: 2026-07-28_12-17-53Z_F_AI_2R_WhoDidWhat_andWhoChecked_VerifiableAIProve.md
Model: None

---

## Summary  
The paper introduces F(AI)2R, an AI‑assisted authoring and verification process that records the provenance of every artefact in a machine‑readable way. It extends the original experiment to any AI‑in‑the‑loop artefact using a PROV‑O extension called **aiprov**. The method is packaged as an executable skill that runs automatically on pushes, gating commits only when graph conformance is satisfied and publishing the current build of the paper itself. The work serves as its own case study, demonstrating end‑to‑end traceability from idea to published manuscript.

## Key Contributions  
- [Finding 1] Generalization of the provenance model beyond scholarly writing into **aiprov**, a PROV‑O extension covering any AI‑in‑the‑loop artefact.  
- [Finding 2] Packaging the method as an executable skill that autonomously sets up CI to gate pushes on graph conformance and publishes the current build.  
- [Finding 3] Enforcing two invariants in the provenance graph: no parentless claim, and verification rungs that only humans may grant.

## Methodology  
The authors approached the problem by first analyzing the limitations of existing AI‑assisted research workflows where contributions are not traceable. They built on the original F(AI)2R experiment and designed **aiprov** to capture every activity, claim, and source as nodes in a PROV‑O graph. The executable skill orchestrates identity resolution via ORCID lookup, configures CI pipelines that validate graph invariants before allowing commits, and logs each operation. Human operators provide their ORCID ID; the system resolves it from the public registry and integrates with GitHub Actions to enforce provenance checks.

## Results  
The implementation demonstrates full end‑to‑end traceability: every line of code, claim, and data source is recorded in the provenance graph. The CI pipeline successfully gates pushes only when invariants hold, preventing parentless claims and unauthorized verification rungs. The paper’s own production process—including its abstract, methods, and results—is fully represented in the graph with human‑granted verification rungs at each step.

## Significance  
This work establishes a reusable framework for verifiable AI provenance that can be applied beyond academia to any domain where AI contributes to artefact creation. By making provenance an executable skill, it bridges automated AI workflows and human accountability, enabling trustworthy research and reducing fraud risk. The approach also showcases how machine‑readable graphs can serve as immutable audit trails.

## Related Concepts  
- PROV‑O: a standard for representing provenance in software engineering.  
- Executable Skills: a concept where AI agents perform tasks autonomously with defined capabilities.  
- CI/CD Pipelines: continuous integration and delivery systems that enforce quality gates.  
- ORCID: Open Research Identifier linking researchers to their work.
