---
layout: "post"
title: "Zelf matomo opzetten"
author: "Pepijn Boers"
date: "2020-11-23 15:00"
excerpt: "Beginners handleiding voor het zelf opzetten van matomo."
tags: NoGA matomo setup opzetten Docker
---

Matomo Analytics biedt privacy vriendelijke software voor het bijhouden van bezoekersaantallen en statistieken van uw website. Het grote voordeel is dat u met het gebruik van matomo alle data in eigen beheer kunt houden en zo niet afhankelijk bent van derden voor het beheren van ebruikersdata. Een veel voorkomend struikelpunt is echter, dat het zelf opzetten van zo een in-house systeem behoorlijk wat technische kennis kan vergen. In deze blog leer je hoe je zelf een basis versie van matomo kunt hosten. 

De makers van matomo zijn gebaat bij een zo eenvoudig mogelijke installatie voor hun gebruikers en bieden [hier](https://matomo.org/docs/installation/) een stappenplan. Voor gebruikers zonder enkele technische kennis biedt matomo een kant-en-klare versie via [matomo Cloud](https://matomo.org/matomo-cloud/). U betaalt dan een standaard bedrag per maand waarnaar hosting, onderhoud en backups voor u geregeld worden. 

De voornaamste moeilijkheden zitten hem in het regelen van een virtuele of dedicated server en het aanleggen van de juiste omgeving voor meerdere stukjes software. In deze blog lopen we door de basisstappen om de standaard matomo webserver te hosten. Om het u zo makkelijk mogelijk te maken hebben wij al een aantal stukken code voor u geschreven die te downloaden zijn vanaf [deze](https://github.com/PepijnBoers/matomo-compose) repository. 

## Een server
Voordat er naar matomo gekeken kan worden, dient u eerst toegang te hebben tot een server. Deze kunt u zelf aanschaffen of ergens huren, bijvoorbeeld via AWS, Azure of Google Cloud. Voor deze tutorial is het van belang dat u een `ssh` verbinding kunt maken met uw server (poort 22) en dat u de poorten voor `HTTP` (80) en `HTTPS` (443) open zet. Uitleg hierover is vrijwel altijd beschikbaar op pagina's van de desbetreffende hosting maatschappij. Hier vindt u een documentatie van de door ons gebruikte opties: [AWS](https://gitlab.science.ru.nl/mdessing/noga/-/tree/master/setup/aws.md) of [Bare Metal](https://gitlab.science.ru.nl/mdessing/noga/-/tree/master/setup/bare_metal.md) (engels).

## Matomo
Om makkelijk en onafhankelijk de juiste omgeving voor matomo te creëren, gebruiken we een combinatie van verschillende [Docker](https://www.strato.nl/server/docker-tutorial/) containers. Het bouwen en beheren van deze containers wordt gedaan door `docker-compose` - een tool waarmee een specifieke figuratie van virtuele omgevingen kan worden opgeroepen. De configuratie file bevat de instructies voor Docker om de juiste containers op te starten en met elkaar te laten samenwerken. Daarnaast houdt docker-compose ook een oogje in het zeil wat betreft 'gezondheid' van de containers, en worden corrupte container automatisch herstart. Het is dus van belang dat u **docker-compose** geinstalleerd heeft en dat u toegang heeft tot de command-line-interface van uw server ([installatie instructies]((https://docs.docker.com/compose/install/))). Om uw installatie te testen kunt u het volgende commando uitvoeren:

```bash
docker-compose --version

>> docker-compose version 1.27.4, build 40524192
```

### De database
Om de statistieken van uw website op te slaan is een database nodig, bijvoorbeeld MySQL of MariaDB. In deze tutorial gebruiken we een MySQL docker container voor het beheren van de data. In de gedownloade bestanden vindt u de `setup-db.sql` setup file voor de mysql database:


```mysql
-- CREATE DATABASE matomo;

CREATE USER 'matomo'@'%' IDENTIFIED WITH mysql_native_password BY '#your_secret_password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON matomo.* TO 'matomo'@'%';
GRANT FILE ON *.* TO 'matomo'@'%';
```


### De webserver
Om verbinding met matomo maken is een webserver nodig, hiervoor gebruiken we een aparte Nginx container. Deze regelt de communicatie tussen gebruiker en matomo. Het is ook mogelijk om matomo's ingebouwde webserver te gebruiken, echter biedt een aparte Nginx webserver in latere fases meer voordelen. Het is hier van belang dat Nginx naar de juiste website/host luistert, verander daarom de `server_name` in het `nginx/nginx/conf` bestand naar uw website/host:

```
server_name uw-matomo-website.nl www.uw-matomo-website.nl;
```

_Het wordt aangeraden om een beveiligde verbinding te creëren via het SSL protocol. Hierdoor beveiligt u alle communicatie tussen gebruiker en matomo. Een SSL certificaat kan aangevraagd worden via een Certificate Authority (CA). Een volgende blog gaat hier verder op in._

U kunt nu de matomo webserver starten met het docker-compose command:

```bash
docker-compose up
```

Bezoek nu de door u ingestelde host: `uw-matomo-website.nl`

### Matomo Installatie
Als alles goed is gegaan zou u nu de welkomstpagina van matomo moeten zien. U kunt bovenin de gewenste taal kiezen en op 'volgende' klikken. Hierna wordt er een systeem controle uitgevoerd en kunt u de database instellen. Als u niks aan wachtwoorden heeft veranderd vult u in de lege velden het volgende in:

* Inloggen: matomo
* Wachtwoord: #your_secret_password
* Naam database: matomo

Hierna kunt u de 'super user' account aanmaken en een eerste website waarvan u de statistieke wilt bijhouden toevoegen. Er verschijnt nu een `Javascript Tracking Code` die u op uw website kunt plaatsen en bij elk bezoek met de matomo server communiceert.

### Toestemming van bezoeker
De regelgeving omtrent het plaatsen van cookies kan soms wat lastig te volgen zijn en bevat een aantal uitzonderingen (zie onze blogs: [cookies](https://nogadata.nl/2020/03/09/cookies.html) en [cookies II](https://nogadata.nl/2020/03/09/borgesius-cookies.html)). Officieel is het in Nederland verplicht om bezoekers van uw website te informeren over het gebruik van cookies. Voordat er cookies mogen worden geplaatst dienen gebruikers eerst actief toestemming (consent) te geven. Er geldt echter een uitzondering voor analytics cookies die privacy-vriendelijk zijn.

De standaard configuratie van matomo anonimiseert de laatste 2 bytes van elk IP adres en respecteert 'Do Not Track' verzoeken. Als u daarnaast ook nog eens uw eigen server gebruikt, kunt u matomo op een privacy vriendelijke manier gebruiken. Deze redenatie gaat echter alleen op binnen de Nederlandse wet. Mocht u ook op internationale bezoekers rekenen is een consent formulier wel op zijn plaats. Matomo geeft hier instructies voor in de 'privacy' tab.

### Conclusie
Met bovenstaande instructies heeft u een begin kunnen maken met het opzetten van uw eigen matomo installatie. Om de installatieprocedure zo eenvoudig mogelijk te houden, betreft de huidige opzet een absolute basis opzet van matomo die op veel punten verbeterd kan worden. Een volgende blog zal daarom aandacht besteden aan het instellen van: SSL verbindingen, automatische archieven en geoptimaliseerde database mogelijkheden. 
