---
---

# Web Analytics, Cookies en de Wet

## Introductie

Google Analytics werkt met het plaatsen van _analytic cookies_ en in bepaalde gevallen ook van _tracking cookies_:

+ [Uitleg van Google](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview).
+ Beschrijving van [Google Analytics cookies](https://www.cookielaw.org/google-analytics-eu-cookie-law/).

Een veel gestelde vraag is of het volgen van websurfers nu eigenlijk consent vereist van de bezoeker van de site.
Helaas leiden verschillende bronnen tot andere antwoorden, en het is ons niet 100% duidelijk of de Nederlandse situatie verschilt van die in andere Europese landen.

## DPA berichten

Elk Europees land heeft een eigen _data autoriteit_ (DPA), die advies kan geven over de juiste interpretatie van de wetgeving.
Die adviezen liggen alleen niet in een lijn: de UK is duidelijk veel strenger dan NL, bijvoorbeeld.

### ICO

De Britse DPA is heel duidelijk: geen Google Analytics zonder consent.

_"You must tell people if you set cookies, and clearly explain what the cookies do and why. You must also get the user’s consent. Consent must be actively and clearly given. 
There is an exception for cookies that are essential to provide an online service at someone’s request."_

Analytics is niet _essential_ en vereist dus consent.

Uit hun online Frequently Asked Questions ([.pdf document](https://ico.org.uk/media/for-organisations/guide-to-pecr/cookies-and-similar-technologies-2-4.pdf)):

Q: Do the rules still apply if the data is anonymous?

A: Yes. Although cookies that process personal data give rise to greater privacy and security risks than those that process anonymous data, PECR apply to all cookies. If your cookie data is not anonymous, note that you will also need to comply with the Data Protection Act and the GDPR. _(Continues with warnings about collecting personal data.)_

Meer achtergrond informatie van de ICO:

+ Relevante sectie in [Guidance on the use of cookies and similar technologies](https://ico.org.uk/for-organisations/guide-to-pecr/guidance-on-the-use-of-cookies-and-similar-technologies/how-do-we-comply-with-the-cookie-rules/#comply15);
+ Cookies deel uit de [Guide to PECR](https://ico.org.uk/for-organisations/guide-to-pecr/cookies-and-similar-technologies/).

### Autoriteit Persoonsgegevens (APG)

De Nederlandse autoriteit is (helaas) veel minder expliciet, en lijkt een uitzondering te maken voor Google Analytics, als de instelling maar "privacy friendly" is. 
Ze schreven zelfs een instructie [Handleiding privacy-vriendelijk instellen google analytics](https://autoriteitpersoonsgegevens.nl/sites/default/files/atoms/files/138._handleiding_privacyvriendelijk_instellen_google_analytics_aug_2018.pdf) (augustus 2018).

Na een recent oordeel van het Europees hof (oktober 2019) lijken ze iets te zijn opgeschoven, maar de APG blijft schimmig over het wel/niet toestaan van _analytic cookies_ zonder consent.
Duidelijk is dat [tracking cookies](https://autoriteitpersoonsgegevens.nl/nl/nieuws/ap-veel-websites-vragen-op-onjuiste-wijze-toestemming-voor-plaatsen-tracking-cookies) expliciete instemming vereisen van de website bezoeker.
De autoriteit heeft 175 organisaties aangeschreven om ze te waarschuwen dat ze zich niet aan de wet houden.

Dat Nederland zich anders lijkt op te stellen wordt ook zo omschreven in een juridisch blog over [het plaatsen van cookies](https://www.ictrecht.nl/blog/hof-van-justitie-voor-het-plaatsen-van-cookies-is-de-actieve-toestemming-van-de-internetgebruikers-vereist): 
_In Nederland geldt dat voor het gebruik van Google Analytics geen toestemming nodig is, mits de cookie privacyvriendelijk is ingesteld. In een handleiding van de Autoriteit Persoonsgegevens is te lezen op welke manier je de cookie privacyvriendelijk kunt instellen. Helaas geldt deze regel niet in alle EU-landen._

Het verschil in interpretatie van de Europese wetgeving lijkt hem te zitten in de uitzonderingen, waarbij de Nederlandse autoriteit kiest voor een interpretatie die toelaat informatie te verkrijgen over de kwaliteit of effectiviteit van de dienst, 
onder de extra voorwaarde dat dit geen of zeer beperkte privacy-impact heeft.

Ook een Italiaanse juridische adviesorganisatie wijst op een [verschil in uitzonderingen per regio](https://www.iubenda.com/en/help/5525-cookies-gdpr-requirements); ze noemen een uitzondering voor _statistical cookies managed directly by you (not third-parties), providing that the data is not used for profiling_ en _anonymized statistical third-party cookies (e.g. Google Analytics)_, maar, expliciet met een voetnoot dat _This exemption is may not be applicable for all regions and is therefore subject to specific local regulations_.
En, even verderop: _even where this exception to the consent requirement applies, you’ll still need to inform the user of your use of cookies via a cookie policy._

## Conclusie

Het lijkt voor een internationaal gerichte site niet verstandig om Google Analytics in te zetten zonder expliciet te vragen om consent.
In de UK is het zeker niet toegestaan, maar de Nederlandse situatie is voor ons minder duidelijk.

De APG stelt wel dat bezoekers hierover informatie moeten krijgen, bijvoorbeeld via het privacybeleid. 
Hier moet dan achtereenvolgens in staan dat de dienst:
+ Google Analytics-cookies gebruikt;  
+ een bewerkersovereenkomst met Google heeft gesloten;  
+ het laatste octet van het IP-adres heeft gemaskeerd;
+ 'gegevens delen' heeft uitgezet;  
+ geen gebruik maakt van andere Google-diensten in combinatie met de Google Analytics-cookies.

Overigens lijkt onze universiteit zich niet correct te houden aan deze beperkingen - de privacy informatie vermeldt dat we zowel Google Analytics als Google AdWords gebruiken:
_Wij delen op geen andere dan voor bovengenoemde redenen gegevens met Google en maken tevens geen gebruik van andere Google-diensten in combinatie met de Google Analytics-cookies, behalve voor het wederzijds uitwisselen van webstatistieken en campagnestatistieken met ons Google AdWords account, teneinde websitegebruik en conversiegebeurtenissen bij te houden._

## Zie ook

+ Een ouder maar recent ge-update artikel over [analytics en cookiewetgeving](https://www.vaneldijk.nl/artikelen/hoe-zit-het-nu-met-de-cookiewetgeving);
+ Volkskrant artikel over [tracking cookies bij gemeenten](https://www.volkskrant.nl/nieuws-achtergrond/enkele-tientallen-gemeenten-maken-gebruik-van-agressieve-online-volgmethoden~b4d87ba5/).
