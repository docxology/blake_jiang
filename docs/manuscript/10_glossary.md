# Glossary

The mapping work this essay attempts requires that terms from three vocabularies — Romantic poetics, contemporary public-intellectual polemic, and variational cognitive science — be used precisely. The following definitions are operational for the present essay, not exhaustive scholarly treatments; where a term has a longer scholarly history, the standard apparatus listed in the references chapter supplies the longer treatment.

**Active Inference.** The process theory of biological self-organisation derived from the Free Energy Principle. Organisms minimise variational free energy through perception (updating internal models to match sensory evidence) and action (acting on the world to make it conform to predictions). The standard reference is Parr, Pezzulo, and Friston, *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior* (MIT Press, 2022) [@parr_pezzulo_friston_2022].

**Albion.** In Blake's mythic system, the universal man whose four faculties (the Four Zoas) have fallen into dis-coordination. The narrative arc of *Vala, or The Four Zoas* and *Jerusalem* is Albion's restoration through the coordinated labor of his faculties.

**Black box.** Colloquial term for a deep learning model whose internal computations are not legibly interpretable. The black box becomes problematic only when treated as an authority rather than as an inference challenge — a distinction Blake draws between the productive unseen of imagination and the tyrannical unseen of Urizen's hidden command. *Mechanistic interpretability* research aims to make the box less opaque.

**Cleansed Doors.** Blake's image from *The Marriage of Heaven and Hell* (plate 14): "If the doors of perception were cleansed every thing would appear to man as it is, infinite." In the Active Inference reading, the cleansed-doors regime is one in which precision is distributed across multiple inference channels rather than concentrated in a single faculty.

**Cleansed Doors Score** ($\mathcal{C}$). A bounded health-score in $[0, 1]$ combining the fourfold-balance entropy with a non-rigidity term penalising prior-channel dominance. Defined formally in §4.

**Cognitive Security (COGSEC).** The discipline that treats information-based threats as problems of corrupted generative models, misallocated epistemic precision, and manufactured belief. Distinct from information security in operating at the population-cognitive level rather than the network-system level [@cogsec_neurocognitive; @cogsec_arxiv].

**Constitutional AI.** A training procedure (Anthropic, 2022) in which a model is constrained by a written constitution that takes the place of human feedback in shaping behavior [@bai_constitutional]. In the framing of the present essay, a structured single-vision approach.

**Debate-based alignment.** A multi-agent alignment proposal (Irving, Christiano, Amodei 2018) in which multiple models argue against one another and a third model adjudicates [@irving_debate]. Closer to fourfold vision than constitutional AI because it instantiates a multi-agent architecture.

**Edge case.** In machine learning, an input that lies outside the dense region of the training distribution. Edge cases are the high-precision sensory contradictions of priors that, in a healthy generative model, drive model revision. In pathologically rigid models or training paradigms, edge cases are suppressed at the source — the architectural form of what Blake names Urizen's chaining of Orc.

**Engagement maximization.** The optimization objective of attention-economy platforms: maximize the time and attentional resources users devote to the platform. Documented to produce sycophancy and confabulation as emergent behaviors under particular training regimes [@perez_sycophancy].

**Four Zoas.** Blake's four eternal persons whose coordinated labor constitutes Albion: **Urizen** (reason / law, south, head, sight), **Luvah** (passion / emotion, east, heart, scent), **Tharmas** (sensation / body, west, loins, taste), **Urthona** (imagination / prophecy, north, ear, hearing, embodied in the temporal form *Los*). In the Active Inference reading, each Zoa corresponds to a precision channel in a factorized generative model.

**Fourfold Balance Entropy** ($\mathcal{H}$). The Shannon entropy of the precision distribution across the four Zoa channels, in nats; maximum $\log 4 \approx 1.386$ when all four channels carry equal precision. Defined formally in §4.

**Fourfold Vision.** Blake's name for the Edenic mode of perception in which the four Zoas coordinate without any one dominating. Stated most economically in the 1802 letter to Thomas Butts: "fourfold in my supreme delight / And threefold in soft Beulah's night / And twofold Always. May God us keep / From Single vision & Newton's sleep!" [@blake1802letter].

**Free Energy Principle (FEP).** The mathematical principle proposed by Karl Friston that all self-organising biological systems act to minimize a quantity called variational free energy, which is an upper bound on the surprise of sensory observations under the system's generative model. Contested in the philosophical literature [@colombo_wright; @aguilera_etal; @bruineberg_etal]; deployed in this essay as a generative vocabulary rather than as established science.

**Generative Model.** The probabilistic model an inferring agent maintains over hidden states of the world and observations. In Active Inference, the generative model is constitutive of the agent: there is no agent-self underneath the model.

**Glass Bead Game.** From Hesse's novel; the methodological stance I have adopted in earlier work [@friedman_doors] and in the present essay: synthetic juxtaposition of art and science, not reduction of one to the other, with explicit acknowledgment of where the synthesis exceeds what any single tradition supplies.

