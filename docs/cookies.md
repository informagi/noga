---
---

# Web Analytics, Cookies en de Wet

## Introductie

Google Analytics werkt met het plaatsen van _analytics cookies_ en in bepaalde gevallen ook van _tracking cookies_:

+ [Uitleg van Google](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview);
+ Beschrijving van [Google Analytics cookies](https://www.cookielaw.org/google-analytics-eu-cookie-law/);
+ Uitleg over verschillende [soorten cookies (analytic, tracking)](https://en.wikipedia.org/wiki/HTTP_cookie#EU_cookie_directive).

Een veel gestelde vraag is of het volgen van websurfers nu eigenlijk consent vereist van de bezoeker van de site.
Helaas leiden verschillende bronnen tot andere antwoorden, en het is ons niet 100% duidelijk of de Nederlandse situatie verschilt van die in andere Europese landen.

## DPA berichten

Elk Europees land heeft een eigen _data protection authority_ (DPA), die advies kan geven over de juiste interpretatie van de wetgeving.
Die adviezen liggen alleen niet in een lijn: GB is duidelijk veel strenger dan NL, bijvoorbeeld.

### ICO

De Britse DPA (de _UK Information Commissioner’s Office_, ICO) is heel duidelijk: geen Google Analytics zonder consent.

_"You must tell people if you set cookies, and clearly explain what the cookies do and why. You must also get the user’s consent. Consent must be actively and clearly given. 
There is an exception for cookies that are essential to provide an online service at someone’s request."_

Analytics is niet _essential_ en vereist dus consent.

Uit hun online Frequently Asked Questions ([.pdf document](https://ico.org.uk/media/for-organisations/guide-to-pecr/cookies-and-similar-technologies-2-4.pdf)):

Q: Do the rules still apply if the data is anonymous?

A: Yes. Although cookies that process personal data give rise to greater privacy and security risks than those that process anonymous data, PECR apply to all cookies. If your cookie data is not anonymous, note that you will also need to comply with the Data Protection Act and the GDPR. _(Continues with warnings about collecting personal data.)_

Meer achtergrond informatie van de ICO:

+ Relevante sectie in [Guidance on the use of cookies and similar technologies](https://ico.org.uk/for-organisations/guide-to-pecr/guidance-on-the-use-of-cookies-and-similar-technologies/how-do-we-comply-with-the-cookie-rules/#comply15);
+ Cookies deel uit de [Guide to PECR](https://ico.org.uk/for-organisations/guide-to-pecr/cookies-and-similar-technologies/).

### Autoriteit Persoonsgegevens (AP)

De Nederlandse DPA, de Autoriteit Persoonsgegevens (AP), is veel minder expliciet en lijkt in de 2019 gepubliceerde 
[normuitleg](https://autoriteitpersoonsgegevens.nl/sites/default/files/atoms/files/normuitleg_ap_cookiewalls.pdf)
bewust een uitzondering te maken voor het gebruik van cookies voor web analyse. De AP schreef daarvoor ook al een instructie 
[Handleiding privacy-vriendelijk instellen google analytics](https://autoriteitpersoonsgegevens.nl/sites/default/files/atoms/files/138._handleiding_privacyvriendelijk_instellen_google_analytics_aug_2018.pdf) (augustus 2018).
Ze staat dus Google Analytics toe, onder voorwaarde dat de instelling van de analytics software "privacy friendly" is.

Na een recent oordeel van het Europees hof (oktober 2019) lijkt de autoriteit wel iets te zijn opgeschoven als het om _tracking cookies_ gaat; 
de AP heeft recent 175 organisaties aangeschreven om ze te waarschuwen dat ze zich niet aan de wet houden als ze geen
[expliciete instemming vragen](https://autoriteitpersoonsgegevens.nl/nl/nieuws/ap-veel-websites-vragen-op-onjuiste-wijze-toestemming-voor-plaatsen-tracking-cookies)
aan de website bezoeker voor het plaatsen van tracking cookies. De AP laat zich daarentegen niet expliciet uit over het wel/niet toestaan van _analytics cookies_ 
zonder consent.

Dat Nederland zich anders lijkt op te stellen wordt ook zo omschreven in een juridisch blog over [het plaatsen van cookies](https://www.ictrecht.nl/blog/hof-van-justitie-voor-het-plaatsen-van-cookies-is-de-actieve-toestemming-van-de-internetgebruikers-vereist): 
_In Nederland geldt dat voor het gebruik van Google Analytics geen toestemming nodig is, mits de cookie privacyvriendelijk is ingesteld. In een handleiding van de Autoriteit Persoonsgegevens is te lezen op welke manier je de cookie privacyvriendelijk kunt instellen. Helaas geldt deze regel niet in alle EU-landen._
Een ouder maar recent ge-update artikel over [analytics en cookiewetgeving](https://www.vaneldijk.nl/artikelen/hoe-zit-het-nu-met-de-cookiewetgeving) komt tot een vergelijkbare conclusie dat Google Analytics in Nederland onder voorwaarden wordt toegestaan.

Het verschil in interpretatie van de Europese wetgeving lijkt hem te zitten in de uitzonderingen, waarbij de Nederlandse autoriteit kiest voor een interpretatie die toelaat informatie te verkrijgen over de kwaliteit of effectiviteit van de dienst, 
onder de extra voorwaarde dat dit "geen of zeer beperkte" privacy-impact heeft.

Ook een Italiaanse juridische adviesorganisatie wijst op dit [verschil in uitzonderingen per regio](https://www.iubenda.com/en/help/5525-cookies-gdpr-requirements); de uitzondering voor _statistical cookies managed directly by you (not third-parties), providing that the data is not used for profiling_ en _anonymized statistical third-party cookies (e.g. Google Analytics)_, maar, expliciet met een voetnoot dat _This exemption may not be applicable for all regions and is therefore subject to specific local regulations_.
En, even verderop: _even where this exception to the consent requirement applies, you’ll still need to inform the user of your use of cookies via a cookie policy._

## Tracking zonder cookies

Het volgen van gebruikers online kan ook door andere technieken in te zetten dan het plaatsen van cookies.
De consumentenbond schreef bijvoorbeeld een toegankelijk artikel over 
[browser fingerprinting](https://www.consumentenbond.nl/internet-privacy/browser-fingerprinting),
en je zou ook kunnen proberen om de cookie te vervangen door data op te slaan in HTML5 local storage. Het inzetten van zogenaamde _similar technologies_ 
wordt echter expliciet genoemd in de wetgeving, en de aanwijzingen van de ICO zijn dan ook wederom uitermate duidelijk: 
_If you use device fingerprinting for analytics instead of or alongside cookies, you should note that doing so is not exempt from the consent requirements either_ (uit de [guidance](https://ico.org.uk/for-organisations/guide-to-pecr/guidance-on-the-use-of-cookies-and-similar-technologies/how-do-we-comply-with-the-cookie-rules/#comply15)).

Enigszins verrassend stelt een andere [post op de juridische ICTrecht blog](https://www.ictrecht.nl/blog/device-fingerprinting-en-de-cookieregels) dat 
_voor device fingerprinting voor trackingdoeleinden en analytische inzichten toestemming nodig is_ volgens de Nederlandse regelgeving.
De minister heeft in [antwoord op kamervragen](https://www.itenrecht.nl/artikelen/minister-cookiewet-ook-van-toepassing-op-device-fingerprinting) 
verklaard dat _device fingerprinting onder hetzelfde regime valt als cookies_; je zou dan alleen ook kunnen redeneren dat het voor analytische doeleinden 
in die interpretatie eveneens onder de uitzonderingen zou moeten vallen.

## Conclusie

Het lijkt voor een internationaal gerichte site niet verstandig om Google Analytics in te zetten zonder expliciet te vragen om consent.
In de Nederlandse situatie lijkt het (oogluikend?) wel toegestaan, maar de autoriteit in GB denkt er zeker anders over.
Meer onderzoek naar de regelgeving is nodig om in kaart te brengen hoe de verschillende regios zich opstellen.

De AP stelt in haar instructies voor gebruik Google Analytics helder dat bezoekers informatie moeten krijgen over deze analyse, bijvoorbeeld via het privacybeleid. 
Hier moet dan achtereenvolgens in staan dat de dienst:
+ Google Analytics-cookies gebruikt;  
+ een bewerkersovereenkomst met Google heeft gesloten;  
+ het laatste octet van het IP-adres heeft gemaskeerd;
+ 'gegevens delen' heeft uitgezet;  
+ geen gebruik maakt van andere Google-diensten in combinatie met de Google Analytics-cookies.

Overigens lijkt de Radboud Universiteit (waar project NoGA wordt uitgevoerd) zich niet correct te houden aan de instructie 
van de AP. Het onderdeel [Privacy & Cookies](https://www.ru.nl/over-ons/contact/vragen/privacy-cookiestatement/) in de privacy-verklaring vermeldt 
dat we zowel Google Analytics als Google AdWords gebruiken: _Wij delen op geen andere dan voor bovengenoemde redenen gegevens met Google en maken tevens geen gebruik van andere Google-diensten in combinatie met de Google Analytics-cookies, behalve voor het wederzijds uitwisselen van webstatistieken en campagnestatistieken met ons Google AdWords account, teneinde websitegebruik en conversiegebeurtenissen bij te houden._
De universiteit voegt daaraan toe dat _het op deze wijze uitwisselen van meetgegevens geen tot zeer beperkte invloed op uw privacy_ heeft, dezelfde
positie als de Nederlandse AP inneemt om af te wijken van de Britse. 

## Tot slot

De publieke opinie richt zich steeds meer tegen de _mass surveillance_ en het daarop gebouwde _surveillance capitalism_.
Tegelijkertijd begrijpen instituten en bedrijven vaak helemaal niet dat ze mass surveillance faciliteren - zo rapporteerde de Volkskrant begin 2020
dat veel gemeenten tracking cookies plaatsen 
([artikel](https://www.volkskrant.nl/nieuws-achtergrond/enkele-tientallen-gemeenten-maken-gebruik-van-agressieve-online-volgmethoden~b4d87ba5/)), 
maar wordt uit interviews duidelijk dat dit tracken niet altijd een bewuste keuze is. Soms ligt het in gebrek aan kennis van gebruikte technologie,
soms aan het onkundig opereren van toeleveranciers.

Als de Nederlandse autoriteit Google Analytics een uitzonderingspositie geeft, komt die interpretatie van de wet niet tegemoed aan de publieke wens
online vrij te kunnen bewegen. Je zou zelfs kunnen zeggen dat de AP het de facto monopolie van Google op web analytics faciliteert. Wat dat betreft
spreekt de stellingname van de ICO ons veel meer aan: als je gebruik van online services niet zelf in kaart brengt, dan moet je de bezoeker vragen
om consent om zijn of haar informatie te delen met een derde partij. Zo ontstaat er tenminste een incentive om de web analyse zelf te regelen,
en bezoekersdata niet door te schuiven naar derden.
