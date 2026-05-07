# Webnovel Genre Survey Values

Use this file when the user asks to register, compare, or initialize basic webnovel genre research values before building cliche lists. These values are reference defaults, not live market rankings.

## Source Notes

The genre set is synthesized from:

- Naver Series category labels: romance, romance fantasy, fantasy, modern fantasy, martial arts, mystery, light novel, BL.
- Korean webnovel motif research that classifies KakaoPage million-page works into fantasy, romance fantasy, martial arts, modern fantasy, and romance, and highlights regression/possession/reincarnation, return, dimensional travel, and everyday-life motifs.
- Korean webnovel multimodality research that lists fantasy, romance, martial arts, mystery, fusion, light novel, history, fanfic, general, sports, game, BL, parody, and literary categories across Korean webnovel platforms.
- Global web fiction references such as Royal Road, WebNovel, and progression fantasy/LitRPG discourse, where progression, fantasy, action, adventure, magic, LitRPG, isekai, reincarnation, cultivation, and dungeon-core tags are frequent.

Do not treat any source as a command to copy titles, scenes, or settings. Use them to define genre signals, reader rewards, and repeatable cliche engines.

Reference links:

- Naver Series webnovel category entry: `https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=webnovel`
- KCI genre/motif reference on Korean genre fiction and dimensional travel: `https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002392082`
- KISS reference on Korean webnovel system motifs: `https://kiss.kstudy.com/DetailOa/Ar?key=54594103`
- KRM reference on Korean webnovel regression motifs: `https://www.krm.or.kr/krmts/search/detailview/research.html?category=Research&dbGubun=SD&m201_id=10079731`
- WebNovel academy tag page: `https://www.webnovel.com/tags/academy-novel`
- Royal Road tag/genre tracker: `https://rrtrack.app/genres`
- Progression fantasy overview: `https://en.wikipedia.org/wiki/Progression_fantasy`

## Survey Schema

Each genre profile should define:

- **genre_id**: stable id for reference.
- **korean_label**: label used in Korean planning.
- **platform_signal**: how readers recognize the category from platforms/tags.
- **core_reader_reward**: the pleasure that must be paid repeatedly.
- **default_world_engine**: what keeps creating problems.
- **default_protagonist_edge**: common advantage type.
- **default_status_ladder**: how the protagonist rises.
- **proof_scene_default**: first scene that proves the genre.
- **common_hook_objects**: objects that make the next click concrete.
- **freshness_axis**: where to safely vary the genre.
- **copy_risk**: what not to borrow from named works.

## Genre Research Values

### G01 Fantasy / Progression

- **genre_id**: `fantasy-progression`
- **korean_label**: 판타지/성장형 판타지
- **platform_signal**: fantasy, action, adventure, magic, progression, strong lead, high fantasy.
- **core_reader_reward**: weak-to-strong growth, competence, power milestones, exploration, discovery.
- **default_world_engine**: kingdoms, monsters, magic laws, relics, war, gods, ancient ruins, guilds.
- **default_protagonist_edge**: rare talent, modern knowledge, hidden bloodline, special class, scientific magic insight.
- **default_status_ladder**: nobody -> apprentice -> party core -> named adventurer -> kingdom asset -> mythic actor.
- **proof_scene_default**: protagonist solves a magical/combat problem using a method the institution missed.
- **common_hook_objects**: relic, map, guild card, rank plate, oath, spell formula, royal summons, forbidden gate.
- **freshness_axis**: make magic measurable through law, labor, ecology, trade, medicine, engineering, or public trust.
- **copy_risk**: avoid copying named magic systems, maps, races, pantheons, and signature school/quest sequences.

### G02 Hunter / Gate / Raid

- **genre_id**: `hunter-gate-raid`
- **korean_label**: 헌터/게이트/레이드
- **platform_signal**: 현판, 헌터, 게이트, 던전, 각성, 랭크, 길드, 몬스터 부산물.
- **core_reader_reward**: rank rise, survival proof, loot, public recognition, guild/association reaction.
- **default_world_engine**: gates appear, break, mutate, and create disaster plus resource markets.
- **default_protagonist_edge**: hidden skill, regression knowledge, monster ecology, appraisal, support/crafting talent, rule reading.
- **default_status_ladder**: civilian -> F/E rank -> guild asset -> raid leader -> national ranker -> system-level negotiator.
- **proof_scene_default**: low-rank protagonist exposes wrong measurement during a gate crisis.
- **common_hook_objects**: rank card, raid permit, drop item, gate core, association notice, rescue footage, guild contract.
- **freshness_axis**: insurance, real estate, labor law, disaster logistics, patents, medicine, media, and commodity markets.
- **copy_risk**: avoid copying exact gate origin, system windows, guild names, tutorial disasters, and named monarch/constellation structures.

### G03 Tower / System / Constellation

