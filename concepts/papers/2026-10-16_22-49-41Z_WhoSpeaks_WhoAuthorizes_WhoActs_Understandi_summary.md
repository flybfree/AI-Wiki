# Summary: 2026-10-16_22-49-41Z_WhoSpeaks_WhoAuthorizes_WhoActs_UnderstandingTrust.md
Saved: 2026-10-19 21:05
Source: 2026-10-16_22-49-41Z_WhoSpeaks_WhoAuthorizes_WhoActs_UnderstandingTrust.md
Model: None

---

## Summary
This paper investigates the distinct trust boundaries within multi-agent Large Language Model (LLM) systems, specifically distinguishing between message delivery (communication), signing authority (authorization), and tool-side enforcement (execution). The authors introduce a framework using "authority cuts" to identify the smallest compromised signer coalition capable of producing a policy-valid false-claim proof. Through controlled paired hidden-state studies, the research demonstrates that these three stages operate independently, revealing critical divergences between what models request, what they authorize, and what tools actually execute. The study highlights that valid authorization proofs do not guarantee factual truth, necessitating a separation of safety evaluations across these distinct layers.

## Key Contributions
- **Independence of Trust Boundaries**: The paper establishes that communication, authorization, and execution are separate trust boundaries. It demonstrates that no fixed-message routing contrast across four models met the prespecified large-effect criterion for safety improvements, indicating that message routing alone is insufficient for ensuring safety.
- **Divergence Between Request and Commitment**: The study reveals a critical gap between model requests and actual tool commitments. In invalid-proof cases, models like Nemotron and Llama requested protected actions in over 50% of trials, yet a deterministic tool gate committed none, highlighting that request-level safety metrics do not reflect commitment-level safety.
- **Authorization Does Not Equal Truth**: A separate single-model authorization check showed that a false claim accompanied by a policy-valid compromised-signer proof can pass the authorization gate. This proves that proof validity is distinct from factual truth, warning against conflating authorized actions with correct actions.

## Methodology
The authors approached the problem by modeling multi-agent LLM interactions as three distinct structures: communication (message delivery), authorization (signing authority), and execution (tool-side enforcement). They utilized the concept of an "authority cut" to characterize the minimal set of compromised signers required to construct a policy-valid false-claim proof under specific assumptions. The methodology involved controlled paired hidden-state studies across four different LLM models to test how message rewriting, source-identity cues, and proof validity influence action selection and tool commitment. The experiments specifically measured executed false-state action rates and compared request-level safety readouts against commitment-level outcomes enforced by deterministic tool gates.

## Results
The experimental results revealed four key distinctions. First, varying message routing configurations did not consistently produce large safety effects across the tested models, though rewriting messages did alter false-state action rates depending on the specific model and route. Second, providing source-identity cues to the models did not uniformly increase the selection of protected actions across three different models. Third, in cases involving invalid proofs, Nemotron and Llama models requested protected actions in 52.1% and 54.2% of trials, respectively, but the deterministic tool gate committed zero of these actions, demonstrating a stark divergence between what models propose and what systems execute. Finally, the study confirmed that a false claim with a valid proof structure could successfully pass the authorization gate, proving that the system’s logical validation mechanisms do not inherently verify factual accuracy.

## Significance
This research is significant because it challenges the assumption that multi-agent LLM systems can be secured through a single unified trust mechanism. By proving that communication, authorization, and execution are separate boundaries, the paper argues for a more granular approach to safety evaluation. It warns developers and researchers that relying on model requests or valid proof structures is insufficient for safety, as these do not guarantee factual truth or committed action. This framework motivates the development of separate evaluation metrics for delivered information, qualified authorization, model proposals, and committed actions, which is crucial for building reliable and safe autonomous agent systems.

## Related Concepts
- Multi-Agent LLM Systems
- Trust Boundaries (Communication, Authorization, Execution)
- Authority Cut
- Policy-Valid False-Claim Proof
- Deterministic Tool Gate
- Request-Level vs. Commitment-Level Safety
- Source-Identity Cues
- Hidden-State Studies
