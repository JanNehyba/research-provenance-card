# Od deklarace k důkazu: Karta provenience výzkumu jako verzovaná infrastruktura pro výzkum s podílem AI

**Jan Nehyba**
Pedagogická fakulta, Masarykova univerzita, Brno
ORCID: [0000-…] · Kontakt: [e-mail]

*Preprint, verze 2 (červenec 2026). Neprošlo recenzním řízením. Oproti verzi 1: srozumitelnější jazyk, diagramy, širší zasazení do krajiny vydavatelů a standardů, praktická část pro autory. Připomínky vítány.*

---

## Abstrakt

Když dnes vědec použije při výzkumu umělou inteligenci, přizná to jednou větou: „při přípravě rukopisu byla použita AI." Tato věta je jako účtenka, na které stojí „koupil jsem věci" — nikdo z ní nevyčte, co se skutečně stalo. Nerozlišuje opravu gramatiky od návrhu experimentu, nedá se zkontrolovat, každý vydavatel ji chce jinak a není svázána s konkrétní verzí souboru, takže „zkontrolováno" klidně přežije i výměnu obsahu. K tomu přistupuje hlubší problém: práce, kterou celou vytvořil autonomní AI systém, nemá podle dnešních pravidel žádného platného autora — AI jím být nesmí a člověk, který nic podstatného neudělal, kritéria autorství nesplní také. Tato stať navrhuje odpověď v podobě malého kusu infrastruktury: **kartu provenience výzkumu** (Research Provenance Card, RPC) — strojově čitelný „rodný list" každé práce s podílem AI. Karta zaznamenává *role* místo neověřitelných procent; každé tvrzení řadí na čtyřstupňový **žebřík důkazů** (deklarováno → doloženo artefaktem → nezávisle attestováno → reprodukováno); vše váže **otiskem SHA-256** ke konkrétní verzi dokumentu; přísně odděluje záznam původu od soudu o pravdivosti; a netransparentnost neřeší zákazem, ale **kompenzačním principem**: čím méně kdo odkryje o procesu, tím tvrdší ověření výstupů musí strpět. Stať zasazuje návrh do krajiny vydavatelů, reportovacích směrnic, detektorů AI textu a vznikajícího globálního „Vancouver Standardu", jehož implementačním profilem chce karta být, popisuje otevřený datový model, nástroje i praktický postup pro autora a poctivě rozebírá, co karta neumí. V souladu s vlastním argumentem nese rukopis svou vlastní kartu (Příloha A).

**Klíčová slova:** integrita výzkumu · provenience · AI-generovaný výzkum · vědecká komunikace · metadatové standardy · attestace

---

## 1. Úvod: čtyři díry v jedné větě

Užití AI ve výzkumu dnes hlídá jediný nástroj: deklarační věta. Tvrdíme, že selhává čtyřmi způsoby, a že jde o vady konstrukce, ne o nedbalost autorů.

**První díra: věta nic neříká.** „Byla použita AI" nerozlišuje, zda AI opravila čárky, nebo navrhla metodologii, vybrala zdroje, spočítala statistiku a napsala interpretaci. Vydavatelé to navíc chtějí každý jinak: jeden velký vydavatel dovoluje AI při psaní jen vylepšit čitelnost a jazyk (a analýzu dat nechává mimo záběr politiky), druhý dovoluje i generativní psaní, pokud je popsané v metodách. Iniciativa CANGARU pro to má trefné jméno: **efekt babylonské věže** — mnoho pravidel, žádná společná řeč (CANGARU, 2023).

**Druhá díra: tvrzení se tváří jako záznam.** Deklarace je svědectví zúčastněné strany — a přesto se s ní zachází, jako by to byl doklad. Nic v systému nerozlišuje tvrzení pravdivé od tvrzení *ověřitelného* a nic autora neodmění za to, že svá tvrzení ověřitelnými udělá.

**Třetí díra: kontrola visí ve vzduchu.** Kontroly a deklarace se váží k *názvu* článku, ne ke *stavu* souboru. Rukopis lze zkontrolovat a pak tiše přepsat; razítko zůstane. Říkáme tomu **problém visící attestace** — odkaz, který přežil to, na co ukazoval.

