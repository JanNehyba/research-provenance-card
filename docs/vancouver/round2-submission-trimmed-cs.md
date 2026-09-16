# Podnět do 2. konzultačního kola: seškrtaná verze: pracovní překlad

**Směrem ke globálnímu reportovacímu standardu pro deklarace užití AI ve výzkumu („Vancouver Standard“)**
Focus Track konference WCRI 2026 · ISC · WCRIF · COPE · STM · GYA
Uzávěrka podání: **16. říjen 2026** · Webový formulář: <https://council.science/AIdisclosure>

---

**O této verzi.** Seškrtaný podnět odvozený z plného textu v souboru [`round2-submission-en.md`](./round2-submission-en.md). Zachovává čtyři návrhy, které obstojí samy o sobě, a odstraňuje dřívější implementační práci, její rámcování a její přílohy. Před odesláním je potřeba otevřít webový formulář v prohlížeči a ověřit, že otázky a možnosti stále odpovídají stavu z 29. července 2026. Doporučené odpovědi u výběrových položek jsou označeny ▶, aby šel celý podnět přenést do formuláře v jednom průchodu. Toto je pracovní překlad pro autorskou kontrolu; podává se anglická verze [`round2-submission-trimmed-en.md`](./round2-submission-trimmed-en.md).

## Respondent

| Pole | Hodnota |
|---|---|
| Jméno | Jan Nehyba |
| Role | Odborný asistent, Pedagogická fakulta, Masarykova univerzita, Brno, Česko |
| ORCID | 0000-0003-4159-5576 |
| Role ve formuláři | Osobní perspektivy fyzické osoby |
| Obor | Pedagogický výzkum / sociální vědy (kvalitativní metody) |
| Země | Česko |
| Kontakt | *[institucionální e-mail: doplnit před odesláním]* |

**Základ tohoto podnětu.** Odpovědi níže nejsou stanovisko. Jsou perspektivou kvalitativního výzkumníka, který právě zkoumá, jak lidé uvádějí, podepisují a označují texty vzniklé s pomocí AI napříč žánry: vědecké články, e-maily a zprávy, výukové a interní materiály, softwarové projekty. Ta práce se dívá na znění deklarací užití AI a na to, které složky odpovědnosti toto znění skutečně nese. Nic níže nestojí na formální implementaci ani na pilotních zjištěních; pokud příklad pochází z mé vlastní praxe, je to uvedeno.

---

## 0: Přehled: čtyři návrhy

| # | Návrh | Otázka |
|---|---|---|
| **P1** | Dát každé kategorii taxonomie **stabilní, strojově čitelný identifikátor** (slug, ne pořadové číslo) a verzovat samotnou taxonomii s politikou ukončování a nahrazování kategorií. Precedentem je CRediT jako ANSI/NISO Z39.104-2022. Bez stabilních identifikátorů nelze „strojovou čitelnost“ na straně dalších uživatelů naplnit. | 3 |
| **P2** | Učinit jednotkou deklarace **řádek, nikoli větu**: jeden řádek na (úlohu × aktéra × co bylo zkontrolováno × stopu). Narativní próza může řádek doprovázet; nemůže jej nahradit, mají-li být deklarace srovnatelné. | 3 |
| **P3** | Přidat ke každému řádku **úroveň důkazu/ověření** z uzavřeného seznamu. Kritéria 1. kola i vlastní „ověřovací žebřík“ Focus Tracku (attestation → review → audit → replication) už tímto směrem míří; uzavřený seznam je to, co z něj dělá strojově čitelné. | 5 |
| **P4** | **Svázat deklaraci s verzí, kterou popisuje**, obsahovým hashem (SHA-256) přijatého souboru. Deklarace a tvrzení o ověření se dnes vážou na titul, nikoli na stav souboru, a přežívají proto tichou výměnu obsahu. | 4, 5 |

---

## 1: Které užití AI se má deklarovat? (Prahy)

### 1A. Stanovisko k navrženému prahu

