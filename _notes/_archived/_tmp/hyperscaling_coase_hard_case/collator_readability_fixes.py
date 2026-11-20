"""Readability fixes to the hard-case sections of the state, from the one cold-reader pass."""
import sys
from pathlib import Path

PATH = Path("/Users/dan/Source/livingthing/_plans/hyperscaling_coase_summary.md")
text = PATH.read_text()
edits = []
rep = lambda o, n: edits.append((o, n))

# 1 miscount in the existence paragraph (river session's phrase)
rep("Four conditions fail under any reading, symmetric or not, over five rows:",
    "Three conditions fail under any reading, symmetric or not, over five rows:")

# 2, 4, 5, 6, 7, 8, 15, 16, 20: the "After the hard case" paragraph
rep("The noise schedule (a fleet choosing among four delivery slots against three residents; parametric pie $6$, the river's; the switches of `hyperscaling_coase_hard_case_instance.md` turning the river's easy features off one at a time) narrowed all nine candidate rows rather than confirming or refuting any outright, seven with both readers agreeing, and the optimist's outcome of $1.5$ each, product $5.06$, was reached only under conditions that \"give everyone an agent\" does not supply (the hard-case table below, rows 18 to 28):",
    "The noise schedule (a fleet choosing among four delivery slots against three residents; parametric pie $6$, the river's; each switch of `hyperscaling_coase_hard_case_instance.md`, when on, removes one of the river's easy features) narrowed all nine candidate rows rather than confirming or refuting any outright, seven with both readers agreeing; they are rows 18 to 27 of the hard-case table below (the finite-budget row split into 22 and 23; the pact row carries the veil), and row 28 is a positive-sign condition the round found. The optimist's outcome of $1.5$ each, product $5.06$, was reached only under conditions that \"give everyone an agent\" does not supply:")
rep("since any fixed offer seat extracts to $(6;\\,0,0,0)$ in the limit and a seat drawn by side gives $(3;\\,1,1,1)$ (rows 22, 26);",
    "since a fixed offer seat extracts everything for its holder in the limit, $(6;\\,0,0,0)$ for the fleet and $(0;\\,2,2,2)$ for a bloc, and a seat drawn by side gives $(3;\\,1,1,1)$ (rows 22, 26);")
rep("and one human, one counted party, since a resident who splits into $m$ agents takes $6m/(m+3)$ (row 26). Two conditions came out with a positive sign,",
    "and one human, one principal, one agent (Petel's phrase, used throughout), since a resident who splits into $m$ agents takes $6m/(m+3)$ (row 26).\n\nTwo conditions came out with a positive sign,")
rep("not toward the holder of the entitlement, since at $k=3$ the fleet's estimation moves the split away from the veto holders in every arm (row 26); and in every arm the cost lands on resident 3,",
    "not toward the holder of the entitlement, since at $k=3$ the fleet's estimation under its own offer moves the split away from the veto holders (row 26); and in every arm where the split moves, the cost lands on resident 3,")
rep("which compute then sharpens. The hard-case rows go to Dan with the symmetric rows; nothing is drafted.",
    "which compute then sharpens (both optimists' returns are in `results.json`; Records). The hard-case rows go to Dan with the symmetric rows; nothing is drafted.")

# 17: roster line in the hard-case preamble; 16 wording
rep("\"Both readers\" means the row's two assessors, from different model families and blind to each other, reached the same verdict; the model family that found each result is in Records.",
    "**The round's roster**, since the cells name its parts: nine row readers, one per candidate row (bits, language, pact, enforcer, budgets, scale, wealth, incumbent, bundling), each with a second reader from the other model family who did not see the first; \"both readers\" means the two reached the same verdict. Two optimists, briefed to argue the null as hard as it goes, one on the information rows and one on the institutions rows. A model critic, barred from assessing rows, who lists what the instance cannot express (open rows). A cold reader of the assembled verdicts. The collator is this session, which verified and wrote this file. \"Optimist's advocate\" and \"criterion agent\" are the previous round's reviewers. \"The sleep term\" is the arbitrary switch's interaction term. A menu-auction agent sells its policy to the highest-bidding coalition (Bernheim and Whinston 1986). Confidence marks are the river table's: [likely] is remembered, not read. Which family found what is in Records.")

# 18 row 20 arithmetic note
rep("so under the veto the fleet-best pact holds resident 3 at exactly $0$, $(3.19;\\,1.0,2.25,0)$, product $0$;",
    "so under the veto the fleet-best pact holds resident 3 at exactly $0$, $(3.19;\\,1.0,2.25,0)$ (ex ante for the fleet, interim for the realised types, so the four need not sum to the realised pie), product $0$;")

