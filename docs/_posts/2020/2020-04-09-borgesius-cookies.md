---
layout: "post"
title: "Cookies (II)"
author: "Frederik Zuiderveen Borgesius"
date: "2020-03-09 12:00"
excerpt: "Gastblog van Prof. Frederik Borgesius Zuiderveen over toestemming voor analytics- en andere cookies."
tags: NoGA "Web analytics"
---

[Prof. Frederik Zuiderveen Borgesius](https://twitter.com/fborgesius) 
heeft voor ons een gastblog geschreven. Prof. Zuiderveen Borgesius is
hoogleraar ICT en recht bij [iCIS](https://www.ru.nl/icis/),
het Institute for Computing and Information Sciences (iCIS), en
verbonden aan [iHub](https://www.ru.nl/ihub/), de Interdisciplinary
Hub for Privacy, Security and Data Governance.

# De wet en toestemming voor analytics- en andere cookies (deel II)

Een veel gestelde vraag is of website-houders toestemming moeten vragen
voordat ze websurfers volgen, met cookies bijvoorbeeld.

Het korte antwoord is: **ja, voor het volgen van websurfers met tracking
cookies of vergelijkbare technologie is hun voorafgaande toestemming
vereist.**

Volgens de Europese e-Privacyrichtlijn (aangepast in 2009) mogen, kort
gezegd, cookies alleen worden geplaatst nadat de websurfer zijn of haar
geïnformeerde toestemming heeft gegeven, tenzij die cookies noodzakelijk
zijn voor communicatie of om een aangevraagde dienst te leveren. Een
website moet ook toestemming vragen aan websurfers, als derden (zoals
advertentienetwerken of social media-bedrijven) via de website cookies
plaatsen op de computers van websurfers.

Er zijn twee uitzonderingen op deze toestemmingsregel. Ten eerste hoeft
een website geen toestemming te vragen als een cookie wordt geplaatst
met als enige doel het verzenden van communicatie. Als een cookie
bijvoorbeeld nodig is voor de inlogprocedure van een online bank, hoeft
geen toestemming gevraagd te worden. Ten tweede hoeft geen toestemming
gevraagd te worden als een cookie noodzakelijk is om een door de
websurfer gevraagde dienst te leveren. Voor cookies die worden gebruikt
voor bijvoorbeeld een virtueel winkelwagentje hoeft dus geen toestemming
verkregen te worden. Er hoeft ook geen toestemming gevraagd te worden
voor een cookie dat wordt geplaatst als een websurfer zijn of haar
taalvoorkeuren voor een website instelt.

Elke EU lidstaat moet de e-Privacyrichtlijn implementeren (omzetten) in
een nationale wet. In Nederland is de cookie-regel geïmplementeerd in
[artikel 11.7a van de Telecommunicatiewet][telecomwet].

Toestemming in de e-Privacyrichtlijn en in de Telecommunicatiewet moet
uitgelegd worden als toestemming in de Algemene Verordening
Gegevensbescherming (AVG, of GDPR). De eisen voor geldige toestemming
zijn streng.

Voor de leesbaarheid spreken we hier van cookies, maar artikel 11.7a van
de Telecommunicatiewet is van toepassing op veel meer technologieën. De
regel is namelijk van toepassing zo gauw een partij informatie (zoals
een cookie) op het apparaat van een gebruiker plaatst, of informatie
leest uit het apparaat van een gebruiker. De regel is dus ook van
toepassing op bijvoorbeeld flash cookies (local shared objects) en veel
vormen van device fingerprinting. Ook is de regel bijvoorbeeld van
toepassing [als een app de contactenlijst op iemands telefoon
uitleest][APWhatsApp].

***Analytics cookies en toestemming: de uitzondering in de Nederlandse
wet***

Is toestemming van de websurfer ook vereist als een website (of een
partner) analytics cookies plaatst of uitleest?

Analytics cookies vallen niet onder de twee uitzonderingen die de
e-Privacyrichtlijn noemt. Maar de Nederlandse wet bevat een extra
uitzondering voor, kort gezegd, privacy-vriendelijke analytics cookies.

In 2015 is namelijk de volgende zin toegevoegd aan de
Telecommunicatiewet. Er is geen toestemming nodig voor het plaatsen of
uitlezen van een cookie, als dat plaatsen of uitlezen gebeurt _-- mits
dit geen of geringe gevolgen heeft voor de persoonlijke levenssfeer van
de betrokken abonnee of gebruiker -- om informatie te verkrijgen over de
kwaliteit of effectiviteit van een geleverde dienst van de
informatiemaatschappij._

Die zin kan worden samengevat als: Voor analytics cookies hoeft geen
toestemming gevraagd te worden, als die analytics cookies
privacy-vriendelijk zijn.

## Vallen Google Analytics cookies onder die uitzondering?

Alleen onder bepaalde omstandigheden vallen Google Analytics-cookies
onder de uitzondering voor privacy-vriendelijke analytics cookies. De
websitehouder moet Google Analytics namelijk privacyvriendelijk
instellen, en een bewerkersovereenkomst met Google sluiten. De
Autoriteit Persoonsgegevens heeft een handleiding gepubliceerd voor het
[privacy-vriendelijk instellen van Google Analytics][APGA].

De Autoriteit Persoonsgegevens stelt in haar instructies voor gebruik
Google Analytics dat websites hun bezoekers moeten inlichten over het
gebruik van analytics cookies, bijvoorbeeld in hun privacyverklaring. De
website moet in elk geval vertellen dat deze:

+ Google Analytics-cookies gebruikt;
+ een bewerkersovereenkomst met Google heeft gesloten;
+ het laatste octet van het IP-adres heeft gemaskeerd;
+ 'gegevens delen' heeft uitgezet;
+ geen gebruik maakt van andere Google-diensten in combinatie met de
Google Analytics-cookies.

Een alternatief voor Google Analytics is [Matomo]( https://matomo.org)
(voorheen: Piwik). Als u, kort gezegd, Matomo via uw eigen server
gebruikt, kunt u Matomo op een privacy-vriendelijke manier gebruiken.

Zoals gezegd, heeft alleen Nederland een uitzondering voor
privacy-vriendelijke analytics cookies. Als u een website heeft die zich
richt op bezoekers uit andere EU lidstaten, is het dus beter om
toestemming te vragen als u privacy-vriendelijke analytics cookies
plaatst. Het lijkt echter niet waarschijnlijk dat een
privacytoezichthouders uit een andere EU lidstaat op zou treden tegen
een Nederlandse website om het enkele feit dat die site
privacy-vriendelijke analytics cookies plaatst.

De Europese Commissie en het Europees Parlement vinden de uitzondering
voor privacy-vriendelijke analytics cookies een goed idee. Er wordt in
Brussel gesproken over een e-Privacyverordening, die de
e-Privacyrichtlijn zou moeten vervangen. Het voorstel voor die opvolger
bevat ook een uitzondering voor internetgebruikers; daarmee neemt de EU
dus de Nederlandse uitzondering over. Het is echter onduidelijk wanneer
die e-Privacyverordening wordt aangenomen.

## Radboud Universiteit

Overigens lijkt de Radboud Universiteit (waar project NoGA wordt
uitgevoerd) zich niet te houden aan de cookie-regels. Zelfs voordat een
websitebezoeker klikt op _cookies toestaan_ bij een bezoek aan
[www.ru.nl](https://www.ru.nl) plaatst Radboud al meerdere cookies,
waaronder tracking cookies voor advertenties, die niet onder een
uitzondering vallen.

## Meer lezen?

De Artikel 29 Werkgroep, een samenwerkingsverband van de nationale
Europese privacy-toezichthouders, heeft richtlijnen gepubliceerd over de
cookie-regels in de ePrivacyrichtlijn:

+ Article 29 Working Party 2013, [Working Document 02/2013 providing
guidance on obtaining consent for cookies][Art29WP209] (WP 208), 2 October 2013.
+ Article 29 Working Party 2013, [Opinion 9/2014 on the application of
Directive 2002/58/EC to device fingerprinting][Art29WP224] (WP224), 25 November 2014.

De Autoriteit Persoonsgegevens geeft ook achtergrond-informatie [over
de cookie-regels][cookiesAP].

[APWhatsApp]:  https://autoriteitpersoonsgegevens.nl/nl/nieuws/overtredingen-whatsapp-deels-beëindigd-na-onderzoek-cbp-en-canadese-privacytoezichthouder "Artikel over overtredingen door WhatsApp"
[APGA]:        https://autoriteitpersoonsgegevens.nl/sites/default/files/atoms/files/138._handleiding_privacyvriendelijk_instellen_google_analytics_aug_2018.pdf "Handleiding AP voor instellen GA"
[telecomwet]:  https://wetten.overheid.nl/BWBR0009950/2020-03-01/#Hoofdstuk11_Paragraaf11.1_Artikel11.7a "Artikel 11.7a v/d telecomwet"
[cookiesAP]:   https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/internet-telefoon-tv-en-post/cookies                        "AP over cookies"
[Art29WP209]:  https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2013/wp208\_en.pdf                "Article 29 WP 2013 WP209"
[Art29WP224]:  https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp224\_en.pdf                "Article 29 WP 2013 WP224"
