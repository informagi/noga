---
layout: "post"
title: "Features van Google Analytics en Matomo"
author: "Marnix Dessing"
date: "2020-06-19 18:00"
excerpt: "Een vergelijking van de features die Google Analytics en Matomo bieden."
tags: NoGA "Web analytics"
---

# Feature vergelijking Matomo en Google Analytics

Deze pagina heeft als doel de functionele overeenkomsten tussen Google Analytics (GA) en Matomo vast te stellen. Hierbij is gekeken naar een overzicht van features van beide tools. Het Google Analytics overzicht is opgezet door Hylke en het Matomo deel door Marnix. Om de eenvoudig inzichtelijk te maken hoe de verschillende categorieën zich tot elkaar  verhouden is het onderstaande schema aangehouden. Google Analytics dient als uitgangspunt in deze vergelijking omdat de Radboud Universiteit (RU) hier reeds gebruik van maakt. Het is belangrijk voor de RU dat de features die Matomo biedt dezelfde behoeftes voorzien als GA. 


| Legenda | Uitleg |
|---------|--------|
| =       | Vergelijkbare  functionaliteit  |
| $       | Betaalde plugin of feature      |
| ~       | Ongeveer vergelijkbare functionaliteit bijv. een andere invalshoek op dezelfde statistieken |
| +       | Matomo kan aangevuld worden met een gratis plugin |
| -       | Deel van de functionaliteit ontbreekt in Matomo |

## Dashboards (=)
Configureren van dashboards en widgets is in beide programma's mogelijk.

## Custom & saved reports ($)
GA biedt functionaliteiten voor het aanmaken van rapporten en het opslaan van configuraties als rapport:
- Custom reports; inzien, aanpassen en maken
- Saved reports; rapporten kunnen worden opgeslagen, de bijbehorende configuratie-instellingen worden dan ook opgeslagen zodat deze kunnen worden toegepast op nieuwe data