# 11 row 21 two cores
rep("At $k=2$ without a pact the core is efficient (M, D, E; fleet $17.5$–$19$) with every resident below no deal;",
    "At $k=2$ without a pact, in the game where each resident's fallback is its harm under all four slots, the core is non-empty and efficient (M, D, E; fleet $17.5$–$19$; the residents pay the fleet not to run the night slot) with every resident below no deal;")
rep("$k=2$: fleet-plus-pair coalitions are worth $13.5$, $8.5$, $7.5$ against a grand-coalition pie of $6$ (the three pair constraints need the fleet at $17.5$ of $6$: core empty),",
    "$k=2$: in the game where fleet-plus-pair coalitions claim their worth, $13.5$, $8.5$, $7.5$ against a grand-coalition pie of $6$, the three pair constraints sum to $29.5$ against twice the pie plus the fleet's share, so they can be met only with the fleet alone holding $17.5$, above the whole pie: that core is empty,")

# 3, 10, 12 row 23
rep("The right class (two parameters) costs $\\sqrt2$ the per-parameter budget; a class-agnostic sixteen-entry table about $10\\times$, a winner's curse killing every deal at error $1$",
    "The right class (two parameters) costs $\\sqrt2$ the per-parameter budget; a class-agnostic sixteen-entry table needs about $10\\times$ the right class's budget to reach the same deal rate, a winner's curse killing every deal at error $1$ (row 18's $5.7\\times$ is a different ratio, parameter counts $17$ against $3$ at equal per-parameter error)")
rep("Gains: the side whose preferences are the complex object, protected by knowing them; the fix is the informed side reporting or proposing, an asymmetric rule",
    "Gains: the side whose preferences are the complex object, when it is the one reporting or proposing; when the other side estimates them in a scalar form (row 18) that same side loses; the fix is the informed side reporting or proposing, an asymmetric rule")
rep("narrowed; computed, found independently by six agents under three protocols agreeing on the sign (bits both, budgets both, incumbent both; also the optimist for institutions);",
    "narrowed; computed, found independently by seven agents under three protocols agreeing on the sign (bits both, budgets both, incumbent both, the optimist for institutions);")
rep("Full table at the same total budget: $4\\times10^{-6}\\to0.31\\to2.18\\to2.44$, needing $2^m-1$ parameters, $5.7\\times$ the budget at $m=4$",
    "Full table at the same total budget: $4\\times10^{-6}\\to0.31\\to2.18\\to2.44$, needing $2^m-1=15$ entries plus two scalars, $17$ parameters against $3$, so $5.7\\times$ the budget for the same per-parameter error at $m=4$")

# 10 row 25 gains; 18 units
rep("resident 3 $-0.20$ against the fleet's $+0.13$, with the equal-money split within",
    "resident 3 $-0.20$ and the fleet $+0.13$ in money relative to the equal split, with the equal-money split within")
rep("Gains: the holder of the entitlement and the seat; never the poor resident, who takes the least money under every regime |",
    "Gains: under reading (b) the holder of the entitlement, which fixes the schedule, and under both readings the holder of the seat; never the poor resident, who takes the least money under every regime (compute moves the split toward the seat, not the entitlement, row 26) |")

# 6, 13, 15 row 26
rep("So \"one human, one principal, one agent\" is needed under unanimity and symmetric protocols, and the criterion needs it too, since the product counts parties: a third blind spot for the preamble.",
    "So \"one human, one principal, one agent\" is needed under unanimity and symmetric protocols, and the criterion needs it too, since the product counts parties: the third blind spot of the product, after the preamble's two.")
rep("the offer seat, the dial, the convention, the threat point, not the entitlement; the other side's compute moves it back only when the protocol randomises the seat. Gains: the seat and dial holder; in every arm the cost lands on resident 3 |",
    "the offer seat, the dial, the convention, the threat point, not the entitlement (which fixes the origin and, under wealth effects, the schedule, row 25, without compute moving the split toward its holder); the other side's compute moves it back only when the protocol randomises the seat. Gains: the seat and dial holder; in every arm where the split moves, the cost lands on resident 3 |")

# 9, 14 row 27
rep("It is a revocation cost on acceptance, indexed to stake and to the renegotiation rule, not the commitment dial's $r$, which makes a demand stick:",
    "It is a revocation cost on acceptance, indexed to stake and to the renegotiation rule, not the commitment dial's cost of revoking a demand, which is what makes a demand stick:")