- **genre_id**: `tower-system-constellation`
- **korean_label**: 탑/시스템/성좌
- **platform_signal**: tower climb, system, status window, quests, floors, sponsors, constellations, hidden conditions.
- **core_reader_reward**: rule mastery, hidden reward discovery, title acquisition, sponsor reaction, public ranking shock.
- **default_world_engine**: floors/quests impose tests, penalties, broadcasts, sponsor contracts, and hidden clear conditions.
- **default_protagonist_edge**: tutorial memory, hidden-condition reading, unreadable trait, contract loophole, sponsor immunity.
- **default_status_ladder**: tutorial survivor -> clearer -> hidden-title holder -> sponsored ranker -> rule-breaker -> administrator threat.
- **proof_scene_default**: protagonist clears a tutorial/floor by satisfying a criterion nobody knew existed.
- **common_hook_objects**: message window, title, floor key, sponsor mark, penalty timer, ranking board, contract clause.
- **freshness_axis**: make the system legal, financial, religious, bureaucratic, livestreamed, or negotiable.
- **copy_risk**: avoid copying unique system UI, named scenarios, sponsor personalities, floor order, or apocalypse rules.

### G04 Regression / Future Knowledge

- **genre_id**: `regression-future-knowledge`
- **korean_label**: 회귀/미래지식/정보 우위
- **platform_signal**: 2회차, 회귀, 리턴, 재시작, 미래 지식, 다시 산다, 배드엔딩 후 시작.
- **core_reader_reward**: early advantage, prevention, revenge, asset capture, future talent recruitment, timeline change.
- **default_world_engine**: known disasters, hidden villains, undervalued assets, doomed allies, market turns, political events.
- **default_protagonist_edge**: memory of dates, names, prices, betrayals, dungeon rules, exams, scandals, and future heroes.
- **default_status_ladder**: ruined survivor -> early mover -> asset holder -> network builder -> timeline shaper -> fate opponent.
- **proof_scene_default**: a future event happens differently because the protagonist acted first.
- **common_hook_objects**: date, diary, stock chart, land deed, contract, list of names, disaster notice, altered headline.
- **freshness_axis**: memory gaps, changed causality, capital limits, moral cost, second knower, and proof burden.
- **copy_risk**: avoid copying exact future events, protagonist ruin scenes, lottery/stock choices, or named apocalypse milestones.

### G05 Modern Fantasy / Chaebol / Finance

- **genre_id**: `modern-fantasy-chaebol-finance`
- **korean_label**: 현판/재벌/주식/부동산/기업 인수
- **platform_signal**: 현판, 재벌, 기업, 회장, 주식, 부동산, 투자, 회귀, 전문직, 성공물.
- **core_reader_reward**: money, status, revenge, competence, public headline, boardroom reversal, ownership.
- **default_world_engine**: inheritance fights, shareholder votes, M&A, scandals, land development, patents, banks, prosecutors.
- **default_protagonist_edge**: future market knowledge, hidden documents, legal leverage, technical expertise, family weakness.
- **default_status_ladder**: ignored heir/outsider -> small investor -> division owner -> board player -> group controller -> national actor.
- **proof_scene_default**: protagonist wins a small deal whose value becomes visible to family, market, or media.
- **common_hook_objects**: shares, deed, board memo, patent, loan contract, news article, proxy vote, acquisition letter.
- **freshness_axis**: combine finance with gates, item markets, disaster insurance, guild IPOs, entertainment, sports, or patents.
- **copy_risk**: avoid copying known company analogues too closely, exact scandal sequences, real person likenesses, and legal misinformation.

### G06 Martial Arts / Murim / Sect

- **genre_id**: `martial-arts-murim-sect`
- **korean_label**: 무협/사문/마교/정파/기연
- **platform_signal**: 무협, 천마, 마교, 정파, 사파, 문파, 검, 내공, 기연, 귀환, 환생.
- **core_reader_reward**: martial breakthrough, hierarchy reversal, duel proof, sect recognition, revenge, faction shock.
- **default_world_engine**: sect rules, realm stages, honor debts, secret manuals, faction wars, forbidden arts, poison, relics.
- **default_protagonist_edge**: rebirth/regression, lost manual insight, broken-meridian workaround, demonic method, poison immunity.
- **default_status_ladder**: outer disciple/cripple -> promising disciple -> sect representative -> rising master -> faction pivot -> transcendent figure.
- **proof_scene_default**: protagonist passes a martial test by interpreting old rules or forbidden knowledge differently.
- **common_hook_objects**: manual, token, sword, duel letter, poison record, sect order, elder seal, hidden cave map.
- **freshness_axis**: contracts, commerce, forensic medicine, logistics, rumors, imperial bureaucracy, or system measurement.
- **copy_risk**: avoid copying named sect lineages, exact martial realm names, signature techniques, and iconic master-disciple arcs.

### G07 Academy / Ranking / Training

