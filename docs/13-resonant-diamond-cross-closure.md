# Resonant Diamond Cross-Closure

The pair-heat observability theorem leaves equal-rate midpoint spheres as the exact linear cancellation kernel. The complex Spin-Shadow law shows that cancellation by pairs with different planes creates phase dispersion. This note proves that such plane dispersion is also visible directly to the *full convolution*: two distinct resonant pair planes necessarily generate a cross-output same-spin interaction unless the original radial or angular selection factors degenerate.

## 1. Two equal-rate decompositions of one output

Fix a nonzero output wavevector `r`, put `rho=|r|`, and consider two decompositions

\[
a_+=\frac r2+x,\qquad a_-=\frac r2-x,
\]

\[
c_+=\frac r2+y,\qquad c_-=\frac r2-y,
\]

with

\[
|x|=|y|=R>0.
\]

The equality `|x|=|y|` is exactly the equal pair-heat-rate condition

\[
|a_+|^2+|a_-|^2
=|c_+|^2+|c_-|^2.
\]

Assume all four parent modes carry the same helicity `s`. Reality supplies the corresponding negative wavevectors with the same helicity magnitude, so every cross pair

\[
a_\varepsilon^s+(-c_\eta)^s,
\qquad
\varepsilon,\eta\in\{+1,-1\},
\]

is present in the full convolution whenever the four original modes are active.

Define

\[
\xi:=r\cdot x,
\qquad
\upsilon:=r\cdot y,
\]

and the plane-separation scalar

\[
\chi:=\frac{|r\cdot(x\times y)|}{|r|}.
\]

For nondegenerate pairs, `chi=0` exactly when the two pair planes `span{r,x}` and `span{r,y}` have the same projective azimuth.

## 2. Every cross pair sees the same plane-separation area

For

\[
A_\varepsilon:=\frac r2+\varepsilon x,
\qquad
C_\eta:=\frac r2+\eta y,
\]

a direct expansion gives

\[
r\cdot(A_\varepsilon\times C_\eta)
=\varepsilon\eta\,r\cdot(x\times y).
\]

Hence for every choice of signs,

\[
\boxed{
|A_\varepsilon\times C_\eta|\ge\chi.
}
\]

Thus changing the pair plane cannot be hidden by choosing a different cross corner of the resonant diamond: all four cross pairings inherit the same scalar-triple obstruction.

## 3. One cross pair must inherit radial defect

Because `|x|=|y|`,

\[
|A_\varepsilon|^2
=\frac{\rho^2}{4}+R^2+\varepsilon\xi,
\]

\[
|C_\eta|^2
=\frac{\rho^2}{4}+R^2+\eta\upsilon.
\]

Therefore

\[
|A_\varepsilon|^2-|C_\eta|^2
=\varepsilon\xi-\eta\upsilon.
\]

Choose

\[
\varepsilon=\operatorname{sgn}(\xi),
\qquad
\eta=-\operatorname{sgn}(\upsilon),
\]

with arbitrary sign when one scalar vanishes. Then

\[
\boxed{
\big||A_\varepsilon|^2-|C_\eta|^2\big|
=|\xi|+|\upsilon|.
}
\]

Consequently the radial mismatch of this cross pair is exactly

\[
\boxed{
\Delta_\times
:=\big||A_\varepsilon|-|C_\eta|\big|
=
\frac{|\xi|+|\upsilon|}
{|A_\varepsilon|+|C_\eta|}.
}
\]

This shows that two resonant decompositions cannot make all four cross pairings radially monochromatic unless both original pair radial defects vanish.

Indeed, for the original decompositions,

\[
\big||a_+|-|a_-|\big|
=\frac{2|\xi|}{|a_+|+|a_-|},
\]

and similarly for the `c` pair.

## 4. Cross-closure coefficient lower bound

Let

\[
B=A_\varepsilon-C_\eta
=\varepsilon x-\eta y
\]

be the output of the selected cross pair `A_epsilon^s+(-C_eta)^s`, and let `b=|B|`.

For the same-spin output `B^s`, the exact coefficient is

\[
|C_\times|
=
\frac1{2\sqrt2}\Delta_\times
\frac{|A_\varepsilon\times C_\eta|}
{b|A_\varepsilon||C_\eta|}
\left(|A_\varepsilon|+|C_\eta|+b\right).
\]

The triangle inequality gives

\[
|A_\varepsilon|+|C_\eta|\ge b,
\]

so

\[
\boxed{
|C_\times|
\ge
\frac{\Delta_\times}{\sqrt2}
\frac{|A_\varepsilon\times C_\eta|}
{|A_\varepsilon||C_\eta|}.
}
\]

Using the previous two sections,

\[
\boxed{
|C_\times|
\ge
\frac{(|\xi|+|\upsilon|)\chi}
{\sqrt2\,(|A_\varepsilon|+|C_\eta|)
 |A_\varepsilon||C_\eta|}.
}
\]

Since every parent radius is at most

\[
L:=\frac\rho2+R,
\]

we obtain the convenient uniform form

\[
\boxed{
|C_\times|
\ge
\frac{(|\xi|+|\upsilon|)\chi}
{2\sqrt2\,L^3}.
}
\]

This is the **Resonant Diamond Cross-Closure Lemma**.

## 5. Angular form

Write the polar angles of `x,y` relative to `r` as `theta_x,theta_y`, and their azimuthal difference around `r` as `phi`. Then

\[
|\xi|+|\upsilon|
=\rho R\left(|\cos\theta_x|+|\cos\theta_y|\right),
\]

and

\[
\chi
=R^2|\sin\theta_x\sin\theta_y\sin\phi|.
\]

Hence

\[
\boxed{
|C_\times|
\ge
\frac{\rho R^3}
{2\sqrt2(\rho/2+R)^3}
\left(|\cos\theta_x|+|\cos\theta_y|\right)
|\sin\theta_x\sin\theta_y\sin\phi|.
}
\]

The exact degeneracies are physically meaningful:

- `sin theta = 0`: an original pair is collinear;
- `cos theta = 0`: an original same-spin pair has equal parent radii and therefore zero critical radial handoff factor;
- `sin phi = 0`: the two resonant pair planes coincide projectively.

Away from these already-known Selection degeneracies, a plane-dispersed resonant cancellation family necessarily produces an order-frequency cross coupling.

## 6. Composition consequence

At the equal-rate exceptional set, the full convolution therefore admits only the following alternatives:

1. pair planes align projectively, feeding the planar-rigidity branch;
2. one of the original radial/angular selection factors degenerates;
3. an off-output cross forcing is generated quantitatively by the lemma above.

If the cross forcing in branch 3 is cancelled by further pairs, the Leakage / Composition-Defect machinery applies again at the new output `B`.

Thus the resonant sphere is not a closed hiding place. Plane dispersion forces the interaction network to **close under new cross differences** unless it collapses toward the already regular planar/degenerate geometry.

## 7. Remaining global problem

This lemma is local in one resonant diamond. A full proof still needs a quantitative iteration statement showing that repeated cross-closure cannot expand through infinitely many critical scales while all resulting outputs remain cancelled at summable cost.

The natural next object is therefore not another isolated triad estimate but the growth/rigidity of the convolution closure generated by repeated resonant diamonds.
