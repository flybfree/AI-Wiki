# Summary: 2026-07-23_EscapeIntelliJ_ScalaandKotlinLSPsonEmacsEglot.md
Saved: 2026-07-23 04:01
Source: 2026-07-23_EscapeIntelliJ_ScalaandKotlinLSPsonEmacsEglot.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
The article explains how Emacs Eglot can replace IntelliJ IDEA for Scala and Kotlin development, offering a lightweight, protocol‑first LSP client that integrates seamlessly with Emacs’ text tools. By using JSON‑RPC language servers and custom ESL advice, the setup provides fast, hackable completions and refactors while avoiding the heavyweight, RAM‑hungry IDE experience.

## Key Takeaways  
- **Unified workflow:** All languages share the same completion, navigation, and refactoring utilities (corfu, company) regardless of mode.  
- **Live patching:** ESL advice can intercept JSON‑RPC payloads to fix bugs instantly without waiting for vendor patches.  
- **Minimal overhead:** Eglot runs as a thin transport layer, keeping Emacs responsive and free from the 8 GB+ RAM consumption typical of IntelliJ.

## Context  
The shift reflects broader trends in AI‑assisted development where developers demand low‑latency, extensible tooling that respects the Unix philosophy. By decoupling language server responsibilities from the editor, Eglot enables rapid prototyping and customization—key for modern AI‑driven coding environments.

## Implications  
This approach democratizes high‑performance LSP support across open‑source ecosystems, reducing reliance on proprietary IDEs and encouraging a more modular, hackable developer experience that aligns with AI‑enhanced productivity goals.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/embodied-ai/embodied-ai-hub.md|Embodied AI Hub]]
- [[concepts/ai-infrastructure/ai-infrastructure-hub.md|AI Infrastructure Hub]]
