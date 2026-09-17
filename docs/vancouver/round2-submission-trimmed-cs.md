# Podnět do 2. konzultačního kola, pracovní překlad

**Global Reporting Standard for AI Disclosure in Research („Vancouver Standard")**
Focus Track WCRI 2026 · ISC · WCRIF · COPE · STM · GYA
Uzávěrka: **16. října 2026** · Formulář: <https://council.science/AIdisclosure>

> **Tento soubor se neodesílá.** Konzultace probíhá anglicky, odesílá se
> [`round2-submission-trimmed-en.md`](./round2-submission-trimmed-en.md).
> Tenhle překlad je na to, abyste si obsah zkontroloval v češtině.

---

**K téhle verzi.** Anglická verze je psaná záměrně jednoduše. V odpovědi 1A(c) se tvrdí, že standard nesmí být těžší pro lidi, kteří nepíšou anglicky. Podnět, který by to tvrdil složitou angličtinou, by si ten argument podrazil. Před odesláním otevřete formulář v prohlížeči a zkontrolujte, že otázky sedí s tím, co bylo ověřeno 29. 7. 2026. Doporučené odpovědi u zaškrtávacích otázek jsou označené ▶.

## Respondent

| Položka | Hodnota |
|---|---|
| Jméno | Jan Nehyba |
| Role | odborný asistent, Pedagogická fakulta, Masarykova univerzita, Brno |
| ORCID | 0000-0003-4159-5576 |
| Za koho | osobní stanovisko fyzické osoby |
| Obor | pedagogický výzkum, sociální vědy, kvalitativní metody |
| Země | Česko |
| Kontakt | *[institucionální e-mail, doplnit před odesláním]* |

**Odkud to vychází.** Jsem kvalitativní výzkumník. Zkoumám, jak lidé uvozují, podepisují a označují texty psané s AI, a jak se to liší podle žánru: vědecké články, e-maily a zprávy, výukové a interní materiály, softwarové projekty, závěrečné práce a sociální sítě. Ten výzkum se ptá, co přiznání doopravdy říká, ne co by podle standardu říkat mělo. Nic z toho, co následuje, na jeho zjištěních nestojí. Zatím žádná nemá.

### Jak tento podnět vznikl

**Tento text napsala AI.** Ne „s určitou pomocí AI" v tom obvyklém smyslu. Velké jazykové modely napsaly každý jeho oddíl, během několika pracovních sezení, a znění je jejich. Já jsem určoval směr, rozhodoval, co v textu bude a co ne, a ručím za všechno, co v něm stojí.

Uvádím to tady ve formátu řádku, který sám v podnětu navrhuji. Podnět, který se zastává přiznávání a svůj vlastní vznik zamlčí, by nestál za čtení. Zároveň to ukazuje slepé místo popsané v 1B(3): třetí řádek je reálné užití, které by žádné pravidlo založené na textu nezachytilo.

| Činnost | Aktér | Co bylo zkontrolováno a kým | Stopa | Co zkontrolovat nešlo |
|---|---|---|---|---|
| Psaní a přepisování všech oddílů | Claude (Anthropic), Opus 5, září 2026; dřívější verze jiné modely | Přečetl jsem to a zkontroloval na úrovni argumentů a rozhodnutí. Za každým doporučením stojím. | Veřejná historie commitů: <https://github.com/JanNehyba/research-provenance-card/commits/vancouver/round2-trimmed> | Jestli modely neovlivnily znění argumentů, se kterými jsem souhlasil, způsobem, kterého jsem si nevšiml |
| Hledání a ověřování literatury | Totéž | Každý zdroj otevřen v originále a u každého je zaznamenáno, jak byl ověřen. | Záznam o ověření zdrojů, veřejný: <https://github.com/JanNehyba/research-provenance-card/blob/vancouver/round2-kit/docs/reserse.md> | Tři zdroje byly ověřeny jen z abstraktu, ne z plného textu |
| Utváření argumentu | Já, s modelem v roli kritika, který měl za úkol napadat mé zarámování | Nezávisle nezkontrolováno | **Žádná. Ta výměna po sobě nenechala trvalý záznam.** | Jak velká část zarámování z té výměny vzešla. Nedokážu to zpětně zrekonstruovat. |
| Rozhodování, co zahrnout a co vyškrtnout | Já | Nezávisle nezkontrolováno | Tatáž historie commitů | Nic. Byla to moje rozhodnutí a stojím si za nimi. |

Repozitář: <https://github.com/JanNehyba/research-provenance-card>
(Popsaná práce je na větvích `vancouver/round2-trimmed` a `vancouver/round2-kit`, ne na výchozí větvi.)

Za každé tvrzení v tomto podnětu ručím.

---

## 0: Přehled: sedm návrhů

| # | Návrh | Otázka |
|---|---|---|
| **P1** | Dát každé kategorii taxonomie **stabilní strojově čitelný identifikátor**, tedy slug, ne pořadové číslo, a verzovat samotnou taxonomii, včetně pravidel pro zrušení a nahrazení kategorie. CRediT to udělal jako ANSI/NISO Z39.104-2022. Bez stabilních identifikátorů nemůže nikdo dál v řetězci dodat „strojovou čitelnost". | 3 |
| **P2** | Udělat jednotkou deklarace **řádek, ne větu**. Jeden řádek na činnost, aktéra, kontrolu a stopu. Volný text může řádek doplnit. Nemůže ho nahradit, mají-li být deklarace srovnatelné. | 3 |
| **P3** | Dát každému řádku **úroveň ověření** z uzavřeného seznamu. Kritéria 1. kola i vlastní žebříček Focus Tracku (attestace, review, audit, replikace) k tomu už míří. Uzavřený seznam je to, co z toho udělá strojově čitelný údaj. | 5 |
| **P4** | **Svázat deklaraci s verzí, o níž mluví**, otiskem obsahu (SHA-256) přijatého souboru. Dnes se deklarace váže k názvu, ne ke stavu souboru. Proto přežije tichou výměnu obsahu. | 4, 5 |
| **P5** | Doplnit **tři chybějící kategorie**: orchestraci (konfigurace a řízení systému), ověřování prováděné AI, a výběr mezi více běhy či výstupy. | 3 |
| **P6** | **Ponechat aspoň jedno povinné pole, které stroj sám nevyplní.** Záznam, který celý vygeneruje agent a zkontroluje druhý agent, může být úplný, správně tvarovaný a prázdný. | 5 |
| **P7** | **Zavést trvalý identifikátor pro samotné systémy AI**, po vzoru RRID, ne po vzoru autorství. Pojmenovaný, verzovaný a citovatelný identifikátor nástroje je to, co z otázky „který model a která verze" udělá ověřitelný údaj místo fráze. | 3, 5 |

### Proč návrhy vypadají takhle

Užitečné rozlišení přichází z blízkého oboru. Corbin, Dawson a Liu (2025) popisují dva druhy změn v hodnocení.[^1] **Diskurzivní** změny fungují jen tím, že lidem říkají, co mají dělat. **Strukturální** změny mění to, jak musí být úkol proveden. Jejich argument je, že samotné instrukce neobstojí, protože lidé je mohou ignorovat.

Totéž platí tady. Standard, který předepíše větu, kterou má autor napsat, je diskurzivní. Standard, který definuje záznam s povinnými poli a uzavřeným seznamem úrovní ověření, je strukturální. Všech sedm návrhů se snaží posunout tenhle standard od prvního druhu ke druhému.

[^1]: Corbin, T., Dawson, P., & Liu, D. (2025). Talk is cheap: why structural assessment changes are needed for a time of GenAI. *Assessment & Evaluation in Higher Education*, 50(7), 1087-1097. Ten článek je o hodnocení studentů, ne o přiznávání AI. Přebírám to rozlišení, ne jeho zjištění.

---

## 1: Které užití AI se má přiznat? (Práh)

### 1A. Stanovisko k navrženému prahu

**Podporuji kvalitativní práh tak, jak je napsaný, včetně rozhodnutí nepoužívat kvantitativní prahy.** Zdůvodnění v poznámce pod čarou je správné a finální standard by to měl říct ještě jasněji. Pro „procento přínosu AI" neexistuje jednotka. Nic ji neměří a žádný postup ji neaudituje.

Procenta selhávají dvěma způsoby. Autoři hádají. A detektory vyrábějí čísla typu „tento rukopis je ze 40 % od AI", která nikdo nemůže potvrdit ani vyvrátit. Tvrzení o rolích a činnostech je jiný druh tvrzení. Dá se přiložit ke kódu, k logům, k výstupům a ke jménům lidí.

Podporuji i kritérium (1), tedy že úsudek utvářený AI se má přiznat **i když výsledek potom ověřil člověk**. To je nejdůležitější věta v návrhu. Zavírá nejčastější únikovou cestu, tedy „zkontroloval jsem to, takže je to moje".

Tři upřesnění.

**(a) Ať práh neunese všechno sám.** Jediná čára, za kterou platí pro všechny stejná cena za vykazování, vytváří sráz. Překročíte ji a platíte plnou cenu. Zůstanete těsně pod ní a neplatíte nic. Autor blízko té čáry má tedy všechny důvody dokazovat, že je pod ní.

Doplňte práh o **odstupňovaný záznam** (P3). Malé užití se pak dá poctivě vykázat jedním levným řádkem na nejnižší úrovni. Velké a dobře zdokumentované užití se vykáže jako takové. Škálovat se nemá to, *jestli* přiznáváte. Má se škálovat to, *kolik důkazů záznam nese*.

**(b) Slovo „podstatný" potřebuje příklady, ne lepší definici.** Test recenzenta je ten správný test a další abstraktní vybrušování nepomůže. Pomůže malá sada zpracovaných příkladů pro každý obor, řekněme tucet, udržovaná a citovatelná jako součást živého standardu. Sítě metodických doporučení si takhle příklady postupně budují. Za pedagogický výzkum je můžu dodat.

**(c) Jazyková práce nesmí být zdaněna podle mateřského jazyka.** Kategorie 17 (Translation) a jazyková část kategorie 18 vytvářejí nerovnost.

Český, ukrajinský nebo indonéský výzkumník přemýšlí a píše v rodném jazyce a potom použije AI, aby z toho vznikl anglický text. Intelektuální práce je stejná jako u anglofonního kolegy. Při doslovném čtení prahu ale musí přiznat víc. První kolo uzavřelo, že standard nesmí být těžší pro hůř situované komunity. Právě tady se ten slib zkouší.

Navržené znění: **překlad vlastního obsahu autora, se zachovaným významem a s autorovou kontrolou, je technické užití pod prahem. Obsah vytvořený AI je nad prahem, a to v jakémkoli jazyce.** Hranice vede podle toho, kdo obsah napsal, ne podle jazyka, ve kterém vznikl.

### 1B. Tři příklady z mého oboru (pedagogický výzkum, kvalitativní metody)

1. **Vyžaduje přiznání.** LLM udělá první průchod tematického kódování přepisů rozhovorů. Výzkumník potom kódy prochází, rozhoduje a upravuje. Úsudek, který by normálně dělal vyškolený člověk, byl předán. Následná kontrola povinnost přiznat neruší (kritérium 1). Kategorie: kvalitativní analýza dat.

2. **Nevyžaduje přiznání.** Oprava pravopisu a interpunkce a přeformátování seznamu literatury v textu, který autor sám napsal a promyslel. Na významu se nic nemění.

3. **Sporné, a tvrdím, že je to nad prahem.** Autor dlouhodobě používá LLM jako sparingpartnera při návrhu práce. Model má za úkol napadat autorovo zarámování. Zarámování se tím mění.

   **Do rukopisu se nedostane ani jedna věta z modelu.** Každé pravidlo, které se dívá na text, tedy nehlásí nic. Přitom ta výměna utvářela návrh práce.

   Takhle pracuji a zarámování mé práce se tím opravdu mění. Viz třetí řádek v tabulce výše. To užití jsem přiznal a nedokázal jsem zrekonstruovat, jak velká část zarámování z něj vzešla. Podle kritérií (1) a (3) se to má přiznat, ale žádná kategorie na to nesedí. Kategorie *orchestrace*, navržená v 3B (P5), má tu díru zaplnit.

   Označuji to za případ, kde je současná praxe nejsystematičtěji slepá, a důvod je prostý. Přínos AI je ve výstupu neviditelný.

### 1C. Souhlas s tvrzeními

| Tvrzení | Odpověď |
|---|---|
| Užití AI, které podstatně utváří obsah výzkumu, interpretaci, vykazovaný obsah nebo výsledky, se má přiznat. | ▶ **Rozhodně souhlasím** |
| Standard má stanovit minimální práh pro přiznání a zároveň umožnit autorům přiznat víc, pokud chtějí. | ▶ **Rozhodně souhlasím** |
| Běžná oprava pravopisu, gramatiky, formátování citací nebo kosmetické úpravy mají vyžadovat přiznání. | ▶ **Spíše nesouhlasím** |
| Opakovaná drobná užití AI se mohou stát předmětem přiznání, když jejich souhrnný vliv utváří práci. | ▶ **Rozhodně souhlasím** |

---

## 2: Kde se má užití AI přiznat? (Umístění)

### 2A. Umístění

▶ **Informace o užití AI může být jak v hlavním textu článku, tak v samostatném prohlášení.**

### 2B. Které informace kam

Tři úrovně, za nimiž stojí jeden zdroj pravdy.

1. **Metody a popisky obrázků, volným textem.** Proč byla AI použita, jak zapadla do designu a co to znamená pro čtení výsledků. To je metodologická transparentnost a patří tam, kde se popisuje metoda. Standardizovat se to nedá dál než na úroveň řízeného slovníku a nemá se to dělat.

2. **Samostatné strukturované prohlášení, srovnatelné a strojově čitelné.** Řádky: činnost, aktér, úroveň ověření, stopa, podmínky přístupu. Publikované vedle prohlášení o přispění autorů a o střetu zájmů, a dostupné jako data, ne jen jako vysázený text. Tohle je to, co vůbec umožní srovnávání napříč články a screening ve velkém.

3. **Záznam v repozitáři, který drží důkazy.** Prompty, logy, kód, výstupy, s trvalými identifikátory, otisky a stavem přístupu. Ne v článku. Odkazované z něj.

**Jeden implementační detail je důležitější, než vypadá.** Úrovně 1 a 2 musí vzniknout z jednoho záznamu. Nesmí se psát dvakrát. Dva ručně psané popisy téhož se časem rozejdou a čtenář nepozná rozejití od podvodu. Takže: nejdřív definujte záznam, potom definujte, jak se zobrazuje.

### 2C. Další poznámky k umístění

Námitka, že to prodlouží články, je oprávněná a úroveň 2 na ni odpovídá. Strukturované prohlášení jsou **data připojená k článku, ne slova uvnitř něj**. Nemá se počítat do rozsahu, stejně jako se nepočítá prohlášení o střetu zájmů.

Námitka o stigmatu si zaslouží přímou odpověď. Ano, samostatné prohlášení dnes AI vyčleňuje a za deset let to bude vypadat jako přechodné opatření. To je v pořádku. Prohlášení o přispění autorů bylo taky kdysi novinkou a zavedlo se kvůli jednomu konkrétnímu problému s integritou. Navrhněte ten záznam tak, aby se dal později začlenit do obecného záznamu o přispění (P1, P2), místo abyste se mu teď vyhýbali.

---

## 3: Jak má být přiznání strukturováno? (Taxonomie)

### 3A. Je navržená taxonomie s 18 kategoriemi přiměřená?

▶ **Většinou přiměřená.**

### 3B. Stanovisko k taxonomii

Míra podrobnosti je v zásadě správná. Oddělení kvantitativní a kvalitativní analýzy dat (12 a 13) je správné rozhodnutí. Stejně tak oddělení vizualizace dat od generování obrázků (14 a 15). Obojí předchází skutečným nejasnostem o tom, co AI vlastně dělala.

**Překryvy, které je potřeba vyřešit.**

- 8 *Data collection (operations)* proti 9 *Data creation*. „Creation" se čte jako generování syntetických nebo simulovaných dat, ale dá se číst i jako sběr. Přejmenovat 9 na *Synthetic or simulated data generation* a obě definovat.
- 4 *Literature summarization* proti 16 *Drafting text*. Přehledová část napsaná AI je obojí. Stanovit pravidlo: třídí se podle činnosti a na jedno užití se smí uvést víc kategorií.
- 18 spojuje editaci a přepisování se seznamy literatury. Práce s citacemi má vlastní selhání, které si každý může ověřit, totiž citace, které nikam nevedou. Zaslouží si oddělení od úprav textu.
- Zacházet s 5, 6 a 7 jako s podkategoriemi *Design* je dobré. Udělejte ten vztah nadřazenosti explicitní a strojově čitelný, jinak ho každý implementátor zploští jinak.

**Strukturální doporučení. Tahle část rozhoduje, jestli je „strojová čitelnost" skutečná.**

1. **Používejte stabilní identifikátory, slugy místo čísel** (P1). `vs:literature-search`, ne „kategorie 3". Čísla se rozbijí, jakmile se kategorie přidá nebo zruší. Publikujte seznam jako verzovaný strojově čitelný slovník, v JSON nebo SKOS, s poli `deprecated` a `replaced_by`. CRediT šel cestou ANSI/NISO Z39.104-2022 a právě proto dnes CRediT v metadatech funguje.

   **Totéž platí pro aktéry, nejen pro kategorie** (P7). „Použili jsme GPT-4" není identifikátor. Řádek má uvést poskytovatele, rodinu modelu, verzi nebo snapshot a rozhraní. A ještě lépe má odkázat na trvalý identifikátor toho systému.

   **Precedent už existuje a není to autorství.** Research Resource Identifiers (RRID) dávají protilátkám, buněčným liniím, modelovým organismům, softwarovým nástrojům a databázím trvalý strojově čitelný identifikátor, který se nikdy nemění a je stejný napříč vydavateli. Žádný z těch zdrojů není autor. Identifikátor existuje proto, aby čtenář nebo nástroj našel všechny články, které použily tentýž zdroj, a aby se z „použili jsme komerční protilátku" stal ověřitelný údaj.

   Model AI je přesně takový výzkumný zdroj. Má výrobce, má verzi a jeho chování se mezi verzemi mění. Navrhuji, aby standard vyzval k **trvalým identifikátorům pro systémy AI po vzoru RRID** a aby je řádek deklarace nesl.

   Aby bylo jasné, co to není. Nenavrhuji, aby se systém AI považoval za autora. COPE tuhle otázku uzavřelo a souhlasím s ním. Identifikace není autorství: datová sada má DOI a autorem není, protilátka má RRID a autorem není. Práce, která systémy AI jako autory rámuje, existuje (AICID, Vidal a Monperrus, arXiv 2606.28756), a já záměrně navrhuji tu slabší a užitečnější verzi. Jde o to, aby **nástroj, který jednal**, byl označen stejně přesně jako člověk, který za něj odpovídá.

   Bez toho se „strojová čitelnost" zastaví u kategorie a nikdy nedojde k aktérovi, což je přitom údaj, který chce čtenář ověřit nejčastěji.

2. **Řádky, ne věty** (P2). Samotná kategorie deklaraci nenese. Nejmenší užitečný řádek je: činnost (ID kategorie), aktér (který systém AI, nebo který člověk), co bylo zkontrolováno a kým, a stopa (jaký záznam existuje a jak se k němu dostat). To je přesně ta struktura, o kterou žádalo 1. kolo: pevné jádro a místo pro volný popis.

3. **Taxonomie třídí činnosti a deklarace potřebuje ještě jednu osu.** Návrh to sám říká, když seznam označuje za „pouhou klasifikaci výzkumných činností". Souhlasím a právě o to jde. Bez osy ověření (oddíl 5) taxonomie čtenáři řekne, čeho se AI dotkla. Neřekne mu, co s tím kdo udělal.

4. **Tři chybějící kategorie** (P5). Všech 18 kategorií popisuje výzkumnou činnost, kterou vykonala AI. Tři úkony s odlišnými vlastnostmi pro integritu se do nich nevejdou.

   - **Orchestrace, neboli řízení agenta.** Lidský úkon konfigurace, promptování a řízení systému, včetně nadřízeného agenta, který vybírá specializované agenty. Právě tady může AI podstatně utvářet práci, aniž by ve výstupu zanechala stopu, jako v příkladu 1B(3). Žádná kategorie, která se dívá na výstup, to nevyjádří. Jediným artefaktem bývá prompt nebo protokol, a právě proto by to mělo být předmětem přiznání.

   - **Ověřování prováděné AI.** Kontrola, kterou dělá AI: dohledávání citací, posuzování, jestli je tvrzení podložené, audit statistiky, kontrola kódu. To je jiný úkon než tvorba výzkumného materiálu a má jiné vlastnosti pro integritu. Kategorie 10 a 11 to propašovaly pod slovem „auditing". Má být zaznamenatelné jako to, čím je, a nést vlastní úroveň důkazu (P3).

   - **Výběr mezi více běhy či výstupy.** Který běh byl uveden, z kolika a podle jakého pravidla. Nepřiznaný výběr nejlepšího z mnoha běhů je neviditelný v každém schématu přiznání, které znám, včetně tohoto návrhu. Je to otázka integrity, ne implementace. Kategorie umožní přiznání. Udělat ho povinným pro agentní řetězce je samostatné rozhodnutí o pravidlech a podpořil bych ho.

---

## 4: Má být neprázdné přiznání povinné?

### 4A. Souhlas s tvrzeními

| Tvrzení | Odpověď |
|---|---|
| Časopisy mají po autorech vyžadovat neprázdné přiznání, včetně záporného prohlášení, když AI podstatně nepoužili. | ▶ **Rozhodně souhlasím** |
| Souhlas s politikou vydavatele o přiznávání AI je dostatečně přesvědčivý na to, aby se dalo věřit, že vykázání bylo přesné. | ▶ **Rozhodně nesouhlasím** |

### 4B. Stanovisko k povinnému neprázdnému přiznání a k záporným prohlášením

**Podporuji, ale z jiného důvodu, než se obvykle uvádí.** Argument o změně kultury je v pořádku, ale měkký. Silný argument je důkazní.

Mlčení nelze vyvrátit. Záporné prohlášení je konkrétní, datované tvrzení jmenovaného člověka. Když se později ukáže podstatné nepřiznané užití AI, mlčení vám dá spor o výklad ve stylu „nikdo se neptal". Záporné prohlášení vám dá doložené nepravdivé tvrzení se jménem a datem.

Povinné neprázdné přiznání nezabrání nepoctivosti. Promění mlhu v písemnou stopu. To je velký zisk za cenu jednoho řádku.

Dvě podmínky. Bez nich se ze záporného prohlášení stane přesně ta prázdná věta, kterou má standard nahradit.

1. **Svázat ho s přijatou verzí** (P4). Prohlášení učiněné při podání a už nikdy nezopakované je tvrzení o souboru, který už neexistuje. Vyžadovat jeho potvrzení při přijetí, navázané na otisk obsahu přijatého rukopisu. Tím se zavře problém, kterému bych říkal **visící attestace**: kontrola, která přežila to, co kontrolovala. Otisk SHA-256 se spočítá za vteřinu a kdokoli ho může ověřit. Je to nejméně využitý mechanismus, který má tenhle standard k dispozici.

2. **Nenechat zaškrtávátko, ať to zastoupí.** Souhlas s politikou vydavatele při podání je pro čtenáře neviditelný a zpětně se nedá ověřit. Prohlášení musí být publikované s článkem.

**Ke stigmatu.** Riziko je skutečné, ale záleží hlavně na znění. Záporné prohlášení formulované jako nepřítomnost užití *dosahujícího prahu*, umístěné ve stejném bloku jako prohlášení o střetu zájmů, spíš normalizuje než vyčleňuje. Větší riziko stigmatu je dnes opačné. Ti, kdo přiznávají poctivě, vypadají hůř než ti, kdo nic neřekli.

---

## 5: Jak signalizovat odpovědnost?

### 5A. Má být obecné prohlášení o odpovědnosti součástí přiznání?

▶ **Ano, výchozí prohlášení má být součástí standardu.**

### 5B. Stanovisko k obecným prohlášením o odpovědnosti

Zahrnout ho, ale nenechat ho stát samotné, a udělat ho **přiřaditelným konkrétní osobě, ne kolektivním**.

„Autoři přebírají plnou odpovědnost" platí o každém článku, který kdy vyšel. Čtenáři to tedy neříká nic a námitka o odškrtávání políček je v tomhle znění oprávněná. Co čtenáři něco říká, je jmenovaný člověk s trvalým identifikátorem, který přebírá odpovědnost za konkrétní užití AI v konkrétním čase. Jeden ručitel na každý přiznaný řádek, kde bylo užití podstatné, podobně jako u role korespondenčního autora. Nestojí to autora nic, co by už nevěděl.

Takže: ponechat výchozí větu pro obecný případ a vyžadovat **jmenovaný dohled u každého podstatného užití**. Viz 5E, poslední řádek, který hodnotím jako zásadní.

**Poznámka k žánrům, které standard nepokrývá.** Přiznání je zároveň jazykový akt. Jeho znění se dá rozložit na to, kdo text posílá, kdo vybral slova a kdo za obsah ručí. Tyhle složky se mimo vědecký článek kombinují jinak.

E-mail, který začíná „Zde je shrnutí od AI", říká čtenáři něco, co prohlášení psané pro článek neřekne. Prezentace podepsaná jen jménem si nárokuje autorství i odpovědnost naráz. Trailer `Co-Authored-By:` v commit message, což je zavedená konvence v gitu a v nástrojích pro psaní kódu s AI, dává systému AI podíl na autorství a žádnou odpovědnost. Stránka s prohlášením u závěrečné práce dělá totéž ve formě, kterou předepsala univerzita.

Standard psaný pro vědecké články nepokryje e-maily, výukové materiály ani interní podklady, kde se táž odpovědnost řeší jinými prostředky: podpisy, zvyklostmi kontroly, pravidly pojmenování. Navrhuji, aby standard svůj žánrový rozsah uvedl otevřeně a nevytvářel dojem, že prohlášení psané pro článek je vzorem pro veškerou komunikaci.

### 5C. Jaké informace o ověření a dohledu mají autoři uvádět

**Strukturovaně, ne vyprávěním, ale s místem pro vyprávění.** Ukázková prohlášení v přípravném materiálu ten problém ilustrují. Obecná ukázka, „autoři zkontrolovali a upravili veškerý obsah vytvořený AI", se nedá vyvrátit. Ukázky označené jako důsledná a popisná jsou dobré, ale nejde je porovnat napříč články, prohnat screeningem ve velkém ani zkontrolovat na vnitřní rozpory.

Řádek o pěti slotech na každé přiznané užití se vyplní za pár minut a dá se porovnávat.

| Slot | Obsah | Proč |
|---|---|---|
| 1. Činnost | ID kategorie z taxonomie | Aby šly řádky porovnávat |
| 2. Aktér | Který systém AI: poskytovatel, rodina modelu, **verze nebo snapshot**, rozhraní. Nebo který člověk. | „Použili jsme LLM" není popis nástroje. Datovaná verze ano. |
| 3. Co bylo zkontrolováno a kým | Uzavřený seznam: *nezkontrolováno* · *autor přečetl* · *namátkově, uveďte jakou část* · *celé znovu spočítáno* · *ověřeno proti primárním zdrojům* · *zkontrolováno jmenovanou třetí stranou* · *nezávisle zopakováno* | Tohle je osa, která z přiznání dělá odpovědnost |
| 4. Stopa | Jaký záznam existuje (prompt, log, kód, výstup), jeho identifikátor a otisk, a stav přístupu: *veřejné · v embargu · na vyžádání · omezené · neuchováno*, s důvodem vždy, když není veřejný | Prompty a logy často publikovat nelze, kvůli osobním údajům, licencovanému textu nebo materiálu třetích stran. I nepublikovatelný záznam se dá odkázat otiskem, což umožní odhalit pozdější výměnu. |
| 5. Co zkontrolovat nešlo | Krátký volný text, **povinný** | Nejinformativnější pole celého záznamu, a první, které vypadne, když bude volitelné |

**P6: ponechat aspoň jedno pole, které stroj nevyplní.** Kritéria konzultace žádají záznamy, které jsou strojově čitelné a strojově generovatelné. Obojí je užitečné. Dohromady to ale nese riziko, které stojí za pojmenování.

Čím je záznam strukturovanější, tím snáz ho agent vyrobí. Když celé přiznání dokáže napsat agent a zkontrolovat ho druhý agent, stane se úplný, správně tvarovaný a naprosto prázdný záznam tou nejlevnější věcí v celém řetězci. Vypadá hotově, netvrdí nic, a práci to přesouvá na čtenáře.

Ochrana už v návrhu výše je. Má se jen vyslovit jako princip, ne nechat na náhodě: **každý záznam musí obsahovat aspoň jedno povinné pole, které nelze poctivě vyplnit, aniž by člověk něco skutečně udělal.** V tomhle návrhu jsou taková pole dvě. Slot 5 je povinný volný text o tom, co zkontrolováno nebylo. A jmenovaný ručitel je člověk s identifikátorem, kterého se dá zeptat.

Stejná logika prochází i seznamem ve slotu 3. Stroj napíše „nezkontrolováno" nebo „autor přečetl", aniž by kdo cokoli četl. Nenapíše „zkontrolováno jmenovanou třetí stranou" ani „nezávisle zopakováno", aniž by někoho jmenoval nebo něco vyrobil. Horní příčky automatizaci odolávají. Dolní ne, a to je v pořádku, protože hodnota dolních příček je v tom, že jsou poctivé.

**Uzavřený seznam ve slotu 3 je žebřík a Focus Track už ho nakreslil.** Session 4.B navrhla attestaci, review, audit, replikaci. Uvnitř se skrývají dvě různé osy. Perkinsův žebřík hodnotí, **jak silný byl ten kontrolní úkon**. Druhá osa hodnotí, **co si o tom tvrzení může ověřit třetí strana**. Potřeba jsou obě, protože „prohlédl jsem výstup" bez dochovaného záznamu je pouhé tvrzení.

| Žebřík ze session 4.B | Co tvrdí | Co si ověří třetí strana |
|---|---|---|
| Attestace, „přebírám odpovědnost" | Odpovědnost | Samotné tvrzení, viditelně neověřené |
| Review, „prohlédl jsem výstup" | Sebekontrolu | Nic, pokud po té kontrole nezůstal trvalý záznam |
| Audit, „zkontroloval jsem postup a důkazy" | Kontrolu postupu | Záznam, pokud ho provedl autor; nebo kontrolu jmenované třetí strany s uvedeným rozsahem |
| Replikace, „zopakoval jsem to nebo ověřil proti jinému zdroji" | Zopakování | To zopakování |

Jeden důsledek stojí za to napsat do standardu výslovně. **Existence logu sama o sobě nedělá tvrzení o práci silnějším.** Log může být neúplný, nebo o něčem jiném. Stopa ukazuje, že se něco zaznamenalo. Že tvrzení někdo prozkoumal, ukáže jen jmenovaný externí kontrolor nebo zopakování.

### 5D. Kde mají být informace o ověření a dohledu k nalezení?

▶ Zaškrtnout: **V samostatném prohlášení v článku** · **V repozitáři, jako doplňkové materiály** · **Na vyžádání pro recenzenty, čtenáře a časopis**

Ne „jen v hlavním textu", protože to nejde porovnávat. A ne „zaznamenáno, ale nepřístupné", protože záznam, ke kterému se nikdo nedostane, není důkaz.

Platí tři úrovně z 2B: odkaz v článku, záznam v repozitáři, omezený materiál na vyžádání. Publikujte **otisky i u materiálu, který zůstane omezený**, aby i u omezených důkazů šlo poznat, jestli se změnily.

### 5E. Jak žádoucí je který druh informace?

| Položka | Hodnocení |
|---|---|
| Která rizika byla zvážena a ošetřena (halucinace, nepřesnost, zkreslení, soukromí, bezpečnost, autorská práva) | ▶ **Středně žádoucí** |
| Které části práce člověk zkontroloval, ověřil nebo opravil | ▶ **Zásadní** |
| Jak byly zdroje, citace, faktická tvrzení, data nebo výstupy ověřeny proti spolehlivým zdrojům nebo primárním datům | ▶ **Zásadní** |
| Jakákoli omezení ověření, včetně toho, co u výstupů AI nešlo plně zkontrolovat | ▶ **Zásadní** |
| Jestli byly uchovány záznamy interakcí, prompty, logy nebo auditní stopy, a za jakých podmínek jsou přístupné | ▶ **Zásadní** |
| Kdo (který člověk) odpovídal za dohled a ověření u každého užití AI | ▶ **Zásadní** |

*Poznámka k prvnímu řádku.* Vyprávění o rizicích hodnotím níž než ostatních pět záměrně a je to jediné hodnocení, u kterého čekám nesouhlas.

Obecný text o rizicích se ze všech částí přiznání vyrábí nejsnáz a nejhůř se kontroluje. Během jednoho publikačního cyklu ustrne v šabloně. Ostatních pět položek jsou tvrzení, se kterými se dá někoho konfrontovat. Pole o rizicích ponechte, udělejte ho volitelné a naveďte ho na konkrétní rizika. Jen ať se z něj nestane pole, které autoři vyplňují **místo** těch ověřitelných.

### 5F. Co má standard doporučit k průhlednosti ověřování?

1. **Doporučit, ať se nepřítomnost kontroly zaznamenává stejně jasně jako její přítomnost.** Standard, jehož jediným kladným signálem je „zkontrolováno", bude všude vyplněný slovem „zkontrolováno". Odstupňovaný záznam funguje oběma směry. Dělá chybějící kontrolu **viditelnou** místo neviditelné.

   Prakticky: autor, který přizná pět podstatných užití AI a u dvou z nich uvede, že je nikdo nezávisle nezkontroloval, napsal informativnější a důvěryhodnější dokument než ten, kdo tvrdí, že zkontroloval všechno.

2. **Doporučit svázání každého tvrzení o ověření s otiskem obsahu** (P4). Kdybych měl zahodit všechna ostatní doporučení, tohle bych si nechal. Tvrzení o ověření, které pojmenovává stav souboru, nemůže zdědit pozdější, jiný stav souboru. Bez toho je „ověřeno" tvrzení o názvu.

3. **Necertifikovat.** Strukturovaný záznam svádí k tomu sečíst z něj skóre, například „kvalita provenience: 8 z 10". Standard má jasně říct, že žádné pole ani žádná kombinace polí není soudem o kvalitě nebo pravdivosti výzkumu.

   Certifikace nese odpovědnost, kterou standard pro vykazování unést nemůže. Souhrnná skóre se začnou optimalizovat, místo aby se naplňovala. A obory se legitimně liší v tom, co vyžadují. Zaznamenejte, kdo co udělal a jaké důkazy existují. A dál už ne.

---

## 6: Shrnutí a další zpětná vazba

**Odkud tahle odpověď vychází.** Je psaná z probíhající kvalitativní práce o tom, jak lidé formulují přiznání AI napříč žánry: vědecké články, e-maily a zprávy, výukové a interní materiály, softwarové projekty, závěrečné práce a sociální sítě.

Ta práce se ptá, které složky reálné přiznání doopravdy nese a jak velká část znění je šablona vydavatele, ne autorův vlastní hlas. Složky, které sleduji, jsou role AI, podíl práce, co udělal člověk, ručení, jistota, stav výstupu, co se čeká od čtenáře, a kde prohlášení stojí.

Zatím žádná zjištění nejsou a do 3. kola žádná nenabízím. Tyhle návrhy se podávají k tomu, aby se použily nebo zahodily podle vlastní hodnoty, a žádnou návaznou práci ode mě nepotřebují.

**K procesu.** Uspořádání do tří kol a publikovaný přípravný materiál udělaly z téhle konzultace něco, do čeho se dá nezvykle snadno věcně zapojit. Jeden návrh: zveřejněte výstup 2. kola jako **verzovaný, strojově čitelný návrh**, tedy soubor se slovníkem plus ukázkové záznamy, ne jen jako text. Implementátoři pak můžou ve 3. kole odpovědět funkčním kódem místo komentářů.

---

## Uvedení autorství a kontakt

- **Volitelné uvedení autorství:** *Jan Nehyba, odborný asistent, Pedagogická fakulta, Masarykova univerzita (Česko)*, souhlasím s uvedením u volných odpovědí.
- **Kontakt po odeslání:** ▶ Ne, nekontaktujte mě ohledně mých odpovědí · ▶ Ne, nezvěte mě do 3. kola · ▶ Ne, další informace nepotřebuji
- **Jak jsem se o kole dozvěděl:** ▶ Jinak → *„Sleduji Focus Track veřejně (web ISC); zkoumám, jak lidé formulují přiznání AI napříč žánry."*
- **Vztah k systémům AI:** ▶ Profesionální, intenzivní uživatel AI
- **Role a fáze kariéry:** ▶ Aktivní výzkumník (s PhD nebo ekvivalentem) · ▶ Výzkumník se stálou smlouvou
