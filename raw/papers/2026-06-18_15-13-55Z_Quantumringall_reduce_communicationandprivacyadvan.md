---

title: "Quantum ring all-reduce: communication and privacy advantages for distributed learning"
published: "2026-06-18T15:13:55Z"
authors: María Gragera Garcés, Lirandë Pira
url: http://arxiv.org/abs/2606.20344v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Quantum ring all-reduce: communication and privacy advantages for distributed learning



**Source**: [Original Paper](http://arxiv.org/abs/2606.20344v1)
## Abstract
Machine learning models have scaled to unprecedented sizes, making training across distributed devices the de facto standard in the field. In this work, we explore how quantum communications can make distributed training both more communication-efficient and information-theoretically private, for both classical and quantum learning models. Ring all-reduce is the foundational communication primitive for large-scale distributed training. We present a quantum version that reduces per-link online communication by a provably optimal factor of two using pre-shared entanglement and superdense coding, without requiring the learning model or gradient computation to change. Beyond bandwidth, the primitive enables privacy guarantees that are information-theoretically impossible for any classical protocol, achieving composable ε-secure aggregation, via verified entanglement, at a 2x overhead in GHZ copies. Our hybrid quantum-classical communication architecture yields simultaneous communication and security advantages for large scale distributed training, regardless of whether the learning itself is quantum or classical. Finally, we characterise quantum advantages in gradient conflict detection for server-to-client communication under bandwidth constraints, a setting that arises after ring all-reduce is completed, when full gradient broadcast to external clients is infeasible. Two variants of the problem admit different separations. For margin-based alignment testing (\textsc{GapIP}_τ), the quantum advantage is quadratic in the margin parameter: \widetilde{O}(τ^{-1}\log P) qubits versus \widetilde{O}(\min(\τ^{-2},P)) bits. For sign-consistency auditing against a private parameter matching (\textsc{TieAudit}_ε), the advantage represents an exponential separation in communication complexity: Ω(\sqrt{P}) bits whereas O(ε^{-2}\log P) qubits suffice.

## Metadata
- **Published**: 2026-06-18T15:13:55Z
- **Authors**: María Gragera Garcés, Lirandë Pira
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.20344v1)