const args = {}; const agent=async()=>({}); const pipeline=async()=>[]; const parallel=async()=>[]; const log=()=>{}; const phase=()=>{}; (async () => {
const meta = {
  name: 'hyperscaling-coase-hard-case',
  description: 'Test the nine candidate rows of the hyperscaling_coase state table on the noise-schedule instance: one agent per row, two optimists, a model critic, an independent second reader per row from the other model family, and a cold reader; read-only; returns deltas for the session to apply',
  phases: [
    { title: 'Rows', detail: 'nine row agents, two optimists, one model critic, in parallel' },
    { title: 'Verify', detail: 'one independent second reader per row, other model family, blind to the first' },
    { title: 'Cold read', detail: 'one reader on the assembled verdicts' },
  ],
}

const DATE = (args && args.date) || '2026-10-21'

const PREAMBLE = `You are one agent in a structured review of a model for a blog essay. You are READ-ONLY: do not edit, create or delete any file in the repository, and do not commit. Scratch computation goes in your scratchpad directory only. Your final output is data for a collating session, not prose for a person.

Read, in the repository at /Users/dan/Source/livingthing, in this order and nothing else: _plans/hyperscaling_coase_mission.md in full; the table and open rows in _plans/hyperscaling_coase_summary.md; _plans/hyperscaling_coase_hard_case_instance.md in full; and, in notebook/hyperscaling_coase.qmd, only the section headed "## Someone pollutes our hypothetical river", ignoring HTML comments. Do not open any other file under _plans/.

The question you are answering, verbatim from the mission: "Under which conditions does more computation for bargaining agents produce better outcomes, and for whom?" "Better" is inequality-sensitive, not Pareto. Compute on the instance's numbers, never on the river's, except for comparison. The instance has switches; say which switches are on in each claim you make. Report every outcome under the measures the instance lists, at finite budgets beside the limit. Mark every cited result [sure], [likely] or [unsure]; quote a primary only if you have read it, and say which. Check every number you report by enumeration (there are sixteen schedules) or by a short script.

Krier's best reply, which you must state against your own finding, is that his secondary institutions, bargaining clubs, option fees, standard forms and courts, are exactly the conditions you find missing, supplied explicitly; say whether that reply holds on the instance and what it concedes.`

const ROWS = [
  { id: 'bits', model: 'opus', title: 'Bits, not operations',
    claim: 'With arbitrary preferences over schedules, finding the efficient schedule requires communication exponential in the number of slots (Nisan and Segal), which no budget of operations buys; with parametric preferences it is one comparison per slot on public inputs. Real noise preferences are parametric enough for the second case.',
    questions: 'On the instance, compute the parametric and the arbitrary optimum and what each side must communicate to find them; state how both scale in the number of slots m; say where the binding constraint is bits and where it is operations; and judge, with evidence, whether real noise preferences are parametric enough, naming what would make them not so.' },
  { id: 'language', model: 'fable', title: 'The contract language is a rule somebody fixes',
    claim: 'The practical remedy for combinatorial preferences is a restricted clause language or standard form; whoever fixes it, by default the platform, decides whose preferences are expressible and is therefore a party to the bargain.',
    questions: 'On the instance, compute the pie and the residents\' split under a four-slot, a two-slot (day and night) and a one-slot (all or nothing) language, parametric and arbitrary; say who loses expressibility under each; say who fixes the language in Krier\'s text and in Petel\'s (the prior-critiques summary quotes them; you may not read it, so cite from the state file\'s foil section only) and what that does to the equity column.' },
  { id: 'pact', model: 'opus', title: 'The pact stage inherits the entitlement',
    claim: 'Once residents know their exposure, proposing a pact or mechanism reveals type (Myerson\'s informed principal); the mechanisms nobody can profitably propose to replace (Holmstrom and Myerson\'s durable mechanisms) are defined relative to the status quo, which is the entitlement, and can be as unequal as the status quo allows. Under a veil, before exposure is known, the expected-externality mechanism is unanimously acceptable; the veil is available for recurring small disputes with standing instructions and not for one-off large ones.',
    questions: 'Make the pact stage explicit on the instance with residents who know their sensitivities. Find the durable mechanisms relative to a no-deal status quo and relative to a liability-rule status quo (fleet may run any slot on paying a statutory amount), and report the equity of each under the instance\'s measures. Then run the veil case: residents choose a mechanism before knowing s_i, drawn from a stated prior; report who would later regret it. Say for which of Krier\'s cases the veil is available.' },
  { id: 'enforcer', model: 'fable', title: 'The enforcer regress ends outside bargaining',
    claim: 'Who chooses the enforcer is itself strategic; the regress stops only at a sovereign (Cooter\'s Hobbes theorem; Acemoglu\'s political Coase theorem) or at a self-enforcing convention of the repeated game (Hurwicz; Greif; Milgrom, North and Weingast); compute\'s role at that level is lock-in of whichever convention formed first.',
    questions: 'Remove the enforcer on the instance. At discount factors 0.5, 0.8 and 0.95, which pacts among the residents are self-enforcing against the fleet\'s best side offer, under k=3 and k=2? If a platform enforces and also fixes the clause language, who chose the platform and what does it extract? State what, if anything, bounds the regress, with sources and confidence marks.' },
  { id: 'budgets', model: 'opus', title: 'Finite budgets pay for distance from the optimum, and the bounded side pays',
    claim: 'Exploitability, the gap between a bounded strategy and its best response, is extracted by whoever can compute the best response, at a rate that shrinks with the bounded side\'s own budget; complexity-cost equilibria differ from unbounded ones; the cell-B deal-rate curve is the river instance of this.',
    questions: 'Give the fleet and the residents the instance\'s budgets at ratios 1:1, 10:1 and 1:10 and errors 1, 0.3 and 0.1. By a short script in your scratchpad, compute for the take-it-or-leave-it arm and the haggling arm who extracts what from whom as the ratio and the level change, parametric case first and the arbitrary case if feasible, including how often estimation error flips the night slot. Report, for every row of the state table you can, the finite-budget effect beside the limit and say where their signs differ.' },
  { id: 'scale', model: 'fable', title: 'Scale worsens the incentive problem where the veil is thinnest; outside options favour whoever holds them',
    claim: 'Mailath and Postlewaite: voluntary efficient provision becomes vanishingly likely as residents multiply, independent of compute. Outside options in realistic cases discipline holdout and favour the side that holds them.',
    questions: 'On the instance, turn on the fleet\'s reroute option at 3 per slot and recompute each arm\'s split and efficiency; then scale the residents from three to thirty and three hundred by replicating the three profiles, and state what happens to the probability of an efficient deal under voluntary participation with private sensitivities, with the result named and marked. Say whom each change favours.' },
  { id: 'wealth', model: 'opus', title: 'Wealth effects couple efficiency to distribution',
    claim: 'With concave utility of money and unequal endowments, the efficient schedule depends on who pays; Coase invariance fails (Petel\'s poor farmer; the essay\'s own aside); the welfare criterion stops being a placeholder.',
    questions: 'Turn on log utility with the instance\'s endowments. Recompute the efficient schedule under each entitlement (residents hold the right; fleet holds the right; liability rule) and report, under the worst-off and the Nash-product measures, who gains and loses relative to the linear case. Say whether more compute for either side changes any of this.' },
  { id: 'incumbent', model: 'fable', title: 'The incumbent reading',
    claim: 'In every row where compute moves the split, it moves it toward whoever already holds the entitlement, the single principal\'s seat, the better agent, the first convention, or the rigid stance. One human, one principal, one agent is a precondition, since a side can otherwise be inflated.',
    questions: 'Test the reading on the instance under k=3 and k=2 and under each switch you can run: for each arm, say which party is the incumbent in each of the five senses, whether more compute for that party moves the split toward it, and whether more compute for the other party moves it back. Test the Sybil case: resident 2 splits into three agents with a third of the exposure each. Report any arm where the reading fails.' },
  { id: 'bundling', model: 'opus', title: 'Bundling of deals is an agent-side commitment device',
    claim: 'When an agent packages many deals into one bundle, the cost of reopening the bundle is a revocation cost the principal did not choose (Snow\'s bike lane: overriding one item costs the renegotiation of all); bundling therefore commits the principal.',
    questions: 'On the instance, compare a slot-by-slot bargain with a single bundled take-it-or-leave-it schedule, parametric and arbitrary. Compute the cost to a resident of reopening one slot once the bundle is agreed, and whether that cost functions as the model\'s revocation cost r. Say who chooses the bundling and whom it favours.' },
]

const OPTIMISTS = [
  { id: 'optimist-information', model: 'fable', rows: 'bits, language, scale, wealth, bundling',
    brief: 'Make the strongest case that the null holds on the instance for the rows named: that with capable agents on both sides and no added rule, play converges to a just schedule and split under a criterion stronger than Pareto. Use every result that points that way and every one of Krier\'s secondary institutions, treated as supplied. For each row, say what it would have to become if you are right.' },
  { id: 'optimist-institutions', model: 'fable', rows: 'pact, enforcer, budgets, incumbent',
    brief: 'Make the strongest case that the null holds on the instance for the rows named: that the pact stage, the enforcer and finite budgets do not prevent convergence to a just outcome once capable agents exist, using repeated play, program equilibrium, conventions and Krier\'s secondary institutions treated as supplied. For each row, say what it would have to become if you are right.' },
]

const ROW_SCHEMA = {
  type: 'object',
  properties: {
    row: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'narrowed', 'refuted', 'open'] },
    status: { type: 'string', enum: ['theorem', 'computed', 'argued', 'empirical', 'open', 'refuted'] },
    answer: { type: 'string', description: 'Your answer to the mission question on the instance, two to five sentences' },
    working: { type: 'string', description: 'The computation and argument, with every number and the switches on' },
    narrowing: { type: 'string' },
    finite_budget: { type: 'string', description: 'The effect at finite budgets, beside the limit' },
    limit: { type: 'string' },
    instance_features_used: { type: 'array', items: { type: 'string' } },
    krier_reply: { type: 'string' },
    sources: { type: 'array', items: { type: 'object', properties: { cite: { type: 'string' }, confidence: { type: 'string', enum: ['sure', 'likely', 'unsure'] }, read: { type: 'boolean' } }, required: ['cite', 'confidence'] } },
    delta: { type: 'string', description: 'Delta to state in the mission\'s form' },
  },
  required: ['row', 'verdict', 'status', 'answer', 'working', 'finite_budget', 'limit', 'krier_reply', 'sources', 'delta'],
}

