# Summary: 2026-07-26_16-04-27Z_AnExactCounterexampletoCarlson_sAssociated_PrimeDe.md
Saved: 2026-07-27 23:55
Source: 2026-07-26_16-04-27Z_AnExactCounterexampletoCarlson_sAssociated_PrimeDe.md
Model: None

---

## Summary  
The paper disproves Carlson’s associated‑prime depth conjecture for a group of order 128 by constructing an exact counterexample where the cohomological depth is two but no associated prime has that dimension. It does so using a specific finite group \(G = S_{128}{859}\) and characteristic zero field \(\overline{k}\), showing \(\depth H^{*}(G;\overline{k})=2\) while all rank‑two elementary abelian centralizers have depth at least three.

## Key Contributions  
- Finding 1: The exact presentation certificate proves that the cohomological depth of \(G\) is exactly two.  
- Finding 2: Enumeration of all 75 rank‑two elementary abelian subgroups shows six distinct centralizer types; four are ruled out by Duflot’s theorem (depth ≥ 3) and the remaining two exhibit regular sequences of length three via ideal‑quotient certificates, confirming depth ≥ 3.  
- Finding 3: The combined evidence demonstrates that no associated prime of dimension two exists in \(H^{*}(G;\overline{k})\), providing a concrete counterexample to Carlson’s conjecture.

## Methodology  
The authors approached the problem by first constructing an explicit finite group \(G\) of order 128 with a known cohomological depth, then applying Okuyama’s associated‑prime theorem to translate any potential rank‑two associated prime into a centralizer of a rank‑two elementary abelian subgroup \(E\). They enumerated all such subgroups (75 in total), computed the cohomology rings for each centralizer using three independent algebraic presentations, and verified depth via exact ideal‑quotient certificates or Duflot’s theorem. The verification was performed through computational algebra to produce presentation data.

## Results  
The main experimental result is that \(\depth H^{*}(G;\overline{k}) = 2\), yet every rank‑two elementary abelian centralizer has cohomological depth at least three, so there are no associated primes of dimension two. This directly contradicts Carlson’s conjecture which claimed such a prime must exist whenever the depth equals the minimal associated prime dimension.

## Significance  
This counterexample is significant because it resolves an open question in finite‑group cohomology and demonstrates that depth can be realized without any associated prime attaining that depth, challenging longstanding assumptions about the relationship between cohomological depth and associated primes. The work also provides a template for testing similar conjectures on other small groups.

## Related Concepts  
- Cohomological depth of a group ring.  
- Associated primes in group cohomology rings.  
- Okuyama’s associated‑prime theorem.  
- Duflot’s theorem on depth via regular sequences.  
- Elementary abelian subgroups and their centralizers.  
- Exact ideal‑quotient certificates.
