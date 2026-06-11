# Summary: 2026-05-13_11-26-32Z_AHornextensionofDL_LitewithNLdatacomplexity.md
Saved: 2026-05-13 21:02
Source: 2026-05-13_11-26-32Z_AHornextensionofDL_LitewithNLdatacomplexity.md
Model: None

---

## Summary
This paper addresses a critical limitation in ontology-mediated query answering (OMQA) by challenging the long-standing dichotomy between first-order rewritability and polynomial-time data complexity. The authors identify that while DL-Lite offers efficient query rewriting, it restricts expressive power to first-order logic, which is insufficient for modern graph-structured data queries that are typically NL-complete. To bridge this gap, the researchers introduce a novel Horn extension of DL-Lite called ELbotpreceq, which strictly extends the core DL-Lite framework while maintaining manageable computational complexity. By introducing a stratification mechanism for the ELI description logic, the work enables reasoning over reachability axioms and restricted conjunctions within the complexity class NL, thereby aligning OMQA capabilities with the requirements of contemporary graph query standards like GQL and SQL/PGQ.

## Key Contributions
- The introduction of ELbotpreceq, a new description logic that strictly extends DL-Lite and supports both reachability axioms and restricted conjunctions while ensuring NL data complexity.
- The development of a novel stratification mechanism for ELI that effectively controls the interaction between logical conjunction and recursive definitions, preventing the complexity explosion typically associated with such features.
- The establishment of an NL upper bound for reasoning tasks through a theoretical rewriting of ontologies into nested two-way regular path queries, a fragment of the GQL language, providing a concrete path for integration with standard graph query engines.

## Methodology
The authors approached the problem by analyzing the theoretical boundaries of existing description logics, specifically focusing on why extensions beyond DL-Lite invariably lead to PTime-hardness. They identified that the core issue lies in the uncontrolled interaction between conjunction and recursion in standard ELI. To mitigate this, they designed a stratification mechanism that partitions the logical expressions to limit recursive dependencies. This allowed them to define ELbotpreceq, a logic that retains the Horn property necessary for efficient reasoning. They then proved the theoretical bounds by demonstrating that queries over this logic can be rewritten into nested two-way regular path queries, leveraging the structural properties of graph data to maintain non-deterministic logarithmic space complexity.

## Results
The primary theoretical result is the proof that ELbotpreceq supports reasoning in NL (Nondeterministic Logarithmic space), strictly lower than the PTime complexity of most other expressive description logics. The authors demonstrated that this logic can express many ontologies previously only possible in ELI or DL-Lite, thus offering a richer expressive power than DL-Lite without sacrificing the low data complexity. Furthermore, they showed that the rewriting into nested two-way regular path queries is feasible, providing initial evidence that this ontology language is compatible with emerging ISO standards for graph queries, such as GQL and SQL/PGQ.

## Significance
This work is significant because it breaks the rigid AC0 vs. PTime dichotomy that has historically limited OMQA solutions. By providing a logic that is both expressive enough for complex graph patterns and computationally efficient enough for large-scale data, it opens the door for OMQA to be integrated directly into modern graph database systems. This alignment with standard graph query languages makes OMQA more practical for real-world applications involving complex networked data, such as social networks or biological pathways.

## Related Concepts
- Ontology-Mediated Query Answering (OMQA)
- DL-Lite Description Logic
- Data Complexity (NL vs. PTime)
- Horn Description Logics
- Stratification Mechanisms
- Nested Two-Way Regular Path Queries
- GQL and SQL/PGQ Standards
- ELI Description Logic

[[A Horn extension of DL-Lite with NL data complexity]]