const OPTIMIST_SCHEMA = {
  type: 'object',
  properties: {
    strongest_case: { type: 'string' },
    rows_attacked: { type: 'array', items: { type: 'object', properties: { row: { type: 'string' }, what_it_would_become: { type: 'string' }, strength: { type: 'string', enum: ['kills', 'narrows', 'fails'] } }, required: ['row', 'what_it_would_become', 'strength'] } },
    answer: { type: 'string' },
    sources: { type: 'array', items: { type: 'object', properties: { cite: { type: 'string' }, confidence: { type: 'string', enum: ['sure', 'likely', 'unsure'] } }, required: ['cite', 'confidence'] } },
    delta: { type: 'string' },
  },
  required: ['strongest_case', 'rows_attacked', 'answer', 'sources', 'delta'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    missing_cases: { type: 'array', items: { type: 'object', properties: { case: { type: 'string' }, why_the_instance_cannot_express_it: { type: 'string' }, smallest_change_that_would: { type: 'string' }, why_it_matters_for_the_question: { type: 'string' } }, required: ['case', 'why_the_instance_cannot_express_it', 'smallest_change_that_would', 'why_it_matters_for_the_question'] } },
    answer: { type: 'string' },
  },
  required: ['missing_cases', 'answer'],
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    row: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'narrowed', 'refuted', 'open'] },
    status: { type: 'string', enum: ['theorem', 'computed', 'argued', 'empirical', 'open', 'refuted'] },
    working: { type: 'string' },
    answer: { type: 'string' },
    sources: { type: 'array', items: { type: 'object', properties: { cite: { type: 'string' }, confidence: { type: 'string', enum: ['sure', 'likely', 'unsure'] } }, required: ['cite', 'confidence'] } },
    delta: { type: 'string' },
  },
  required: ['row', 'verdict', 'status', 'working', 'answer', 'sources', 'delta'],
}