**Matomo** kan gebruik maken van de [custom reports plugin](https://plugins.matomo.org/CustomReports).

Prijs:
* tot 4 users, unlimited websites 199 EUR/year
* 5 tot 15 users, unlimited websites 399 EUR/year
* Onbeperkt users, unlimited websites 599 EUR/year

## Aangepaste meldingen (+)
GA biedt aangepaste meldingen. In Matomo kan hiervoor een [gratis custom alerts plugin](https://plugins.matomo.org/CustomAlerts) worden geïnstalleerd.

## Realtime (~)
Matomo biedt de real-time visitor log met, per bezoek, inzicht in:
* Acties
* Goals
* Locatie
* Apparaat en software info
Daarnaast biedt Matomo een real-time locatie overzicht.

GA biedt real-time gegevens aan onder de volgende rapporten:
- Overzicht; dashboard van realtime verkeer op de site.
- Locaties; overzicht van de locaties van realtime gebruikers.
- Verkeersbronnen; inzicht in waar realtime gebruikers vandaan komen. (Bron, medium en campagne)
- Content; overzicht met welke pagina’s realtime gebruikers bekijken.
- Gebeurtenissen; overzicht met acties die realtime gebruikers doen, klikken op video, link of een chat openen.
- Conversies; De realtime conversaties die plaatsvinden voor de ingestelde doelen.

Het verschil zit in de invalshoek die Matomo geeft op de data. Dit is namelijk per bezoeker. Hoewel in beide tools dezelfde data terug te vinden is, biedt GA geraffineerdere overzichten.

## Doelgroep en bezoekers
Beide tools beschikken over een overzichtspagina in deze categorie.

### Lifetime value (=)
In GA laat deze feature de opbrengst per gebruiker zien. De gegevens zijn aanwezig in Matomo voor e-commerce sites. Eveneens per bezoeker.

### Cohortanalyse ($)
De cohortanalyse die GA biedt is beschikbaar in Matomo [via een betaalde plugin](https://plugins.matomo.org/Cohorts). Een overzicht met percentage van gebruikers per cohort (dag/week/etc) dat nog actief is na x dagen, is een onderdeel van de plugin. Daarnaast kan er in Matomo ook op acquisitiedatum worden gefilterd met de plugin.

Prijs:
* Tot 4 users, unlimited websites 89 EUR/year
* 5 to 15 users, unlimited websites 169 EUR/year
* Ongelimiteerd users, unlimited websites 259 EUR/year

### Doelgroep informatie (-)
De volgende informatie die in GA wordt aangeboden is niet beschikbaar in Matomo:
- Doelgroepen: Informatie over het sitegebruik van gedefinieerde doelgroepen. Lijkt niet gebruikt te worden door de RU.
- Demografie:
   - Overzicht: Dashboard met demografische statistieken over gebruikers, man/vrouw, leeftijd
   - Leeftijd: Statistieken over gebruikers per leeftijdscategorie
   - Geslacht: Statistieken over gebruikers per geslacht
- Interesses:
   - Overzicht: Dashboard met overzicht o.b.v. interesses.
   - Affiniteitscategorieën: Statistieken over gebruikers per Affiniteitscategorie
   - Marktsegmenten:  Statistieken over gebruikers per marktsegment
   - Overige categorieën:  Statistieken over gebruikers per categorie
- Benchmarking: Uitgeschakeld op GA van de RU.

### Software (~)
GA biedt onder technologie de volgende rapporten:
- Browser en besturingssysteem: statistieken over gebruikers per categorie
- Netwerk: statistieken over gebruikers per serviceprovider of hostnaam.

Bij Matomo is het browser en besturingssysteem rapport te vinden onder software. Statistieken o.b.v. netwerk gegevens is niet te vinden in de standaard matomo installatie.

### Visit log (=)
De GA gebruiksanalyse: Analyse van individuele gebruikers, medium/bron, devices, aantal sessies, conversies, etc. Is terug te vinden in de Matomo visit log per gebruiker.

### Locatie (=)
Matomo en GA statistieken m.b.t. locatie en taal komen overeen.

### Gedrag (=)
De informatie onder "gedrag" in GA kan vergeleken worden met de "engagement" informatie in Matomo.

### Apparaten (=)
De rapporten in GA zijn te vergelijken met de Matomo rapporten over gebruikers en apparaten.

### Gebruiker gedefinieerde variabelen & dimensies (=)
De volgende configureerbare onderdelen van de tracking in GA zijn ook aanwezig in Matomo:
- Vrije variabele: statistieken over gebruikers per categorie
- Door gebruiker gedefinieerd: statistieken over gebruikers per categorie

### Gebruikersstroom ($)
Om gebruikersstroomen in Matomo te gebruiken is de [User flow plugin](https://plugins.matomo.org/UsersFlow?pk_vid=92fd1468b8251aee1588171135de8439) nodig.

Prijs:
* Tot 4 users, unlimited websites 79 EUR/year
* 5 tot 15 users, unlimited websites 149 EUR/year
* Ongelimiteerd users, unlimited websites 229 EUR/year

## Acquisitie
Beide tools beschikken over een vergelijkbare overzichtspagina om acquisitie informatie in te zien.

### Alle verkeer (~)
GA biedt een aantal opties om te zien waar gebruikers vandaan komen:
- Kanalen: statistieken over gebruikers per kanaal (direct, sociale media, websites etc.)
- Bron / medium: statistieken over gebruikers per bron of medium.
- Verwijzingen: statistieken over gebruikers per externe link.

Matomo biedt deze informatie aan verdeeld over 2 rapporten:
- Alle kanalen (vergelijkbaar met kanalen in GA). Dit rapport bevat ook de bron van het verkeer onderverdeeld o.b.v. kanalen.
- Het rapport websites bevat informatie over welke websites verwijzen naar pagina's.

Matomo kent het concept medium niet. GA definieert een medium als: [de algemene categorie van de bron, bijvoorbeeld organisch zoeken (organische), betaald zoeken op basis van kosten per klik (cpc) of webverwijzing (referral).](https://support.google.com/analytics/answer/6099206?hl=nl&ref_topic=6083659)

GA biedt ook de mogelijkheid dit te visualiseren in een boomdiagram. Matomo heeft hiervoor [een plugin](https://plugins.matomo.org/TreemapVisualization). Die een nieuw grafiektype toevoegt die in elk rapport in Matomo gebruikt kan worden.

### Zoekmachines ($)
GA biedt integratie met Google search:
- statistieken over hoe gebruikers de site vinden in google
   - Bestemmingspagina: statistieken over gebruikers per bestemmingspagina
   - Landen:  statistieken over gebruikers per land
   - Apparaat:  statistieken over gebruikers per apparaat type
   - Zoekopdrachten:  statistieken over gebruikers per zoekopdracht

Matomo biedt vergelijkbare functionaliteit met de betaalde [Search engine performance plugin](https://plugins.matomo.org/SearchEngineKeywordsPerformance?pk_vid=92fd1468b8251aee1588248233de8439). Uitbreiding hierop is dat deze plugin ook voor andere zoek platformen (Yahoo! of Bing) kan worden ingezet.

Prijs:
* Tot 4 users, unlimited websites 129 EUR/year
* 5 to 15 users, unlimited websites 249 EUR/year
* Ongelimiteerd users, unlimited websites 379 EUR/year

### Google Ads
GA biedt een scala aan verschillende rapporten om Google Ads prestaties inzichtelijk te maken. All rapporten zijn gericht op verschillende groeperingen / invalshoeken op dezelfde data.

De statistieken die getoond worden zijn de volgende:
* Klikken
* Kosten
* CPC
* Gebruikers
* Sessies
* Bouncepercentage
* Pagina's/sessie
* Conversiepercentage van e-commerce
* Transacties
* Opbrengst

Deze gegevens kunnen worden gegroepeerd op basis van:
- Account (campagne categorie/groep)
- Campagne
- Site link set
- Bodaanpassing
- Zoekwoord
- Zoekopdracht
- uur van de dag   
- Uiteindelijke URL
- Display targeting
- Videocampagne
- Shopping campagne

Matomo biedt minder invalshoeken, hoewel rapporten gegenereerd zouden kunnen worden met de custom reports plugin. De gratis AOM plugin (genoemd bij campagnes) biedt integratie met o.a. GoogleAds om dezelfde statistieken op te halen uit de Google Ads API. Het is niet geheel duidelijk welke groeperingen er wel en niet mogelijk zijn in Matomo omdat er geen beschikking is over deze data.

### Sociaal
De GA sociale media rapporten met betrekking tot:
- Netwerk verwijzingen: statistieken over gebruikers per verwijzing op sociale media per bron.
- Bestemmingspagina’s: statistieken over gebruikers per bestemmingspagina
- conversies: statistieken over conversies per sociale media

Zijn terug te vinden onder sociale netwerken in Matomo. Gebruikersstroom rapporten zoals ook beschikbaar in GA zijn in Matomo te gebruiken m.b.v. een betaalde plugin zoals eerder genoemd.

Matomo biedt geen mogelijkheid voor het volgen van sociale media plug-ins. Wel zou met behulp van [event of content tracking](https://matomo.org/docs/event-tracking/) vergelijkbare statistieken verzameld kunnen worden.

### Campagnes (+)
GA biedt de volgende functionaliteit aan onder campagnes:
- Alle campagnes: statistieken over gebruikers per campagnes
- Betaalde zoekwoorden: statistieken over gebruikers per zoekwoord
- Organische zoekwoorden: statistieken over gebruikers per zoekwoord
- Kostenanalyse: Lijkt niet gebruikt te worden.

Het eerste punt is in Matomo terug te vinden onder campagnes. Hierbij zijn ook uitgebreidere rapporten te vinden als de [Marketing Campaigns Reporting plugin](https://plugins.matomo.org/MarketingCampaignsReporting) is geïnstalleerd.

De rapporten m.b.t. zoekwoorden zijn in Matomo terug te vinden onder "zoekmachines & zoekwoorden".

Matomo biedt integratie voor het integreren van kosten van bijvoorbeeld Google AdWords. Dit is met behulp van de [gratis AOM plugin](https://plugins.matomo.org/AOM).

## Gedrag

### Content
Gedragsstroom is via de Gedragsteam plugin te gebruiken. (Zie kopje gebruikersstroom).

De volgende GA reports zijn terug te vinden in Matomo onder pages:
   – Alle pagina’s: Statistieken per pagina
   – Gedetailleerd inhoud rapport: Statistieken per pagina pad (folder)

De GA rapporten Bestemmingspagina’s, Uitstap pagina’s zijn terug te vinden in Matomo onder entry pages en exit pages respectievelijk.

### Snelheid (-)
Matomo biedt statistieken over de laadsnelheid van elke pagina.
GA biedt deze data op een meer gedetailleerd niveau aan. Zo wordt er onderscheid gemaakt tussen tijden voor:
- Domein opzoeken
- DOM weergave
- Server verbindingstijd

Daarnaast zijn de rapporten in GA uitgebreider, Matomo beschikt niet over de volgende twee rapporten:
- Snelheid Suggesties: Een rapport met de pagina's die het meest laadtijd winst zouden opleveren (o.b.v. pageviews en laadtijden).
- Gebruikers Timing: Een overzicht van laadtijden voor (door gebruiker gespecificeerde) categorieën.

### Zoeken op site
De volgende twee GA rapport zijn in Matomo terug te vinden onder site search:
- Zoektermen: Statistieken over wat gebruikers zoeken op de site
- Zoekpagina’s: Statistieken over zoekopdrachten per pagina

Tot slot biedt GA ook informatie over het gebruik van de zoekfunctie, in Matomo is deze informatie minder uitgebreid. Punten die ontbreken zijn bijvoorbeeld statistieken over:
- % uitstappunten zoekopdrachten
- % zoek verfijningen
- Tijd na zoekopdracht
Hoewel de data om deze statistieken uit te rekenen wel beschikbaar is. Zo kan bijvoorbeeld in het bezoekers overzicht het aantal zoekopdrachten op de site worden weergegeven.

### Gebeurtenissen (~)
GA heeft eenzelfde insteek voor het tracken van events als Matomo. Het is nodig deze events handmatig af te vuren op basis van Javascript events.

Voor bepaalde events zijn in Matomo standaard opties beschikbaar:
- Downloads: worden gevolgd op basis van de extensie van de URL.
- Outlinks: bij het verlaten van de site.
- Media analytics: tracking van veel gebruikte videospelers door middel van een betaalde plugin.
- Ads / HTML content: content tracking kan worden verwerkt in de pagina.

Wat betreft de rapporten. De data in Matomo is verdeeld over dezelfde categorieën die hierboven genoemd zijn (en de bijbehorende pagina's). De volgende rapporten zijn veelal onder events terug te vinden in Matomo:
- Overzicht: Dashboard met alle gebeurtenissen.
- Topgebeurtenissen: Statistieken over meest voorkomende gebeurtenissen.
- Pagina’s: Statistieken over gebeurtenissen per pagina.

Matomo lijkt niet te beschikken over het gebeurtenisproces rapport met funnels voor gebeurtenissen. 

#### Media analytics plugin ($)
De [media analytics plugin](https://www.media-analytics.net/) is een betaalde plugin van een derde partij. Deze plugin kan ingezet worden om de events m.b.t. media te tracken. Bijvoorbeeld het afspelen van embedded YouTube content. De plugin ondersteund de meest gebruikte plugins voor het plaatsen van media op websites.

Prijs:
* Tot 4 Users 149 EUR/year.
* 5 tot 15 Users 299 EUR/year.
* Ongelimiteerd users 449 EUR/year.

### Uitgever (-)
Koppeling met AdSense en AdExchange, lijkt niet gebruikt te worden bij de Radboud. Matomo biedt geen integratie met deze platformen.

### A/B testen ($)
GA heeft eerder contentexperimenten (A/B tests) aangeboden. Deze worden niet meer ondersteund in GA en zijn verplaatst naar Google Optimize. Matomo kan voorzien in een mogelijke de A/B test wens met [de A/B test plugin](https://plugins.matomo.org/AbTesting).

Prijs:
* Tot 4 users, unlimited websites 199 EUR/year
* 5 to 15 users, unlimited websites 399 EUR/year
* Ongelimiteerd users, unlimited websites 599 EUR/year

## Conversies

### Doelen (~)
Voor GA en Matomo komen de volgende rapporten overeen verdeeld over:
- Overzicht: Dashboard met statistieken over conversies van doelen
- Doel-URL’s: Statistieken over conversies per URL met een doel

Van de funnel gerelateerde doel-rapporten is het niet duidelijk of deze in Matomo mogelijk zijn:
- Omgekeerd doelpad: omgekeerde funnel vanaf de doelen
- Doelprocesstroom: funnels van verschillende doelen

Een equivalent voor [slimme doelen](https://support.google.com/analytics/answer/6153083?hl=nl) ontbreekt in Matomo.

#### Funnels ($)
Matomo kan funnels gebruiken met behulp van de [betaalde funnel plugin](https://plugins.matomo.org/funnels). Hoe deze plugin zich verhoud tot de opties die GA biedt is nog niet duidelijk.

Prijs:
* Tot 4 users, 179 EUR/year
* 5 to 15 users, 349 EUR/year
* Ongelimiteerd users, 529 EUR/year

### E-commerce (~)
De overzichten die GA aanbiedt m.b.t. e-commerce zijn:
- Productprestaties
- Verkoopprestaties
- Transacties
- Tijd tot aankoop
Matomo lijkt de eerste drie punten hiervan te ondersteunen.

### Multi-channel trechters (~)
GA biedt hiervoor:
- Overzicht: Visualisatie van conversies die van meerder kanalen komen.
- Ondersteunde conversies: Statistieken over indirecte conversies per kanaal
- Beste conversiepaden: Overzicht van paden die het beste converteren
- Vertraging: Overzicht van aantal conversies per aantal dagen tussen eerste interactie en conversie.
- Padlengte: Overzicht van aantal conversies per aantal interacties voor een conversie plaats vond
- Tool voor modelvergelijking: Statistieken om verschillende categorieën te vergelijken op basis van conversie modellen (eerste interactie, laatste interactie, etc.)

Matomo kan met behulp van de multi-channel conversion plugin een soortgelijk overzicht van conversies en attributie van conversies genereren. Hierbij lijken de conversiepaden, vertraging en padlengte niet te worden meegenomen.

# Opmerkingen
Een aantal opmerkingen en constateringen na het vergelijken van de features voor beide web analytics tools.

## Instellingen
Instellingen en configuratie opties zijn niet meegenomen in deze vergelijking. Matomo biedt bijvoorbeeld meer opties voor een privacy vriendelijke configuratie. 

## Aangepaste rapporten & metrics
Met behulp van de aangepaste rapporten plugin is het in Matomo mogelijk een hoop rapporten zoals in GA na te maken.

Als input voor deze aangepaste rapporten kunnen enkel bestaande metrics worden gebruikt, het is dus niet mogelijk calculaties en afgeleide op te nemen in deze rapporten. [Zie deze Github issue](https://github.com/matomo-org/matomo/issues/12390)

## Andere invalshoek van Google
Het is te verwachten dat GA een andere invalshoek geeft op de statistieken dan Matomo doet. Het zijn immers twee onafhankelijke producten. Dit maakt dat wanneer de features van GA vertaald worden naar Matomo dit niet terug te vinden is in een en dezelfde feature maar gedistribueerd kan zijn over meerdere rapporten.

## Gebruik
Wat deze vergelijking ook niet in overweging neemt zijn de verschillen in de mogelijkheden om de statistieken in andere vormen of in gedetailleerde rapporten op te vragen. Hier zitten ook grote verschillen tussen beide tools. Bijvoorbeeld het gebruik van een visit of e-commerce log in Matomo geeft een gedetailleerd beeld per gebruiker, dit is in GA niet terug te vinden.

## Marktplaats van dashboard / doelen / campagnes
GA beschikt over een [solutions galary](https://analytics.google.com/analytics/gallery/#landing/start/). In de Matomo marketplace zijn wel features en themes beschikbaar, maar geen kant en klare solutions.

## Trechters (funnels)
Over de toepassingen van trechters in GA en Matomo zijn op basis van deze vergelijking geen duidelijke uitspraken te doen.