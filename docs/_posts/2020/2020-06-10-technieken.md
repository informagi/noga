---
layout: "post"
title: "Web analytics technieken"
author: "Marnix Dessing"
date: "2020-06-10 17:00"
excerpt: "Web analyse technieken."
tags: NoGA "Web analytics"
---

# Web Analytics technieken
Een belangrijk deel van web analytics is het verzamelen van gebruiks data op de website. Er bestaan hiervoor verschillend technieken, die werken vanaf verschillende invalshoeken en hierdoor verschillende voor en nadelen hebben.    

In [1] en [3] worden vier schillende technieken om click stream data te verzamelen beschreven. 
* Web logs
* Web beacons
* JavaScript tags
* Packet sniffing

## Web logs
Web logs, vooral access logs, kunnen gebruikt worden om website statistieken per webserver te verzamelen[1, 2, 3].

| Voordelen                              | Nadelen                                        |
|:---------------------------------------|:-----------------------------------------------|
| Data eigendom (transporteerbaar)       | Incompleet beeld van de data (bijv. geen uitgaande links) |  
| Veel volwassen en gratis tools beschikbaar (bijv. de ELK stack) | Bezoeker / gebruiker identificatie is lastig te realiseren |  
| Alle verkeer naar de website wordt afgevangen (ook browsers zonder JS of content blocking) | Alle requests naar de website (inclusief assets) |  
| De data bron is makkelijk toegankelijk | Caching kan de integriteit van data aantasten   |  


## Web beacons (tracking pixel)
Een web beacon heeft vaak de vorm van een 1x1 transparante pixel die wordt gelade op een webpagina of in een email. Het laden van een dit plaatje geeft de hosting partij van de pixel informatie (op basis van bijv. een access log). Maar geavanceerder gebruik incorporeert vaak URL parameters in de html src van de pixel om zo extra informatie door te sturen. Bijvoorbeeld een username of de pagina titel. De techniek wordt veel gebruikt bij ad providers.[1, 3]

| Voordelen                              | Nadelen                                              |
|:---------------------------------------|:-----------------------------------------------------|
| Lage complexiteit                      | Blocking van pixels (door browser) |  
| Data verzamelen / sturen via URL parameters | Standaard geblokeerd in veel email clients           |  
| Niet domein gebonden (bijv. door cookies)   | Data verzamelen mogelijk, maar minder geavanceerd dan in een JS tracker |  
|                                        | Blocking van third-party cookies (door browser)  |  


## JavaScript tags
JavaScript tags worden uitgevoerd binnen de browser en sturen gebruiks statistieken naar het data verzamel endpoint (bijv. Matomo of Google Analytics). De functionaliteit is niet gelimiteerd tot een enkel request maar kan worden uitgebreid tot meer events (bijv. producten in of uit de winkelwagen) of reguliere intervallen[1, 2, 3]. Dit is de techniek de meeste web analytics tools gebruiken, bijvoorbeeld: [Google Analytics](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview), [Matomo](https://developer.matomo.org/guides/tracking-javascript-guide), [Adobe Analytics](https://docs.adobe.com/content/help/en/analytics/implementation/js/overview.html) [Open web analytics](https://github.com/Open-Web-Analytics/Open-Web-Analytics/wiki/Tracker).

| Voordelen                                                     | Nadelen                                               |
|:--------------------------------------------------------------|:------------------------------------------------------|
| Eenvoudig te implementeren                                    | JavaScript moet uitgevoerd worden in de browser       |
| Geen toegang tot logs nodig                                   | Site taxonomie is altijd duidelijk uit de metadata    |
| Caching is geen probleem omdat de call vanuit JS komt         | Server-side data is onzichtbaar (bijv. sessie data)   |
| Controle over de data die verzameld wordt                     | File downloads worden vaak niet geregistreerd         |
| Minder afhankelijk van technical website staff (Enkel een script) | Javascript kan impact hebben op de performance van de site |
| Innovatie vind vooral plaats binnen deze techniek             |                                                       |
| Tracking over meedere domeinen                                |                                                       |


## Packet sniffing
Packet sniffing is het server-side inspecteren van elk netwerk paket. Zo kunnen verschillende statistieken gerelateerd aan web analytics worden bijgehouden.[1, 3]

| Voordelen                         | Nadelen                               |
|:----------------------------------|:--------------------------------------|
| Site wordt niet aangepast         | Extra laag hardware en software       |
| Enkel 1st party cookies nodig     | Privacy & versleuteling               |
| Alle data kan worden geïnspecteerd| Caching blijft een probleem vormen    |
|                                   | Duur (apparatuur en resources)        |


## Belangrijke overwegingen
Naast tracking mechanismes die worden gebruikt in de web analytics tools, moeten karakteristieken van een implementatie ook in overweging worden genomen, bijvoorbeeld kosten, belang van de gebruiker etc.

De volgende punten m.b.t. web analytics zijn belangrijk volgens[1]:
* Geen, first-party of third-party cookies
    * Bepaalde browsers blokeren standaard third-party cookies.
    * In de EU is het nodig voor First-party cookies een cookie notice te geven.
* Data ownership - wie is eigenaar van de data?
    * Voor het volledig beschikken over de data bij Google Analytics, [is een 360 abbonoment nodig](https://marketingplatform.google.com/intl/nl/about/analytics-360/compare/).
    * Als alle data analytics en verzameling in eigen beheer gebeurt ben je 100% eigenaar van de data.
* Tijd op de laatste pagina.
    * Wanneer de site verlaten wordt, hoe weeten we dan hoe lang de gebruiker op de laatste pagina heeft doorgebracht? Bijv. als de browser gesloten wordt of een exit signaal niet meer verstuurd kon worden. 
* Er bestaat geen perfect tracking mechanisme.
    * Alle technieken zullen soms gebruikers missen of kapot gaan.
* Gebruiker is belangrijk.
    * Het is belangrijk de gebruiker eerst te voorzien van de pagina voor het verzamelen van data kan beginnen.
* Kosten.
    * Sommige tracking technieken en oplossingen zijn duurder dan andere.

## References
[1] Kaushik, Avinash. Web analytics: an hour a day. John Wiley & Sons, 2007.<br/>
[2] Booth, Danielle, and Bernard J. Jansen. "A review of methodologies for analyzing websites." Web technologies: Concepts, methodologies, tools, and applications. IGI Global, 2010. 145-166.
[3] Waisberg, Daniel, and Avinash Kaushik. "Web Analytics 2.0: empowering customer centricity." The original Search Engine Marketing Journal 2.1 (2009): 5-11.