const other = m => (m === 'opus' ? 'fable' : 'opus')

phase('Rows')
log(`Hard-case round ${DATE}: ${ROWS.length} rows, ${OPTIMISTS.length} optimists, 1 critic; second readers per row from the other family.`)

const rowResults = pipeline(ROWS,
  r => agent(`${PREAMBLE}\n\nYour row: ${r.title}.\nThe claim under test: ${r.claim}\nYour questions: ${r.questions}\nEnd with your answer to the mission question, Krier's best reply, and your delta.`,
    { label: `row:${r.id}`, phase: 'Rows', schema: ROW_SCHEMA, model: r.model, agentType: 'general-purpose' })
    .then(res => ({ ...(res || {}), id: r.id, title: r.title, claim: r.claim, model: r.model })),
  (first, r) => agent(`${PREAMBLE}\n\nYou are the independent second reader of one row. A first reader has assessed it; you are not shown its reasoning or verdict, and you must reach your own.\nThe row: ${r.title}.\nThe claim under test: ${r.claim}\nThe questions it was tested on: ${r.questions}\nAssess the claim on the instance, with your own computation. End with your answer to the mission question and your delta.`,
    { label: `verify:${r.id}`, phase: 'Verify', schema: VERIFY_SCHEMA, model: other(r.model), agentType: 'general-purpose' })
    .then(second => ({ first, second: second ? { ...second, model: other(r.model) } : null,
                       agree: !!(second && first && second.verdict === first.verdict) })),
)