**Navržený kvalitativní práh podporuji tak, jak je napsaný, včetně explicitního odmítnutí kvantitativních prahů.** Argumentace v poznámce pod čarou je správná a v konečném standardu by se dala vyjádřit ještě pevněji: neexistuje jednotka, nástroj ani auditní procedura pro „procento příspěvku AI“. Procenta zvou ke dvěma režimům selhání: autoři hádají, a třetí strany produkují čísla („tento rukopis je ze 40 % AI“), která nelze ani potvrdit, ani vyvrátit. Tvrzení postavené na rolích a úlohách je jiný druh výpovědi: lze mu postavit do cesty kód, logy, výstupy a pojmenované kontrolory.

Podporuji také kritérium (1), tedy že delegovaný úsudek nebo úsudek formovaný AI podléhá deklaraci **i tehdy, když člověk výsledek následně validoval**. To je nejdůležitější věta celého návrhu, protože blokuje nejběžnější vyhýbání („zkontroloval jsem to, takže je to mé“).

Tři upřesnění:

**(a) Nenechte práh nést celou zátěž.** Binární práh s jednotnými náklady na reportování nad ním vytváří útes: autor, který jej překročí, platí plnou cenu, autor těsně pod ním neplatí nic, a pobídka na hraně směřuje k tomu, aby se člověk přesvědčil pod práh. Spojte práh s **gradovaným záznamem** (P3), aby šlo okrajové užití poctivě zapsat do jednoho levného řádku na nejnižší úrovni důkazu, a těžké, dobře zdokumentované užití tak, jak se rovnalo. Proporční má být ne *to, zda* se kdo deklaruje, ale *kolik důkazu záznam nese*.

**(b) „Substantive“ potřebuje oborové příklady, ne lepší definici.** Test recenzent/čtenář je správná formulace a další abstraktní dolaďování nepomůže. Pomůže malá, rostoucí, citovatelná sada odvedených příkladů pro oblast (tucet na obor, udržovaná jako součást živého standardu), tak jak sítě reportovacích guideline sbírají exempláře. Vzdělávacě-výzkumné příklady mohu dodat.

**(c) Rovnost: jazyková práce nesmí být zdaněna prvním jazykem.** Kategorie 17 (Translation) a jazyková část kategorie 18 vytvářejí strukturální asymetrii. Český, ukrajinský nebo indonéský výzkumník, který přemýšlí a píše v rodném jazyce a AI využívá k tvorbě anglického textu, koná *stejnou intelektuální práci* jako anglofonní kolega, ale při doslovném čtení prahu musí deklarovat více. 1. kolo uzavřelo, že standard nesmí být pro hůře situované komunity obtížnější; právě tady se ten princip projeví. Navržené znění: **překlad vlastního obsahu autora, se zachovaným významem ověřeným autorem, je technické užití pod prahem a deklaruje se pouze tam, kde to vyžaduje časopis; AI generovaný *obsah* v jakémkoli jazyce je nad prahem bez ohledu na to, v jakém jazyce vznikl.** Hranice vede autorstvím obsahu, nikoli jazykem produkce.

### 1B. Tři příklady z mého oboru (pedagogický výzkum, kvalitativní metody)

1. **Vyžaduje deklaraci.** LLM provede první průchod tematickým kódováním přepisů rozhovorů; výzkumník kódy kontroluje, rozhoduje o nich a reviduje je. Úsudek, který by jinak vykonával expert-člověk, byl delegován; pozdější lidská validace povinnost deklarace neruší (kritérium 1). Taxonomie: *qualitative data analysis*.
2. **Nevyžaduje deklaraci.** Oprava pravopisu a interpunkce a přeformátování referencí textu, který autor sám napsal a sám obhájil. Žádný vliv na význam, interpretaci ani podstatu.
3. **Sporné, a tvrdím, že jde nad práh.** Dlouhodobé využívání LLM jako adversariálního sparing partnera během koncepčního návrhu: model dostane instrukci napadat autorovo zarámování a zarámování se v důsledku mění. **Do rukopisu se nedostane jediné slovo ani řádek kódu z modelu**, takže každé pravidlo orientované na text nehlásí nic, přestože výměna utvářela návrh práce. Není to hypotetické: takto vznikal rukopis, který za tímto podnětem stojí, a sedm obratů v designu se k tomu dá dohledat. Podle kritérií (1) a (3) jde o užití podléhající deklaraci, ale žádná existující kategorie je nevystihuje dobře. Označuji to za případ, kde je současná praxe deklarace nejsystematičtěji slepá, právě proto, že přínos AI je ve výstupu neviditelný.

