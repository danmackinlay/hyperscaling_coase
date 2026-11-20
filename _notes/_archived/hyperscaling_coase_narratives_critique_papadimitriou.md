*This is a simulated reading by an AI critic in the manner of Christos Papadimitriou, not the words of the person.*

# A reading of "Coasean street stories"

Dear Dan,

I read Krier first and then your ten sketches, and I came to them with one question, the one I bring to any argument that cheap cognition will dissolve an economic problem: which of these problems are computational at all? Krier's premise is that transaction costs are mostly cognitive and logistical, so inference at a penny a call drives them toward zero. Your counter-premise, stated in the model summary, is that "more computation" buys one side speed, estimation, commitment and adaptation, and so helps whoever already holds the advantage. I think your stories are mostly right about the world and mostly careless about the word. In nearly every sketch the resource doing the work is information, an incentive constraint, a property right or a protocol, and in only two or three is it computation in the sense my field would recognise. That is not a defect in the argument; it is the argument, and you should say so plainly. A problem that is hard because of what people will truthfully report, or who speaks first, stays hard when inference is free. Krier's error is to treat all transaction costs as the kind that Moore's law erodes. Yours is to keep calling the other kinds "computation".

## 1. The honeymoon

This is a good story, and the curve it describes is familiar. A seller learning a buyer's valuation from repeated refusals leaves a margin early and closes it later; Kleinberg and Leighton (2003) priced exactly this in the posted-price setting, and Bergemann, Brooks and Morris (2015) map how much consumer surplus can be extracted as the seller's information about buyers grows. Your "estimation budget" is a sample budget, and "an agent that can only say yes or no has nothing to compute" should read "has nothing to estimate that would change its answer". The responder in an ultimatum game is not computation-starved; the protocol has given it a single bit.

Two observations for fairness to Krier. First, his own leading example has the residents' agents broadcast a price that the truck accepts or routes around, so in his picture the households are the proposers. The consultation in your story inverts his protocol, which is a legitimate move (who writes the protocol is your real subject) but you should say you are inverting it. Second, your remedy, a lottery over who makes the final offer, is a correlation device. Krier explicitly invokes correlated equilibrium, conditioning on "shared signals". Correlated equilibria, unlike Nash equilibria, can be computed in polynomial time even in succinct many-player games (Papadimitriou and Roughgarden, 2008), whereas finding a Nash equilibrium is PPAD-complete (Daskalakis, Goldberg and Papadimitriou, 2009). So Krier chose the computationally friendly solution concept, and your lottery is an instance of it; random recognition is also the backbone of Baron and Ferejohn (1989). The point that survives is the one you make last: the device is a rule, and nobody inside the bargain proposes it.

## 2. Seventy-five percent

This is divide and conquer, and it is old: Segal (1999) on contracting with externalities, and Rasmusen, Ramseyer and Wiley (1991) on naked exclusion, show a principal buying a decisive coalition cheaply when each signer imposes a cost on the non-signers. Your claim that no division of the pact's proceeds keeps every member in is a claim that a cooperative game has an empty core. Here my field has something to add that strengthens you: deciding whether the core of a general game is non-empty, or whether a proposed division lies in it, is computationally hard for natural succinct representations (Deng and Papadimitriou, 1994). Krier's "flash coalitions" that form "in a nanosecond" assume a stable coalition exists and can be found; sometimes neither holds. The story is credible and the precondition follows. None of the failure needs computation, as your own model notes, so do not count this one as a computation story.

## 3. The form that cannot say "but not both"

This is the strongest sketch from my standpoint, because it is the one about representation, and representation is where complexity lives. "Morning or evening, not both" is a complementarity, and complementarities are what break the gross-substitutes condition under which ascending prices find efficient allocations (Kelso and Crawford, 1982). Your doubling table is the communication lower bound of Nisan and Segal (2006): for general valuations, any protocol that finds an efficient allocation must in the worst case exchange a number of bits exponential in the number of items. That bound holds however fast the agents think. An hourly day is not out of reach because inference is expensive; it is out of reach because the message is too long and because a person cannot be queried that many times. Preference elicitation as query learning (Blum, Jackson, Sandholm and Zinkevich, 2004) is the literature to cite.

Two cautions. "More computation means fewer deals" is the wrong lesson: the company is estimating a misspecified model more precisely, which is a statistics failure, not a cost of thought. And the paragraph conceding that agents searching 128 combinations find the double glazing is the fairest passage in the set to Krier. Search over joint remedies is exactly what cheap cognition does well, until the space grows exponentially, so keep it.

## 4. Everybody's child has asthma

This is Myerson and Satterthwaite (1983) and its relatives, retold with care: efficient, incentive-compatible, individually rational mechanisms must pay information rents, and the rents go to whoever's type is cheapest to mimic. The story is credible and the bargaining-club analysis, a uniform price transferring to whoever minds least, is a nice concrete demonstration. Krier invoked mechanism design for the club and should be held to its theorems. But nothing here is computational. A perfect, instantaneous agent cannot reveal a private type that its principal benefits from hiding. That is the strongest possible rebuttal of Krier's premise, and you should state it as such rather than leave it implicit.

