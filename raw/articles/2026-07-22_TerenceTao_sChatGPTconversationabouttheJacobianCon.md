---
title: Terence Tao's ChatGPT conversation about the Jacobian Conjecture counterexample
date: 2026-07-22
url: https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56
source_feed: Hacker News
scraped: 2026-07-22 23:19
---

# Terence Tao's ChatGPT conversation about the Jacobian Conjecture counterexample

## Full Article

This is a copy of a shared ChatGPT conversation

Monday 9:01 PM

#### You said:

Uploaded a file

After the first announcement of a solution, an alternate approach has been given in the attached PDF. Can you compare this approach with the previous example and see if it retroactively helps explain the construction of the former?

#### ChatGPT said:

Yes. I checked the identities independently, and the two maps are mutually inverse polynomial isomorphisms.

Let

$$
X = \left{\right. \left(\right. a , b , c , d , e \left.\right) \in \mathbb{C}^{5} : a^{2} e - a b d + c b^{2} = 1 , a d + b c = 1 \left.\right} .
$$

Define $\Phi : \mathbb{A}^{3} \rightarrow X$ by

$$
b & = 1 + a y , \\ c & = 1 - \frac{3}{2} a y + a^{2} z , \\ d & = \frac{1}{2} y - a z + \frac{3}{2} a y^{2} - a^{2} y z , \\ e & = - 2 z + 4 y^{2} - 4 a y z + 3 a y^{3} - 2 a^{2} y^{2} z .
$$

Direct expansion gives

$$
a d + b c = 1
$$

and

$$
a^{2} e - a b d + c b^{2} = 1
$$

identically in $a , y , z$. Thus $\Phi$ is defined on all of $\mathbb{A}^{3}$, including $a = 0$.

Now define $\Psi : X \rightarrow \mathbb{A}^{3}$ by

$$
y & = 2 b d - a e , \\ z & = 2 d^{2} + c e + 6 b d^{2} + 3 b c e - \frac{9}{2} e .
$$

Substituting the forward formulas into these expressions gives identically

$$
2 b d - a e = y
$$

and

$$
2 d^{2} + c e + 6 b d^{2} + 3 b c e - \frac{9}{2} e = z .
$$

Hence

$$
\Psi \circ \Phi = \left(id ⁡\right)_{\mathbb{A}^{3}} .
$$

Conversely, start with $\left(\right. a , b , c , d , e \left.\right) \in X$, define $y , z$ by the polynomial formulas above, and reconstruct

$$
b^{'} & = 1 + a y , \\ c^{'} & = 1 - \frac{3}{2} a y + a^{2} z , \\ d^{'} & = \frac{1}{2} y - a z + \frac{3}{2} a y^{2} - a^{2} y z , \\ e^{'} & = - 2 z + 4 y^{2} - 4 a y z + 3 a y^{3} - 2 a^{2} y^{2} z .
$$

Reducing $b^{'} - b , c^{'} - c , d^{'} - d , e^{'} - e$ modulo the two defining equations of $X$ gives zero in each case. Therefore

$$
\Phi \circ \Psi = \left(id ⁡\right)_{X} .
$$

So indeed

$$
\boxed{X \cong \mathbb{A}^{3}}
$$

by the explicit polynomial isomorphism

$$
\left(\right. a , y , z \left.\right) \leftrightarrow \left(\right. a , b , c , d , e \left.\right)
$$

displayed above.

In particular, there is no hidden restriction or exceptional locus at $a = 0$; the apparent divisions in the preliminary formulas for $d$ and $e$ have removable singularities, and the final maps are polynomial everywhere.

#### You said:

If one composes Phi with the map F(a,b,c,d,e) = (ac, ad + bc, ae + bd, be) and then drops the ad+bc=1 term, can you confirm symbolically that one obtains a polynomial from (a,y,z) to C^3 with constant Jacobian?

#### ChatGPT said:

Yes. After composing $\Phi$ with

$$
F \left(\right. a , b , c , d , e \left.\right) = \left(\right. a c , \textrm{ } a d + b c , \textrm{ } a e + b d , \textrm{ } b e \left.\right)
$$

and discarding the identically constant coordinate $a d + b c = 1$, one gets the polynomial map

$$
G : \mathbb{C}_{a , y , z}^{3} \rightarrow \mathbb{C}^{3}
$$

given by

$$
G \left(\right. a , y , z \left.\right) = \left(\right. G_{1} , G_{2} , G_{3} \left.\right) ,
$$

where

$$
\boxed{G_{1} = a c = a - \frac{3}{2} a^{2} y + a^{3} z ,}
$$

$$
\boxed{G_{2} = a e + b d = \frac{1}{2} y - 3 a z + 6 a y^{2} - 6 a^{2} y z + \frac{9}{2} a^{2} y^{3} - 3 a^{3} y^{2} z ,}
$$

and