const optimistResults = parallel(OPTIMISTS.map(o => () =>
  agent(`${PREAMBLE}\n\nYour role: the strongest possible advocate for the computational-optimist agenda. Rows in your remit: ${o.rows}. ${o.brief}\nEnd with your answer to the mission question and your delta.`,
    { label: o.id, phase: 'Rows', schema: OPTIMIST_SCHEMA, model: o.model, agentType: 'general-purpose' })
    .then(res => res ? { ...res, id: o.id } : null)))

const criticResult = agent(`${PREAMBLE}\n\nYour role: the model critic. Your only job is to find the hard cases the instance still cannot express, the open system above all (agents in many bargains at once, carrying reputation and incentives across them), and for each to say the smallest change to the instance that would express it and why it matters for the question. Do not assess the rows. End with your answer to the mission question.`,
  { label: 'model-critic', phase: 'Rows', schema: CRITIC_SCHEMA, model: 'fable', agentType: 'general-purpose' })

const [rows, optimists, critic] = await Promise.all([rowResults, optimistResults, criticResult])
const rowsDone = rows.filter(Boolean)
log(`Rows done: ${rowsDone.length}/${ROWS.length}; agreement between readers on ${rowsDone.filter(x => x.agree).length}.`)

phase('Cold read')
const digest = rowsDone.map(x => ({
  row: x.first && x.first.title, first: x.first && { model: x.first.model, verdict: x.first.verdict, status: x.first.status, answer: x.first.answer, finite_budget: x.first.finite_budget, limit: x.first.limit, delta: x.first.delta },
  second: x.second && { model: x.second.model, verdict: x.second.verdict, status: x.second.status, answer: x.second.answer, delta: x.second.delta },
  agree: x.agree,
}))
const cold = await agent(`You are reviewing the results of a structured review for internal consistency and for what they say about one question. You are READ-ONLY. Read, in the repository at /Users/dan/Source/livingthing, only _plans/hyperscaling_coase_mission.md and _plans/hyperscaling_coase_hard_case_instance.md. Then read the results below. For each row: do the two readers agree, and if not, which is better supported on the instance's numbers? Across rows: where do they contradict one another? Which instance features does each verdict depend on? Finally, state the answer to the mission question that the results jointly support, in five sentences at most, and the conditions the optimist's outcome was found to need. Return plain text.\n\nRESULTS:\n${JSON.stringify(digest, null, 1)}`,
  { label: 'cold-read', phase: 'Cold read', model: 'opus', agentType: 'general-purpose' })

return { date: DATE, rows: rowsDone, optimists: optimists.filter(Boolean), critic, cold }
})();
