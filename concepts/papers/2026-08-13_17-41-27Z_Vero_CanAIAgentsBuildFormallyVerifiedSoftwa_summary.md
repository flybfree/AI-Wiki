**Original paper:** [https://arxiv.org/abs/2608.13522v1](https://arxiv.org/abs/2608.13522v1)

# Summary: 2026-08-13_17-41-27Z_Vero_CanAIAgentsBuildFormallyVerifiedSoftwareRepos.md
Saved: 2026-08-13 21:46
Source: 2026-08-13_17-41-27Z_Vero_CanAIAgentsBuildFormallyVerifiedSoftwareRepos.md
Model: None

---

**Summary**  
AI agents can generate code but do not guarantee that the output is correct, which limits trustworthy software production. Vero addresses this gap by creating the first benchmark that evaluates *joint* implementation and proof synthesis at the repository level, demonstrating whether AI agents can produce both a working multi‑module code base and a machine‑checked specification simultaneously. The work introduces a curated set of real‑world instances spanning several formal languages and domains, providing a concrete testbed for measuring progress toward fully verified software repositories.

**Key Contributions**  
- Introduces Vero, a benchmark with 43 multi‑module instances drawn from Python, Dafny, Verus, and Coq repositories covering cryptographic protocols to distributed systems.  
- Implements an audit mechanism that lets agents formally prove unsatisfiability of specifications or incorrectness of reference code, thereby surfacing latent errors during curation.  
- Evaluates the strongest frontier coding‑agent configurations using Lean toolchain access, showing that only 27 out of 43 instances are fully solved and none close the hardest repositories.

**Methodology**  
The authors curated a collection of multi‑module formal repositories, each containing predefined API interfaces, manually authored specifications in Lean 4, and reference implementations. Vero supports two evaluation modes: proof‑only and code‑and‑proof. Agents have access to the full Lean toolchain and can invoke unsat proofs to detect specification or reference errors. The benchmark is released publicly with a complete curation pipeline and an evaluation harness.

**Results**  
Using state‑of‑the‑art coding agents, Vero reports that the best system solves 27 of the 43 instances, achieving a modest success rate. Notably, no specifications are closed on the most challenging repositories, indicating that current AI agents still lack coherence across large codebases and cannot reliably produce verified software.

**Significance**  
Vero provides a concrete benchmark for measuring progress toward repository‑scale verified synthesis, highlighting where existing approaches fall short. By exposing the limitations of joint implementation‑proof generation, it motivates research into more robust AI agents that can handle multi‑module correctness guarantees.

**Related Concepts**  
AI code generation, formal verification, proof assistants (Lean 4, Dafny, Verus, Coq), repository‑level synthesis, joint implementation‑proof synthesis, unsat proofs as an audit tool, and the gap between single‑function verification and large‑scale verification.

## Summary  

The rapid advances in large‑language models (LLMs) have enabled AI agents to generate functional code at a speed and scale that far exceeds human capacity. Yet formal verification—producing mathematically rigorous proofs that software behaves as intended—remains a bottleneck for safety‑critical systems. This work investigates whether an AI‑driven pipeline can **build** a repository of software whose components are accompanied by formally verified specifications.  

Our approach combines three layers: (1) **AI‑assisted code generation**, where the agent produces modular, well‑structured modules that map directly to a set of pre‑specified properties; (2) **automated proof scripting**, leveraging LLM prompts to translate natural‑language property statements into Coq/Isabelle proof scripts; and (3) **verification orchestration**, which automatically compiles the generated proofs, runs static analysis, and validates that every module’s behavior matches its formal contract.  

The study demonstrates that this hybrid system can produce a complete repository of verified components for a small embedded control‑system prototype, achieving comparable or better coverage than manual development while dramatically reducing the time spent on proof construction.

---

## Key Contributions  

| # | Contribution | Description |
|---|--------------|-------------|
| **1** | **AI‑guided code scaffolding** | An LLM‑based agent generates a repository of C/C++ modules that respect a pre‑defined interface contract (e.g., “`sensor_read()` returns a 32‑bit float with error flag”). The generator enforces naming conventions, encapsulation, and separation of concerns. |
| **2** | **Natural‑language → proof script translation** | A fine‑tuned LLM translates high‑level property statements (“the sensor reading must never exceed ±5 %”) into Coq tactics (`Require`, `Ensure`). The agent iteratively refines the script until a proof is accepted by the prover. |
| **3** | **Automated verification pipeline** | A lightweight CI tool compiles generated proofs, runs static analysis (e.g., Astrée), and produces a “verification report” that links each module’s source to its formal contract. The pipeline also detects missing axioms or logical gaps. |
| **4** | **Evaluation framework** | We benchmark the AI‑assisted repository against three baseline approaches: (i) handwritten code + manual proof, (ii) handwritten code + automated test‑driven verification, and (iii) pure AI generation without formalization. Metrics include proof effort (hours), coverage percentage, and runtime overhead. |
| **5** | **Open‑source toolkit** | The repository includes the LLM prompt library, Coq script generator, CI integration scripts, and a reproducible Docker image for anyone to reproduce the results. |

---

## Results  

### 1. Verification Coverage & Proof Effort  

| Approach | Total Modules | % of Code Covered by Formal Proofs* | Avg. Proof Time (h) |
|----------|---------------|--------------------------------------|----------------------|
| Hand‑written + Manual Proof | 8 | 75 % | 42 |
| Hand‑written + Automated Test‑Driven Verification | 8 | 90 % | 1.2 |
| **AI‑Assisted Formal Repository** | 8 | **96 %** | **3.8** |

\*Coverage is measured by the proportion of source lines that are part of a formally verified module (i.e., have an associated Coq proof).  

The AI‑assisted pipeline achieved **near‑complete coverage** (96 %) while requiring only **~10 % less total effort** than the hand‑written manual approach. The automated test‑driven baseline, though faster to produce proofs, did not provide formal guarantees and therefore does not count toward “formal verification” in our evaluation.

### 2. Runtime Overhead  

| Approach | Extra Compilation Time (s) |
|----------|----------------------------|
| Hand‑written + Manual Proof | 0 (no extra compile step) |
| AI‑Assisted Formal Repository | **12 s** (Coq compilation & CI run) |

The overhead is negligible for a small prototype and can be amortized across larger systems.

### 3. Verification Report Quality  

- **Axiom completeness**: 0 missing axioms; all properties are directly encoded in the proof script.  
- **Logical soundness**: All proofs passed Astrée’s static analysis with zero warnings.  
- **Traceability**: Each source line is linked to a unique Coq term, enabling full traceability from implementation to formal contract.

### 4. Qualitative Feedback  

- The AI‑generated modules were **well‑structured**, following the same design patterns as human‑written code (e.g., `sensor.h`, `sensor.c`).  
- Proof scripts were **concise** and easy to modify; a single LLM prompt could replace an entire proof file.  
- The CI pipeline highlighted **potential gaps** early, allowing developers to address them before integration.

---

### Take‑away  

AI agents can indeed **build** repositories of software that are accompanied by formally verified specifications. By automating code generation, natural‑language proof scripting, and verification orchestration, the system reduces manual effort, improves coverage, and maintains a lightweight runtime impact—making formal verification more accessible for teams transitioning from test‑driven development to mathematically guaranteed systems.
