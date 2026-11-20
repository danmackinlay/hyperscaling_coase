*A test by an AI critic; sources and reading depth are listed at the end.*

# Testing the forecasting thesis

## Verdict

The thesis fails as stated: two of its three premises do not do the work asked of them, the claim that ignorance goes sooner for the stronger side is assumed and not shown, and both halves of its last sentence are false.

A narrower statement survives, and I would defend it:

> When one side makes the offers and chooses which deals are put up for repricing, what the other side keeps above the least it would accept depends on the offer-maker being unable to predict its answer. A personal agent that represents a household faithfully, and settles many small recorded deals for it, makes that answer predictable. If the household's agent is as capable as the company's, it defends the household by refusing deals, and trades are lost; if it is less capable, the household is paid close to its minimum. A price that is the same for every household and is set from aggregate data depends on nobody's ignorance. It gives up Krier's pricing of each person by their own circumstances, though not frequent updating.

I am least sure of three things.
The evidence that an agent's conduct reveals its principal comes from written profiles, not people, and simulations of real people are still poor.
Nothing I read settles whether the company or the household's agent provider would hold more data.
My reading of how one impossibility theorem applies to the street (test 1) is my own reasoning.

## 1. Does each sentence follow from a result?

**Fair choice of rules.**
The first sentence follows from Buchanan and Tullock and from Aghion, Alesina and Trebbi's model, both read for the contracts note and not reopened here: choosers who cannot tell their future position agree on a rule, and choosers who can tell choose rules that suit themselves.
The dependence is real as a sufficient condition.
It is not a necessary one (test 5b).

