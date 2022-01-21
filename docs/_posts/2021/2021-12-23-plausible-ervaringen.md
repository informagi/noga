---
layout: "post"
title: "Ervaringen met Plausible"
author: "Gijs Hendriksen"
date: "2021-12-23 9:00"
excerpt: "Interview over gebruikerservaringen met Plausible Analytics."
tags: NoGA Plausible interview Spinque
---

Tijdens onze [vergelijking van verschillende open source analytics software oplossingen](/2020/06/10/oswa.html) hebben we het al kort gehad over [Plausible Analytics](https://plausible.io). Op dat moment kwamen we tot de conclusie dat Plausible nog niet volwassen genoeg was om mee te nemen in onze overwegingen. Inmiddels zijn we echter ruim een jaar verder en is Plausible flink gegroeid, zowel in volwassenheid als in populariteit. Dit was voor ons reden genoeg om nog een keer een blik te werpen op Plausible als alternatief voor Google Analytics. Om een goed beeld te krijgen van de ervaringen met Plausible hebben we gesproken met Peter Tessel van Spinque, waar ze nu een tijdje gebruikmaken van Plausible.


## Spinque en analytics

[Spinque](https://spinque.com/) is een bedrijf dat op maat gemaakte zoekmachines levert aan haar klanten. De voornaamste reden dat ze bij Spinque gebruikmaken van analytics is redelijk eenvoudig, namelijk om gebruikersaantallen op hun website bij te houden en in te zien hoe deze veranderen naar aanleiding van bepaalde posts op externe media. De specifieke aanleiding om te beginnen met het gebruik van analytics was een korte video over een specifieke case bij een van hun klanten, die ze graag op LinkedIn wilden plaatsen. Eigenlijk waren ze wel benieuwd wat voor effect het plaatsen van deze video zou hebben over het verkeer dat hun website aantrok, en waar deze gebruikers vandaan kwamen. De zoektocht naar analytics begon, en uiteindelijk viel de keuze op Plausible.


## Gebruik van Plausible

In het interview met Peter vroegen we allereerst naar zijn ervaringen met de overstap naar Plausible. Hoe makkelijk was het op te zetten, en hoe duidelijk is het in het gebruik? "Ontzettend makkelijk", zei Peter. Hij vertelde dat ze de keuze hebben gemaakt om _niet_ hun eigen infrastructuur op te zetten (wat wel mogelijk is met [Plausible Self-Hosted](https://plausible.io/self-hosted-web-analytics)). In plaats daarvan worden hun servers onderhouden door het team van Plausible en wordt de data veilig op Europese bodem opgeslagen. Daarnaast is het overzicht van Plausible zo eenvoudig en duidelijk, dat het heel simpel is om te gebruiken en ermee aan de slag te gaan.

Daarnaast hebben we het gehad over het daadwerkelijke gebuik van Plausible, en waar ze analytics bij Spinque precies voor gebruiken. Peter gaf aan dat de video van hun client case uiteindelijk niet op LinkedIn gezet is, dus het bereik daarvan hebben ze nooit kunnen meten. Toch vertelde hij dat hij het erg handig vond om inzicht te hebben op wat er gebeurt op hun website. Je krijgt een idee van welke pagina's veel bezocht worden, hoe lang mensen op deze pagina's blijven hangen en hoeveel bezoekers direct de website weer verlaten (ook wel bekend als de "[bounce rate](https://plausible.io/docs/metrics-definitions#bounce-rate)"). Ook merkte Peter op dat hij het effect van bepaalde LinkedIn posts wel duidelijk terug kon zien in de analytics, doordat er pieken te zien waren in de bezoekersaantallen vlak na het plaatsen van zulke posts.

Toen we Peter vroegen om de voor- en nadelen van Plausible op een rijtje te zetten, had hij vooral voordelen te noemen. Zo hoefde hij zich met Plausible niet bezwaard te voelen dat de data van bezoekers ergens terechtkomt waar het niet hoort. Plausible verzamelt al zo min mogelijk data, en gaat ook erg secuur, respectvol en zorgvuldig om met de data die ze wel verzamelen. Het doet precies wat het moet doen, en dat sluit nauw aan op de use cases van Spinque. Ook hoeven ze gebruikers niet lastig te vallen met cookie banners, en leveren ze deze data niet in bij grote bedrijven als Google.

Het enige nadeel waar Peter op kon komen was dat het, vanwege de minimale hoeveelheid data die er verzameld wordt, niet mogelijk was om bepaalde gebruikers (bijvoorbeeld de medewerkers van Spinque) uit te sluiten van de analytics data. Nu moesten zijn collega's een script installeren dat Plausible blokkeerde, wat niet ideaal was. Aan de andere kant gaf hij wel aan dat dit niet echt een probleem was, en dat het voor de algehele statistieken niet ontzettend veel uit zou maken als deze data wel meegenomen zou worden.

Naast het gebruik van Plausible van Spinque zelf vroegen wij ons ook af of Spinque ook analytics bijhoudt van of voor hun klanten. Peter bevestigde dat ze dit inderdaad voor één klant doen, voor wie ze ook de webpagina zelf hosten. Hij legde uit dat het in Plausible eenvoudig is om een nieuw domein toe te voegen, en deze alleen open te stellen voor specifieke gebruikers. Zo hebben ze de betreffende klant dus ook gemakkelijk toegang kunnen geven tot hun eigen analytics data.


## Dataverzameling door Plausible

Aangezien privacy en dataverzameling belangrijke onderwerpen zijn bij de keuze voor analytics software, vroegen we ons af in hoeverre Peter op de hoogte was van welke data Plausible van hun gebruikers verzamelt. Volgens hem verzamelt Plausible alleen de pagina's die ze bezoeken, vanaf welke sites ze komen (bijvoorbeeld Google of Twitter), wat voor apparaat ze gebruiken en welk land ze vandaan komen.

Ook vertelde Peter dat Plausible geen gebruik maakt van cookies om terugkerende bezoekers te herkennen. In plaats daarvan genereren ze een unieke, onherleidbare token die gebaseerd is op het ip-adres van de gebruiker, de _User-Agent_ van de gebruiker en de huidige website. Dit token is dus uniek voor elke gebruiker van een website, maar ook verschillend per website die de gebruiker bezoekt. Hierdoor is hij dus niet te volgen tussen verschillende websites. Bovendien wordt in dit token ook een willekeurig gegenereerde _salt_ meegenomen die elke dag verwijderd en opnieuw gegenereerd wordt. Hierdoor is het token voor dezelfde gebruiker toch elke dag weer anders. Dit komt de privacy van de gebruiker ten goede, maar het betekent ook dat terugkerende gebruikers niet over meerdere dagen heen te volgen zijn. Zie, voor meer informatie, ook Plausible's [Data Policy](https://plausible.io/data-policy#how-we-count-unique-users-without-cookies).

Op de vraag hoeveel _controle_ hij zelf heeft over welke data Plausible verzamelt antwoordde Peter dat hij hier zelf nog niet heel erg in gedoken was. Hij wist wel dat het mogelijk was om bijvoorbeeld extra scripts toe te voegen om bepaalde sites uit te sluiten en de dataverzameling verder te personaliseren, maar dit was voor hun doeleinden nog niet nodig geweest.


## Waarom Plausible?

Tijdens de zoektocht naar analytics kiezen veel gebruikers toch voor het gemak van Google Analytics. We vroegen ons af welke alternatieven er bij Spinque nog meer overwogen waren, en waarom dan toch de keuze voor Plausible was gemaakt. En inderdaad, volgens Peter was ook Google Analytics langsgekomen als optie bij Spinque. Ook hebben ze gekeken naar Matomo, die qua functionaliteit wat dichter bij Google Analytics in de buurt komt. Voor de klant die ook gebruikmaakte van analytics hadden ze zelfs een keer met het gebruik van serverlogs geëxperimenteerd, bijvoorbeeld door te kijken naar hoe vaak het logo van de website opgevraagd werd. Hiervan was de conclusie dat dit erg onduidelijke resultaten oplevert (bijvoorbeeld door caching, maar ook door bot-verkeer), en dat je eigenlijk geen idee hebt hoe ver je van de daadwerkelijke bezoekersaantallen af zit.

Uiteindelijk, zei Peter, was Plausible om een aantal redenen de beste keuze. Allereerst is Plausible ontzettend goed in het respecteren van de privacy van de gebruikers. Er wordt alleen de minimaal noodzakelijke informatie verzameld, en deze data is zo generiek en geaggregeerd dat er eigenlijk geen persoonlijke data verwerkt wordt. Ook gebruiken ze geen cookies, en is er dus ook geen cookie consent popup nodig. Door de keuze om cookies niet te gebruiken volledig weg te nemen bij de gebruiker gaat Plausible respectvol om met de gebruiker en bieden ze een prettige gebruikerservaring. Volgens Peter is dit een erg fijne uitgangspositie bij het gebruiken van analytics. Je maakt per definitie de keuze die voor de gebruiker het best is, zonder deze keuze aan hen voor te hoeven leggen.

Daarnaast is Plausible overzichtelijk, eenvoudig en vooral ook transparant. Het is duidelijk waar de data wordt opgeslagen, de code is open source en publiekelijk in te zien, en ze bieden zelfs standaard de optie aan om je analytics data openbaar te maken en met de hele wereld te delen. Dit doet het team van Plausible overigens zelf ook: je kunt hun [openbare dashboard](https://plausible.io/plausible.io) gewoon inzien.

Ook het businessmodel van Plausible sluit goed aan bij de kernwaarden en ambities van Spinque, zei Peter. Plausible wordt ontwikkeld door twee developers, en je betaalt duidelijk voor de service en om het team te onderhouden. In tegenstelling tot een gratis service als Google Analytics, waar je "betaalt" met je data, is het businessmodel hier transparant (lees ook [wat Plausible hier zelf over zegt](https://plausible.io/open-source-website-analytics#google-analytics-is-free-so-why-is-plausible-analytics-cloud-not-free)). Verder hielp het feit dat Plausible een kleine startup is ook met de "gun"-factor, en paste de keuze voor een klein bedrijf beter bij de principes van Spinque dan aansluiten bij een multinational als Google.

Tot slot pasten de functionaliteiten van Plausible perfect bij de use case van Spinque. We hadden het eerder al gehad over de doelen die Spinque voor ogen had bij het gebruik van analytics, en dat deze vooral bedoeld waren voor een globaal overzicht van het gebruik van hun website. Plausible verzamelt precies die data die hiervoor nodig is, niet meer en niet minder (lees ook: [Plausible is simple web analytics](https://plausible.io/simple-web-analytics)). Plausible doet wat het doet, en dat op een zorgvuldige manier, concludeerde Peter.

Op de vraag of hij geen functionaliteiten miste reageerde hij dat hij eigenlijk voldoende informatie had om hun beperkte use case uit te voeren. Hij noemde wel dat het met andere systemen (die gebruikmaken van cookies) makkelijker was om terugkerende bezoekers te volgen. Vanwege de manier waarop Plausible unieke bezoekers telt (met een token die elke dag verandert) kan dit daarmee niet. Voor Spinque kwam het uiteindelijk neer op de vraag welke data ze precies nodig hebben. Je kunt altijd meer data verzamelen en meer willen weten, zoals ook bij Google Analytics gebeurt, maar dat vond Peter gewoon nergens voor nodig. Dat paste wat hem betreft ook helemaal niet bij Spinque als bedrijf.


## Conclusie

Plausible is een ontzettend goed alternatief voor Google Analytics. Het is overzichtelijk, transparant, privacyvriendelijk en eerlijk. Overige voordelen van Plausible zijn het [lichte script](https://plausible.io/lightweight-web-analytics), hun [toewijding aan het milieu en open source software](https://plausible.io/giving-back) en de aantrekkelijke user interface (probeer hem [hier](https://plausible.io/plausible.io) uit). Mocht je interesse hebben en het een keer willen uitproberen, op [de website](https://plausible.io) kun je je gratis inschrijven voor een proefperiode.

Plausible is alleen niet voor iedereen de juiste oplossing. Voor gebruikers die alleen globale overzichten en statistieken willen bijhouden is het een perfecte optie. De mensen die graag meer data willen verzamelen zullen helaas toch verder moeten zoeken. Die mensen raden wij aan om nog eens naar [Matomo](https://matomo.org/) te kijken, of [onze vergelijking tussen open source web analytics systemen](/2020/06/12/oswa_f.html) te raadplegen.

Voor deze blogpost willen we graag Peter Tessel van Spinque bedanken dat hij tijd heeft vrijgemaakt voor dit interview, zijn ervaringen wilde delen en ons de toestemming gaf om deze te delen in een blogpost.
