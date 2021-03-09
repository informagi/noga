---
layout: "post"
title: "Pilot binnen de Radboud Universiteit"
author: "Pepijn Boers"
date: "2021-01-29 12:00"
excerpt: "Vergelijking Google Analytics en Matomo"
tags: NoGA Matomo Google Analytics Radboud universiteit pilot
---


Wie aan zijn of haar organisatie voorstelt om Google Analytics 'de deur uit te doen' krijgt direct de wedervraag 'hoe dan?!'. In deze blog beschrijven we de bevindingen die een pilot met Matomo Analytics binnen de Radboud Universiteit heeft opgeleverd. De hoofdvraag hierbij is: "Vormt Matomo een geschikt alternatief voor Google Analytics?"

# Pilot
Gedurende een periode van een maand hebben Matomo en Google Analytics naast elkaar gedraaid en is er door beide systemen bezoekersdata verzameld. Daarnaast is er onderzoek gedaan naar het gebruik van web analytics binnen de Universiteit en zijn er 30+ scenario's beschreven waarin Google Analytics een rol speelt. Vervolgens is er per scenario gekeken wat de functionaliteiten van Matomo zijn.

Een vergelijking van de gemeten bezoekersdata biedt een indicatie van de nauwkeurigheid van Matomo, daarbij is de vraag "Is Matomo in staat om even nauwkeurige of zelfs betere metingen te doen dan Google?". Een vergelijking in scenario's wordt gebruikt om de competentie van Matomo als vervanger van Google Analytics te pijlen. De vraag die daar centraal staat is "Bevat Matomo gelijkwaardige functionaliteiten als Google Analytics?"

## Basale metingen
Om een indicatie van de nauwkeurigheid van Matomo te krijgen is er een selectie van de meeste basale metingen gemaakt en zijn de door beide systemen gemeten waardes met elkaar vergeleken. Hieronder staan de definities die Matomo en Google voor deze metingen hanteren:


| Meting            | Google Analytics[^1]                                                                                                                                                                                                                                                                                                                                                                     | Matomo[^2]                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Pageviews         | A pageview is defined as a view of a page on your site that is being tracked by the Analytics tracking code. If a user clicks reload after reaching the page, this is counted as an additional pageview                                                                                                                                                                              | The number of times this page was visited.                                                      |
| Avg. time on page | Average time on page is simply the average amount of time all users spend on a single page. But measuring it isn’t as straightforward as you’d think.Google Analytics tracks time on page and time on site by measuring the difference between the timestamps of hits. If the visit is a bounce (that is, the visitor leaves after viewing just one page), no time will be recorded. | The average amount of time visitors spent on this page (only the page, not the entire website). |
| Bounce Rate       | Bounce rate is the percentage of sessions with a single pageview.                                                                                                                                                                                                                                                                                                                    | The percentage of visits that started on this page and left the website straight away.          |
| Exit rate         | The page’s exit rate indicates how often visitors exit from it after visiting any number of pages on the site; as a percentage, exit rate is calculated as the number of exits / number of pageviews for a particular page.                                                                                                                                                          | The percentage of visits that left the website after viewing this page.                         |
| Entrances         | The first page that someone views during a session is known as an entrance. You can see the number of times a page was viewed first using the ‘entrance’ metric.                                                                                                                                                                                                                     | Number of visits that started on this page.                                                     |