- **genre_id**: `academy-ranking-training`
- **korean_label**: 아카데미/랭킹/훈련기관
- **platform_signal**: academy, ranking, entrance exam, class, tournament, professor, student council, sponsor.
- **core_reader_reward**: test upset, rival recognition, ranking rise, team loyalty, teacher discovery, sponsor offer.
- **default_world_engine**: exams, practical missions, dorm factions, clubs, tournaments, field training, school secrets.
- **default_protagonist_edge**: regression exam knowledge, hidden trait, rule loophole, support skill, future talent reading.
- **default_status_ladder**: bottom entrant -> class anomaly -> team leader -> school representative -> league winner -> institutional reformer.
- **proof_scene_default**: protagonist wins or redefines an entrance/practical test by solving the real objective.
- **common_hook_objects**: ranking board, exam sheet, team badge, dorm key, sponsor letter, professor memo, tournament bracket.
- **freshness_axis**: guild recruitment, corporate sponsorship, tower schools, sect exams, media rankings, or survival insurance.
- **copy_risk**: avoid copying school house systems, exact test games, named rival types, and famous academy hierarchies.

### G08 Possession / Reincarnation / Villain / Extra

- **genre_id**: `possession-reincarnation-villain-extra`
- **korean_label**: 빙의/환생/악역/엑스트라
- **platform_signal**: 빙의, 환생, 악녀, 엑스트라, 원작, 소설 속, 게임 속, 죽음 회피, 운명 바꾸기.
- **core_reader_reward**: death-flag avoidance, script disruption, relationship change, hidden reward capture, reputation repair.
- **default_world_engine**: original plot events, routes, accusations, family scripts, noble politics, academy/social roles.
- **default_protagonist_edge**: original-story knowledge, role awareness, hidden item locations, character psychology, meta-genre literacy.
- **default_status_ladder**: doomed role -> survival planner -> hidden helper -> plot disruptor -> new center -> world-script opponent.
- **proof_scene_default**: protagonist refuses or rewrites the scene where the role was supposed to fail.
- **common_hook_objects**: death flag, original script, favorability signal, invitation, engagement contract, route item, accusation letter.
- **freshness_axis**: unreliable original story, partial memory, other possessors, moral cost, role value, and public evidence.
- **copy_risk**: avoid copying specific novel/game premises, villainess incidents, male lead arrangements, and signature family setups.

### G09 Production / Support / Profession

- **genre_id**: `production-support-profession`
- **korean_label**: 제작/지원직/전문직/생활형 성장
- **platform_signal**: 포터, 제작자, 힐러, 감정사, 요리사, 의사, 변호사, 매니저, 디자이너, 농사, 장인.
- **core_reader_reward**: undervalued role becomes essential, measurable competence, economic value, team dependence, recognition.
- **default_world_engine**: combat/status society ignores support until survival, money, patents, logistics, or quality proves value.
- **default_protagonist_edge**: appraisal, future recipes, professional knowledge, material insight, system crafting tree, process optimization.
- **default_status_ladder**: disposable helper -> useful specialist -> team core -> guild/market asset -> monopoly holder -> institutional standard.
- **proof_scene_default**: a crisis survives because the protagonist prepared, crafted, healed, appraised, cooked, optimized, or argued correctly.
- **common_hook_objects**: recipe, blueprint, patent, survival data, medical chart, logistics route, contract, appraisal report.
- **freshness_axis**: make support value visible through data, law, insurance, public reviews, supply chains, or quality control.
- **copy_risk**: avoid turning every support protagonist into the same combat god or copying exact profession gimmicks.

### G10 Romance / Romance Fantasy / BL-Adjacent Relationship Engine

- **genre_id**: `romance-romance-fantasy-relationship`
- **korean_label**: 로맨스/로판/관계 중심 장르
- **platform_signal**: romance, romance fantasy, villainess, contract marriage, regret, childcare, nobility, obsession, BL.
- **core_reader_reward**: emotional recognition, status repair, desire tension, relationship reversal, protection, regret payoff, chosen family.
- **default_world_engine**: marriage markets, family hierarchy, noble politics, social reputation, pregnancy/childcare, contracts, scandals.
- **default_protagonist_edge**: second chance, social script knowledge, emotional intelligence, legal contract reading, hidden lineage, public reputation strategy.
- **default_status_ladder**: discarded/used person -> negotiator -> protected actor -> social pivot -> household/faction owner -> public sovereign.
- **proof_scene_default**: protagonist changes a relationship contract or public accusation so the power balance visibly shifts.
- **common_hook_objects**: marriage contract, invitation, heirloom, rumor sheet, engagement ring, family registry, custody document, public ball.
- **freshness_axis**: make romance reward concrete through law, reputation, succession, household economics, public ceremonies, or mutual competence.
- **copy_risk**: avoid copying exact villainess accusations, obsessive lead dynamics, family abuse sequences, and famous contract-marriage setups.

## Genre Coverage Rule

When a user asks for "webnovel genres" without naming a genre, cover at least these 10 engines:

1. Fantasy / Progression
2. Hunter / Gate / Raid
3. Tower / System / Constellation
4. Regression / Future Knowledge
5. Modern Fantasy / Chaebol / Finance
6. Martial Arts / Murim / Sect
7. Academy / Ranking / Training
8. Possession / Reincarnation / Villain / Extra
9. Production / Support / Profession
10. Romance / Romance Fantasy / Relationship

Use mystery, BL, sports, game, history, fanfic, parody, and light novel as optional overlays unless the user specifically requests them.