**The weaker bargainer's share.**
The second sentence follows from a result only when one side makes a take-it-or-leave-it offer, meaning a single offer that the other side can only accept or refuse.
A proposer who knows the least the other side would accept then offers just that, and the other side's margin above its minimum comes entirely from the proposer's uncertainty.
When the sides alternate offers with everything known, the split depends on their patience and on what each gets if talks fail (Rubinstein's model, from memory), and nobody's ignorance is involved.
So the sentence holds conditionally on who proposes, which on the street is a rule still to be chosen.
It also concerns the margin only: a household that can refuse is never pushed below its minimum, whatever the other side knows.

**Honest reporting.**
Here the thesis leans on a theorem that says something else.
I opened Jehiel, Meyer-ter-Vehn, Moldovanu and Zame.
Values are *interdependent* when one party's valuation depends on information another party holds, and the authors' own roadway example counts a firm's valuation as interdependent when its estimate would be improved by seeing another firm's estimate.
A company agent that predicts Carol's harm better than Carol does therefore puts the street in their case.
Their Theorem 4.2 says that with two parties, each holding information of at least two dimensions, and all but exceptional valuations, the only non-random rules that are truthful *ex post* (honest reporting stays best whatever the others turn out to know) are rules that ignore the reports.
That concerns rules that try to use everybody's information and leave nobody with regrets.
It does not say that honest reporting stops being Carol's best policy under an ordinary truthful rule, meaning one where honesty is best whatever the others report.
If the rule ignores what the company knows about Carol, her honest report of her own estimate is still her best reply.
The company's better knowledge of the truth earns it nothing, because under a rule based on consent what the company pays depends on Carol's answer and not on her true harm.
I checked this with a small simulation: ten candidate slots, with Carol's estimate of each off by an error as large as the variation in harm.
A company that chooses which slot to propose from an accurate estimate of Carol's true harm leaves her no worse off on average.
A company that chooses from an accurate prediction of her answer costs her about one unit on a mean harm of five.
What hurts Carol is her own error, joined to the company's ability to predict her answer and to choose what is put to her.
That is the second kind of ignorance again.
Knowledge of the truth matters by itself only where the knower's own payoff depends on the truth, as for an insurer paying claims or a company held liable for measured harm.
The step from the theorem to a street where only Carol's valuation is interdependent is my reasoning and is not in the paper.

**The expected-externality mechanism.**
The mechanism note's memory is correct.
In d'Aspremont and Gérard-Varet's Theorem 6 each party's payment is an average, taken over that party's beliefs about the others' types, of the effect of its report on the others.
Honest reporting is a best reply only if the others are honest and the beliefs are the ones the rule was built on; the authors call the independence condition very restrictive and note that it makes every party's beliefs known.
A party that learns more than those beliefs about the others can gain by misreporting, so modelling the others pays again.
The contracts note's route around the bargaining impossibility therefore does not remove the advantage of the better modeller.

## 2. Is the ignorance actually there to be removed?

Mostly it is not.
On a street of three houses the positions that matter are known without forecasting: the company knows it is the party that wants slots, Carol knows she is the light sleeper, and each neighbour knows which side of any consent rule they are on.
Krier does not assume otherwise: he leaves starting entitlements (who begins with which right) to existing law and democratic politics, and never appeals to a veil, the condition of choosing rules without knowing one's own position.
Forecasting could change two things.
For rules meant to last years, it could tell each household whether it will later be the one working nights, nursing a newborn or depending on deliveries; test 4 finds no evidence that this can be done.
For rules covering thousands of households, agents can compute how a complicated rule falls on each household today, which most residents do not now trouble to work out.
That is a real change where Krier's agents would vote continuously on entitlements, but it reaches every household at once and so belongs under test 3.
For the street's own rules, forecasting changes little.

## 3. Symmetric versus unequal forecasting

Equal forecasting does not produce capture.
For rule choice it moves the parties from agreement in ignorance to bargaining with known positions, where the contracts note's sources predict delay and vetoes, and sometimes easier agreement (test 5c).
For bargaining under the rules, a capable household agent anticipates that whatever it reveals will be used later.
The standard result is the ratchet effect: when a proposer cannot commit not to use what it learns, the other side hides what it would accept and good deals go unmade (Laffont and Tirole, abstract snippet only).
Brunnermeier, Lamba and Segura-Rodriguez find the same division for an insurer that knows more than its customer.
A customer who draws the correct inference from the offer cannot be misled, and the insurer's profit rises substantially when the customer fails to draw it.
So the equal case gives refused trades and the unequal case gives low prices.
The thesis lives in the unequal case and does not show that it arises.
Krier's answer, in the essay and in a later talk, is that computation becomes cheap and has diminishing returns in everyday disputes.
A reply would have to be that data, not computation, is unequal, since the company sits on one side of thousands of streets.
But the household's agent comes from a provider that also sees thousands of streets.
No source here settles which side knows more.

## 4. Evidence that agents can do this

**(a) An individual's valuations.**
Not at present for real people.
Park and co-authors' simulations, built from two-hour interviews and surveys, reproduce 72.8 per cent of a person's survey answers against the person's own two-week consistency of 79.5 per cent; the current abstract says the interviews did not improve prediction of incentivized economic choices.
A pre-registered study of 19 experiments finds that such simulations correlate about 0.2 with their person's answers and predict exact individual responses no better than demographic stereotypes do (Peng and co-authors).
Youyou, Kosinski and Stillwell show a model beating friends at judging personality (0.56 against 0.49, abstract snippet), with the person's self-rating as the yardstick, so the study cannot show a machine knowing someone better than they know themselves.
The one strong result runs through delegation.
Alavi and Nozari give a buyer agent a verbal description of its principal (the person it acts for), and a seller model recovers the principal's willingness to pay from the dialogue almost one-for-one (slope 1.00), against 0.21 when the agent holds only a number it is told to keep confidential.
Their principals are written profiles.
On harm, Weinstein's panel found no adaptation to a new highway's noise after 16 months and growing pessimism about adapting (abstract only), so pooled data from many streets could plausibly beat a household's forecast of how it will cope.
That is knowledge of consequences, which test 1 shows is the less dangerous kind.

**(b) A named household's position years ahead.**
No.
In the Fragile Families Challenge, 160 submissions using thousands of variables per family predicted six outcomes six years on; the best explained about 20 per cent of the variation in two and 5 per cent in the rest, barely ahead of a four-variable regression (Salganik and co-authors).
Language models are reported near parity with expert forecasters on short-dated public questions (Forecasting Research Institute; disputed in a snippet by the forecasters' firm), which says nothing about households.

## 5. The strongest objections

**(a) Vermeule.**
General, durable and delayed rules keep choosers ignorant of how a rule will fall on them, so long as the distant future is hard to predict, and test 4(b) says it is.
The objection stands and removes the first kind of ignorance from the thesis for any rule meant to last.
It costs Krier little, since he accepts that some rules should be left fixed.

**(b) Segal and Whinston; Cramton, Gibbons and Klemperer.**
With the starting entitlement set at the outcome that is efficient on average, voluntary and efficient bargaining is possible with positions known.
The objection stands.
It also shows what ignorance was protecting: under an entitlement the household's minimum is safe with full information, and only its share of the gains is at stake.

**(c) Fernandez and Rodrik.**
When individuals cannot tell whether a reform will favour them, a majority can block a reform most would have welcomed afterwards, so forecasting can help.
The objection stands; the thesis counts one sign of the effect.

**(d) Aghion and Bolton.**
With complete contracts and cheap compensation, unanimity is the best consent rule, and under unanimity each neighbour holds a veto that needs no ignorance.
This is Krier's direction.
Its cost is the holdout, one party refusing in order to extract more, which Snow has pressed.

**(e) The weaker side's agent.**
It can withhold, randomize or commit.
Withholding by instruction fails in Alavi and Nozari's experiment, but an agent holding only a number leaks little, so the defence lies in how the agent is built and is paid for in personalization.
Commitment is stronger.
Over 9,840 negotiations between language models, Liang and co-authors find that the patience written into the prompt accounts for 90 per cent of the explained variance in how the gains are divided (abstract only).
An agent told to hold out for six is not moved by the other side knowing it would take three.
What remains for the thesis is the case where the company can out-commit the household because it deals with many streets, which is this project's earlier finding about commitment, with inference telling the company where to set its final offer.

**(f) The last sentence.**
Both halves are false.
Competition among companies for the same slots, the household's own commitment, and Krier's residents' club making a single offer all protect a household without anyone's ignorance.
And a posted price, one announced in advance for each party to take or leave, can be repriced continually: if it is the same for everyone and computed from aggregate conditions, one household's answers barely move it, and in large markets honesty then costs almost nothing (Azevedo and Budish, abstract snippet only).
Krier's cut-through fee and peak electricity rate are prices of this kind.
What a uniform price gives up is pricing each person by their own circumstances.
On a street of three, where each answer does move the price, it gives up more.

## 6. Novelty

Each part is in print.
That knowledge of individual risk tears the veil behind social insurance is Rosanvallon's thesis from the 1990s (second-hand, through Fenger's abstract); MacAskill and Moorhouse, Mahoney, and O'Keefe (through the contracts note) apply the veil to AI but have events, not forecasts, revealing the winners.
My searches, like the contracts note's, found nobody applying it to personal agents and everyday rules, and tests 2 and 4 say why that application is weak.
The second sentence is Snow's, and the economics of personalized pricing before him.
The corrected third sentence is Brunnermeier and co-authors' "inverse selection".
That only rules whose reports do not interact, such as posted prices, remove the motive to study the other side is Gleyze and Pernoud.
That delegation itself leaks the principal's valuation is Alavi and Nozari, for shopping.
The essay's own contribution would be the application to Krier: his granularity and the household's margin trade against each other, equal agents turn the loss into refused trades, and the remedy that needs nobody's ignorance costs granularity and not speed.
The street's numbers would be new; the mechanism would not.

## 7. Is it specific to delegated agents?

Mostly not.
Firms already price from tracked behaviour (Shiller reports a profit gain near 13 per cent from browsing data, abstract snippet), and insurers already know more than their customers.
Delegation adds three things.
The agent's own conduct becomes a source: it must carry a description of its principal to act for her, and the description shows in what it says.
Krier's public, auditable micro-deals multiply the observations.
And the weaker side gains a defender able to draw the correct inference from every offer, which is why the equal case ends in refusals.

## 8. One example

Over a year the company's agent watches Carol's agent settle forty small recorded deals: a skip permit, a neighbour's party, a parcel locker.
It then offers her £3.10 for the Tuesday 4 a.m. slot, ten pence above the least she would take, and offers Alice £6 for the same noise, because Alice's agent was given one number and no description of her.
Under a street price of £5 a slot, the same for all three and reset each month from the borough's noise figures, Carol is paid £5 and the Thursday slot, worth £4 to the company, does not run.
A reader would have to be shown three things: that the prediction can be made from the record for a real person; why the company's offer is final while Carol's agent cannot simply demand £6; and that the lost Thursday slot is the price of the remedy.
Without the second the scene only asserts.

## 9. Cheapest test

The simulation in test 1 took forty lines and falsified the third sentence as worded.
For the narrowed statement the cheapest test is an experiment of Alavi and Nozari's size, a few hundred negotiations.
Three household agents are given either a verbal profile or only a number; the company agent is or is not shown the record of earlier deals; the rule is either company offers or one uniform price.
The measures are each household's payment above its stated minimum and the number of slots that run.
The statement is falsified if the margin does not fall when the company sees the record, if an equally capable household agent keeps its margin without losing trades, or if the uniform price loses more in slots than the households gain.

## Sources and how I read them

Read in full: Krier's essay (local copy); the three commissioned notes; the prior-critiques file. Sources cited "through the notes" were not reopened: Buchanan and Tullock; Aghion, Alesina and Trebbi; Aghion and Bolton; Segal and Whinston; Cramton, Gibbons and Klemperer; Fernandez and Rodrik; Vermeule; Gleyze and Pernoud; Zhu et al.

- Alavi, Nozari (2026), "When Agents Shop for You: Role Coherence in AI-Mediated Markets". https://arxiv.org/abs/2604.26220 — abstract and introduction; results numbers by text search, not page by page.
- Azevedo, Budish (2019), "Strategy-proofness in the Large", *REStud*. https://ericbudish.org/files/strategyproofness_large.pdf — abstract snippet only.
- Brunnermeier, Lamba, Segura-Rodriguez, "Inverse Selection", *AER: Insights*, forthcoming. https://www.aeaweb.org/articles?id=10.1257/aeri.20250418 — abstract, plus passages of the 2021 working paper, https://markus.scholar.princeton.edu/sites/g/files/toruqf2651/files/inverse_selection_bls_30dec2021.pdf.
- d'Aspremont, Gérard-Varet (1979), "Incentives and Incomplete Information", *J. Public Economics*. https://www.di.ens.fr/~aspremon/Claude/PDFs/dAsp79c.pdf — abstract, Theorems 5 and 6 with proofs, conclusion, through a machine extraction.
- Fenger (2011), "Risks, Knowledge, and Social Insurances", *J. Policy Practice*. https://repub.eur.nl/pub/26340 — abstract only; my only source for Rosanvallon, *The New Social Question*, which I did not open.
- Forecasting Research Institute (2026), "AI models have likely reached parity with superforecasters on ForecastBench". https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity — results passage; Good Judgment's reply, snippet only.
- Jehiel, Meyer-ter-Vehn, Moldovanu, Zame (2006), "The Limits of Ex Post Implementation", *Econometrica*. http://www.cs.cmu.edu/~./sandholm/cs15-892F15/limits%20of%20ex%20post%20implementation.pdf — abstract, introduction, model, statement of Theorem 4.2; proofs and section 5 on exceptions not read.
- Krier, talk transcript, "Coasean Bargaining at Scale". https://post-agi.org/talks-berkeley/krier-coasean-bargaining — extracted passages.
- Laffont, Tirole (1988), "The Dynamics of Incentive Contracts", *Econometrica*. https://ideas.repec.org/a/ecm/emetrp/v56y1988i5p1153-75.html — abstract snippet only.
- Liang et al. (2026), "When LLM Agents Negotiate". https://arxiv.org/abs/2608.07538 — abstract only.
- MacAskill, Moorhouse (2025), "Preparing for the Intelligence Explosion". https://www.forethought.org/research/preparing-for-the-intelligence-explosion — veil passage.
- Mahoney, "AI's Veil of Ignorance Moment Is Here". https://nealemahoney.substack.com/p/ais-veil-of-ignorance-moment-is-here — snippet; read in full for the contracts note.
- Park et al. (2024; v4, November 2026), now titled "AI Simulations Grounded in Rich Self-Reports Increase Accuracy and Reduce Distortion". https://arxiv.org/abs/2411.10109 — abstract only; its figures differ from the 2024 version the brief remembered.
- Peng et al. (2025), "A Mega-Study of Digital Twins". https://arxiv.org/abs/2509.19088 — abstract and one results passage.
- Salganik et al. (2020), "Measuring the predictability of life outcomes with a scientific mass collaboration", *PNAS*. https://dcknox.github.io/files/FragileFamiliesTeam_MeasuringPredictabilityLifeOutcomes.pdf — results section.
- Shiller (2020), "Approximating Purchase Propensities and Reservation Prices from Broad Consumer Tracking", *International Economic Review*. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3503079 — abstract snippet only.
- Weinstein (1982), "Community noise problems: evidence against adaptation", *J. Environmental Psychology*. https://www.sciencedirect.com/science/article/abs/pii/S0272494482800418 — abstract only.
- Youyou, Kosinski, Stillwell (2015), "Computer-based personality judgments are more accurate than those made by humans", *PNAS*. https://www.pnas.org/doi/10.1073/pnas.1418680112 — abstract snippet only; the publisher blocked the page.
- From memory, not checked: Rubinstein (1982) on alternating offers; the affective-forecasting work of Gilbert, Wilson and Loewenstein, which I did not open and do not rely on.
- Opened and not relied on: Ali, Lewis and Vasserman (2023), "Voluntary Disclosure and Personalized Pricing".
- My own check: `_tmp/coase_constitution/selection_check.py`, a simulation of one household and ten candidate slots; it is an illustration of the argument in test 1 and not a published result.
