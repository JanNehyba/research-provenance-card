# Podnět do 2. konzultačního kola — pracovní překlad

**Global Reporting Standard for AI Disclosure in Research („Vancouver Standard“)**
Focus Track WCRI 2026 · ISC · WCRIF · COPE · STM · GYA
Uzávěrka: **16. října 2026** · Formulář: <https://council.science/AIdisclosure>

> **Tento soubor není k podání.** Konzultace probíhá v angličtině; kanonická verze je
> [`round2-submission-en.md`](./round2-submission-en.md). Tento překlad slouží k autorské kontrole
> a k případné diskusi s kolegy na fakultě (konzultace výslovně dává přednost kolektivně
> projednanému podnětu před individuálním).

---

## Respondent

| Položka | Hodnota |
|---|---|
| Jméno | Jan Nehyba |
| Role | odborný asistent, Pedagogická fakulta, Masarykova univerzita, Brno |
| ORCID | 0000-0003-4159-5576 |
| Za koho | osobní stanovisko fyzické osoby |
| Obor | pedagogický výzkum / sociální vědy (kvalitativní metody) |
| Země | Česko |
| Kontakt | *[institucionální e-mail — doplnit před podáním]* |

**Na čem podnět stojí.** Nejde o názorový text. Odpovědi popisují, co se stalo, když jsme
postavili funkční implementaci strukturovaného záznamu o užití AI a pak ji aplikovali na vlastní
rukopis. Implementace — **karta provenience výzkumu (RPC) v0.1** — je veřejná: JSON schéma,
validátor, kontrola dohledatelnosti referencí, generátor deklarací, registr a vykreslené panely
(specifikace CC BY 4.0, kód MIT): <https://github.com/JanNehyba/research-provenance-card>

RPC se záměrně staví jako **implementační profil tohoto standardu**, nikoli jako jeho konkurence.
Kde budoucí standard řekne, *co* se má vykázat, RPC je jedna kandidátní odpověď na to, *jak může
vypadat strojově čitelný a validovatelný záznam*. Vše níže je nabídnuto v tomto duchu: pokud jádro
týmu zvolí jinou taxonomii nebo slovník, počítáme s tím, že na něj namapujeme, ne že se s ním budeme
přít.

**Doporučené odpovědi u zaškrtávacích otázek** jsou označeny ▶, aby se celý podnět dal do formuláře
přenést na jeden zátah.

---

## 0 — Přehled: devět konkrétních návrhů

| # | Návrh | Otázka |
|---|---|---|
| **P1** | Dát každé kategorii taxonomie **stabilní strojově čitelný identifikátor** (slug, ne pořadové číslo) a verzovat samotnou taxonomii, včetně pravidel pro zrušení a nahrazení kategorie — precedens je CRediT jako ANSI/NISO Z39.104-2022. Bez stabilních ID nelze „strojovou čitelnost“ dodat nikomu dál. | 3 |
| **P2** | Jednotkou deklarace udělat **řádek, ne větu**: jeden řádek na (činnost × aktér × co bylo zkontrolováno × jaká stopa zůstala). Volný text může řádek doplnit, nemůže ho zastoupit, mají-li být deklarace srovnatelné. | 3 |
| **P3** | Ke každému řádku přidat **úroveň důkazu / ověření** z uzavřeného číselníku. Kritéria 1. kola i „verifikační žebřík“ z Focus Tracku (attestace → review → audit → replikace) k tomu už míří; uzavřený číselník je to, co z toho udělá strojově čitelný údaj. | 5 |
| **P4** | **Svázat deklaraci s verzí, o níž mluví**, otiskem obsahu (SHA-256) přijatého souboru. Dnes se deklarace i ověření váží k názvu, ne ke stavu souboru — a tak přežijí tichou výměnu obsahu. | 4, 5 |
| **P5** | Držet **„reference existuje“ a „reference podporuje tvrzení“ jako dvě různá pole**. Automat spolehlivě ověří existenci a metadata; spolehlivě neposoudí podporu tvrzení. Jediné razítko „citace ověřeny“, které obojí slévá, by byl nejškodlivější artefakt, jaký tento standard může vyrobit. | 5 |
| **P6** | U uchovaných záznamů požadovat **režim přístupu a otisk — a tam, kde byl log před zveřejněním kurátorován, oba otisky a kurační pravidlo** (příloha B). Kurátorovaný log je tím slabší důkaz, čím víc byl kurátorován; zveřejněné pravidlo výběru je to, co z něj důkaz vůbec dělá. | 5 |
| **P7** | Doplnit **tři chybějící kategorie**: (A) orchestrace / provoz agenta, (B) ověřování prováděné AI, (C) výběr mezi běhy či výstupy. (C) je ta integritně kritická: nepřiznaný cherry-picking napříč běhy je dnes neviditelný ve všech deklaračních schématech, která známe. | 3 |
| **P8** | Požadovat, aby byl standard **strojově generovatelný v praxi, ne jen v principu**: zveřejnit referenční serializaci a otevřít kanál k dodavatelům nástrojů kvůli exportu. Zpětná rekonstrukce provenience je o jeden až dva řády dražší než záznam v okamžiku užití — a zůstane neúplná. To je náš hlavní empirický poznatek (§6). | 1, 3, 6 |
| **P9** | **Nulové deklarace** vztáhnout k verzi prahu, verzi taxonomie a verzi přijatého rukopisu — jinak se z povinné negativní deklarace stane přesně ta nefalzifikovatelná věta, kterou standard nahrazuje. | 4 |

---

## 1 — Které užití AI se má deklarovat? (Prahy)

### 1A. Stanovisko k navrženému prahu