## 5. Two towns, one depot

The outside-option principle (Binmore, Rubinstein and Wolinsky, 1986) and the tax-competition literature already say this. The bidding war is credible, the precondition follows, and the HQ2 and Foxconn examples land. As a contribution it is the least new of the ten, and it says nothing about agents except that they run the race faster. That is a fair point against Krier but a short one.

## 6. The boundary road

The mechanism is right, but I would retell it in my own terms. Each street's bargain can be locally efficient while the composition of all of them is not, which is the price of anarchy (Koutsoupias and Papadimitriou, 1999). For traffic specifically, Roughgarden and Tardos (2002) bound how much selfish routing costs relative to the optimum, and Braess's paradox shows local improvements can make the network worse. Your sketch is about a coalition excluding a neighbour; the stronger and more computational version is that a million locally Coasean bargains, each correct, need not add up to anything good, and nobody's agent sees the network. As written the precondition, a court and a rule of who counts, follows.

## 7. Branch stacking

This is the second strongest, and the most specifically about cheap agents. It is the Sybil attack (Douceur, 2002), and in mechanism design the false-name bids of Yokoo, Sakurai and Matsubara (2004), who showed that VCG is not robust to one bidder posing as several. What makes it a computation story is that the attack's cost is the cost of an agent: as inference gets cheaper, identities get cheaper, and a rule counting agents is undone by the very price fall Krier celebrates. Your model's line that "the side with cheaper agents wins" deserves to be in the sketch. The precondition, identity administered from outside, follows directly.

## 8. On commission

A plain principal-agent story with good evidence (Levitt and Syverson, 2008, are correctly described). It is credible and fair to Krier, whose switching-cost argument assumes a client can observe what the agent could have got. The non-computational core is that outcomes are unobservable to the client; auditing across clients is a statistical remedy that does need scale, which is a small point in Krier's favour that you could grant.

## 9. Repeat players

Strong, and better than its citation suggests. Galanter is apt, but the formal kernel is Selten's chain-store paradox (1978) and its resolution by reputation under incomplete information (Kreps and Wilson, 1982): a long-lived player facing many short-lived ones can sustain a commitment that no single encounter would justify. Cheap memory and public records make that reputation cheaper to build, so here more capacity does favour one side. The scoring and tying paragraphs are each a different mechanism and should be separated; together they read as a list.

## 10. The poor street

Morally the most serious and analytically the least about agents. Wealth effects, the Summers memo and the dependence of efficiency on initial endowments are all conceded by Krier in his poor-farmer paragraph, so the sketch mostly holds him to what he said. It is fair, and the observation that he routes these choices to institutions he calls captured is pointed. But "no agent capability touches any of this" is the whole verdict, and it can be one paragraph of the essay rather than a sketch.

## Overall

The strongest sketches from my standpoint are 3, 7 and 9: representation, identity and memory are the places where the cost of computation, communication or storage actually changes who wins. The weakest as contributions are 5 and 10, which are true but restate known critiques of Coase that Krier partly concedes. Sketches 2 and 4 are strong as arguments but should be relabelled as information and incentive results, which no amount of inference touches.

The story I miss is about dynamics. Krier promises "continuous self-calibration", governance as a thermostat, with millions of agents repricing in real time. Nobody in the sketches asks whether that process converges. Hart and Mas-Colell (2003) show that uncoupled adaptive dynamics cannot in general be guaranteed to reach Nash equilibrium, and the hardness results say we should not expect efficient algorithms to find one either. The agents may cycle, oscillate or settle somewhere bad. In the other direction, Calvano and coauthors (2020) found that simple reinforcement-learning pricing agents learn to sustain supracompetitive prices without communicating, which is the delivery companies' counterpart to Krier's "digital union". A sketch in which three logistics firms' agents, never conferring, settle on the same low payments to every street would be the one story in which cheap computation itself manufactures the harm, and it would answer Krier on his own ground.

Does the set convince? It convinces me that Krier's preconditions are fragile, and fragile for reasons he names but underweights. It does not yet convince me that computation is the axis along which they fail, and I think the honest version of the essay is the stronger one: most of what blocks good Coasean outcomes is information, incentives and agenda power, which cheap inference leaves untouched, and in the few places where computation does matter, it tends to favour the party that already speaks first and remembers most.

## Three changes I would ask for

Replace "computation" throughout with the specific resource each story turns on (samples, message length, memory, commitment, or none), and reserve the word for sketches 3, 7 and 9 and any dynamics story you add. Name the known results each sketch re-derives (Myerson–Satterthwaite, divide and conquer, the chain-store paradox, the Sybil attack, the outside-option principle) so the reader can see what is new, which is their joint application to an agent economy rather than any one of them. Add a sketch on convergence or tacit algorithmic collusion, and in sketch 1 acknowledge that Krier's own protocol has residents post prices and that your lottery is the correlation device he asked for.

Yours,
C.