### 1C. Míra souhlasu s tvrzeními

| Tvrzení | Odpověď |
|---|---|
| Užití AI, které substantivně formuje obsah, interpretaci, reportovaný obsah nebo výsledky výzkumu, by mělo být deklarováno. | ▶ **Zcela souhlasím** |
| Standard by měl definovat minimální práh deklarace a zároveň autorům umožnit deklarovat více, pokud chtějí. | ▶ **Zcela souhlasím** |
| Rutinní opravy pravopisu, gramatiky, formátování referencí nebo kosmetické úpravy by měly vyžadovat deklaraci. | ▶ **Spíše nesouhlasím** |
| Opakovaná drobná užití AI se mohou dostat pod deklaraci, když jejich kumulativní vliv formuje práci. | ▶ **Zcela souhlasím** |

---

## 2: Kde se má užití AI deklarovat? (Umístění)

### 2A. Umístění

▶ **Jak v hlavním textu článku, tak v samostatném prohlášení se mohou objevit informace o užití AI.**

### 2B. Které informace kam

Tři úrovně, s jediným zdrojem pravdy:

1. **Metodika a popisky obrázků (narativ):** *proč* byla AI použita, jak zapadala do designu, co její užití znamená pro interpretaci výsledků. To je metodologická transparentnost a patří tam, kde se popisuje metoda. Nelze to standardizovat dál než řízeným slovníkem, a nemělo by se to.
2. **Samostatné strukturované prohlášení (srovnatelné, strojově čitelné):** řádky (úloha, aktér, úroveň ověření, stopa, podmínky přístupu). Publikované vedle prohlášení o příspěvcích autorů a o střetu zájmů a dostupné jako data, ne jen jako vykreslená próza. To je to, co umožňuje srovnávání mezi články a redakční i automatizovanou kontrolu.
3. **Záznam v repozitáři (důkaz):** prompty, logy, kód, výstupy, s persistentními identifikátory, hashy a stavem přístupu. Ne v článku; odkazováno z něj.

**Kritický implementační detail:** úrovně 1 a 2 musí vznikat z jednoho záznamu, ne se psát dvakrát. Dva ručně psané popisy stejných fakt se rozcházejí a rozpor mezi nimi je nerozlišitelný od pochybení. Doporučení pro standard: definovat záznam, potom definovat jeho vykreslování.

### 2C. Další poznámky k umístění

Námitka „může prodloužit článek“ je reálná a řeší ji to, že úroveň 2 jsou **data připojená k článku, nikoli slova v něm**; strukturované prohlášení by nemělo spotřebovávat rozsah textu, přesně tak, jak ho nespotřebovává prohlášení o střetu zájmů či o dostupnosti dat.

Námitku stigmatizace si zaslouží přímá odpověď: samostatné prohlášení dnes AI *vyčleňuje* a za deset let bude působit přechodně. To je přijatelné. Prohlášení o příspěvcích autorů byla také kdysi novinkou motivovanou konkrétním problémem integrity. Navrhnout záznam tak, aby bylo možné jej později vstřebat do obecného záznamu o přispěvatelích (P1, P2), nikoli se mu teď vyhýbat.

---

## 3: Jak má být deklarace strukturovaná? (Taxonomie)

### 3A. Přiměřenost navržené 18kategoriální taxonomie

▶ **Většinou přiměřená.**

### 3B. Stanovisko k navržené taxonomii

Granularita je v zásadě správná. Oddělení *kvantitativní* od *kvalitativní* analýzy dat (12/13) a *vizualizace dat* od *generování obrázků a obrazů* (14/15) jsou správná rozhodnutí; obě brání skutečným zmatkům o tom, co AI dělala.

**Nejasnosti a překryvy k vyřešení.**

