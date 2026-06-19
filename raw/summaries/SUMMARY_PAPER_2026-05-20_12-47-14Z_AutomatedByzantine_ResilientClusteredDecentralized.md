---

title: Automated Byzantine-Resilient Clustered Decentralized Federated Learning for Battery Intelligence in Connected EVs
url: http://arxiv.org/abs/2605.21115v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_12-47-14Z_AutomatedByzantine_ResilientClusteredDecentralized.md
generated_at: "2026-06-11 10:43"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces ABC-DFL, an automated Byzantine‑resilient clustered decentralized federated learning framework for electric vehicle battery intelligence. The system replaces centralized servers with a blockchain oracle and uses FLECA to filter malicious updates, achieving convergence comparable to FedProx while keeping attack impact below 0.10.

## Key Takeaways
- ABC-DFL employs an open‑permissioned blockchain and dynamic Quorum Byzantine Fault Tolerance to eliminate reliance on a central server, enhancing trust and security in connected EV networks.
- The FLECA protocol enables each EV to filter outlier updates using adaptive thresholds tied to deviations from its reference model, effectively reducing the impact of Byzantine attacks.
- Experimental results show that ABC-DFL matches FedProx performance under benign conditions and outperforms existing defenses when adversarial attacks are introduced.

## Context
Federated learning is increasingly vital for privacy‑preserving data aggregation in IoT environments such as smart transportation. Existing approaches often suffer from centralization vulnerabilities, making them unsuitable for large‑scale EV fleets where trust and security are paramount.

## Implications
By integrating blockchain with adaptive clustering, ABC-DFL offers a scalable model that can be deployed across millions of vehicles without compromising data integrity. Practitioners can leverage this framework to build robust battery intelligence services while maintaining user privacy and system resilience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21115v1)