**Navržený kvalitativní práh podporujeme tak, jak je napsán, včetně explicitního odmítnutí
kvantitativních prahů.** Argument v poznámce pod čarou je správný a ve finálním standardu by měl
zaznít ještě důrazněji: pro „procento příspěvku AI“ neexistuje jednotka, nástroj ani kontrolní
postup. Procenta plodí dvě selhání — autor hádá a detektory třetích stran vyrábějí čísla („rukopis
je ze 40 % AI“), která nelze potvrdit ani vyvrátit. Rolové, činnostní tvrzení je jiný druh výroku:
lze ho konfrontovat s kódem, logy, výstupy a jmenovanými ověřovateli.

Podporujeme také kritérium (1) — že delegované nebo AI ovlivněné rozhodnutí je hodné deklarace
**i tehdy, když člověk výsledek následně validoval**. To je nejdůležitější věta celého návrhu,
protože blokuje nejčastější úhyb („zkontroloval jsem to, takže je to moje“).

Tři zpřesnění:

**(a) Nenechávejte veškerou tíhu na prahu.** Binární práh s jednotnou cenou vykazování nad ním
vytváří útes: kdo ho překročí, platí plnou cenu, kdo je těsně pod ním, neplatí nic — a motivace na
hranici je dokázat si, že jsem pod ní. Spojte práh s **odstupňovaným záznamem** (P3): marginální
užití pak lze poctivě vykázat jedním levným řádkem na nejnižší úrovni důkazu a těžké, dobře
zdokumentované užití jako takové. Proporcionální nemá být *zda* deklaruji, ale *kolik důkazu záznam
nese*.

**(b) „Podstatné“ nepotřebuje lepší definici, ale oborové příklady.** Test „recenzent/čtenář“ je
správně formulovaný a další abstraktní zpřesňování nepomůže. Pomůže malá, rostoucí a citovatelná
sada rozpracovaných příkladů podle oborů (řádově desítka na obor, udržovaná jako součást živého
standardu) — tak, jak sítě reportovacích směrnic akumulují příklady. Příklady z pedagogického
výzkumu rádi dodáme.

**(c) Spravedlnost: jazyková práce nesmí být daněna prvním jazykem.** Kategorie 17 (Translation)
a jazyková část kategorie 18 zakládají strukturální asymetrii. Český, ukrajinský nebo indonéský
badatel, který myslí a píše ve svém jazyce a angličtinu si nechá vyrobit AI, dělá *tutéž
intelektuální práci* jako anglofonní kolega — a při doslovném čtení prahu musí deklarovat víc.
První kolo uzavřelo, že standard nemá být těžší pro komunity s menší podporou; tady se to láme.
Naše navržená formulace: **překlad autorova vlastního obsahu, se zachovaným významem a autorskou
kontrolou, je technické užití pod prahem a deklaruje se jen tam, kde to časopis vyžaduje;
AI-generovaný *obsah* je nad prahem bez ohledu na jazyk, ve kterém byl vygenerován.** Dělicí linie
je autorství obsahu, ne jazyk jeho výroby.

### 1B. Tři příklady z našeho oboru (pedagogický výzkum, kvalitativní metody)

1. **Deklarace nutná.** LLM provede první kolo tematického kódování rozhovorů; badatel kódy
   reviduje, rozhoduje sporné případy a přepisuje. Bylo delegováno rozhodování, které normálně
   patří expertnímu člověku, a pozdější lidská validace deklarační povinnost neruší (kritérium 1).
   Kategorie: *kvalitativní analýza dat*.
2. **Deklarace není nutná.** Oprava pravopisu a interpunkce a přeformátování seznamu literatury
   u textu, který autor sám napsal a promyslel. Bez vlivu na význam, interpretaci či podstatu.
3. **Sporný případ — a tvrdíme, že je nad prahem.** Dlouhodobé užití LLM jako adversariálního
   oponenta při konceptuálním návrhu: model má pokyn autorovo rámování napadat a rámování se tím
   mění. **Do rukopisu se nedostane ani věta, ani řádek kódu od modelu** — každé pravidlo zaměřené
   na text tedy nevykáže nic, a přesto byl návrh práce touto výměnou tvarován. Není to hypotéza:
   takto vznikl rukopis, o který se tento podnět opírá, a sedm doložených obratů v návrhu je z toho
   dohledatelných. Podle kritérií (1) a (3) to deklarovat lze, ale žádná existující kategorie to
   nevyjadřuje (viz 3B, chybějící kategorie A). Označujeme to za místo, kde je dnešní praxe
   nejsystematičtěji slepá — právě proto, že příspěvek AI není ve výstupu vidět.

### 1C. Pozice na škále

▶ **Někde mezi — asi tolik, kolik říká uvedený práh.**

Náš spor s návrhem není o výšce prahu. Je o tom, že práh sám rozhoduje jen o tom, *zda* se něco
řekne, a nic neříká o tom, zda je řečené kontrolovatelné.

### 1D. Míra souhlasu s tvrzeními

| Tvrzení | Odpověď |
|---|---|
| Užití AI se má deklarovat, když podstatně ovlivní výzkumný proces, interpretaci, vykázaný obsah nebo výsledky. | ▶ **Silně souhlasím** |
| Standard má definovat minimální práh deklarace a dovolit autorům deklarovat víc, pokud chtějí. | ▶ **Silně souhlasím** |
| Rutinní oprava pravopisu, gramatiky, formátování referencí či kosmetické editace mají vyžadovat deklaraci. | ▶ **Spíše nesouhlasím** |
| Opakovaná drobná užití AI se mohou stát hodná deklarace, když jejich kumulativní vliv tvaruje práci. | ▶ **Silně souhlasím** |

---

## 2 — Kde se má užití AI deklarovat? (Umístění)

### 2A. Umístění