rep("Gains: the proposer (a reliable acceptance), the agent (fewer overrides), the designer of the form or club; among residents the one furthest from the margin, against the one with the unexpressed preference and the poorest |",
    "Gains, in the limit with a renegotiation friction: whoever the agreed terms favour, since the bundle locks them in; the proposer in that its acceptances stick, the agent in fewer overrides, the designer of the form or club; among residents the one furthest from the margin, against the one with the unexpressed preference and the poorest. At finite budgets the proposer prefers slots, so a bundle is imposed on it by the form, not chosen |")

# 14 open rows: M and r
rep("(A) the chain store, one fleet against $M$ successive fresh resident triples with its record public and a tough type with prior $\\mu$:",
    "(A) the chain store, one fleet against $L$ successive fresh resident triples with its record public and a tough type with prior $\\mu$:")
rep("(D) cross-bargain scoring of refusals, a penalty $r=1$ outside the bargain: the fleet offers $h_i-1+\\epsilon$",
    "(D) cross-bargain scoring of refusals, a penalty $\\rho=1$ outside the bargain: the fleet offers $h_i-1+\\epsilon$")
rep("(F) endogenous budget ratio: a party in $M$ bargains of one type has $M$ times the samples, one in $B$ bargains at once a $B$th of the budget each; the $10{:}1$ arm is $M=10$.",
    "(F) endogenous budget ratio: a party in $L$ bargains of one type has $L$ times the samples, one in $B$ bargains at once a $B$th of the budget each; the $10{:}1$ arm is $L=10$.")
# 13 open row C
rep("the no-deal origin is a strategic variable in an open system, a third blind spot of the product.",
    "the no-deal origin is a strategic variable in an open system, the fourth blind spot of the product (the third, that it counts parties, is row 26's).")
# 19
rep("The mission's \"in utility units when money has wealth effects\" clause is the one the readers flag. No session change.",
    "The mission's \"in utility units when money has wealth effects\" clause is the one the readers flag. No change by the session; the mission is Dan's.")

# 2, 4, 8, 15, 20: the answer paragraph, split and corrected
rep("**The answer the hard case adds, in one sentence:** off the river, with the switches the river lacked, more compute for bargaining agents produces a better outcome under the Nash product only where the rules already fix the symmetric limit, a veto for everyone, a seat drawn by party, personalised transfers, a language that carries every harm, verified harms, no one-sided outside option, linear money and one party per human, and it then helps everyone up to a middling budget; past that, and wherever one of those is missing, it helps the holder of the offer seat, the dial, the outside option or the form, and the cost lands on the resident who is most harmed, poorest and least standard at once; with two exceptions in the foil's favour, an agent that carries a table rather than a scalar, and an agent that searches the joint schedule-and-remediation space, both of which raise the pie for everyone. **In the terms of the existence test:** the null fails off the river on rows 21, 23, 24 and 25 under any reading, survives on rows 18, 19, 22, 26 and 27 only under the symmetry and the rules listed, and the essay's spine, the list of conditions the agenda presupposes without supplying, is now computed on two models.",
    "**The answer the hard case adds:** off the river, with the switches the river lacked, more compute for bargaining agents produces a better outcome under the Nash product only where the rules already fix the symmetric limit: a veto for everyone, a seat drawn by party, personalised transfers, a language that carries every harm, verified harms, no one-sided outside option, linear money, and one human, one principal, one agent. There it helps everyone, monotonically. Where the limit is a fixed seat, it helps the residents only up to a middling budget; past that, and wherever one of the conditions is missing, it helps the holder of the offer seat, the dial, the outside option or the form, and the cost lands on the resident who is most harmed, poorest and least standard at once. Two exceptions run in the foil's favour: an agent that carries a table rather than a scalar, and an agent that searches the joint schedule-and-remediation space, both of which raise the pie for everyone. **In the terms of the existence test:** the null fails off the river on rows 20, 21, 23 and 24 under any reading and on row 25 under the utility-loss reading; it survives on rows 18, 19, 22, 26 and 27 only under the symmetry and the rules listed; row 28 is a condition with a positive sign; and the essay's spine, the two lists (the symmetries the agenda presupposes, and the rules that repair the rows symmetry cannot), is now computed on two models.")

bad = False
for o, n in edits:
    c = text.count(o)
    if c != 1:
        print(f"ANCHOR COUNT {c}: {o[:100]!r}"); bad = True
if bad:
    sys.exit("aborting")
for o, n in edits:
    text = text.replace(o, n, 1)
PATH.write_text(text)
print(f"applied {len(edits)} fixes; {len(text)} bytes")
