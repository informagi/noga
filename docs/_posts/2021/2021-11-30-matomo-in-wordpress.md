---
layout: "post"
title: "Matomo draaien in WordPress"
author: "Gijs Hendriksen"
date: "2021-11-30 9:00"
excerpt: "Matomo gemakkelijk draaien in een bestaande WordPress website."
tags: NoGA Matomo setup opzetten WordPress
---

In [een van onze eerdere blogposts](/2020/11/23/matomo-opzetten.html) hebben we uitgelegd hoe je zelf een installatie van Matomo op kunt zetten. Voor veel gebruikers zal dit echter nog steeds te technisch zijn, of meer tijd, moeite kosten dan wat voor hun doeleinde nodig is. Een andere optie is om [Matomo's eigen Cloud Hosting](https://matomo.org/matomo-cloud/) te gebruiken, maar dan betaal je weer extra kosten voor hosting terwijl je waarschijnlijk ergens al een hostingpakket hebt draaien voor je webserver.

Gelukkig is er voor veel gebruikers een nog simpelere oplossing om Matomo zelf te draaien. Als je website gebruikmaakt van WordPress (zoals inmiddels al [40% van het internet](https://wordpress.org/40-percent-of-web/)) kun je de [Matomo Analytics for WordPress plugin](https://matomo.org/blog/2019/10/matomo-analytics-for-wordpress/) installeren. Deze plugin installeert Matomo Analytics in jouw WordPress website, waardoor er dus geen noodzaak meer is voor een aparte Matomo installatie. Bovendien kun je je overzichten en rapportages direct bekijken vanuit het administratiepanel van WordPress zelf. Al je data is dus op één plek te vinden!

In deze blogpost geven we een korte introductie over de WordPress plugin van Matomo, hoe hij te installeren is en hoe hij in gebruik werkt. Op deze manier wordt het voor een flink aantal gebruikers hopelijk nog makkelijker om hun analytics data in eigen handen te nemen.

## Installatie

Als je een eigen WordPress website draait is de kans groot dat je al eens een plugin hebt geïnstalleerd. Het installeren van de Matomo Analytics plugin gaat even eenvoudig, en is binnen een paar klikken gedaan:

1. In de administratie van je WordPress site, navigeer naar **Plugins > Nieuwe plugin**
2. In de zoekbalk, voer in: _"Matomo Analytics Ethical Stats"_
3. Klik op de **Installeer** knop bij de Matomo Analytics plugin
4. Nadat de plugin is geïnstalleerd, klik op de **Activeer** knop

Voor een uitgebreidere uitleg over het installeren van een WordPress plugin, zie ook [deze site](https://www.wpbeginner.com/beginners-guide/step-by-step-guide-to-install-a-wordpress-plugin-for-beginners/).

Als bovenstaande stappen zijn voltooid, is het installeren van Matomo gelukt! Er hoeven geen superusers aangemaakt of database-instellingen aangepast te worden. Matomo is compleet geïnstalleerd en draait meteen. Tijdens de installatie heeft de plugin zelfs een volledige Matomo installatie in de achtergrond opgezet, inclusief dashboard met rapportages en specifieke instellingen. Hoe we daar bij moeten komen zien we later in deze blogpost. Eerst moeten we echter nog wat instellingen aanpassen om te beginnen met het verzamelen van data.

## Configuratie

Om Matomo goed in te stellen voor je website zul je de configuratie nog aan moeten passen en, bovenal, tracking aan te zetten. Dit kun je doen in de instellingen van de Matomo plugin. Na de installatie is er in het administratiepanel een kopje **Matomo Analytics** verschenen. Hier kun je verschillende pagina's van Matomo bezoeken. Voor het aanpassen van de instellingen gaan we naar **Matomo Analytics > Settings**.

![Matomo configuratie in WordPress](/assets/img/wordpress_configuratie.png)

In de instellingen van de Matomo plugin vinden we de volgende tabbladen:

* **Tracking**, waar de JavaScript tracking code terug te vinden is. Je kunt ervoor kiezen om de tracking code zelf aan je pagina's toe te voegen, maar het makkelijkste is om te kiezen voor de optie _Default tracking_. Dit zorgt ervoor dat de plugin automatisch de tracking code toevoegt aan elke pagina. Bovendien verschijnen er dan een hoop opties die aangepast kunnen worden om aan te geven welke data wel en welke data niet verzameld moet worden. Aan de hand van de opties die je hier invult wordt de tracking code automatisch aangepast, waardoor je hier zelf niet mee aan de haal hoeft.
* **Access**, waar in te stellen is welk soort gebruiker van je website toegang heeft tot Matomo. Voor elke _rol_ (bijv. "redacteur" of "auteur") kun je aangeven of gebruikers met die rol _View_, _Write_ of _Admin_ toegang krijgen tot Matomo. Je hoeft dus geen nieuwe accounts aan te maken via Matomo; een account binnen WordPress kan automatisch inloggen op Matomo. Gebruikers met de rol "beheerder" krijgen trouwens automatisch _Super User_ toegang.
* **Privacy & GDPR**, waar informatie staat over hoe Matomo met privacy en de GDPR/AVG omgaat. Ook staan er enkele links naar instellingen van Matomo die met privacy te maken, zoals IP anonimisatie en het vragen van consent. Ook geven ze een [shortcode](https://www.wpbeginner.com/wp-tutorials/how-to-add-a-shortcode-in-wordpress/) om gebruikers een opt-out te bieden voor het tracken via Matomo.
* **Exclusions**, waar je aan kunt geven welke gebruikers, IP adressen of parameters niet getrackt moeten worden. Dit kan handig zijn om bijvoorbeeld administrators niet mee te tellen in de analytics van je website, om de focus puur op bezoekers te houden.
* **Geolocation**, waar je de optie krijgt om [MaxMind](https://www.maxmind.com/en/home) te gebruiken voor geolocation in plaats van de standaard gratis functionaliteit van Matomo.
* **Advanced**, waar instellingen te vinden zijn voor het aanpassen van IP adressen als Matomo achter een proxy draait (zie ook onze [vorige blogpost](/2020/11/23/matomo-opzetten.html#proxy)).
* **Matomo Admin**, waar je wordt doorverwezen naar het standaard administratiegedeelte van Matomo. Hier kun je ook een aantal standaard instellingen van Matomo aanpassen. Het administratiegedeelte is wel een stuk beperkter, omdat een aantal opties al uit handen worden genomen door de integratie met WordPress (bijvoorbeeld het instellen van gebruikers).

### Archiveren

In onze tweede blogpost over het opzetten van Matomo hebben we het gehad over [het opzetten van een automatische taak voor het genereren van rapporten](/2020/12/01/matomo-geavanceerd.html#archiveren-van-rapporten). Voor de WordPress plugin van Matomo is het niet nodig om dit in te stellen. Standaard maakt de plugin namelijk gebruik van WP Cron, wat een systeem binnen WordPress is om taken op vaste momenten of intervallen uit te voeren. Rapportages worden dus niet gegenereerd als ze geladen worden, maar alleen op de momenten dat WP Cron aangeeft dat dit moet gebeuren. Dit komt de laadsnelheid van de rapportages alleen maar ten goede.

Een nadeel van WP Cron kan echter zijn dat het de laadtijd van je website op momenten vertraagt. WP Cron wordt namelijk alleen uitgevoerd als iemand een pagina op je website laadt. Op het moment dat WP Cron dus veel operaties uit moet voeren, kan de laadtijd voor die persoon een stuk langer worden. Om dit te verhelpen is het mogelijk om WP Cron zo in te stellen dat het niets uitvoert op het moment dat een willekeurige gebruiker een pagina laadt. In plaats daarvan creëer je dan een geautomatiseerde taak die eens in de zoveel tijd expliciet WP Cron aanroept om alle geplande taken uit te voeren. Mocht je tegen performance problemen aanlopen die met WP Cron te maken hebben is het dan ook zeker aan te raden om dit te doen. Hoe je dit precies moet doen, vind je bijvoorbeeld op [deze pagina](https://kinsta.com/nl/kennisbank/uitschakelen-wp-cron/).


## Inzichten en rapportages

Als Matomo eenmaal geconfigureerd is en data heeft verzameld kun je deze data op twee manieren inzien:

1. Via het menu-item **Matomo Analytics > Summary** kun je een eenvoudig overzicht van de rapportages zien, direct vanuit WordPress:

   ![Matomo rapportage in WordPress admin](/assets/img/rapportages_wordpress_admin.png)

2. Aangezien de Matomo plugin achter de schermen een volledige Matomo installatie opzet, kunnen we ook gebruikmaken van het standaard dashboard van Matomo. Deze kun je bereiken door op het menu-item **Matomo Analytics > Reporting** te klikken.

   Als je in het bovenstaande overzicht vanuit WordPress bij een van de rapportages op de knop linksboven drukt om de rapportage in detail te bekijken, word je ook automatisch doorgestuurd naar de bijbehorende pagina in het dashboard van Matomo.


## Conclusie

Met de Matomo Analytics plugin voor WordPress is het installeren van Matomo nog gemakkelijker dan de andere versies. Hiervoor hoef je niets in te leveren op het gebied van functionaliteit: je kunt via het Matomo dashboard nog steeds alles inzien en instellen zoals je zelf wilt. Bovendien wordt het via de plugin instellingen een stuk gemakkelijker om de tracking aan te passen naar je eigen wensen. Matomo zorgt er automatisch voor dat de JavaScript tracking code wordt aangepast en op de juiste manier op elke pagina wordt ingeladen.

Wel is het belangrijk om te weten dat deze installatie vooral voor kleinere organisaties en website goed te gebruiken is. Bij grotere websites met veel verkeer (meer dan 50K bezoekers per maand) raadt Matomo aan om een aparte Matomo installatie te draaien, ofwel zelf gehost ofwel via Matomo Cloud. Maar juist voor de kleinere websites, waarvoor zo'n aparte installatie te kostbaar om aan te schaffen of te lastig in te stellen is, biedt Matomo Analytics met hun WordPress plugin een perfecte manier om de data van je gebruikers weer in eigen handen te nemen.
