#set quote(block: true)
#set math.equation(numbering: "(1)")
#set heading(numbering: "1.1.")
#show link: underline

#import "@preview/algorithmic:1.0.7"
#import algorithmic: style-algorithm, algorithm-figure
#show: style-algorithm

#set page(numbering: "1", header: [_Version: #datetime.today().display()_])
#import "@preview/diagraph:0.3.6": *

#set text(font: "Libertinus Serif")
#show heading.where(
  level: 1
): it => block(width: 100%)[
  #set align(center)
    #set text(20pt, tracking: 2pt, weight: "regular", font: "EB Garamond")
  #smallcaps("\n"+it+"\n")
]
#show heading.where(
  level: 2
): it => block(width: 100%)[
  #text(it, font: "EB Garamond")
]

#show regex("\!TBD"): set text(rgb("#0501ca"), size: 20pt, weight: "bold")

#block(width: 100%)[
  #set align(center)
    #set text(25pt, weight: "regular", tracking: -0.1pt, font: "EB Garamond")
  #text("\nA Model of Informed Choice in Dynamical Systems\n\n")
]

#set par(
  first-line-indent: 1.5em,
  justify: true,
)
#let dan(..args) = text(fill: blue, args.pos().join())

#block(width: 100%)[#set align(center)
#text[
  Chris Pang\
  _Independent_
]]

= Introduction
== Definitions
A dynamical system $X$ is defined by a phase space $Omega_X$ and an operator $F_X$. We consider the discrete time case for simplicity. Given any state $x_t in Omega_X$ which represents the state of the system at time $t$ we can obtain the next state $x_(t+1)$ via the master equation:

$ x_(t+1) = F_X (x_t) $

We consider the case where $X$ is embedded in some larger environment, which we represent as a separate dynamical system $Y$. The integrity of $X$ is determined #dan[indicated?] by a conservation rule $C(dot) = c$. If $C(F_X (x)) != c_X$, then the system is _broken_ and no longer functional. Note that it is not mandatory that $forall x in Omega_X, C(x) = c_X$. We call the subset of conservation-rule-preserving states $Omega_X^C subset Omega_X$.

We consider the sensitivity of $x_t$ to small perturbations, $epsilon$ where $epsilon$ is e.g. random noise scaled based on the norm of $x_t$ and its fluctuations. We restrict the size of the norm of $epsilon$ to be under some threshold $|epsilon| < U$, and require that if $x_t$ satisfies $C$, $x_t + epsilon$ must also satisfy $C$.

An uncoupled system $X$ is said to approach some _decision point_ when there exists some $epsilon$ where $F_X^n (x_t)$ and $F_X^n (x_t + epsilon)$ lie in distinct outcome basins $A_1, A_2 subset Omega_X^C$.

== Coupling
We assume that $X$ is exposed to the current state of the environment $y_t$ via some partial or coarse-grained view $phi(y_t)$. For a physical system, this is the local environment that is physically proximate to $X$. We assume that the environment $Y$ is of the same _kind_ as $X$, such that their state vectors have different lengths but encode similar phenomena (e.g. atomic position and momentum). Therefore the master equation is now

$ x_(t+1) = F(x_t, phi(y_t)) $

We say that an _information channel_ exists between $X$ and $Y$ if the resulting state $x_(t+1)$ does not violate the conservation law $C$ for $X$. It is possible for an information channel to be two-way between $X$ and $Y$, forming an informational (rather than energetic) coupling.

In the coupled case, the definition of a decision point allows both $x_t$ or $phi(y_t)$ to be perturbed. Let $z_t = (x_t, phi(y_t))$ s.t. $F_X (z_t) = F_X (x_t, phi(y_t))$ and the perturbation be $eta = (eta_x, eta_y), |eta_x| < U, |eta_y| < U, z_t + eta = (x_t + eta_x, phi(y_t) + eta_y)$. We also require the conservation laws to hold such that $C(x_t + eta_x) = c_X  "if" C(x_t) = c_X$ Then the decision point arises when an $eta$ can be found which leads again to two or more distinct outcome basins.

An _informed choice_ is when $X$ is at a decision point and has an information channel to $Y$ which it is _selectively sensitive_ to, such that there is some $eta_y$ which causes the outcome basin to change but there exists no $eta_x$ which could change the outcome basin.

In one reading, control over the final outcome basin is concentrated in the environment rather than the system itself. In another, the system uses information from the environment to _choose_ which basin to enter.


== Applied Examples

- *Case 1.* We are having dinner at a restaurant I have not been in before but you have. I ask you where the toilet is. Depending on your answer I am prepared to walk in many directions, and since I have no knowledge _a priori_ of where the toilet is my final trajectory is entirely dependent on the information you give me.

- *Case 2.* I am on a roller coaster while on the phone to you. Nothing you say will make me or allow me to change my trajectory.

!TBD what if I hallucinate you telling me where to go? Newton's problem. Also, check possibility of using basin entropy/fractal basin box counting https://arxiv.org/pdf/1605.02342