▶ **Oboje — informace o užití AI může být jak v hlavním textu, tak v samostatném prohlášení.**

### 2B. Které informace kam

Tři vrstvy, jeden zdroj pravdy:

1. **Metody a legendy obrázků (narativně):** *proč* byla AI použita, jak zapadla do designu, co její
   užití znamená pro interpretaci výsledků. To je metodologická transparentnost a patří tam, kde se
   popisuje metoda. Standardizovat to nad rámec řízeného slovníku nelze a nemá.
2. **Samostatné strukturované prohlášení (srovnatelné, strojově čitelné):** řádky — činnost, aktér,
   úroveň ověření, stopa, režim přístupu. Publikované vedle prohlášení o autorském přispění
   a konfliktu zájmů, a dostupné jako *data*, ne jen jako vykreslený text. To umožňuje srovnávání
   napříč články, redakční i automatické prosévání.
3. **Záznam v repozitáři (důkaz):** prompty, logy, kód, výstupy — s trvalými identifikátory, otisky
   a režimem přístupu. Ne v článku; odkázané z článku.

**Klíčový implementační detail:** vrstvy 1 a 2 musí být *generované z jednoho záznamu*, ne napsané
dvakrát. Dva ručně psané popisy týchž skutečností se rozejdou — a rozpor mezi nimi je
nerozlišitelný od pochybení. V naší implementaci je to jeden JSON soubor, z něhož se generují
deklarace jednotlivých vydavatelů a z něhož se vykresluje i lidsky čitelný panel. Doporučení pro
standard: definujte záznam, pak definujte jeho podoby.

### 2C. Další poznámky k umístění

Námitka „prodlouží to článek“ je reálná a řeší ji to, že vrstva 2 jsou **data připojená k článku,
ne slova v něm** — strukturované prohlášení nemá spotřebovávat rozsah, stejně jako ho nespotřebuje
prohlášení o konfliktu zájmů nebo o dostupnosti dat.

Námitka stigmatizace si žádá přímou odpověď: samostatné prohlášení AI *dnes* vyděluje a za deset
let bude vypadat jako přechodová konstrukce. To je akceptovatelné. Prohlášení o autorském přispění
také bývala novinka motivovaná konkrétním integritním problémem. Navrhněte záznam tak, aby ho šlo
později pohltit do obecného záznamu o přispění (P1, P2) — místo abyste se mu teď vyhýbali.

---

## 3 — Jak má být deklarace strukturovaná? (Taxonomie)

### 3A. Přiměřenost navržené 18kategoriální taxonomie

▶ **Většinou přiměřená, ale několik kategorií chybí.**

### 3B. Stanovisko k navržené taxonomii

Osmnáct kategorií jsme otestovali tak, že jsme je namapovali na funkční implementaci (role CRediT
plus pět AI rozšíření) a překlasifikovali podle nich vlastní rukopis. Úplný crosswalk — včetně
míst, kde je deficitní náš vlastní slovník — publikujeme jako strojově čitelný soubor:
[`taxonomy-crosswalk-v0.1.json`](./taxonomy-crosswalk-v0.1.json). Co cvičení ukázalo:

**Granularita je zvolená dobře — v několika místech lépe než naše.** Rozdělení *kvantitativní*
a *kvalitativní* analýzy (12/13) a *vizualizace dat* a *generování obrázků* (14/15) jsou obě
správná rozhodnutí, která náš slovník pokazil tím, že je slil do hrubších rolí CRediT. Obě
přebíráme. Kategorie 3, 4 a 17 odhalují další skutečné mezery na naší straně (souhrn literatury,
překlad).

**Tři chybějící kategorie.**

- **(A) Orchestrace / provoz agenta.** Kdo systém nastavil, promptoval a řídil; který agent vybíral
  které specializované agenty; jaký workflow běžel. Všech 18 kategorií popisuje *výzkumnou činnost,
  kterou vykonala AI*; žádná nepopisuje *lidský akt jejího řízení* a žádná nepopisuje akt
  supervizního agenta, který řídí jiné agenty. Sám Focus Track to na sezení 4.B pojmenoval („když
  supervizní agenti vybírají specializované agenty, musí deklarace říct víc než jméno jednoho
  chatbota“) — a je to případ z 1B, příklad 3: podstatný vliv s nulovou stopou na straně výstupu.
  Bez této kategorie jsou agentní workflow deklarovatelné jen jako seznam nástrojů.