- 8 *Data collection (operations)* vs 9 *Data creation*: „creation“ se čte jako generování syntetických/simulovaných dat, ale lze to číst i jako sběr. Přejmenovat 9 na *Synthetic or simulated data generation* a obě definovat.
- 4 *Literature summarization* vs 16 *Drafting text*: AI napsaná sekce přehledu literatury je obojí. Stanovit pravidlo (klasifikovat podle úlohy, umožnit více kategorií na jedno užití).
- 18 spojuje *editaci/přepis* s *referencemi*. Práce s referencemi má specifické, kontrolovatelné selhání (nerozpoznávající citace) a zaslouží si oddělení od editace prózy.
- 5/6/7 jako podpoložky `Design > …` je dobré; udělat vztah rodič/podřízený explicitní a strojově čitelný, jinak jej implementátoři budou nesoustavně zplošťovat.

**Strukturální doporučení (část, která rozhoduje o tom, zda je „strojová čitelnost“ skutečná).**

1. **Stabilní identifikátory, slugové, ne pořadová čísla** (P1). `vs:literature-search`, ne „kategorie 3“. Pořadová čísla se rozbijí ve chvíli, kdy je kategorie vložena nebo zrušena. Publikovat seznam jako verzovaný strojově čitelný slovník (JSON/SKOS) s `deprecated` a `replaced_by`. Cesta CRediT přes ANSI/NISO Z39.104-2022 je precedent a důvod, proč je CRediT dnes v metadatech použitelný.
2. **Řádky, ne věty** (P2). Samotná kategorie deklaraci nese. Minimální řádek je: *úloha* (ID kategorie) · *aktér* (který AI systém / který člověk) · *co bylo zkontrolováno a kým* · *stopa* (jaký záznam existuje a jak k němu lze přistoupit). To je přesně struktura, o kterou 1. kolo žádalo: konzistentní jádro s prostorem pro volný popis.
3. **Poznamenejte, že taxonomie klasifikuje úlohy a deklarace potřebuje ještě jednu osu.** Návrh to říká („merely a classification of research tasks“). Souhlasím, a právě to je pointa: bez ověřovací osy (§5) řekne taxonomie čtenáři, čeho se AI dotkla, ale ne, co s tím kdo udělal.

---

## 4: Má být neprázdná deklarace povinná?

### 4A. Míra souhlasu

| Tvrzení | Odpověď |
|---|---|
| Časopisy by měly od autorů vyžadovat neprázdnou deklaraci (včetně negativní deklarace, pokud AI substantivně nevyužili). | ▶ **Zcela souhlasím** |
| Souhlas s publikační politikou ohledně deklarace užití AI je dostatečně přesvědčivý na to, aby se dalo věřit, že reportování AI bylo přesné. | ▶ **Zcela nesouhlasím** |

### 4B. Stanovisko k povinné neprázdné deklaraci a „nulovým“ deklaracím

**Podpora, a z důvodu, který není tím obvyklým.** Argument kulturní změny je v pořádku, ale měkký. Silný argument je evidenční: mlčení nelze falzifikovat, zatímco nulová deklarace je **konkrétní, datované, přičitatelné tvrzení**. Ukáže-li se později substantivní nezveřejněné užití AI, vede mlčení na argument o interpretaci („nikdo se neptal“), zatímco nulová deklarace vede na zdokumentované nepravdivé tvrzení s pojmenovaným autorem a časovým razítkem. Povinná neprázdná deklarace nebrání nepoctivosti; mění mlhu v papírovou stopu. To je velký zisk za cenu jednoho řádku.

Dvě podmínky, bez nichž se nulová deklarace stane přesně prázdnou větou, kterou standard nahrazuje:

1. **Svázat ji s přijatou verzí** (P4). Deklarace učiněná při podání a nikdy znovu nepotvrzená je tvrzení o souboru, který už neexistuje. Vyžadovat potvrzení při přijetí, připojené k obsahovýmu hashi přijatého rukopisu. Tím se uzavírá problém *dangling-attestation*: kontrola, která přežije to, co zkontrolovala. Je to levné, výpočet SHA-256 stojí sekundu a může jej ověřit kdokoli, a je to nejméně využívaný mechanismus, který má tento standard k dispozici.
2. **Nenechat ji nahradit zaškrtávacím políčkem.** Souhlas s publikační politikou při podání je pro čtenáře neviditelný a zpětně nefalzifikovatelný. Deklarace musí být publikována s článkem.