[^1]: [Definities](https://www.lovesdata.com/blog/google-analytics-glossary#bounce-rate=) meeteenheden Google analytics
[^2]: [Definities](https://glossary.matomo.org/#/metrics) meetenheden Matomo Analytics

Een overzicht van de gemiddelde waardes is te zien in onderstaande tabel:

|                   | Google Analytics | Matomo |
|-------------------|------------------|--------|
| Pages             | 27737            | 27737  |
| Pageviews         | 44.93            | 44.90  |
| Avg. time on page | 92.01            | 65.82  |
| Bounce rate       | 39.17            | 36.38  |
| Exite rate        | 48.31            | 47.68  |
| Entrances         | 15.02            | 22.04  |

De verdeling van de gemeten waardes is te zien in de volgende boxplots:
 
<img src="{{site.baseurl}}/assets/img/boxplot_per_meting.png">

Bij het plotten van het aantal paginaweergaven voor een selectie willekeurige pagina's is de volgende verdeling te zien:

 <img src="{{site.baseurl}}/assets/img/sampled_per_page_difference_150.png">

In deze resultaten is zichtbaar dat beide systemen overeenkomstige waardes meten voor 'paginaweergave', 'Exit-rate' en 'Bounce-rate'. Als er wordt gekeken naar een willekeurige selectie van 150 pagina's, is te zien dat er soms kleine verschillen in het aantal paginaweergaven te vinden zijn. Naar alle waarschijnlijkheid zullen verschillen van deze omvang in de praktijk niet tot andere conclusies leiden. Voor de gemiddelde tijd op een pagina en de gemeten binnenkomsten (entrances) worden grotere verschillen geregistreerd. Deze kunnen mogelijk verklaard worden door een afwijkende implementatie van bezoeksessies. Wanneer blijf je tijd doortellen en wanneer start je een nieuwe sessie? Ook hier is het onwaarschijnlijk dat de gemeten verschillen de gebruiker tot andere conclusies laat komen. Daarbij is het wel van belang dat er consequent met dezelfde maat wordt gemeten.

## Scenario's
Voor de vergelijking van functionaliteiten, is er gekeken naar een selectie van 36 scenario's waarin relevante activiteiten van Google Analytics binnen de universiteit beschreven staan. Voor ieder scenario is er gekeken naar de mogelijkheden die Matomo biedt in een vergelijkbaar scenario. Hierbij zijn officiële documentatie, FAQ's en andere fora geraadpleegd. Daaruit heeft zich een [overzicht](https://github.com/informagi/noga/raw/master/docs/assets/pdf/noga_scenarios.pdf) gevormd waarin er per scenario beschreven staat welke mogelijkheden er door Matomo worden geboden. 

<img src="{{site.baseurl}}/assets/img/scenarios_pie.png">

Uit dit overzicht volgt dat Matomo in 30 van de 36 scenario's een volwaardig alternatief kan bieden en daarmee in staat is om Google Analytics in zijn huidige staat te vervangen. Van de overige scenario's zijn er vier gedeeltelijk en twee niet uitvoerbaar. Zo bleek het bijvoorbeeld lastig om bezoekersstatistieken bij te houden wanneer bezoeken over meerdere domeinen verspreid zijn en was er voor sommige functionaliteiten een hoop handmatig werk vereist alvorens een scenario uit te voeren was. Daarnaast zijn scenario's waarin specifieke Google diensten met elkaar samen werken niet direct mogelijk in Matomo. Denk bijvoorbeeld aan het re-targeten van een specifieke bezoekersgroep met een reclames vanuit Google Ads. Of het filteren op bezoekerseigenschappen zoals leeftijd en geslacht (Google doet dit aan de hand van account profielen of DoubleClick cookies).

Verder valt het op dat Matomo in veel gevallen een kant-en-klare plugin beschikbaar heeft die een specifieke klus geheel op zich kan nemen. Hierdoor kan het invoeren van handmatige instructies tot een minimum worden beperkt. Deze plugins worden in veel gevallen gemaakt door van de online community, welke een groot open source project met zich meebrengt. Extra plugins zijn beschikbaar via de Matomo marktplaats, waarin ontwikkelaars deze met elkaar kunnen delen. Het is echter wel zo dat om garantie van kwaliteit en drijfveer tot maken van plugins te waarborgen, deze vaak tegen betaling beschikbaar zijn.

De door ons beschreven scenario's vereisen de volgende plugins, waarvoor jaarlijks een van het aantal gebruikers afhankelijk bedrag moet worden betaald. 

| Plugin                               | 1-4 gebruikers | 5-15 gebruikers | ongelimiteerd |
|--------------------------------------|----------------|-----------------|---------------|
| Funnels                              | 179            | 349             | 529           |
| Media Analytics                      | 149            | 299             | 449           |
| Multi Channel Conversion Attribution | 79             | 149             | 229           |
| Custom Reports                       | 199            | 399             | 599           |
| Search Engine Keywords Performance   | 129            | 249             | 379           |
| Totaal (in $)                        | 735            | 1445            | 2185          |


Mocht er geen plugin klaar liggen voor het gewenste scenario, dan kan met behulp van Matomo's uitgebreide [API](https://developer.matomo.org/api-reference/api-reference-introduction), zelf een oplossing worden gecreëerd. Dit biedt ruimte voor nieuwe mogelijkheden die bij bijvoorbeeld Google niet haalbaar zijn. Denk hierbij aan het volgen van geavanceerde interne processen die door de API makkelijk aan bezoekersstatistieken te koppelen zijn.

## Discussie
Het doel van deze pilot is om een zo goed mogelijke vergelijking te maken tussen beide systemen. Het is echter onhaalbaar om een perfecte vergelijking te maken waarin elk aspect volledig wordt belicht. Daarom heeft deze pilot zich beperkt tot een vergelijking op nauwkeurigheid van metingen en op functionaliteiten in specifieke scenario's. Daarbij lag de focus op de huidige toepassing van web analytics binnen de Radboud universiteit. 

Mede door een complexe opzet van interne websites binnen de universiteit was het niet mogelijk om gebruikersdata direct met elkaar te vergelijken. Het gebruik van specifieke filters op url parameters en de opdeling van verschillende stukken data over aparte Google Analytics profielen speelt daarbij een belangrijke rol. Om hiervoor te corrigeren en als nog een vergelijking mogelijk te maken, is er alleen gekeken naar de overlappende pagina's in de geëxtraheerde data. 

Het blijft echter de vraag hoe relevant een vergelijking op geregistreerde paginaweergaven daadwerkelijk is. In de loop der jaren is het bijhouden van het handelen van een bezoekers steeds belangrijker geworden en zijn statistieken als paginaweergaven of exit-rates meer naar de achtergrond verdwenen. Het is immers veel interessanter om te weten hoe een bezoeker zich op jouw website heeft gedragen dan om te weten dat er een bezoek heeft plaatsgevonden. Een vergelijking op basis van bezoekersgedrag zou daarom een waardevolle bijdragen kunnen leveren aan toekomstig onderzoek.

Ook is het zo dat programma's zoals Matomo en Google Analytics een breed scala aan mogelijkheden hebben die in verschillende manieren, vaak per bedrijf verschillend, kunnen worden ingezet. Het is daarom moeilijk om een representatieve verzameling van test scenario's te maken. De vergelijkingen in deze pilot zijn voornamelijk gericht op de huidige gang van zaken binnen de universiteit en generaliseren daardoor niet per se naar andere organisaties of algemeen voorkomen. Daarnaast zijn, door de grote hoeveelheid maatwerkoplossingen en de afhankelijkheid van campagne-momenten, de meeste oplossingen voor scenario's enkel in theorie beschreven. Hierdoor zijn wellicht onverwachte complicaties onder de radar gebleven.  


## Conlcusie
De resultaten van de pilot wijzen erop dat Matomo en Google een vergelijkbare nauwkeurigheid van bezoekersdata leveren. In sommige gevallen kunnen geregistreerde waardes verschillen, maar deze zullen in de praktijk niet snel tot verschillende conclusies leiden. 

Aan de hand van de opgestelde scenario's is gebleken dat Matomo in staat is om in meer dan 80% van de gevallen Google Analytics’ plek in te nemen als web analytics tool binnen een organisatie zoals de Radboud universiteit. Wel zijn hiervoor in sommige gevallen betaalde plugins of handmatige koppelingen nodig.

Verder is het zo dat Google Analytics voor veel eigen diensten automatische integratie biedt. Dit kan in veel gevallen erg handig zijn, bijvoorbeeld bij een koppeling tussen een specifieke bezoekersgroep en een reclame campagne via Google Ads. Deze integratie is bij een overstap naar Matomo vaak een stuk minder intuitief. Daartegenover staat wel dat ook de barriere die Google heeft opgebouwd om koppelingen met concurrenten te bemoeilijken wegvalt bij een eventuele overstap. Daarnaast heeft Matomo een uitgebreide community waarin vaak nieuwe plugins worden ontwikkeld die specifieke functionaliteiten of koppelingen beschikbaar stellen.

### Vormt Matomo Analytics een waardige vervanger voor Google Analytics binnen de Radboud Universiteit?

**minpunten**
- Geen automatische integratie met Google diensten
- Hogere kosten (plugins en hosting)
- Sommige scenario's zijn niet langer uitvoerbaar

**pluspunten**
- 100% eigenaar van eigen data
- Grote hoeveelheid extra functionaliteit via plugins
- Toegang tot een uitgebreide API waardoor zeer specifieke functionaliteit kunnen worden gebouwd
- Niet langer beperkt tot integratie met enkel Google diensten

### Aanbeveling
Resultaten uit deze pilot laten zien dat Matomo technisch gezien in staat is om veel van Google Analytics' taken over te nemen. Daarbij is wel een vereiste dat er genoeg IT kennis aanwezig is om eventuele ontbrekende koppelingen handmatig aan te kunnen leggen. Daarnaast dient er bereidheid te zijn tot het aanleren en uitzoeken van Matomo's interne functionaliteiten. Want ondanks de vele instructie videos en documentatiepagina's, valt er moeilijk op te boksen tegen Googles instructie (en opleidings) materiaal. Het oplossen van bepaalde vraagstukken zal dus met Matomo in sommige gevallen meer uitzoekwerk vereisen. Financieel gezien gaat een overstap op Matomo gepaard met extra kosten, omdat er niet langer gebruik kan worden gemaakt van gratis (met data betaalde) Google diensten. Uiteindelijk zal het besluit om over te stappen afhangen van de mate waarin men bereid is om het gemak van Google in te leveren voor meer zeggenschap over de eigen data en daarmee over de privacy van eigen bezoekers.

Deze pilot is ook beschikbaar in [poster](https://github.com/informagi/noga/raw/master/docs/assets/pdf/noga_poster.pdf) formaat.