$$
\boxed{G_{3} = b e = - 2 z + 4 y^{2} - 6 a y z + 7 a y^{3} - 6 a^{2} y^{2} z + 3 a^{2} y^{4} - 2 a^{3} y^{3} z .}
$$

Equivalently,

$$
G_{1} & = a - \frac{3}{2} a^{2} y + a^{3} z , \\ G_{2} & = \frac{1}{2} y - 3 a z + 6 a y^{2} - 6 a^{2} y z + \frac{9}{2} a^{2} y^{3} - 3 a^{3} y^{2} z , \\ G_{3} & = - 2 z + 4 y^{2} - 6 a y z + 7 a y^{3} - 6 a^{2} y^{2} z + 3 a^{2} y^{4} - 2 a^{3} y^{3} z .
$$

A direct symbolic differentiation gives

$$
\boxed{det ⁡ \frac{\partial \left(\right. G_{1} , G_{2} , G_{3} \left.\right)}{\partial \left(\right. a , y , z \left.\right)} = - 1.}
$$

Thus $G$ is a polynomial map with constant nonzero Jacobian.

A quick consistency check at $a = 0$ is

$$
G \left(\right. 0 , y , z \left.\right) = \left(\right. 0 , \frac{y}{2} , 4 y^{2} - 2 z \left.\right) ,
$$

whose Jacobian matrix at $a = 0$ is triangular enough to give determinant $- 1$, consistent with the global calculation.

So this composition produces exactly the desired Keller map

$$
\boxed{G : \mathbb{C}^{3} \rightarrow \mathbb{C}^{3} , det ⁡ D G \equiv - 1.}
$$

#### You said:

The original counterexample to the Jacobian conjecture is $$ F(z_1,z_2,z_3) = \Big((1+z_1 z_2)^3 z_3 + z_2^2 (1+z_1z_2) (4+3z_1z_2), z_2 + 3 z_1 (1+z_1z_2)^2 z_3 + 3 z_1 z_2^2 (4+3z_1z_2), 2 z_1 - 3 z_1^2 z_2 - z_1^3 z_3\Big)$$. Can you see how this relates to the map G?

#### ChatGPT said:

Yes. They are the same map, up to a linear change of source coordinates, a reversal of the output coordinates, and two output rescalings.

Set

$$
\boxed{a = z_{1} , y = z_{2} , z = - \frac{1}{2} z_{3} .}
$$

Recall

$$
G = \left(\right. G_{1} , G_{2} , G_{3} \left.\right) ,
$$

where

$$
G_{1} = a - \frac{3}{2} a^{2} y + a^{3} z .
$$

Under this substitution,

$$
2 G_{1} = 2 z_{1} - 3 z_{1}^{2} z_{2} - z_{1}^{3} z_{3} ,
$$

which is exactly the third coordinate of the original counterexample.

Likewise, direct expansion gives

$$
\boxed{2 G_{2} = z_{2} + 3 z_{1} \left(\right. 1 + z_{1} z_{2} \left.\right)^{2} z_{3} + 3 z_{1} z_{2}^{2} \left(\right. 4 + 3 z_{1} z_{2} \left.\right) ,}
$$

the second coordinate, and

$$
\boxed{G_{3} = \left(\right. 1 + z_{1} z_{2} \left.\right)^{3} z_{3} + z_{2}^{2} \left(\right. 1 + z_{1} z_{2} \left.\right) \left(\right. 4 + 3 z_{1} z_{2} \left.\right) ,}
$$

the first coordinate.

Consequently, writing $F_{o r i g}$ for the displayed counterexample,

$$
\boxed{F_{o r i g} \left(\right. z_{1} , z_{2} , z_{3} \left.\right) = \left(\right. G_{3} , \textrm{ }\textrm{ } 2 G_{2} , \textrm{ }\textrm{ } 2 G_{1} \left.\right) \left(\right. z_{1} , z_{2} , - \frac{z_{3}}{2} \left.\right) .}
$$

Equivalently, define the linear maps

$$
A \left(\right. z_{1} , z_{2} , z_{3} \left.\right) = \left(\right. z_{1} , z_{2} , - \frac{1}{2} z_{3} \left.\right)
$$

and

$$
B \left(\right. u_{1} , u_{2} , u_{3} \left.\right) = \left(\right. u_{3} , 2 u_{2} , 2 u_{1} \left.\right) .
$$

Then

$$
\boxed{F_{o r i g} = B \circ G \circ A .}
$$

This also checks the Jacobian constants. Since

$$
det ⁡ A = - \frac{1}{2} , det ⁡ B = - 4 , det ⁡ D G = - 1 ,
$$

we obtain

$$
det ⁡ D F_{o r i g} = \left(\right. - 4 \left.\right) \left(\right. - 1 \left.\right) \left(\right. - \frac{1}{2} \left.\right) = \boxed{- 2} ,
$$

which agrees with the Jacobian of the original formula.

So the factorization construction has recovered the original map exactly, modulo these elementary linear normalizations.

## Metadata
- **Source**: [Original Article](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56)