**Ke stigmatizaci:** riziko je reálné, ale je většinou funkcí znění. Nulová deklarace formulovaná jako absence *prahu dosahujícího* užití, ve stejném bloku jako prohlášení o střetu zájmů, normalizuje spíše než vyčleňuje. Větší riziko stigmatu je dnes opačné: poctivě deklarující působí hůř než mlčící nedeklarující.

---

## 5: Jak signalizovat odpovědnost a accountability?

### 5A. Má být obecné prohlášení o odpovědnosti součástí deklarace?

▶ **Ano, výchozí prohlášení by mělo být součástí standardu deklarace.**

### 5B. Stanovisko k obecným prohlášením o odpovědnosti

Zahrnout jej, ale nenechat jej stát samotné, a formulovat jej **přičitatelně, nikoli kolektivně**. „Autoři přebírají plnou odpovědnost“ platí o každém článku, jaký kdy byl publikován, a proto nenese žádnou informaci; námitka odškrtávacího mechanického souhlasu je na toto znění oprávněná. Informaci nese pojmenovaná osoba s persistentním identifikátorem, která přijímá odpovědnost za konkrétní užití AI v konkrétním čase: jeden ručitel na každý deklarovaný řádek s substantivním užitím AI, srovnatelné s rolí korespondujícího autora. Nestojí to autora nic, co by už nevěděl.

Takže: ponechat výchozí větu pro obecný případ a vyžadovat **pojmenovaný dohled u každého substantivního užití** (viz 5E, poslední řádek, který hodnotím jako zásadní).

**Perspektiva žánrů, které standard nepokrývá.** Deklarace je zároveň jazykový akt: její znění lze rozložit na to, kdo text posílá, kdo vybral slova a kdo za obsah ručí. Tyto složky se v žánrech mimo vědecký článek kombinují jinak. E-mail, který začíná „Zde je shrnutí od AI“, říká příjemci něco, co artikulové prohlášení neřekne; prezentace podepsaná jen jménem si nárokuje autorství i ručení naráz; trailer v commit message („Generated-with: …“) je rozděluje zase jinak; stránka s prohlášením u závěrečné práce to dělá ve formě předepsané institucí. Standard psaný pro vědecké články nepokryje e-maily, výukové materiály ani interní podklady, kde se táž odpovědnost řeší jinými prostředky (podpisy, kontrola, konvence pojmenování). Navrhuji, aby standard svůj žánrový rozsah uvedl explicitně a nevytvářel dojem, že artikulové prohlášení je vzorem pro veškerou komunikaci.

### 5C. Jaké informace o ověření a dohledu mají autoři uvádět

**Strukturovaně, ne narativně, s narativním slotem.** Ukázková prohlášení v přípravném čtení ilustrují problém: „generický“ příklad („autoři zrevidovali a editovali všechen AI generovaný obsah“) je nefalzifikovatelný a „rigorózní“ a „popisný“ příklad jsou výborné, ale nelze je srovnávat mezi články, hromadně screenovat ani kontrolovat na vnitřní konzistenci. Pětislotový řádek na každé deklarované užití je zvládnutelný v řádu minut a je srovnatelný:

| Slot | Obsah | Proč |
|---|---|---|
| 1. Úloha | ID kategorie taxonomie | srovnatelnost |
| 2. Aktér | který AI systém (poskytovatel, rodina modelů, **verze/snapshot**, rozhraní) nebo který člověk | „použili jsme LLM“ není popis nástroje; datovaná verze je |
| 3. Co bylo zkontrolováno, kým | uzavřený seznam: *nezkontrolováno* · *pročetl autor* · *vzorek (uvést podíl)* · *plně přepočítáno/znovu spuštěno* · *zkontrolováno proti primárním zdrojům* · *zkontroloval pojmenovaná třetí strana* · *nezávisle replikováno* | to je osa, která mění deklaraci v odpovědnost |
| 4. Stopa | jaký záznam existuje (prompt/log/kód/výstup), jeho identifikátor a hash a stav přístupu: *veřejné · embargo · na vyžádání · restrikce · nezachováno*, s odůvodněním, kdykoli není veřejné | prompty a logy často nemohou být publikovány (osobní údaje, licencovaný text, materiál třetích stran); nepublikovatelný záznam lze stále *referencovat hashem*, což činí pozdější substituci detekovatelnou |
| 5. Co nešlo zkontrolovat | krátký volný text, **povinný** | nejinformativnější pole celého záznamu a první, které se zahodí, bude-li volitelné |

