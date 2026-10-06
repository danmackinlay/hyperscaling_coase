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

#block(width: 100%)[#set align(center)
#text[
  Chris Pang\
  _Independent_
]]

= Introduction
== High Level Sketch
A system $X$ refers to a dynamical system with current state $x_t$, phase space $Omega_X$ and time evolution operator $F_X (dot)$:

$ x_(t+1) = F_X (x_t) $

We assume that the states  of $X$ obey some coarse-grained conservation rule $C(x) = c$ which we take to represent the conservation of energy or otherwise the integrity of the system. If the current state of the system no longer obeys this conservation rule, we say that the system has _broken_.

A system $X$ is said to be coupled to another system $Y$ if the evolution operator $F$ is dependent on the state of that system

$ x_(t+1) = F_X (x_t, y_t) $

This dependence is usually based on a coarse-grained view of $y_t$ which we call $phi(y_t)$, unless both systems have very high degrees of integration with each other. In the normal case, part of $F_X$ will depend on $phi(y_t)$, which we call $D$, and another part will not, which we call $I$. If the resulting state vector $x_(t+1)$ does not violate the coarse-grained energy conservation rule $C(x_(t+1)) = c$, we say that $y_t$ did not contribute any meaningful _energy_ to $x_(t+1)$, and there is instead a purely _informational channel_ between $X$ and $Y$.

$ x_(t+1) = F_X (x_t, phi(y_t)) $
$ F_X (x_t, phi(y_t)) = I(x_t) + D(x_t, phi(y_t)) $

$X$ is said to make an _informed choice_ if it is at a high divergence point in state space with multiple rapidly diverging trajectories possible i.e. high Lyapunov exponent, and the final trajectory of the system is largely or entirely trajectory on the signal from $Y$. In other words, a small change $epsilon$ in $y_t$ leads to a large change in $x_(t+1)$, with discrete choices implying multiple distinct basins in state space.

Importantly, $x_(t+1)$ should _not_ be equally sensitive to an equally small change in $x_t$. This _selective sensitivity_ separates a merely chaotic system (e.g. snow in an avalanche) from a system close to criticality acting on received information. Therefore:

$ |F_X^n (x_t, phi(y_t)) - F_X^n (x_t + epsilon, phi(y_t))| << |F_X^n (x_t, phi(y_t)) - F_X^n (x_t, phi(y_t) + epsilon)| $

For some small intervention $epsilon$, where $F^n$ represents $F$ applied for $n$ steps.

== Applied Examples

- *Case 1.* We are having dinner at a restaurant I have not been in before but you have. I ask you where the toilet is. Depending on your answer I am prepared to walk in many directions, and since I have no knowledge _a priori_ of where the toilet is my final trajectory is entirely dependent on the information you give me.

- *Case 2.* I am on a roller coaster while on the phone to you. Nothing you say will make me or allow me to change my trajectory.

= Analysis

== Dynamical system and decision points
A dynamical system $X$ is defined by a phase space $Omega_X$ and an operator $F_X$. We consider the discrete time case for simplicity. Given any state $x_t in Omega_X$ which represents the state of the system at time $t$ we can obtain the next state $x_(t+1)$ via the master equation:

$ x_(t+1) = F_X (x_t) $

We consider the case where $X$ is embedded in some larger environment, which we represent as a separate dynamical system $Y$. The integrity of $X$ is determined by a conservation rule $C(dot) = c$. If $C(F_X (x)) != c$, then the system is _broken_ and no longer functional. Note that it is not mandatory that $forall x in Omega_X, C(x) = c$. We call the subset of conservation-rule-preserving states in $Omega_X$ $Omega_X^C$.

We measure the sensitivity of $x_t$ to small perturbations:

$ delta(x_t, epsilon) = |F_X (x_t) - F_X (x_t+epsilon)| $

Where $epsilon$ is some small intervention e.g. random noise scaled to be some small proportion of the norm of $x_t$. We restrict the size of the norm of $epsilon$ to be under some threshold $|epsilon| < U$, and require that if $x_t$ satisfies $C$, $x_t + epsilon$ must also satisfy $C$.

//Assuming that $F$ is Lipschitz continuous with Lipschitz constant $L_F$, $delta(x)$ is upper bounded by $L_F |epsilon|$. Therefore we can also upper bound the $n$-step version of $delta$ via $L_F$:

//$ delta^n (x_t, epsilon) = |F_X^n (x_t) - F_X^n (x_t+epsilon)| <= L_F^n |epsilon| <= L_F^n |U| $

An uncoupled system $X$ is said to approach some _decision point_ when there exists some $epsilon$ where $F_X^n (x_t)$ and $F_X^n (x_t + epsilon)$ lie in distinct outcome basins $A_1, A_2 subset Omega_X^C$.

== Coupling
We assume that $X$ is exposed to the current state of the environment $y_t$ via some partial or coarse-grained view $phi(y_t)$. For a physical system, this is the local environment that is physically proximate to $X$.

//$F_X$ can now be split into the part of $F_X$ which is dependent on $y_t$, which we call $D$, and the part that does not, which we call $I$.

//$ F_X (x_t, y_t) = I(x_t) + D(x_t, y_t) $

This dependence on $Y$ is called an _information channel_ if the resulting state $x_(t+1)$ does not violate the conservation law $C$.

In the coupled case, the definition of a decision point allows both $x_t$ or $phi(y_t)$ to be perturbed. Let $z_t = (x_t, phi(y_t))$ s.t. $F_X (z_t) = F_X (x_t, phi(y_t))$ and the perturbation be $eta = (eta_x, eta_y), |eta_x| < U, |eta_y| < U, z_t + eta = (x_t + eta_x, phi(y_t) + eta_y)$. Then the decision point arises when an $eta$ can be found which leads again to two distinct outcome basins.

An _informed choice_ is when $X$ is at a decision point and has an information channel to $Y$ which it is _selectively sensitive_ to, such that there is some $eta_y$ which causes the outcome basin to change but there exists no $|eta_x| < U$ which could change the outcome basin.

In one reading, control over the final outcome basin is concentrated in the environment rather than the system itself. In another, the system uses information from the environment to _choose_ which basin to enter.

// If we linearise the relationship between $x_t$, $y_t$ and $x_(t+n)$ into a linear operator $hat(F)_X^n (x_t, y_t) approx x_(t+n)$, the magnitude of the Jacobian of $hat(F)_X^n$ derived with respect to $x_t$ and $y_t$ should mostly lie within $y_t$. Equivalently, the partial derivative of $F_X^n$ with respect to $y_t$ accounts for most of the divergence of $F_x^n$.
