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
  #text("\nA Composite Model of Complex System Behaviour\n\n")
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

= Motivations

== Turing machines, master equations, Markov systems

Previous work has shown that we can connect Turing Machines, discrete numerical simulations of master equation, and Markovian systems via a simple set of connections @pang2026markoviandynamicscomputational. We briefly examine the master equation case as it is instructive:

Let $S$ be the world state, $Omega(t)$ the operator at time $t$. We can write the master equation as follows @kolmogoroff1931markovanalytischenmethodenwahrscheinlichkeitsrechnung.

$ (d S)/(d t) = Omega(t) S "(Kolmogorov forward equation)" $

Using $I$ as the identity matrix:
$  S_(t+1) = alpha (Omega(t)+I) S_t "(Euler's method approximation of master equation)" $

$ hat(Omega)(t) := alpha (Omega(t)+I) S $
$ S_(t+1) = hat(Omega)(t) S_t "(Simplified Markovian model of master eqution)" $

For a Turing machine with a finite tape length (an LBA) the state $S_t$ contains information about the tape state, the location of the head, and the tape of the machine. The operator $Omega(t)$ implements the state transition and read-write rules.

== Time symmetry
We now correct some confusions in our previous work. It is known that physics systems e.g. thermodynamics obey detailed balance. However, for discrete simulations and Turing machines, reversibility is not guaranteed. Furthermore, identity operations for each element are not guaranteed either (identities or fixpoints in LBAs are halting states). Therefore this structure is best described as a semigroup rather than a group #footnote[It may also be possible to map these systems in more detail to a transformation semigroup.]. Time symmetry for our simulations should be taken as the claim that $Omega(a) = Omega(b) forall a, b in NN$. This is true e.g. for Turing machines, and enables the definition of conserved quantities (e.g. information) #footnote[A useful analogy is between Roger's fixed point theorem and Brouwer's fixed point theorem.].

== Sufficient for description but insufficient for prediction
We now have a descriptive model which captures the behaviour of such systems over time. Yet it is difficult to make predictions or gain understanding about the underlying systems using this model. This is because all of the dynamics of the model are concentrated in the operator $Omega$, which _in extremis_ becomes a lookup table from state to state, telling us exactly nothing about what principles guide these evolutions.

Moreover, reconstructing the operator from observation is a very hard problem: With LBAs where we have total access to the machine we know the specifics of $Omega$ beforehand, but from observation of programs one can easily infer incorrect or only partial dynamics. If you are looking at the operation of a list sorted program, you may be fooled into thinking that a computer is a machine for sorting lists of numbers #footnote[In fact, a program can in fact be said to be a structure that defines a local operator/"laws of physics" for data]. When observing physical systems this is even more difficult, and is related to the problem of induction @henderson2024probleminduction. Therefore, specifying more of our proposed operator's actual mechanics is desirable.

= The Turing-Ising Model

== Construction of the model
We propose a more detailed model to capture more interesting aspects of the systems we observe, drawing from models in complex systems theory. We conceive of these systems as being nonequilibrium thermodynamic systems governed by time symmetric rules receiving free energy from an external source @england2015dissipativeadaptationdriven. Therefore, we begin with the Ising Hamiltonian where some of the lattice sites are subject to an external drive @ising1925contributiontheoryferromagnetism.

$ H(sigma) = sum_(<i, j>) J_(i j) sigma_i sigma_j - mu sum_j h_j sigma j $

We relax this formulation in several ways: first, we connect the state vector $sigma$ to our world state vector $S$, and therefore the entries are no longer required to be either $-1$ or $1$. Next we specify that all lattice sites can interact with each other instead of having a set of pre-specified "adjacent" lattice sites. To recover the original formulation, non-adjacent or non-connected sites simply have an interaction of $0$. Now we can see that the first term is a sum over the rows of $J compose sigma sigma^T$ where $sigma sigma^T$ is the outer product of the state vector with itself and $compose$ is the Hadamard product. We further note that the inhibition-activation dynamics of the Ising model where sites either drive other sites to "flip" or align them with themselves resembles the inhibitor-activator dynamics of Turing patterns @turing1952chemicalbasismorphogenesis, only with the system regulating itself rather than having an activator and an inhibitor substance.

The Turing pattern model also has something the Ising model lacks, which is the idea of some intrinsic flow or direction which guides the evolution of the system. Therefore we finish the model with the diffusion term $nabla^2 sigma$, parameterised by a Hessian matrix.

// We connect these models via the inner product rather than the addition of sums to reflect the fact that the system is performing the reification of emergent dynamics, and so each part is indivisibly coupled rather than additive to each other.

We call this joint model the Turing-Ising model, substituting $S$ for $sigma$ and $Omega$ for $H$:

$ U = h S "(drift)" $
$ Sigma = J compose S S^T "(self-interaction)" $
$ V = nabla^2 S "(diffusion)" $
$ (d S)/(d t) = Omega(t)(S) = U +Sigma+ V "(Turing-Ising model)" $

This is then approximated as before using Euler's method into $hat(Omega)(t)(S)$. If we have the previously defined weak time symmetry condition this is just the approximation of the operator $hat(Omega)(S)$ which is consistent over time.

== Interpretation of the model
The connection between emergence of higher order organisation and causal dynamics in a dynamic physical system that interacts with and partially conditions itself is a well studied question @gacs1994boltzmannentropy @schrodinger1992whatlife @hoel2025causalemergence20quantifying @england2015dissipativeadaptationdriven @kachman2017selforganisedresonance @klein2021evolutionemergencehigher @aaronson2014quantifyingrisefallcomplexity. We map _drift_ to the incorporation of external data/energy/disturbance into a system, _self-interaction_ with the system's self regulation or dissipative process @prigogine1978timestructurefluctuations, and _diffusion_ with the relaxation or correction of the system back to its "original course" #footnote[See the concept of _telos_ in biology used by Michael Levin @levin2025nothingbiologyteleology]. These can be loosely analogised to variation, selection, and replication in evolutionary dynamics. The switch from an inhibitor-activator model with two substances as posited by Turing to a self-regulating model with a single substance can be mapped to the dissolution of the boundaries between code and data in a computer or structural atoms and energy-carriers atoms in a physical system. Again, see prior work @pang2026markoviandynamicscomputational.

We also note that there is now a triad of dynamics: drift and diffusion (Fokker-planck), self-interaction and diffusion (Turing pattern), self-interaction and drift (Ising). In the Fokker-Planck case the diffusion term uses a stochastic Ito or Wiener process, in the Turing pattern case it is governed by a function relating the state of the system to the "change in flow rate" at some coordinate.

#bibliography("new.bib")