**Uzavřený seznam ve slotu 3 je žebřík a Focus Track už ho nakreslil.** Session 4.B navrhla attestation → review → audit → replication. Skrývají se v něm dvě osy a rozdíl je poučný: Perkinsův žebřík graduje **sílu kontrolního aktu** a doplňková osa graduje **co může třetí strana o tvrzení stále ověřit**. Obě jsou potřeba, protože „prohlédl jsem výstup“ bez přeživší stopy je evidenčně holé tvrzení:

| Žebřík session 4.B | Co tvrdí | Co třetí strana může ověřit |
|---|---|---|
| Attestation, „přebírám odpovědnost“ | odpovědnost | samotné tvrzení, viditelně neověřené |
| Review, „prohlédl jsem výstup“ | vlastní kontrola | nic, pokud kontrola nezanechala trvalou stopu |
| Audit, „zkontroloval jsem proces a důkaz“ | kontrola procesu | stopu, pokud ji provedl autor; kontrolu pojmenované třetí strany s uvedeným rozsahem |
| Replication, „reprodukoval nebo zkřížil“ | opětovné spuštění | reprodukci |

Jeden důsledek, který by se měl do standardu dostat explicitně: **existence logu sama o sobě neposiluje tvrzení o práci.** Log může být neúplný nebo se týkat něčeho jiného. Stopa ukazuje, že něco bylo zaznamenáno; jen pojmenovaný externí kontrolor nebo opětovné spuštění ukazuje, že tvrzení bylo zkoumáno.

### 5D. Kde mají být informace o ověření a dohledu dohledatelné?

▶ Zaškrtnout: **V samostatném prohlášení v článku** · **V repozitáři, jako doplňkové materiály** · **K dispozici na vyžádání pro recenzenty, čtenáře, časopis**

Nikoli „pouze v hlavním obsahu“ (nesrovnatelné) a nikoli „zaznamenáno, ale nepřístupné“ (neověřitelný záznam není důkazem). Platí třiúrovňová odpověď z 2B: ukazatel v článku, záznam v repozitáři, restrikované artefakty na vyžádání, s **publikovanými hashi i u artefaktů, které zveřejněné nejsou**, takže restrikovaný důkaz zůstává odolný vůči zásahu.

### 5E. Žádoucnost jednotlivých informací

| Položka | Hodnocení |
|---|---|
| Která rizika byla zvážena a zmírněna (halucinace, nepřesnost, zkreslení, soukromí, bezpečnost, autorská práva, IP) | ▶ **Středně žádoucí** |
| Které aspekty práce byly lidmi zrevidovány, ověřeny nebo opraveny | ▶ **Zásadní** |
| Jak byly zdroje, citace, faktická tvrzení, data nebo výstupy kontrolovány proti spolehlivým zdrojům nebo primárním datům | ▶ **Zásadní** |
| Jakákoli omezení ověření, včetně aspektů výstupů AI, které nešlo plně zkontrolovat | ▶ **Zásadní** |
| Zda byly zaznamenány záznamy interakcí s AI, prompty, logy či auditní stopy a za jakých podmínek jsou přístupné | ▶ **Zásadní** |
| Kdo (který člověk) byl odpovědný za dohled a ověření každého užití AI | ▶ **Zásadní** |

*Poznámka k prvnímu řádku.* Vyhodnocuji narativy o zmírnění rizik nižší než ostatních pět záměrně a je to jediné hodnocení, kde očekávám nesouhlas. Obecná próza o rizicích je nejsnáze produkovaná a nejhůře kontrolovatelná část každé deklarace; během jednoho publikačního cyklu se sblíží na boilerplate. Ostatních pět položek jsou výroky, kterým lze někoho postavit tváří v tvář. Pole rizik ponechat, udělat jej volitelným a navádět jím ke konkrétním rizikům, ale nenechat jej zůstat polem, které autoři vyplní *místo* kontrolovatelných.