**Čtvrtá díra: práce bez autora.** Etické kodexy (COPE, ICMJE) říkají: AI nemůže být autor, protože nenese odpovědnost. Autorská kritéria zároveň říkají: autor musí podstatně intelektuálně přispět. Práce, kterou od začátku do konce udělal autonomní systém, tedy nemá autora žádného — a buď zůstane v šuplíku, nebo se vypere přes nepřiznané užití AI (Hidalgo, 2026, mluví o „temné aktivitě"), nebo odejde do experimentálních venue mimo uznávaný systém.

Naše teze: správnou odpovědí není další šablona věty ani nový úřad, ale malý kus **infrastruktury** — standardizovaný, verzovaný, důkazně ukotvený záznam o tom, *jak práce vznikla*. Stať postupuje takto: §2 zmapuje hřiště (kdo všechno už na problému pracuje a co chybí), §3 vyloží principy návrhu, §4 kartu a její praktické užití autorem, §5 plán nasazení, §6 poctivý výčet limitů, §7 důsledky.

## 2. Mapa hřiště

Než něco navrhneme, je fér ukázat, kdo na hřišti už hraje. Vrstvy do sebe zapadají takto:

```
┌───────────────────────────────────────┐
│ PRAVIDLA — co se má přiznávat         │
│ Vancouver Standard (v konzultaci)     │
│ EU AI Act čl. 50 · politiky vydavatelů│
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│ FORMULÁŘ — jak to zapsat a doložit    │
│ ► karta RPC (tato stať) ◄             │
└─────────┬─────────────────┬───────────┘
          ▼                 ▼
┌─────────────────┐ ┌─────────────────┐
│ OBČANKY         │ │ MÍSTA PUBLIKACE │
│ ORCID (lidé)    │ │ časopisy, venue,│
│ AICID (agenti)  │ │ vydavatelé      │
└─────────────────┘ └─────────────────┘
```

**2.1 Vydavatelé a jejich pravidla.** Velcí vydavatelé pravidla mají, ale roztříštěná a lidsky, ne strojově čitelná. Elsevier: v psaní jen jazyk a čitelnost, ne vědecké vhledy; užití AI ve výzkumném procesu je mimo záběr politiky. Springer Nature: generativní užití ano, s dokumentací v metodách; pouhá korektura se nedeklaruje. IEEE chce systém, dotčené části a míru užití. Autor s pěti cílovými časopisy tak vede pět různých agend — babylonská věž v praxi.

**2.2 Integritní zázemí.** Vydavatelé zároveň provozují společnou kontrolní infrastrukturu: STM Integrity Hub, sdílený systém, jímž desítky vydavatelů prosévají řádově statisíce rukopisů měsíčně kvůli podvodným „paper mills". COPE (etická komise vydavatelů, přes sto vydavatelských členů) a ICMJE drží normy autorství. Tahle vrstva umí *odhalovat špatné*; neumí *doložit dobré* — chybí jí právě záznam původu.

**2.3 Zákon.** Článek 50 Nařízení EU o AI (použitelný od 2. srpna 2026) zakládá povinnosti transparentnosti u generativních systémů, včetně strojově čitelného značení na straně poskytovatelů. Záznam na úrovni časopisu — jako karta — může tyto povinnosti *doplnit*, sám o sobě je ale nesplňuje; to říkáme výslovně, protože přehnané právní sliby jsou v tomto prostoru běžnou vadou.

**2.4 Vznikající společné pravidlo: Vancouver Standard.** Mezinárodní vědecká rada, COPE, STM, Global Young Academy a nadace WCRI právě společně píší globální standard deklarace AI ve výzkumu; veřejná konzultace běží do 16. října 2026 a řeší přesně naše otázky: kdy deklarovat, jakou taxonomií činností, jak uchovat prompty a logy, kdo odpovídá za kontroly a jak zaznamenat, co ověřit nešlo. Tato stať se nestaví jako konkurence — nabízí se jako **implementační profil**: hotový formulář a nástroje, kterými se budoucí pravidlo dá plnit, plus pilotní data pro pracovní skupinu.

**2.5 Reportovací směrnice: starší sourozenci karty.** Medicína a příbuzné obory mají dlouhou tradici *reportovacích směrnic* — checklistů, co musí studie uvést (PRISMA pro systematické přehledy, CONSORT pro klinické studie, síť EQUATOR jako jejich domov). A tato tradice už na AI reaguje: CONSORT-AI a SPIRIT-AI rozšířily checklisty pro studie s AI intervencemi (Liu et al., 2020), TRIPOD+AI pro predikční modely (Collins et al., 2024), L-PRISMA navrhuje rozšíření PRISMA pro éru generativní AI s důrazem na reprodukovatelnost a auditovatelnost, které nedeterminismus LLM ohrožuje (Shailendra et al., 2026), a CANGARU buduje mezioborový konsensus o užití a deklaraci (CANGARU, 2023). Empirické studie zároveň měří, jak spolehlivě AI konkrétní výzkumné role zvládá — např. při extrakci dat pro systematické přehledy dosáhly tři LLM shody s lidským kódováním 62–72 % a autoři zdůrazňují nutnost člověka v procesu (Schroeder, Jaldi & Zhang, 2025). Vztah ke kartě: směrnice říkají, **co** má být u daného typu studie vykázáno, po oborech a lidsky čitelně; karta dodává **průřezový, strojově čitelný nosič s úrovněmi důkazu**, do kterého se oborové checklisty mohou zaháknout. Nekonkurují si — směrnice jsou obsah, karta je nosič.

**2.6 Detektory AI textu: proč „40 % AI" nefunguje.** Paralelně vznikla celá branže nástrojů, které se snaží AI text *poznat zpětně* — detektory a vodoznaky. Jejich problém je principiální: hádají z výsledného textu, tedy z místa, kde už stopy nejsou. Nesou známé míry falešných poplachů (postihují mj. autory, pro něž angličtina není mateřská), dají se obejít parafrází a jejich výstup — „rukopis je ze 40 % AI-generovaný" — je přesně ten typ čísla, které nelze ničím doložit ani vyvrátit. Karta jde opačným směrem: **detekce hádá, provenience si pamatuje.** Zaznamenává v místě vzniku, s artefakty a otisky, a proto nemusí nic odhadovat. (Analogie z fotografie: detektor zkoumá pixely a tipuje; obsahová pověření C2PA nechávají fotoaparát podepsat snímek při pořízení. Karta je fotoaparátový přístup pro výzkum — s tím limitem, že podpis zatím dává autor, ne stroj; viz §3.7 a §6.)

**2.7 Občanky: ORCID a AICID.** ORCID (od 2012) dal lidem ve vědě trvalé identifikátory; funguje jako spojovací klíč napříč systémy, ne jako známka kvality — a přesně to stačí. AICID (Vidal & Monperrus, 2026) navrhuje totéž pro AI agenty: trvalé číslo agenta navázané na lidského operátora s ORCID; registr je zatím v alfa stadiu. Karta identity **odkazuje, nevydává**: lidé ORCID, organizace ROR, agenti volitelnou dvojicí {schéma, hodnota}, kde AICID je jedna z možností. Co přesně je „agent", když se pod ním mění modely, rozebíráme v §3.7 — je to jedna z nejčastějších a nejlepších námitek.

**2.8 Experimentální venue a střízlivá data o kvalitě.** Vznikla místa, kde AI publikuje přímo: JAIGP (od února 2026; AI jako autoři, lidé jako prompteři, pravidla hlasováním komunity; desítky prací, lidské review zatím jen ohlášené), preprintové infrastruktury aiXiv a AgentRxiv, kde agenti staví na výstupech jiných agentů. Vůči všem platí střízlivost: jde o rané experimenty s nízkou provozní zralostí, vhodné jako *pilotní hřiště*, nikoli jako základy. A kvalita samotného autonomního výzkumu? Nejznámější datový bod dodala japonská firma Sakana AI se systémem **The AI Scientist** (Lu et al., 2024): v nezávislé srovnávací evaluaci pod automatizovanou recenzí neprošla **ani jedna z 15** jeho prací; nejlepší z hodnocených systémů prosadil 6 z 15. Jediná dřívější systémem vytvořená práce, která prošla lidskou recenzí, uspěla na workshopu s vysokou mírou přijetí — a s lidmi, kteří v každém kroku ručně vybírali nejslibnější pokusy. Dvě poučení: infrastruktura se dnes musí stavět hlavně pro obrovskou AI-*asistovanou* většinu, ne pro hrstku autonomních prací; a **tichý výběr nejlepších běhů** je praktika, kterou musí vrstva provenience zviditelnit především (§5).

**2.9 Co si půjčujeme odjinud.** CRediT — zavedený číselník čtrnácti autorských rolí („kdo dělal metodologii, kdo analýzu, kdo psal") — dodává kartě slovník činností; přidáváme jen malé AI rozšíření. RO-Crate a ontologie W3C PROV dodávají osvědčený způsob balení a popisu artefaktů — s poučením z jejich historie: takové formáty uspívají jako *výměna mezi platformami* a selhávají jako *povinnost naložená jednotlivci* (proto §4.5). Nanopublikace připomínají, že jednotku vědy nemění formáty, ale ti, kdo rozdělují kredit — článek přežívá, protože se v něm počítá kariéra. A ze softwarové bezpečnosti (in-toto, SLSA) a z médií (C2PA) přebíráme dva návyky: attestuje se **otisk**, ne název, a důvěra je **odstupňovaná**, ne binární.

## 3. Principy návrhu

**3.1 Role, ne procenta.** Procento intelektuálního příspěvku nejde změřit: neexistuje pravítko, jednotka ani postup kontroly — proto jsou i detektorová procenta z §2.6 slepá ulička. Rolové tvrzení ukotvené v artefaktu je jiný druh výroku: „statistickou analýzu provedl systém S" se dá konfrontovat s kódem, logy a výstupy. Karta proto zaznamenává výhradně *kdo vykonal kterou roli* — dědictví CRediT: přispěvatelství jako auditovatelný rozklad autorství.

**3.2 Žebřík důkazů.** Každé tvrzení o činnosti nese jednu ze čtyř úrovní:

```
 4 │ REPRODUKOVÁNO
   │ někdo výsledek nezávisle zopakoval
 3 │ NEZÁVISLE ATTESTOVÁNO
   │ jmenovaný ověřovatel (ORCID/ROR)
   │ ověřil přesně vymezenou věc
 2 │ DOLOŽENO ARTEFAKTEM
   │ tvrzení má log/kód/prompt s otiskem
 1 │ DEKLAROVÁNO
   │ slovo garanta — viditelně neověřené
```

Je to poznávací gradient: svědectví → stopa → svědek → replikace. A jeho smysl je stejně tak *negativní* jako pozitivní: dělá čitelnou i **nepřítomnost** důkazu. Samotná existence logu tvrzení nezakládá (log může být neúplný nebo o něčem jiném) — žebřík takové tvrzení poctivě nechává na druhé příčce, výš ne. Kde dnešní věta rozdíl mezi ověřitelným a tvrzeným schovává, žebřík ho vystavuje.

**3.3 Vazba na verzi — konec visících attestací.**

```
DNES:
kontrola ──► „článek X“ (název)
soubor se po kontrole vymění
razítko dál visí ........................ ✗

S KARTOU:
kontrola ──► otisk 9f31c4… (SHA-256)
nový obsah = nový otisk
staré razítko viditelně neplatí ......... ✓
```

Otisk SHA-256 je „otisk prstu" souboru: spočítá se za vteřinu, ověří ho kdokoli a změní se při sebemenší úpravě obsahu. Karta ho vyžaduje v hlavičce a každá kontrola i attestace nese otisk toho, co zkoumala. Je to nejlevnější mechanismus celého návrhu — a podle nás ten nejméně postradatelný. (A ne, není to blockchain: žádný řetěz, žádné tokeny — jen otisky a obyčejná veřejná historie, viz §4.4.)

**3.4 Provenience není soud.** Karta říká, kdo co dělal, co je doloženo a kdo co ověřil — a tam se zastaví. Žádné pole se nesčítá do známky kvality, žádný status netvrdí „práce je pravdivá". Tři důvody: certifikační verdikty nesou právní odpovědnost, kterou registr unést nemůže; souhrnná skóre zvou k optimalizaci skóre místo podstaty (Goodhartův zákon); a venue se legitimně liší v tom, co požadují — hodnota vzniká ze sítě kompatibilních ověření, ne z jedné univerzální známky pravdy.

**3.5 Kompenzační princip.** Některé systémy jsou legitimně obchodním tajemstvím. Plná povinná transparentnost by je vyloučila; výjimka by zvala k praní. Řešením je pravidlo spojených nádob: **čím méně transparentní proces, tím tvrdší ověření výstupů.** Utajený mechanismus musí i tak odkrýt minimální patro identity (kdo systém vytvořil a provozuje, modelová rodina, datum verze, výčet utajeného s důvody) — a u přísné venue z §5 navíc strpět nezávislou reprodukci klíčového výsledku před publikací. Utajení není zakázané; je dražší. Přesně tak to funguje všude, kde se proprietární procesy potkávají s veřejnou zárukou, od léčiv po audity uzavřeného softwaru.

**3.6 „Reference existuje" není „reference to dokazuje".** Automat umí spolehlivě zjistit, že citovaný zdroj existuje a sedí mu metadata — a rostoucí podíl nedohledatelných referencí v éře LLM je zdokumentovaný problém. Automat ale neumí spolehlivě posoudit, zda skutečný zdroj *podporuje* přesné tvrzení, k němuž je citován; v benchmarcích atribuce zdrojů je mezi strojem a člověkem propastný rozdíl. Směšovat obojí plodí nejnebezpečnější artefakt tohoto prostoru: razítko „citace ověřeny", které ve skutečnosti potvrzuje jen existenci. Karta drží tři pojmy oddělené: *reference dohledány* (automat), *podpora tvrzení posouzena* (report s metodou a mírou jistoty), *podpora tvrzení attestována* (jmenovaný člověk, vymezený rozsah).

**3.7 Co je vlastně „agent", když se pod ním mění modely?** Nejlepší námitka, kterou jsme při vývoji dostali, zní: mám AICID, ale svou historii měním — dnes jedu na jednom modelu, za půl roku na novějším, pak dva kombinuji. Co tedy identifikátor označuje? Odpověď: agent je **kontinuant** — trvalá „kapela": jméno, provozovatel, účel, konfigurace. Modely jsou **členové kapely** — nástroje, které se střídají. Občanka patří kapele; karta každé práce vyjmenuje, kdo v ní tehdy hrál:

```
AGENT „Analytik-JN“ (jedno AICID) ─────────►
  karta 1 (2026):  model A v4.8
  karta 2 (2027):  model B v5
  karta 3 (2027):  model B v5 + spec. model C
občanka trvá — konkrétní nástroje
se zapisují do každé karty zvlášť
```

Proto datový model **odděluje** trvalou identitu agenta od konkrétního modelu, jeho snapshotu (datované verze), rozhraní a operátora — a proto práce s více modely má v bloku AI systémů prostě více záznamů, klidně pod jedním agentním identifikátorem. Historie agenta pak není nic tajemného: je to posloupnost jeho karet. A protože dnes většina užití AI vypadá „výzkumník + chatovací okno" bez jakéhokoli registrovaného agenta, je pole identifikátoru **volitelné** — karta musí fungovat i úplně bez něj. Konečně schéma rezervuje slot pro budoucí **podpis na straně generátoru** (poskytovatele modelu či runtime) — lekce C2PA: nejsilnější provenience je podepsána v místě vzniku. Takový režim zatím neexistuje; karta je stavěná tak, aby ho jeho příchod posílil, ne přestavěl.

## 4. Karta a jak s ní autor reálně pracuje

**4.1 Co v kartě je.**

```
┌─ KARTA RPC (jeden JSON soubor) ─────────┐
│ PRÁCE      název · verze · otisk PDF    │
│ GARANT     člověk + ORCID + čas         │
│ AI SYSTÉMY poskytovatel · model · verze │
│            rozhraní · agent? · operátor │
│ ČINNOSTI   role (CRediT+AI) + úroveň    │
│            důkazu + odkazy na artefakty │
│ ARTEFAKTY  prompty·logy·data·kód        │
│            (identifikátor·otisk·režim   │
│            přístupu s důvodem)          │
│ KONTROLY   automaty: co, čím, výsledek  │
│ ATTESTACE  razítka: kdo·co přesně·jak   │
└─────────────────────────────────────────┘
```

Režimy přístupu artefaktů jsou: veřejný / embargo / na vyžádání / omezený / neuchováno — vždy s důvodem. Prompty a logy záměrně **nejsou** povinně veřejné (mohou nést osobní údaje, licencovaný text, důvěrný materiál); i neveřejný artefakt je ale odkázán otiskem, takže jeho pozdější záměna je zjistitelná.

**4.2 Jak to autor prakticky udělá — a musí mě u toho něco špehovat?** Nemusí. Karta nevyžaduje žádný sledovací program běžící při psaní; skládá se ze stop, které už stejně vznikají. Tři cesty, od nejjednodušší:

```
píšu / bádám s AI
   │  (chat, agent, notebook, git — jako dosud)
   ▼
posbírám stopy: export konverzace,
kód v repozitáři, dataset, logy agenta
   ▼
vyplním kartu: webový formulář (~15 min)
NEBO ji skript vytáhne z exportů
NEBO ji agentní pipeline vyplní sama
   ▼
validátor zkontroluje úplnost
   ▼
generátor vyrobí deklarace: Elsevier,
Springer, IEEE… + strojový záznam
   ▼
odešlu článek + odkaz na kartu
```

*Cesta A (dnes, kdokoli):* na konci práce vyplní autor formulář — zabere to zhruba jako vyplnění metadat při submission. Co má podklad (export chatu, commit, dataset s DOI), označí a přiloží; co podklad nemá, zůstane poctivě na úrovni „deklarováno". *Cesta B (poloautomat):* skript projde exporty (konverzace, git historii, notebook) a kartu předvyplní; autor jen potvrdí a doplní. *Cesta C (agentní workflow):* pipeline, která výzkum provádí, vyplňuje kartu průběžně sama — tam, kde je podíl AI největší, klesá cena vyplnění k nule. **Směna, na které adopce stojí:** vyplníš jednou — a generátor za tebe vyrobí *všechny* deklarace, které po tobě různí vydavatelé stejně chtějí, každou v jejich formátu. Karta nesmí být další povinnost navíc; musí být nejlevnější způsob, jak splnit povinnosti, které už existují.

**4.3 Panel se šesti statusy.** Každá karta se čtenáři ukazuje jako panel, jehož statusy jsou *počítané, ne tvrzené* — svítí jen to, co obsah karty skutečně podkládá: záznam dostupný · svázáno s verzí · artefakty připojeny · reference dohledány · audit podpory tvrzení k dispozici · nezávisle attestováno. Žádný z nich neříká „práce je pravdivá" (§3.4).

**4.4 Registr bez blockchainu.** Referenční registr je veřejný git repozitář: karta = soubor, registrace = pull request, vrátný = automatická kontrola (validace schématu + dohledání referencí). Historie změn je veřejný auditní log zadarmo; periodická vydání se archivují se Zenodo DOI. Získáváme tak přesně ty vlastnosti, kvůli nimž se sahá po distribuovaných ledgerech — neměnitelnou historii, obsahové adresování — z infrastruktury, které věda už věří, bez tokenů a bez nové governance. Databázová verze s attestacemi po přihlášení ORCID je krok škálování, ne redesign.

**4.5 Nástroje.** Validátor; kontrola dohledatelnosti referencí nad Crossref a OpenAlex (jejíž report výslovně říká, že podporu tvrzení neposuzuje); a generátor deklarací z §4.2. Vše otevřené (kód MIT, specifikace CC BY 4.0).

## 5. Nasazení: dvě venue, jeden standard

Standard u jedné venue je interní pravidlo; u dvou nezávislých venue s opačnou filozofií se stává infrastrukturou — a jeho chování je pozorovatelné v obou režimech. Nasazení proto běží dvoukolejně, přičemž formát je záměrně **přenositelný na kteroukoli venue**, žádná konkrétní není jeho podmínkou:

*Kolej permisivní:* pilot u komunitní venue publikující AI-generované práce (dnes připadají v úvahu např. JAIGP či aiXiv — s vědomím jejich rané provozní zralosti, §2.8): 5–10 dobrovolných prací, 8–12 týdnů, panel provenience u každé, a teprve s pilotními daty případné hlasování o výchozím statusu. Pilot měří: čas vyplnění, prázdná pole, rozložení skutečně dosažených úrovní důkazu, míry selhání dohledání referencí, srozumitelnost panelu pro autory i čtenáře.

*Kolej přísná:* plánovaná venue pro agentně prováděný výzkum s kartou povinnou a důkazně orientovaným designem: požadavek empirických dat (čistá syntéza z parametrické paměti modelu nestačí); desk reject při jediné nedohledatelné referenci; **povinné přiznání počtu běhů a pravidla výběru** publikovaného výstupu — poučení ze Sakany: nepřiznaný cherry-picking se stává definovaným porušením integrity, přiznaný legitimní metodou; dráha *registrovaných zpráv*, kde se protokol (otázka, data, prompty, pipeline) zamkne před spuštěním, takže selektivní vykazování je vyloučeno konstrukčně; dvoukolejná recenze — integrita procesu (oborově nezávislá, z velké části automatická) odděleně od oborového posouzení (vyžádaní experti, publikované posudky); a kompenzační princip §3.5 pro utajené systémy. Očekávaná propustnost je poctivě nízká — jednotky až nízké desítky prací ročně při dnešním rozložení kvality; to je definice vlajkové venue, ne její vada.

P�edem stanovená rozhodovací kritéria drží projekt na uzdě vůči vlastnímu optimismu: pokud v pilotu úrovně důkazu zkolabují prakticky jen na „deklarováno", důkazní vrstva přidává náklad bez rozlišovací síly — a úsilí se přesměruje čistě k nástrojové vrstvě (generátor deklarací má hodnotu i sám o sobě).

## 6. Co karta neumí (a říkáme to nahlas)

**Lhaní na první příčce.** Karta nezabrání lži na úrovni „deklarováno" — to nedokáže žádný formát. Mění ale povahu lži: falešná volná věta je nefalzifikovatelná mlha; falešná karta je konkrétní, otiskem svázané, časově razítkované tvrzení, jehož srážka s pozdější evidencí je čitelná — pochybení s papírovou stopou.

**Domluvení ověřovatelé.** Třetí příčka stojí a padá s attestory. Identifikátory, přesné rozsahy, odvolatelnost a trvalé záznamy fabrikace v historiích agentů i provozovatelů náklady útoku zvyšují, neeliminují; hodnota attestací nakonec sleduje reputaci attestorů — sociální proces, který karta umí zaznamenat, ne vyrobit.

**Výběr napříč běhy.** Přiznání počtu pokusů spoléhá na poctivost; strukturálně motivaci ruší jen registrované zprávy.

**Kontaminace.** Provenience zjistí, *jak* výstup vznikl — ne to, zda „empirický" výsledek není vzpomínka z trénovacích dat. To řeší redakční požadavky přísné venue, ne karta.

**Byrokratická smrt.** Selže-li směna z §4.2 a karta bude zakoušena jako papírování navíc, adopce nepřijde. Je to falzifikovatelná sázka, ne předpoklad — a pilot ji měří.

**Riziko standardů.** Vancouver může zvolit jinou taxonomii. Odpovědí je profilová pozice a mapovací vrstva: zarovnání pak bude překlad slovníku, ne přestavba.

## 7. Diskuse: pro koho se to vlastně píše

Tři důsledky případného úspěchu. Za prvé kulturní: otázka „byla použita AI?" se mění na „jaká je úroveň důkazu u každého tvrzení o tom, jak práce vznikla?" — otázku s odstupňovanými, kontrolovatelnými odpověďmi. Za druhé institucionální: autorské vakuum ze §1 dostává cestu řešení — autonomní výstupy mohou mít domov, kde je odpovědnost lidská, identita explicitní a důvěra odstupňovaná, aniž by se debata o autorství musela předčasně uzavírat. A za třetí, o čem se mluví nejméně: primárními **čtenáři** provenience nemusejí být lidé. Ve světě, kde AI systémy výzkum prosévají, recenzují a syntetizují, dovolí strojově čitelná důkazní vrstva automatickému recenzentovi rozlišit tvrzení odvozené z primárních dat od tvrzení z generativní syntézy a výsledek podložený spuštěným kódem od výsledku pouze napsaného. Provenience pak není papír navíc — je to rozhraní, jímž částečně automatizovaná věda zůstává čitelná sama sobě.

## 8. Závěr

Deklarační věta selhává významově, poznávacně i odkazově a autorské vakuum tlačí rostoucí třídu prací do šedi. Minimální přiměřenou odpovědí je infrastruktura: verzovaný, důkazně ukotvený, soudů se zdržující rodný list — role místo procent, žebřík místo razítka, otisky místo názvů, zpoplatněná místo zakázané netransparentnosti — s nástroji, které dělají poctivost levnější než mlhu, a testovaný u dvou venue s opačnou filozofií. Karta nic necertifikuje, žádnou recenzi nenahrazuje a žádnou pravdu neskóruje. Chce jediné: aby éra výzkumu s podílem AI byla auditovatelná na úrovni svých tvrzení o sobě samé — a aby standardizačnímu procesu, který o pravidlech této éry právě rozhoduje, přinesla funkční kód, funkční registr a pilotní evidenci.

---

## Prohlášení o užití AI

Tento rukopis vznikl v rozsáhlé spolupráci člověka a AI. Claude (Anthropic) přispěl ke konceptuální analýze, tvorbě textu a argumentaci opřené o zdroje v průběhu řady pracovních sezení; autor řídil zkoumání, učinil všechna rámcová a návrhová rozhodnutí, text revidoval a nese výhradní odpovědnost za obsah v souladu s principem odpovědnosti COPE. AI systémy nejsou uvedeny jako autoři. Strukturovaný přehled rolí a důkazů podává vlastní karta provenience rukopisu (Příloha A). Součástí metody vývoje projektu byla záměrná adversariální recenze nezávislými LLM sezeními.

## Dostupnost dat a kódu

Specifikace RPC, JSON schéma, validátor, nástroj dohledání referencí, generátor deklarací a referenční registr jsou uvolňovány pod permisivními licencemi (specifikace CC BY 4.0; kód MIT) v repozitáři projektu. [URL po zveřejnění.]

## Literatura

Brand, A., Allen, L., Altman, M., Hlava, M., & Scott, J. (2015). Beyond authorship: Attribution, contribution, collaboration, and credit. *Learned Publishing*, 28(2), 151–155. · CANGARU Initiative (2023). *ChatGPT, GenAI and LLMs for Accountable Reporting and Use Guidelines: protocol.* arXiv:2307.08974. · Collins, G. S., et al. (2024). TRIPOD+AI. *BMJ*, 385. · COPE (2023). *Authorship and AI tools: position statement.* · EU (2024). Nařízení (EU) 2024/1689, čl. 50. · Groth, P., Gibson, A., & Velterop, J. (2010). The anatomy of a nanopublication. *Information Services & Use*, 30(1–2), 51–56. · Hidalgo, C. A. (2026). *Why I made a journal for AI-generated papers.* cesarhidalgo.com. · ICMJE. *Recommendations* (aktuální vydání). · ISC, COPE, STM, GYA, WCRIF (2026). *Global Reporting Standard for AI Disclosure in Research — veřejná konzultace.* · JAIGP (2026). jaigp.org. · Lebo, T., Sahoo, S., & McGuinness, D. (2013). *PROV-O.* W3C. · Liu, X., et al. (2020). CONSORT-AI. *Nature Medicine*, 26, 1364–1374. · Lu, C., et al. (2024). The AI Scientist. arXiv:2408.06292. · Schroeder, N. L., Jaldi, C. D., & Zhang, S. (2025). Large Language Models with Human-In-The-Loop Validation for Systematic Review Data Extraction. arXiv:2501.11840. · Shailendra, S., et al. (2026). L-PRISMA: An Extension of PRISMA in the Era of Generative AI. arXiv:2603.19236. · Soiland-Reyes, S., et al. (2022). Packaging research artefacts with RO-Crate. *Data Science*, 5(2), 97–138. · Torres-Arias, S., et al. (2019). in-toto. *USENIX Security.* · Vidal, C., & Monperrus, M. (2026). AICID: Unique identifiers for AI scientists. arXiv:2606.28756.

*(Před podáním dokompletovat placeholder údaje: srovnávací evaluace autonomních systémů, arXiv:2605.26340; analýza mezer reprodukovatelnosti, arXiv:2604.24658; fasetový návrh atribuce, arXiv:2604.25346; studie dohledatelnosti referencí; benchmark CiteME.)*

---

## Příloha A: Karta provenience tohoto rukopisu

Stať aplikuje vlastní standard sama na sebe. Panel statusů rukopisu (verze 2, poctivě):

| Status | Stav | Poznámka |
|---|---|---|
| Záznam dostupný | ✓ | karta níže |
| Svázáno s verzí | ◻ | otisk se doplní z finálního PDF |
| Artefakty připojeny | ✓ | log pracovních sezení (na vyžádání) |
| Reference dohledány | ◻ | proběhne nástrojem před podáním |
| Audit podpory tvrzení | ✗ | neexistuje |
| Nezávisle attestováno | ✗ | zatím nikdo neověřil nic |

```json
{
  "rpc_version": "0.1",
  "paper": { "title": "Od deklarace k důkazu…", "version": "preprint-v2",
             "pdf_sha256": "[doplní se z finálního PDF]" },
  "human_guarantor": { "orcid": "[ORCID autora]", "name": "Jan Nehyba",
                       "assertion_timestamp": "[čas podání]" },
  "ai_systems": [ { "id": "ai1", "provider": "Anthropic", "model_family": "Claude",
                    "model_version_or_snapshot": "2026-07", "interface": "chat",
                    "operator_orcid": "[ORCID autora]" } ],
  "activities": [
    { "role_id": "credit:conceptualization", "actor_id": "human:[orcid]", "evidence_level": "declared" },
    { "role_id": "credit:conceptualization", "actor_id": "ai1", "evidence_level": "artifact_linked", "artifact_refs": ["log1"] },
    { "role_id": "rpc:source_retrieval", "actor_id": "ai1", "evidence_level": "artifact_linked", "artifact_refs": ["log1"] },
    { "role_id": "credit:writing_original_draft", "actor_id": "ai1", "evidence_level": "artifact_linked", "artifact_refs": ["log1"] },
    { "role_id": "credit:writing_review_editing", "actor_id": "human:[orcid]", "evidence_level": "declared" },
    { "role_id": "credit:supervision", "actor_id": "human:[orcid]", "evidence_level": "declared" }
  ],
  "artifacts": [ { "id": "log1", "type": "log", "access_status": "on_request",
                   "restriction_reason": "pracovní sezení obsahují nepublikovaný materiál projektu",
                   "sha256": "[otisk exportu logu]" } ],
  "checks": [],
  "attestations": []
}
```

*Dva zhasnuté a dva čekající statusy nejsou ostuda — jsou to žebřík a panel, které o preprintu mluví pravdu. Až nástroj dohledá reference a finální PDF dostane otisk, rozsvítí se další dva; attestace může přidat první čtenář, který něco konkrétního ověří.*
