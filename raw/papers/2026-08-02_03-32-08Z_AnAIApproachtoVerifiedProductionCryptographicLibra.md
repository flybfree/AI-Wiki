---
title: An AI Approach to Verified Production Cryptographic Libraries
published: 2026-08-02T03:32:08Z
authors: Chuyue Sun, Su Fong, Zhiyi Kuang, Yizheng Jiao, Nina Narodytska, Haoze Wu, David L. Dill, Clark Barrett
url: http://arxiv.org/abs/2608.00965v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An AI Approach to Verified Production Cryptographic Libraries

## Abstract
Cryptographic code is critical infrastructure that must be correct, yet formally verifying production libraries remains difficult. Existing language-model proof systems solve isolated obligations with specifications and premises already given, leaving production-library verification unresolved.   We present CryptoProver, an AI-based system that synthesizes internal specifications and Verus-checked proofs from high-level API contracts. Without changing executable code, CryptoProver constructs a new independent proof of curve25519-dalek and verifies RustCrypto's previously unverified chacha20 implementation against an RFC 8439 specification. These cryptographic lineages underpin deployed systems including Signal and Shadowsocks; Signal has an estimated 218M global downloads. The independent, human-led curve25519-dalek verification was developed publicly over eight months by five main contributors. Given the API contracts and a fixed trusted library of field specifications, arithmetic facts, axioms, and vstd, CryptoProver synthesizes the internal specifications and proofs in 11.4 hours with USD 466.99 in recorded API cost. CryptoProver follows a trust-first design principle: mechanical gates reject specification weakening, invented axioms, and cross-module breakage, while isolation blocks reference proof retrieval, including from git history.

## Metadata
- **Published**: 2026-08-02T03:32:08Z
- **Authors**: Chuyue Sun, Su Fong, Zhiyi Kuang, Yizheng Jiao, Nina Narodytska, Haoze Wu, David L. Dill, Clark Barrett
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00965v1)