### 5F. Co má standard doporučit ohledně transparentnosti ověření a dohledu

1. **Doporučit zaznamenávat absenci ověření stejně explicitně jako jeho přítomnost.** Standard, jehož jediné pozitivní signály jsou „zkontrolováno“, se vyplní „zkontrolováno“. Hodnota gradovaného záznamu je symetrická: dělá chybějící kontrolu *čitelnou* místo *neviditelnou*. Prakticky: autor, který deklaruje pět substantivních užití AI, z nichž dvě nebyla nikdy nezávisle zkontrolována, vytvořil informativnější a důvěryhodnější dokument než autor, který tvrdí plošnou revizi všeho.
2. **Doporučit svázat každé tvrzení o ověření s obsahovým hashem** (P4). Toto je doporučení, které bych si ponechal, kdybych musel všechna ostatní zahodit. Tvrzení o ověření, které se odkazuje na stav souboru, nemůže být zděděno pozdějším, odlišným stavem souboru. Bez toho je „ověřeno“ tvrzením o titulu.
3. **Necertifikovat.** Strukturovaný záznam o ověření svádí k agregovanému skóre („kvalita provenience: 8/10“). Doporučuji, aby standard explicitně uvedl, že žádné pole ani kombinace polí nekonstituuje úsudek o kvalitě nebo pravdivosti výzkumu. Certifikace nese zodpovědnostní zátěž, kterou reportovací standard unést nemůže, agregovaná skóre se optimalizují místo aby byla plněna a jednotlivá místa legitimně vyžadují různé věci. Zaznamenat, kdo co udělal a co bylo doloženo; a už nic.

---

## 6: Souhrn a další zpětná vazba

**Odkud tento podnět vychází.** Vychází z probíhající kvalitativní práce o tom, jak lidé formulovali deklarace užití AI napříč žánry: vědecké články, e-maily a zprávy, výukové a interní materiály, softwarové projekty. Mezi otázky, které si ten pilot klade, patří: které složky reálná deklarace skutečně nese (role AI, podíl na práci, co udělal člověk, odpovědnost, jistota, stav výstupu, očekávání příjemce, umístění) a jak velká část znění je šablona vydavatele, nikoli hlas autora. Validovaná zjištění z tohoto pilotu lze nabídnout do 3. kola.

K procesu: tříkolový design a publikované přípravné čtení z této konzultace dělají konzultaci, do níž lze neobvykle snadno vstoupit se substancí. Jedna připomínka: zveřejnit výsledek 2. kola jako **verzovaný, strojově čitelný návrh** (soubor slovníku plus ukázkové záznamy), ne jen jako prózu, aby mohli implementátoři reagovat ve 3. kole běžícím kódem místo komentářů.

---

## Atribuce a kontaktní preference

- **Volitelná atribuce:** *Jan Nehyba, odborný asistent, Pedagogická fakulta, Masarykova univerzita (Česko)*, souhlas s citací otevřených odpovědí se jménem.
- **Kontakt po podání:** ▶ Ano, kontaktujte mě ohledně mých odpovědí · ▶ Ano, přizvěte mě do 3. konzultačního kola · ▶ Ano, informujte mě o konečném výsledku
- **Jak jsem se o tomto kole dozvěděl:** ▶ Jiné → *„Sleduji Focus Track veřejně (web ISC); zkoumám, jak lidé formulují deklarace užití AI napříč žánry.“*
- **Vztah k AI systémům:** ▶ Profesní intenzivní uživatel AI
- **Role/kariérní fáze:** ▶ Aktivní výzkumník (s PhD nebo ekvivalentem) · ▶ Výzkumník s trvalým úvazkem

---

*Připraveno k podání přes <https://council.science/AIdisclosure> do 16. října 2026. Zdroje procesních faktů jsou uvedeny v [`README.md`](./README.md). Anglická verze tohoto podnětu je [`round2-submission-trimmed-en.md`](./round2-submission-trimmed-en.md).*





