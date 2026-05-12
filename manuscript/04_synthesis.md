# Active Inference and the Blake Correspondences (Compressed)

This chapter compresses the formal apparatus I developed at length in two earlier papers (Zenodo records 18600041 and 18807971) into the minimum needed to make the Jiang mapping in the following chapter legible. Readers interested in the full apparatus — derivation, philosophical commitments, the eight Blake correspondences, the six pragmatist convergences, and the synergetic geometry — should consult the earlier papers directly [@friedman_doors; @friedman_pragmatism].

## The Framework, in One Pass

The Free Energy Principle (FEP) proposes that all self-organizing biological systems act to minimize variational free energy — a mathematical bound on surprise [@friston2010fep; @friston_unified]. *Active Inference* is the process theory derived from the FEP: organisms minimize free energy through a combination of perception (updating internal models to match sensory evidence) and action (acting on the world to make it conform to predictions) [@parr_pezzulo_friston_2022]. ![The Markov blanket as Blake's doors of perception: internal states (the self / model) separated from external states (the world / other agents) by sensory states (perception) and active states (action). Inference *across* the blanket is the engine of cognition.](../output/figures/markov_blanket_light.png){ width=65% }

The *Markov blanket* — the statistical boundary between internal and external states — defines selfhood [@kirchhoff_markov_blankets]. *Precision weighting* determines how much relative influence prior beliefs versus incoming sensory evidence have in driving inference. Misallocated precision is the formal model of pathological mental states and, in the framing I develop, the formal analogue of what Blake names Newton's Sleep.

The FEP's status is contested. Colombo and Wright [@colombo_wright] argue that its grand-unifying claims outrun what the mathematics supports. Aguilera et al. [@aguilera_etal] argue that the Markov-blanket formalism, applied to biological organisms, requires assumptions that are either trivially true or empirically unsupported in many systems of interest. Bruineberg, Dołęga, Dewhurst, and Baltieri [@bruineberg_etal] distinguish *instrumentalist* readings (the FEP is a useful modeling tool) from *literalist* readings (free energy minimization is what life *is*), and argue that the literalist readings face severe philosophical difficulties. Sajid, Ball, Parr, and Friston [@sajid_etal] offer a within-framework demystification.

I use Active Inference here as a *generative vocabulary* rather than as established science. Whether or not the FEP is literally true of brains, the formal apparatus of generative models, precision weighting, and Markov blankets gives me redescriptions of Blake-adjacent diagnostics that contemporary cognitive science can engage with — and the Jiang mapping that follows in the next chapter depends on those redescriptions, not on FEP literalism.

## Eight Correspondences with Blake (Compressed Table)

The first earlier paper [@friedman_doors] develops the following correspondences as functional analogues across incompatible metaphysics:

| Blake concept                                          | Active Inference functional analogue                                       |
|--------------------------------------------------------|----------------------------------------------------------------------------|
| **Boundary** ("doors of perception")                   | Markov blanket — statistical boundary separating self from world           |
| **Vision** ("Newton's Sleep")                          | Pathology of rigid priors crushing sensory evidence                        |
| **States** (Eden / Beulah / Generation / Ulro)         | Hidden states in the generative model                                      |
| **Imagination** (as "real & eternal World")            | Generative model as constitutive of selfhood                               |
| **Time**                                               | Temporal depth of planning and memory                                      |
| **Space**                                              | Spatial inference; active sampling                                         |
| **Action**                                             | Active inference — acting to confirm predictions                           |
| **Collectives** (Four Zoas)                            | Multi-agent coordination; factorized model of collective mind              |

The deepest of these — and the one doing the most work in the Jiang mapping — is the reading of the Four Zoas as factors in the factorized generative model. Urizen carries the prior channel; Luvah the affective precision channel; Tharmas the sensory channel at the Markov blanket; Urthona / Los the temporally extended imagination that constitutes the deep generative model. Coordination of the four is what Blake names fourfold vision. Tyranny of Urizen over the others is what he names Single Vision — and it is the specific architecture Jiang's diagnostic targets when he describes AI systems as demanding clean data, suppressing edge cases, and restructuring human society to fit the system's parameters.

## Six Pragmatist Convergences (Brief Recap)

The second earlier paper [@friedman_pragmatism] extends the architecture into American pragmatism:

| Blake figure / event                                    | Pragmatist analogue                                                  |
|--------------------------------------------------------|----------------------------------------------------------------------|
| **Orc's revolutionary fire**                           | Peirce's "irritation of doubt" compelling inquiry                    |
| **The Thirteen Angels' collective transformation**     | Mead's social self constituted through the generalized other         |
| **Consumption of the "five gates"**                    | Dewey's collapse of spectator theory; James on relations as real     |
| **Four Zoas**                                          | Factorized generative model (Active Inference)                       |
| **Multi-agent belief alignment**                       | Peirce's community of inquirers under fallibilism                    |
| **Synergetics** (Fuller / Applewhite)                  | Tetrahedron as fundamental unit; pragmatic-maxim operationalism      |

The Peircean half rests on Pietarinen and Beni's argument that FEP variational free-energy minimization formalizes Peircean abduction [@pietarinen_beni_2021; @beni_pietarinen_2021]. Gallagher's framing of classical pragmatism as the conceptual ancestor of enactivism [@gallagher_enactivist; @gallagher_pragmatism] supplies the broader connection. The pragmatist–enactivist literature is internally contested [@menary_integration; @chemero_radical; @hutto_myin_radicalizing; @madzia_jung; @misak_pragmatists; @hookway_maxim] and I do not resolve those debates here. The narrower claim I deploy below is that *Peirce's abductive structure of inquiry* — irritation of doubt, hypothesis formation, fallibilistic correction through community — supplies a structural-functional vocabulary I find useful when reading Jiang's diagnostics against engagement-maximization architectures that suppress precisely this kind of inquiry.

## Cognitive Security as Adjacent Measurement Program

The political extension goes through my work on cognitive security (COGSEC), which treats information-based threats as problems of corrupted generative models, misallocated epistemic precision, and manufactured belief [@cogsec_neurocognitive; @cogsec_arxiv]. The COGSEC framework supplies an *adjacent measurement program* for what Jiang describes as consciousness capture — adjacent rather than equivalent, because COGSEC makes no claim about divinity or sovereignty and does not invoke a hidden elite as the proximate cause of population-level cognitive pathology. The framework treats the pathology as an *infrastructure* problem that can be specified, measured, and (in principle) defended against, irrespective of the intentions of system designers.

Combined with the Active Inference reading of Blake, this gives a partial pipeline from architectural diagnosis to political-technical intervention: the structural pathology Blake diagnoses (Single Vision / Urizenic dominance), the formal model that redescribes it (rigid-prior precision allocation), and the discipline that addresses it at population scale (cognitive security). The next chapter deploys this compressed apparatus against Jiang's specific claims.

## Mathematical Formalism: Newton's Sleep as Precision Misallocation

The compressed apparatus above is metaphorical until it is grounded in the variational mathematics from which it is derived. This subsection supplies the minimum formal machinery needed to make the mapping rigorous, drawing on the standard presentation in Parr, Pezzulo, and Friston [@parr_pezzulo_friston_2022] and on the mechanistic-Bayesian reading in Ramstead and colleagues [@ramstead_bayesian_mechanics].

An Active Inference agent maintains a generative model $p(o, s) = p(o \mid s)\, p(s)$ over observations $o$ and hidden states $s$, together with an approximate posterior $q(s)$ that is updated to minimize the *variational free energy*

\begin{equation}
\label{eq:free-energy}
F[q] \;=\; \mathrm{D}_{\mathrm{KL}}\!\left[q(s) \,\Vert\, p(s \mid o)\right] - \log p(o).
\end{equation}

Free energy is an upper bound on surprise $-\log p(o)$; minimizing $F$ tightens the bound while updating beliefs to match evidence. The agent acts to bring future observations into agreement with predicted observations under its generative model — perception and action are two faces of the same variational problem.

The decomposition that matters here is

\begin{equation}
\label{eq:fe-decomp}
F[q] \;=\; \underbrace{\mathbb{E}_{q}\!\left[-\log p(o \mid s)\right]}_{\text{accuracy term}} \;+\; \underbrace{\mathrm{D}_{\mathrm{KL}}\!\left[q(s) \,\Vert\, p(s)\right]}_{\text{complexity term}}.
\end{equation}

The accuracy term penalizes mismatch between predicted and observed sensory states; the complexity term penalizes posterior divergence from the prior. One reading of *Newton's Sleep* available within this framework is the regime in which the complexity term dominates: the prior $p(s)$ has been given so much precision that the posterior $q(s)$ is dragged toward it irrespective of what $o$ contains, the accuracy term grows large, and the agent cannot reduce free energy by updating $q$ because the prior's precision penalises every deviation. Whether Blake intended anything like this parameter-level claim is, of course, a separate question; the present essay treats the mapping as a functional analogy.

Precision is the inverse-variance parameter of each Gaussian factor in the model. Writing $\pi_p$ for prior precision and $\pi_o$ for sensory precision, the posterior precision in a single-step Gaussian inference is

\begin{equation}
\label{eq:posterior}
\pi_{q} \;=\; \pi_p \,+\, \pi_o, \qquad \mu_{q} \;=\; \frac{\pi_p \,\mu_p \,+\, \pi_o \,\mu_o}{\pi_p \,+\, \pi_o}.
\end{equation}

The posterior mean is a precision-weighted average of prior and evidence. The regime $\pi_p \gg \pi_o$, in which $\mu_{q} \approx \mu_p$ regardless of evidence, is one possible operationalisation of *pathological prior dominance*. A multi-channel generalisation distributes precision across several inference channels — corresponding, in the reading offered here, to the four Zoas — so that no single channel's precision exceeds the others by more than a small constant factor.

The Newton's-Sleep metric used in the precision-dynamics analysis (Figure 4) operationalises this by

\begin{equation}
\label{eq:newtons-sleep}
\mathcal{N} \;=\; \frac{\pi_{\text{Urizen}}}{\pi_{\text{Luvah}} + \pi_{\text{Tharmas}} + \pi_{\text{Urthona}}},
\end{equation}

with $\mathcal{N} \gg 1$ corresponding to Single Vision and $\mathcal{N} \approx 1/3$ (all four channels carrying equal precision) corresponding to Fourfold Eden. The *fourfold-balance entropy* is the Shannon entropy of the precision distribution across the four channels in nats,

\begin{equation}
\label{eq:fourfold-entropy}
\mathcal{H} \;=\; -\!\!\!\sum_{k \in \{U,L,T,O\}} \!\! p_k \log p_k, \qquad p_k \;=\; \frac{\pi_k}{\sum_{j} \pi_j},
\end{equation}

with maximum $\log 4 \approx 1.386$ when all four channels carry equal precision. The *cleansed-doors score*

\begin{equation}
\label{eq:cleansed-doors}
\mathcal{C} \;=\; \frac{\mathcal{H}}{\log 4}\,(1 - p_U)
\end{equation}

combines the entropy term with a non-rigidity term penalising prior-channel dominance; $\mathcal{C} \in [0, 1]$, attaining its observed maximum of $3/4$ when all four channels carry equal weight (the simplex constraint forbids the higher abstract limit at vanishing prior share).

![Three metrics across four canonical precision regimes. Newton's-Sleep ratio (top), fourfold-balance entropy (middle, dashed line marks the $\log 4$ maximum), and cleansed-doors score (bottom, bounded in [0, 1]). The same total precision budget produces qualitatively different cognitive regimes depending on its distribution across the four Zoas.](../output/figures/precision_dynamics_light.png){ width=95% }

![Belief trajectories under three prior-precision regimes, all converging on the same evidence stream ($\mu_o = 5$, $\pi_o = 1$). Under Newton's Sleep ($\pi_p = 8$) the posterior remains anchored to the prior mean ($\mu_p = 0$); under twofold parity ($\pi_p = 1$) the posterior steadily converges to the evidence; under Cleansed Doors ($\pi_p = 0.25$) the posterior reaches the evidence within two updates.](../output/figures/precision_phase_light.png){ width=85% }

These quantities make the proposed convergence checkable rather than merely rhetorical. In the canonical precision palette of the source code [`generative_model.canonical_regimes`], the *Newton's Sleep* configuration produces $\mathcal{N} = 4.0$, $\mathcal{H} \approx 0.78$ nats, $\mathcal{C} \approx 0.099$; the *Fourfold Eden* configuration produces $\mathcal{N} \approx 0.33$, $\mathcal{H} = \log 4$, $\mathcal{C} = 0.75$. The same total precision budget, distributed differently across the four channels, yields qualitatively different inferential regimes. This is not a measurement of Blake — Blake had no posterior distributions to allocate. It is a demonstration that the architectural distinction his vocabulary names has a clean quantitative counterpart in precision allocation, and that the difference between Single Vision and Fourfold Eden, in this framing, is a difference of *how* a system distributes its inferential confidence rather than *how much* of it the system has.

The multi-agent extension — central to the cooperation off-ramp developed in the next chapter — generalises this to a network of agents, each with its own generative model and Markov blanket, exchanging belief updates through joint-posterior protocols. The consensus rule used in the cooperation analysis is the precision-weighted Gaussian product,

\begin{equation}
\label{eq:consensus}
\mu_{\text{cons}} \;=\; \frac{\sum_i \pi_i\, \mu_i}{\sum_i \pi_i}, \qquad \pi_{\text{cons}} \;=\; \sum_i \pi_i,
\end{equation}

in which $N$ agents with beliefs $(\mu_i, \pi_i)$ pool their posteriors. The architectural diagnosis carries over without alteration: a multi-agent network in which one agent's precision dominates the others' instantiates Single Vision at the network level, regardless of how individually well-balanced each agent's internal precision allocation is. Fourfold restoration at the network level requires precision balance both within and across agents [@friston_multiagent; @hipolito_multiagent; @heins_pymdp].

The next chapter deploys this compressed apparatus against Jiang's specific claims.