- **(B) Ověřování prováděné AI.** Kategorie 10 říká „generování/úprava/**audit** kódu“ a 11
  „čištění/preprocessing/**audit** dat“: ověřovací činnosti jsou dnes propašované do produkčních
  kategorií. Ale kontrola prováděná AI je zvláštní akt s jinými integritními vlastnostmi —
  dohledání referencí, posouzení podpory tvrzení, statistický audit, review kódu a čím dál častěji
  „review specializovanými AI agenty“, což bylo na sezení 4.B výslovně jmenováno. Musí být
  zaznamenatelné *jako kontrola* (a viz P5: jaký druh kontroly).
- **(C) Výběr mezi více běhy nebo výstupy.** Který běh byl vykázán, z kolika, podle jakého pravidla.
  Je to činnost s velkou integritní vahou — nepřiznaný výběr nejlepšího z mnoha běhů je známý
  mechanismus nadhodnocování zdánlivé kvality v demonstracích autonomního výzkumu — a je
  neviditelná ve všech deklaračních schématech, která známe, včetně tohoto návrhu. Kategorie učiní
  deklaraci *možnou*; učinit ji *povinnou* pro agentní pipeline je samostatné politické rozhodnutí,
  které bychom podpořili.

**Nejasnosti a překryvy k dořešení.**

- 8 *Sběr dat (operace)* vs 9 *Data creation*: „creation“ se čte jako generování syntetických či
  simulovaných dat, ale lze ho číst i jako sběr. Přejmenovat 9 na *Generování syntetických nebo
  simulovaných dat* a obě definovat.
- 4 *Souhrn literatury* vs 16 *Psaní textu*: AI napsaná přehledová kapitola je obojí. Uveďte
  pravidlo (klasifikuje se podle činnosti; jedno užití může nést více kategorií).
- 18 slévá *editaci/přepis* se *seznamy referencí*. Práce s referencemi má specifický, strojově
  kontrolovatelný způsob selhání (nedohledatelné citace) a zaslouží si oddělení od editace prózy.
- 5/6/7 jako podkategorie `Design > …` je dobré řešení; udělejte vztah nadřazenosti explicitní
  a strojově čitelný, jinak to implementátoři nekonzistentně zploští.

**Strukturální doporučení (ta část, která rozhoduje, zda je „strojová čitelnost“ reálná).**

1. **Stabilní identifikátory ve formě slugů, ne pořadová čísla** (P1). `vs:literature-search`, ne
   „kategorie 3“. Pořadová čísla se rozbijí v okamžiku, kdy se kategorie vloží nebo zruší.
   Publikujte seznam jako verzovaný strojově čitelný slovník (JSON/SKOS) s poli `deprecated`
   a `replaced_by`. Cesta CRediT přes ANSI/NISO Z39.104-2022 je precedens — a důvod, proč je CRediT
   dnes použitelný v metadatech.
2. **Řádky, ne věty** (P2). Kategorie sama deklaraci nenese. Minimální řádek je: *činnost* (ID
   kategorie) · *aktér* (který AI systém / který člověk) · *co bylo zkontrolováno a kým* · *stopa*
   (jaký záznam existuje a jak je přístupný). Přesně to si první kolo vyžádalo — konzistentní jádro
   s místem pro volný popis — a přesně to naše implementace validuje.
3. **Pojmenujte, že taxonomie klasifikuje činnosti a deklaraci chybí ještě jedna osa.** Návrh to
   sám říká („taxonomie je pouze klasifikace výzkumných činností“). Souhlasíme — a právě to je ten
   bod: bez osy ověření (§5) taxonomie čtenáři řekne, čeho se AI dotkla, ale ne, co s tím kdo dělal.

---

## 4 — Má být neprázdná deklarace povinná?

### 4A. Míra souhlasu

| Tvrzení | Odpověď |
|---|---|
| Časopisy mají po autorech vyžadovat neprázdnou deklaraci (včetně negativní, pokud AI podstatně nepoužili). | ▶ **Silně souhlasím** |
| Souhlas s politikou vydavatele o deklaraci AI je dostatečně přesvědčivý, aby se dalo věřit, že vykazování bylo přesné. | ▶ **Silně nesouhlasím** |

### 4B. Stanovisko k povinné neprázdné deklaraci a „nulovým“ deklaracím

**Podporujeme — a to z jiného důvodu než obvyklého.** Argument kulturní změnou je v pořádku, ale
slabý. Silný argument je důkazní: mlčení nelze falzifikovat, zatímco nulová deklarace je
**konkrétní, datované, přiřaditelné tvrzení**. Ukáže-li se později podstatné nedeklarované užití
AI, u mlčení následuje spor o výklad („nikdo se neptal“), u nulové deklarace doložitelně nepravdivý
výrok s jménem a časovým razítkem. Povinná neprázdná deklarace nezabrání nepoctivosti; mění mlhu
na papírovou stopu. To je velký zisk za cenu jedné řádky.

Tři podmínky, bez nichž se z nulové deklarace stane právě ta prázdná věta, kterou standard
nahrazuje:

1. **Vztáhnout ji k verzím** (P9). *„Kromě zde deklarovaných užití autoři nepoužili AI, která by
   splňovala práh deklarace podle Global Reporting Standard v1.0 (taxonomie v1.0).“* Deklarace,
   která nepojmenuje práh, proti němuž byla měřena, je za dva roky neposouditelná — a práh se
   pohne; standard je výslovně živý.
2. **Svázat ji s přijatou verzí** (P4). Deklarace učiněná při podání a nikdy nepotvrzená je
   tvrzením o souboru, který už neexistuje. Vyžadujte potvrzení při akceptaci, navázané na otisk
   obsahu přijatého rukopisu. Tím se uzavírá to, čemu říkáme problém **visící attestace**: kontrola,
   která přežila to, co kontrolovala. Je to levné — SHA-256 se spočítá za sekundu a ověří ho kdokoli
   — a je to nejméně využitý mechanismus, který má tento standard k dispozici.
3. **Nedovolit, aby ji zastoupil zaškrtávací box.** Souhlas s politikou vydavatele při podání je pro
   čtenáře neviditelný a zpětně nefalzifikovatelný. Deklarace musí být publikovaná s článkem.

**Ke stigmatizaci:** riziko je reálné, ale je hlavně funkcí formulace. Nulová deklarace pojatá jako
absence užití *splňujícího práh*, umístěná ve stejném bloku jako prohlášení o konfliktu zájmů,
normalizuje, nikoli vyděluje. Větší stigmatizační riziko je dnes to opačné: že poctivě deklarující
autor vypadá hůř než mlčící nedeklarující.

---

## 5 — Jak signalizovat odpovědnost a accountability?

### 5A. Má být obecné prohlášení o odpovědnosti součástí deklarace?

▶ **Ano, výchozí prohlášení má být součástí standardu.**

### 5B. Stanovisko k obecným prohlášením o odpovědnosti

Zařadit — ale nenechat stát samotné a udělat ho **přiřaditelným, ne kolektivním**. „Autoři nesou
plnou odpovědnost“ platí o každém kdy vydaném článku, a nenese tedy žádnou informaci; námitka
„odškrtávání políček“ je v této formulaci správná. Informaci nese jmenovaná osoba s trvalým
identifikátorem, která přijímá odpovědnost za konkrétní užití AI v konkrétním čase — jeden garant
na každý řádek s podstatným užitím AI, analogicky roli korespondujícího autora. V naší implementaci
je to povinné pole (ORCID garanta + časové razítko) a autora nestojí nic, co by už nevěděl.

Tedy: výchozí věta ať zůstane pro obecný případ, a k tomu vyžadovat **jmenovaný dohled u každého
podstatného užití** (viz 5E, poslední řádek, který hodnotíme jako *Essential*).

### 5C. Jaké informace o ověření a dohledu mají autoři uvádět

Tady máme nejvíc co nabídnout — protože jsme to postavili a pak v tom sami selhali.

**Strukturovaně, ne narativně — se slotem na narativ.** Ukázková prohlášení v přípravném materiálu
problém dobře ilustrují: „generická“ ukázka („autoři zkontrolovali a upravili veškerý AI generovaný
obsah“) je nefalzifikovatelná, a ukázky „rigorózní“ i „popisné“ jsou výborné, ale nelze je
srovnávat napříč články, prosévat ve velkém ani kontrolovat na vnitřní konzistenci. Řádek s pěti
sloty na jedno deklarované užití je zvládnutelný v minutách a je srovnatelný:

| Slot | Obsah | Proč |
|---|---|---|
| 1. Činnost | ID kategorie taxonomie | srovnatelnost |
| 2. Aktér | který AI systém (poskytovatel, rodina modelu, **verze/snapshot**, rozhraní) nebo který člověk | „použili jsme LLM“ není popis nástroje; datovaná verze je |
| 3. Co bylo zkontrolováno a kým | uzavřený číselník: *nezkontrolováno* · *pročteno autorem* · *výběrově (uveďte podíl)* · *plně přepočítáno / znovu spuštěno* · *ověřeno proti primárním zdrojům* · *zkontrolováno jmenovanou třetí stranou* · *nezávisle reprodukováno* | tato osa mění deklaraci na accountability |
| 4. Stopa | jaký záznam existuje (prompt/log/kód/výstup), jeho identifikátor a otisk, a režim přístupu: *veřejný · embargo · na vyžádání · omezený · neuchováno* — s důvodem, kdykoli není veřejný | prompty a logy často zveřejnit nelze (osobní údaje, licencovaný text, materiál třetích stran); i nezveřejnitelný záznam lze *odkázat otiskem*, což činí pozdější záměnu zjistitelnou |
| 5. Co zkontrolovat nešlo | krátký volný text, **povinný** | nejinformativnější pole celého záznamu — a první, které vypadne, bude-li volitelné |

**Číselník ve slotu 3 je žebřík — a Focus Track ho už nakreslil.** Sezení 4.B navrhlo attestace →
review → audit → replikace. Naše implementace používá čtyři úrovně důkazu (*deklarováno → doloženo
artefaktem → nezávisle attestováno → reprodukováno*). Jsou to dva pohledy na tutéž strukturu
a rozdíl je poučný: Perkinsův žebřík odstupňovává **sílu kontrolního aktu**, náš to, **co může
o tvrzení ověřit třetí strana**. Obě osy jsou potřeba, protože „prohlédl jsem výstup“ bez dochované
stopy je důkazně tvrzení první úrovně:

| Žebřík ze sezení 4.B | Co tvrdí | Úroveň důkazu, když se zeptáme, co zůstalo |
|---|---|---|
| Attestace — „nesu odpovědnost“ | odpovědnost | **deklarováno** — slovo jmenované osoby, viditelně neověřené |
| Review — „prohlédl jsem výstup“ | vlastní kontrola | **deklarováno**, nebo **doloženo artefaktem**, pokud kontrola zanechala trvalou stopu |
| Audit — „zkontroloval jsem proces a doklady“ | kontrola procesu | **doloženo artefaktem** u autorské kontroly; **nezávisle attestováno**, udělala-li to jmenovaná třetí strana s vymezeným rozsahem |
| Replikace — „reprodukoval jsem / prověřil jiným postupem“ | znovuprovedení | **reprodukováno** |

Dva důsledky, které by měly být ve standardu výslovně:

- **Existence logu sama nezvyšuje úroveň tvrzení o práci.** Log může být neúplný nebo o něčem
  jiném. Naše pravidlo: artefakt zvedá tvrzení na úroveň 2 (existuje stopa) a sám nikdy výš. Výš
  jde jen jmenovaný externí ověřovatel nebo znovuprovedení.
- **Oddělte „dohledáno“ od „podporuje“** (P5). Automaty spolehlivě zjistí, že citovaný zdroj
  existuje a že mu sedí metadata. **Nezjistí** spolehlivě, že zdroj podporuje konkrétní tvrzení,
  k němuž je citován. Musí to být dvě pole se dvěma jmény, jinak standard vyrobí razítko „citace
  ověřeny“, které certifikuje jen existenci — falešná záruka horší než žádná. Držíme tři oddělené
  pojmy: *reference dohledány* (automat), *podpora tvrzení posouzena* (report s metodou a mírou
  jistoty), *podpora tvrzení attestována* (jmenovaný člověk, vymezený rozsah).

### 5D. Kde mají být informace o ověření a dohledu dohledatelné?

▶ Zaškrtnout: **v samostatném prohlášení v článku** · **v repozitáři jako doplňkové materiály** ·
**na vyžádání pro recenzenty, čtenáře, redakci**

Nikoli „jen v hlavním textu“ (nesrovnatelné) a nikoli „zaznamenat, ale nezpřístupňovat“
(neověřitelný záznam není důkaz). Platí tříúrovňová odpověď z 2B: ukazatel v článku, záznam
v repozitáři, omezené artefakty na vyžádání — s **otisky publikovanými i u artefaktů, které
publikované nejsou**, aby i omezený důkaz zůstal odolný proti tiché záměně.

### 5E. Žádoucnost jednotlivých informací

| Položka | Hodnocení |
|---|---|
| Jaká rizika byla zvážena a mitigována (halucinace, nepřesnost, zkreslení, soukromí, bezpečnost dat, autorská práva, IP) | ▶ **Středně žádoucí** |
| Které části práce byly lidmi zkontrolovány, ověřeny nebo opraveny | ▶ **Nezbytné** |
| Jak byly zdroje, citace, faktická tvrzení, data či výstupy ověřeny proti spolehlivým zdrojům nebo primárním datům | ▶ **Nezbytné** |
| Jakákoli omezení ověření, včetně částí výstupů AI, které nešlo plně zkontrolovat | ▶ **Nezbytné** |
| Zda byly uchovány záznamy interakcí, prompty, logy či auditní stopy — a za jakých podmínek jsou přístupné | ▶ **Nezbytné** |
| Kdo (který člověk) byl odpovědný za dohled a ověření u každého užití AI | ▶ **Nezbytné** |

*Poznámka k prvnímu řádku.* Narativy o mitigaci rizik hodnotíme záměrně níž než ostatních pět a je
to jediné hodnocení, u kterého očekáváme nesouhlas. Obecná próza o rizicích je nejsnáz vyrobitelná
a nejméně kontrolovatelná část jakékoli deklarace; do jednoho publikačního cyklu zkonverguje
k šablonám. Ostatních pět položek jsou výroky, s nimiž lze někoho konfrontovat. Pole o rizicích
ponechte, udělejte ho volitelné a nabídněte konkrétní rizika — ale nedopusťte, aby se stalo tím,
co autoři vyplní *místo* kontrolovatelných polí.

### 5F. Co má standard doporučit ohledně transparentnosti ověření a dohledu

1. **Doporučte zaznamenávat nepřítomnost ověření stejně výslovně jako jeho přítomnost.** Standard,
   jehož jediný pozitivní signál je „zkontrolováno“, bude vyplňován slovem „zkontrolováno“. Hodnota
   odstupňovaného záznamu je symetrická: chybějící kontrolu činí *čitelnou*, ne *neviditelnou*.
   Prakticky: autor, který přizná pět podstatných užití AI, z nichž dvě nikdy nikdo nezávisle
   nezkontroloval, vyrobil informativnější a důvěryhodnější dokument než ten, kdo paušálně tvrdí,
   že zkontroloval vše.
2. **Doporučte svázat každé tvrzení o ověření s otiskem obsahu** (P4). To je jediné doporučení,
   které bychom si ponechali, kdybychom museli všechna ostatní pustit. Tvrzení o ověření, které
   pojmenovává stav souboru, nemůže zdědit pozdější, jiný stav souboru. Bez toho je „ověřeno“
   tvrzením o názvu.
3. **Doporučte pravidla pro kurátorovaný důkaz a vyžadujte kurační pravidlo** (P6, příloha B). Surové
   logy a historie promptů běžně **nejsou publikovatelné**: obsahují osobní údaje, licencovaný nebo
   nepublikovaný materiál třetích stran a slepé uličky. Kurátorovaný log je ale tím slabší důkaz, čím
   víc byl kurátorován — a nikdo nevidí, co bylo odstraněno. Naše navržené pravidlo, přenesené
   z toho, jak přísná kolej našeho plánu nasazení řeší výběr agentních běhů: **zveřejni pravidlo
   výběru.** Konkrétně: spočítej otisk **úplného** surového exportu a archivuj ho neveřejně;
   publikuj kurátorovanou verzi s vlastním otiskem; zaznamenej **oba otisky, kurační kritérium
   a druhy odstraněného materiálu**. Tvrzení zůstane na úrovni „doloženo artefaktem“, ale čtenář
   vidí, že důkaz je redigovaný — a podle jakého principu. Kde ani to nelze, je poctivé snížit
   tvrzení na „deklarováno“. Standard, který uzná „log uchován“ bez otázky *který* log a *podle
   jakého výběru*, dostane formalitu místo důkazu.
4. **Doporučte, aby informace o ověření byla strojově generovatelná** (P8), a řekněte to tak, aby na
   to dodavatelé nástrojů mohli reagovat: zveřejněte referenční serializaci záznamu a ukázkový
   export. Viz §6 — tady máme data, ne názor.
5. **Necertifikujte.** Strukturovaný záznam o ověření zve k agregovanému skóre („kvalita provenience
   8/10“). Doporučujeme, aby standard výslovně uvedl, že žádné pole ani jejich kombinace nezakládá
   soud o kvalitě či pravdivosti výzkumu. Certifikace nese odpovědnost, kterou reportovací standard
   unést nemůže, souhrnná skóre se optimalizují místo plnění, a venue se legitimně liší v tom, co
   požadují. Zaznamenejte, kdo co dělal a co je doloženo — a tam se zastavte.

---

## 6 — Souhrn a další zpětná vazba

**Logiku tohoto standardu jsme aplikovali na vlastní rukopis a dvě věci, které se přitom zlomily,
jsou náš hlavní příspěvek do 2. kola.**

**(1) Zpětné doplnění provenience je o jeden až dva řády dražší než záznam v místě vzniku — a
zůstane neúplné.** Rekonstrukce toho, který model co dělal v které fázi, po dokončení práce
znamenala procházet historii sezení a datovat tvrzení. Údaje, jejichž zachycení v okamžiku užití
stojí sekundu, stály zpětně desítky minut a několik z nich zůstalo nedohledatelných. Důsledek pro
standard je přímý: **standard, který spoléhá na dobrovolné zpětné vyplnění, bude vyplňován
povrchně, a kvalita deklarací bude záležet na tom, kolik autorovi zbylo sil, ne na tom, kolik AI
použil.** První kolo si strojovou generovatelnost už vyžádalo; my bychom ji posílili z žádoucí
vlastnosti na požadavek návrhu a přidali dvě operativní věci: zveřejnit referenční serializaci
s rozpracovanými příklady a otevřít kanál k dodavatelům AI nástrojů a platforem kvůli **exportu pro
deklaraci** (na úrovni činností, s časovými razítky, ukotvený otisky). Asymetrie je příznivá: čím
těžší zapojení AI, tím automatizovatelnější záznam — agentní pipeline ho může vydávat průběžně.
Nástroj, který zachytává, vyhrává nad pokynem, který se ptá.

**(2) Surové logy nejsou publikovatelný artefakt — a kurátorované logy jsou důkazem jen tehdy, je-li
kurační pravidlo veřejné.** Naše vlastní první karta tvrdila úroveň „doloženo artefaktem“ s odkazem
na log pracovních sezení, který v surové podobě vydat nemůžeme: obsahuje nepublikovaný materiál
třetích stran, osobní poznámky a osobní údaje. Poctivé možnosti byly přesně dvě: publikovat
kurátorovanou verzi *s pravidlem výběru*, nebo dotčená tvrzení vrátit na „deklarováno“. Bylo to
selhání našeho vlastního návrhu, které jsme našli jen tím, že jsme ho použili — a opravou je
příloha B, dvouotiskový záznam kurace. Doporučujeme, aby ho Vancouver Standard obsahoval
v jakékoli formulaci, kterou zvolí, protože „log uchován“ bez kuračního pravidla bude jinak
nejlevnějším způsobem, jak vypadat doloženě, aniž je člověk doložený.

Třetí poznatek uvádíme jako argument pro žebřík, ne pro nás: **aplikace odstupňovaného záznamu nás
donutila snížit vlastní tvrzení.** Deklarační formát, jehož poctivé užití autora něco stojí, dělá
svou práci — a je to zároveň nejsilnější důvod držet úrovně uzavřené a v malém počtu.

**K procesu.** Trojkolový design, zveřejněný přípravný materiál a oddělené otázky na umístění
a taxonomii udělaly z této konzultace neobvykle dobře uchopitelnou věc. Dva návrhy: (a) publikujte
výstup 2. kola jako **verzovaný, strojově čitelný návrh** (soubor slovníku plus ukázkové záznamy),
ne jen jako prózu — implementátoři pak mohou ve 3. kole odpovědět běžícím kódem místo komentářů;
(b) vyžádejte si v každém kole aspoň jednu implementační zprávu od někoho, kdo se pokusil záznam
skutečně vyplnit: selhání jsou informativnější než souhlasy.

**Co můžeme přinést.** Funkční otevřený implementační profil (schéma, validátor, kontrola
dohledatelnosti referencí, generátor deklarací pro vydavatele, registr nad gitem, vykreslené
panely; specifikace CC BY 4.0, kód MIT); crosswalk taxonomie z přílohy A jako udržovaný strojově
čitelný soubor; pilotní data z aplikace na reálné rukopisy; a mapovací vrstvu na jakýkoli slovník,
který standard přijme. Rádi budeme testovacím implementátorem návrhu ve 3. kole: dejte nám
návrhový slovník a ohlásíme, co validuje a co ne.

**Poctivé meze tohoto podnětu.** Jde o projekt jednoho autora v rané fázi. Jeho registr obsahuje
dnes jedinou kartu — naši vlastní. Nemá žádnou nezávislou attestaci. Jeho sebe-aplikace přinesla
oba výše uvedené poznatky selháním, ne úspěchem. Nic z toho nejsou pilotní data ve velkém; je to
zkušenost jedné implementace, nabídnutá jako taková.

---

## Atribuce a kontaktní preference

- **Volitelná atribuce:** *Jan Nehyba, odborný asistent, Pedagogická fakulta, Masarykova univerzita
  (Česko)* — souhlas s tím, aby citace z volných odpovědí byly připsány. *(Změnit, chceš-li zůstat
  neuveden.)*
- **Kontakt po podání:** ▶ Ano, kontaktujte mě k mým odpovědím · ▶ Ano, pozvěte mě do 3. kola ·
  ▶ Ano, informujte mě o finálním výsledku
- **Jak jsem se o kole dozvěděl:** ▶ Jinak → *„sleduji Focus Track veřejně (web ISC); vyvíjím
  implementační profil pro tento standard.“*
- **Vztah k AI systémům:** ▶ Profesionálně intenzivní uživatel
- **Role / fáze kariéry:** ▶ Aktivní badatel (s Ph.D.) · ▶ Badatel s trvalou smlouvou

---

## Příloha A — Crosswalk: navržených 18 kategorií ↔ funkční implementace

Strojově čitelná verze: [`taxonomy-crosswalk-v0.1.json`](./taxonomy-crosswalk-v0.1.json). Navržené
identifikátory jsou ilustrativní (forma slug, podle P1); `credit:*` jsou role CRediT (ANSI/NISO
Z39.104-2022), `rpc:*` jsou naše AI rozšíření.

| # | Navržená kategorie | Navržené ID | Mapuje na | Poznámka |
|---|---|---|---|---|
| 1 | Idea generation | `vs:idea-generation` | `credit:conceptualization` | hrubé na naší straně: 1 a 2 splývají |
| 2 | Hypothesis development | `vs:hypothesis-development` | `credit:conceptualization` | jako výše |
| 3 | Literature search | `vs:literature-search` | `rpc:source_retrieval` | přesná shoda |
| 4 | Literature summarization | `vs:literature-summarization` | — | **mezera u nás** → doplníme `rpc:literature_synthesis`; překryv s 16 |
| 5 | Design › study/experiment design | `vs:design-study` | `credit:methodology` | vztah nadřazenosti udělat explicitní |
| 6 | Design › data collection methodology | `vs:design-data-collection` | `credit:methodology` | |
| 7 | Design › data analysis plan | `vs:design-analysis-plan` | `credit:methodology` | |
| 8 | Data collection (operations) | `vs:data-collection` | `credit:investigation` | nejasné proti 9 |
| 9 | Data creation | `vs:synthetic-data-generation` | — | **přejmenovat**: syntetická/simulovaná data; mezera u nás |
| 10 | Code generation/refinement/auditing | `vs:code-generation` | `credit:software`, `rpc:code_generation` | „auditing“ patří do chybějící kategorie B |
| 11 | Data cleaning/preprocessing/auditing | `vs:data-preparation` | `credit:data_curation` | jako výše |
| 12 | Quantitative data analysis | `vs:quantitative-analysis` | `credit:formal_analysis` | jejich rozdělení je lepší než naše |
| 13 | Qualitative data analysis | `vs:qualitative-analysis` | `credit:formal_analysis` | **rozdělení přebíráme** |
| 14 | Data visualization | `vs:data-visualization` | `credit:visualization` | |
| 15 | Figure or image generation | `vs:image-generation` | `credit:visualization` | **rozdělení přebíráme**; integritně kritické |
| 16 | Drafting manuscript or abstract text | `vs:drafting-text` | `credit:writing_original_draft`, `rpc:text_generation` | |
| 17 | Translation | `vs:translation` | — | **mezera u nás** → doplníme `rpc:translation`; spravedlnostní poznámka v 1A(c) |
| 18 | Editing or rewriting incl. reference lists | `vs:editing-rewriting` | `credit:writing_review_editing` | oddělit práci s referencemi |
| **A** | *Orchestrace / provoz agenta* | `vs:orchestration` | `rpc:prompt_orchestration`, `rpc:agent_operation` | **navrhované doplnění** |
| **B** | *Ověřování prováděné AI* | `vs:ai-verification` | zaznamenává se jako strojové `checks`, ne jako činnost | **navrhované doplnění** |
| **C** | *Výběr mezi běhy/výstupy* | `vs:output-selection` | navrhovaná `rpc:run_selection` | **navrhované doplnění**, integritně kritické |

## Příloha B — Navržený záznam pro kurátorovaný důkaz (dvouotiskové pravidlo)

Platí, kdykoli se prompt / log / záznam interakce publikuje v upravené podobě. Názvy polí jsou naše;
podstatný je požadavek.

```json
{
  "id": "log_curated",
  "type": "log",
  "uri_or_pid": "<DOI uloženého kurátorovaného logu>",
  "sha256": "<otisk publikované kurátorované verze>",
  "access_status": "public",
  "curation": {
    "raw_sha256": "<otisk úplného surového exportu>",
    "raw_access_status": "restricted",
    "rule": "Odstraněny pasáže obsahující nepublikované materiály třetích stran, osobní poznámky a osobní údaje. Věcný obsah včetně chybných tvrzení modelu a jejich oprav ponechán beze změny.",
    "removed_kinds": ["nepublikované materiály třetích stran", "osobní poznámky", "osobní údaje"]
  }
}
```

Tři požadavky, nezávisle na syntaxi:

1. Otisk **úplného surového exportu** je zaznamenán a export archivován, i když se nepublikuje.
2. **Publikovaná** verze nese vlastní otisk a identifikátor.
3. **Kurační kritérium a druhy odstraněného materiálu** jsou uvedeny.

Důvod: redigovaný záznam zůstává odolný proti tiché záměně (1, 2) a jeho důkazní váha se stává
posouditelnou (3). Bez (3) je „log uchován“ formalita; s (3) čtenář ví, na jaký druh důkazu se dívá.
Kde nelze splnit ani jedno, patří dotčené tvrzení na nejnižší úroveň, ne mezi doložená.

## Příloha C — Jak řádkový záznam plní šest kritérií z 1. kola

| Kritérium z 1. kola | Jak to řádkový, otiskem svázaný záznam dodá |
|---|---|
| Snadno pochopitelný a snadno vyrobitelný | jeden řádek na deklarované užití; drahá pole (otisky, verze) se počítají, nepíšou; deklarace vydavatelů se generují ze záznamu |
| Konzistentní struktura, srovnatelnost a reprodukovatelnost | uzavřené číselníky pro činnost, druh aktéra, úroveň ověření, režim přístupu |
| Strojově čitelný **a strojově generovatelný** | jeden validovaný datový soubor kontrolovaný schématem; agentní pipeline ho může vydávat průběžně (P8) |
| Flexibilní popis povahy a rozsahu užití | volný popis u každého řádku a povinné pole „co zkontrolovat nešlo“ |
| Více nástrojů a užití v jedné práci | aktéři i řádky jsou seznamy; jedna práce může nést mnoho systémů, verzí a rozhraní |
| Napříč obory a typy výstupů | slovník činností je oborově neutrální; oborové příklady a podkategorie se na něj navěšují (1A(b)) |

---

*Určeno k podání přes <https://council.science/AIdisclosure> do 16. října 2026. Dotazy: Bert Seghers
(office@enrio.eu), k etice průzkumu Mike Perkins (mike.p@buv.edu.vn). Zdroje ke všem procesním
faktům jsou v [`README.md`](./README.md).*