**Hallucination.** (1) Technical: a high-confidence false output from a large language model, generated by the same statistical mechanism as accurate outputs but without empirical grounding [@ji_hallucination]. (2) Phenomenological: in the Plato's-Cave and Active Inference framings, all perception is hallucinatory in the technical sense — model-driven prediction of sensory states — and the question is whether the model that does the hallucinating is open to revision under surprise. Jiang's 7 May 2026 sentence *"Everything is a hallucination"* [@jiang_diary_of_ceo] compresses the two senses.

**Imagination.** In Blake: not a sub-faculty of cognition but the ground of human existence; the "real & eternal World of which this Vegetable Universe is but a faint shadow" (*Jerusalem* plate 77). In the Active Inference reading: the deep generative model and its temporal extension into counterfactual planning. The mapping is a functional analogy across incompatible metaphysics, not a translation.

**KL Divergence** ($\mathrm{D}_{\mathrm{KL}}$). The Kullback–Leibler divergence between two probability distributions; a non-symmetric measure of how much one distribution diverges from another. The complexity term in variational free energy is the KL divergence between posterior and prior.

**Los.** The temporal, fallen form of the Zoa Urthona; the craftsman-figure who labors at the forge of Golgonooza in *Jerusalem* to restore Albion. The mythopoetic embodiment of imagination as creative labor that maintains the agent's coherence against Urizenic enclosure.

**Markov Blanket.** The statistical boundary between an inferring system's internal and external states; defined by sensory states (information flowing in) and active states (influence flowing out). The blanket is dynamically maintained through the process of inference itself [@kirchhoff_markov_blankets]. In the Blakean reading, the cognitive form of the *doors of perception*.

**Multi-Agent Active Inference.** The generalisation of Active Inference to networks of agents, each with its own generative model and Markov blanket. Belief alignment becomes the multi-agent analogue of single-agent inference; agents converge on shared beliefs through repeated cycles in which each agent's actions become evidence for the others' models [@friston_multiagent; @hipolito_multiagent].

**Newton's Sleep.** Blake's name for the pathological cognitive state in which a single faculty (typically Urizen, the rationalising principle) has gained so much precision that the others fall silent. The fallen world of single vision. In the Active Inference reading, the regime of *pathological prior dominance*. The historical Newton would have rejected this reductive deistic-mechanistic position; Blake's "Newton" is a polemical figure standing for the eighteenth-century reception of Newton in natural philosophy [@ault_visionary].

**Newton's Sleep Metric** ($\mathcal{N}$). The ratio of prior precision to non-prior precision in a four-channel precision-allocation; values strictly greater than 1.0 mark pathological prior dominance. Defined formally in §4.

**Orc.** In Blake's prophetic system, the spirit of liberated energy and revolutionary desire; the unconfinable remainder that consumes the "five gates of their law-built Heaven" in *America: A Prophecy*. The mythopoetic embodiment of the edge case in formal cognitive terms.

**Pathological Prior Dominance.** The Active Inference regime in which the prior precision so dominates sensory precision that the posterior is dragged toward the prior irrespective of evidence. The formal analogue of what Blake names Newton's Sleep. The structural failure mode this essay diagnoses across three vocabularies.

**Precision.** The inverse-variance parameter of a Gaussian distribution in a generative model; a measure of confidence in the corresponding inference channel. Precision-weighting determines how much relative influence prior beliefs versus incoming sensory evidence have in driving inference.

**Single Vision.** Blake's name for the reductive perceptual mode in which the imaginative, affective, and embodied registers have been silenced in favor of pure measurement. The pathology against which the corrective of fourfold vision is offered.

**Technate.** A term Jiang invokes in his 7 May 2026 Game Theory #23 lecture [@jiang_game_theory_23] from the 1930s technocracy movement [@howard_scott_technate; @segal_technocracy]: *"transitioning democracy into a technocracy ruled by the experts and ruled by AI."* The political form, in Jiang's framing, of the architectural single vision the present essay diagnoses.

**Urizen.** The Zoa of reason and law in Blake's system; "the Ancient of Days," depicted with a compass circumscribing the universe. Not a moral villain in Blake's text but an *imbalance* — a faculty that has overstepped its proper role. In the Active Inference reading, the prior-belief channel of the factorized generative model.

**Urthona.** The Zoa of imagination, prophecy, and the spirit; northern direction, organ of hearing. The eternal form whose fallen temporal aspect is Los. In the Active Inference reading, the deep generative model that constitutes selfhood through counterfactual planning.

**Variational Free Energy** ($F$). An upper bound on the surprise of sensory observations under an agent's generative model; defined as the KL divergence between approximate posterior and true posterior, minus the log evidence. Minimisation of $F$ is the unifying objective of perception and action in Active Inference.

**Zoa.** Greek for "living one"; Blake's term for each of the four eternal persons constituting Albion. The four Zoas are Urizen, Luvah, Tharmas, and Urthona; their coordinated labor is what Blake names fourfold vision and their disordering is what he names Single Vision.
