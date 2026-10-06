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
  #text("\nAgent Model Retry\n\n")
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

== Agent Overview
== Definitions
Agent - dynamical system, self regulating to a fixpoint, relaxed setting of a conservation law

Survival - Execute repeated potential energy conversions (bets that investments of energy now will result in energy later, e.g. if ATP synthesis had a 50% success rate) to sustain itself

Goals - High energy states that it is trying to steer environment towards

Planning/steering - Using computation to convert loss/error/state signals into policy (always necessarily approximate), computation and correction both consume energy because they resist entropy + using computation to plot out bets to take