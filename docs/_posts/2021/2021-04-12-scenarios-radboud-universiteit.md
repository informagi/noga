---
layout: "post"
title: "Radboud Scenario's met Matomo en Google Analytics"
author: "Alessandra van Veen"
date: "2021-04-12 16:00"
excerpt: "Vergelijking Google Analytics en Matomo aan de hand van 36 Radboud Scenario's"
tags: NoGA Matomo Google Analytics Radboud universiteit pilot
---

In de [vorige blog](/2021/01/29/pilot-radboud-universiteit.html) werd een pilot beschreven binnen de Radboud universiteit waarin Matomo en Google Analytics met elkaar werden vergeleken. Hiervoor waren ook scenario's opgesteld. In deze blog beschrijven we een paar van de scenario's en vergelijken we de resultaten van Matomo met die van Google Analytics. Het doel van de vergelijking is om aan de hand van een paar realistische scenario's te kijken of er dezelfde conclusies kunnen worden getrokken met Matomo en Google Analytics.

# De Scenario's

Van de [36 scenario's](https://raw.githubusercontent.com/informagi/noga/master/docs/assets/pdf/noga_scenarios.pdf) hebben wij er vier geprobeerd uit te voeren. We kozen voor deze scenario's omdat ze simpel zijn en daardoor goed de resultaten kunnen vergelijken. In een volgende blogpost zullen we ook kijken naar gebruiksvriendelijkheid van beide systemen aan de hand van deze scenario's.  We hebben de volgende scenario's uitgeprobeerd:

1. Vergelijk de bezoekersdata van twee verschillende master webpagina's in een bepaalde periode en zoek uit hoeveel nieuwe bezoekers er op de informatiepagina's van de desbetreffende masters gevonden zijn.
2. Rapporteer de volgende gegevens: de bezoekersaantallen, de 'bounce rate' en de zoektermen die zijn gebruikt om de pagina te vinden. Doe dit voor zowel de Duitse, de Nederlandse en de Engelse pagina, en vergelijk vervolgens de resultaten. Is er een site die vaker bezocht wordt?
3. Er is een flinke piek te zien in bezoekers op dag X. Zoek uit waar deze piek door is veroorzaakt: een mailing, een specifieke pagina die ineens veel wordt opgevraagd via Google, een link op een andere site, ...?
4. Zoek uit naar welke vervolgpagina's bezoekers van pagina X hebben doorgeklikt. Zoek ook uit of er een directe stap is gemaakt van pagina X naar pagina Y.

# Resultaten

Voor scenario een hebben wij gekeken naar een periode van 7 februari tot en met 13 februari. De resultaten zijn in de tabel hieronder te zien. Het valt op dat er kleine verschillen zijn tussen Matomo en Google Analytics, maar dat de verschillende niet substantieel zijn.

Pagina                                | Analytics | Total pageviews | Total unique pageviews | Total pageviews from new visitors | Total unique pageviews from new visitors
 ------------------------------------ | --------- | --------------- | ---------------------- | --------------------------------- | --- 
/english/education/masters/data-science/ | Google   | 453           | 355                    | 251                               | 195
/english/education/masters/data-science/ | Matomo   | 460           | 362                    | 264                               | 205
/english/education/masters/cognitive-neuroscience/ | Google | 401   | 312                    | 211                               | 165
/english/education/masters/cognitive-neuroscience/ | Matomo | 397   | 312                    | 194                               | 151

Voor scenario twee is weer gekeken naar de periode van 7 februari tot en met 13 februari.  Ook hier zijn geen substantiële verschillen, behalve bij de bounce rate van de Nederlandse pagina van Data Science. Hier geeft Google Analytics een bounce rate van 0% en en Matomo een bounce rate van 20%.

Pagina                                   | Analytics | Unique pageviews | Bounce rate | Zoektermen (intern)
---------------------------------------- | --------- | ---------------- | -----------
/english/education/masters/data-science/ | Google    | 355              | 39.71%      | "data science" "computing science data science" "data" "data analysis" "law" "master's in data science"
/english/education/masters/data-science/ | Matomo    | 31               | 41%         | geen
/opleidingen/master/data-science/        | Google    | 362              | 0.00%       | "data science" "Data science" "computing science" "Computing Science: data science" "data", others.
/opleidingen/master/data-science/        | Matomo    | 33               | 20%         | geen


Voor scenario drie, hebben we gekeken naar de top 3 acquisitiemethoden. Hierbij is er gedaan alsof er op 8 februari een piek was. Voor de methode om de informatie op te zoeken maakt het niet uit of er wel of geen piek was. In de tabel is te zien dat Matomo en Google Analytics andere termen gebruiken. Waar Google Analytics doorverwijzing gebruikt, gebruikt Matomo websites. Hetzelfde wordt hier bedoeld. Er zit wel een verschil tussen organische zoekmethodes en zoekmachines. In Matomo wordt er geen onderscheid gemaakt tussen betaalde zoekresultaten en onbetaalde. Google analytics maakt hier wel een onderscheid in en onbetaalde zoekresultaten zijn dan organisch. Toch zien we dat ondanks het onderscheid Google maakt, Google Analytics een hoger percentage weergeeft.  Matomo laat ook een percentage dat ongeveer 1.5 keer hoger dan dat van Google Analytics is zien voor directe toegang.

Analytics        | #1                         | #2                  | #3
---------------- | -------------------------- | ------------------- | ----
Google Analytics | 61% organische zoekmethode | 20% directe toegang | 6,4% doorverwijzing
Matomo           | 54% zoekmachines           | 34% directe toegang | 7,0% websites

Verder keken we ook welke pagina het meest werd bezocht. De hoofdwebsite en de engelse variant daarvan waren het meest bezocht. Na die twee was `/opleidingen/bacheloropleidingen/toelating-inschrijving/selectie-plaatsing/` de meest bezochte pagina.

Het laatste scenario voerde we uit in dezelfde periode van 7 tot en met 13 februari. Voor pagina X, hebben wij /over-ons/diensten-faciliteiten/vm/aula/livestream/livestream-academiezaal/ gebruikt.  Het eerste figuur zijn de resultaten van Google Analytics. Het tweede figuur zijn de resultaten van Matomo. Zowel Google Analytics als Matomo laten de vervolgpagina's zien op volgorde van het aantal pageviews. Google Analytics laat er maximaal 10 zien. Matomo toonde de eerste vijf en categoriseert de rest onder 'others'. Wel laat Matomo meerdere tops zien. Hoewel Google Analytics alleen een onderscheid maakt tussen exits en next pages, maakt Matomo een onderscheid tussen internal pages, internal searches, download, outlinks, en exits. Voor dit scenario willen we ook graag weten of er naar een specifieke pagina een directe stap is gezet. We hadden gekozen om te kijken of er een stap naar ru.nl was gezet vanaf onze pagina. Zowel Matomo als Google Analytics gaven aan dat er inderdaad een directe stap was.

<img src="/assets/img/scenario4matomo.png">

<img src="/assets/img/scenario4google.png">

# Discussie

In de vorige blog bleek het al dat er verschillen waren, maar dat Matomo en Google Analytics een vergelijkbare nauwkeurigheid leveren. In alle scenario's was dit voor het grootste gedeelte ook aantoonbaar het geval, maar in scenario twee en drie waren er toch significante verschillen te zien.

De oorzaak van de verschillen is niet goed te bepalen. Het is mogelijk dat het verschil komt door de complexe opzet van Google Analytics binnen de Radboud Universiteit. Zoals ook genoemd in de vorige blog, zijn er ook specifieke filters op url parameters gebruikt en verschillende profielen opgesteld dat vergelijking moeilijk maakt. We zagen ook dat Matomo consistent meer bezoekersaantallen had dan Google Analytics. Het is ook mogelijk dat er adblockers zijn die onderdelen van Google Analytics blokkeerde, maar Matomo (nog) niet.  Een factor die mogelijk ook meespeelt is hoe Matomo en Google Analytics bepaalde termen heeft gedefinieerd. In de resultaten van scenario drie was te zien dat Google Analytics een onderscheid maakt of een zoekmachine resultaat organisch of betaald is. Ook zit er verschil in hoe Google Analytics en Matomo directe toegang telt. Google Analytics bewaard data van campagnes en de gebruikers daarvan voor maximaal 6 maanden. Als een gebruiker origineel valt onder de campagne, en vervolgens weer direct op de site komt binnen die periode, zal de acquisitie vallen onder campagne in plaats van directe toegang. Matomo zal het nog steeds onder directe toegang laten vallen.  Een factor die ook invloed kan hebben op de resultaten is hoe Matomo en Google Analytics bezoekers en bezoeken tellen. Matomo telt 100% van de bezoekers, terwijl Google Analytics soms bezoekers sampled.

De substantiële verschillen kunnen in sommige scenario's tot verschillende conclusies leiden. Hoewel dit bij onze huidige scenario's niet het geval is, kunnen we wel een scenario uitbreiden waardoor het wel het geval is. Stel voor dat we scenario twee uitbreiden met de vraag of een pagina effectief is op basis van de bounce rate en we hiervoor een minimum van 20% opstellen, dan zouden we met Matomo zeggen dat het wel effectief is, en met Google Analytics zouden we zeggen dat het niet effectief is. Een theoretisch geval dat ook mogelijk is is dat er op een dag Matomo veel directe toegangen telt, maar Google Analytics geeft juist een hoog getal aan de toegangen door campagnes. Als je dan uitzoekt waar de piek door komt, zal je door Google Analytics denken dat het door een campagne komt, terwijl je die conclusie niet zal trekken met Matomo. Uiteindelijk blijven dit theoretische scenario's en is het niet zeker of deze scenario's überhaupt vaak genoeg voorkomen om een impact te hebben.

# Conclusie

Met het uitvoeren van vier realistische scenario's, kunnen we concluderen dat hoewel de resultaten grotendeels gelijk zijn, er substantiële verschillen kunnen ontstaan. Dit kan invloed hebben op de conclusies die worden gemaakt. Het is natuurlijk de vraag of deze verschillen er nog zijn als Matomo is opgesteld op dezelfde manier als Google Analytics, met complexe filters en segmenten. Omdat we de oorzaak van de verschillen niet zeker weten, is het moeilijk hier een conclusie over te trekken zonder Matomo ook zo op te zetten, wat buiten de scope van de pilot valt. Natuurlijk is het ook maar de vraag hoe vaak er scenario's voor zullen komen waar er echt een andere conclusie wordt getrokken. We kunnen dus concluderen dat Matomo een goed alternatief is voor Google Analytics als we kijken naar resultaten op dezelfde vraag.
