---
layout: "post"
title: "Zelf matomo opzetten"
author: "Pepijn Boers"
date: "2020-11-23 15:00"
excerpt: "Beginners handleiding voor het zelf opzetten van matomo."
tags: NoGA matomo setup opzetten Docker SSL
---

Matomo Analytics biedt privacy vriendelijke (opensource) software voor het bijhouden van bezoekersstatistieken van online webpagina's. Het grote voordeel is dat u met het gebruik van Matomo al uw data in eigen beheer kunt houden en zo niet afhankelijk bent van derden voor het bijhouden van uw gebruikersdata. Een veel voorkomend struikelpunt is echter, dat het zelf opzetten van een in-house systeem behoorlijk wat technische kennis kan vergen. In deze blog leer je hoe je zelf een basis versie van Matomo kunt opzetten met enkel basale kennis van de command-line-interface. 

De makers van matomo zijn gebaat bij het leveren van een zo eenvoudig mogelijke installatie voor hun gebruikers en bieden [hier](https://matomo.org/docs/installation/) een stappenplan. Voor gebruikers zonder enkele technische kennis biedt Matomo ook een kant-en-klare versie via [matomo Cloud](https://matomo.org/matomo-cloud/). U betaalt dan een standaard bedrag per maand waarnaar hosting, onderhoud en back-ups voor u geregeld worden. 

In deze blog lopen we door de basisstappen om de standaard matomo webserver te hosten. De voornaamste moeilijkheden zitten hem in het regelen van een virtuele of dedicated server en het aanleggen van de juiste omgeving om meerdere stukjes software samen te laten werken. Om het u zo makkelijk mogelijk te maken hebben wij al een aantal stukken code voor u geschreven die [hier](https://github.com/PepijnBoers/matomo-compose) te downloaden zijn.

## Een server
Voordat er naar Matomo gekeken kan worden, dient u eerst toegang te hebben tot een server. Deze kunt u zelf aanschaffen of ergens huren, bijvoorbeeld via AWS, Azure of Google Cloud. Voor deze tutorial is het van belang dat u een `ssh` verbinding kunt maken met uw server (poort 22) en dat u de poorten voor `HTTP` (80) en `HTTPS` (443) open zet. Uitleg hierover is vrijwel altijd beschikbaar op pagina's van de desbetreffende hosting maatschappij. Hier vindt u een documentatie van de door ons gebruikte opties: [AWS](https://gitlab.science.ru.nl/mdessing/noga/-/tree/master/setup/aws.md) of [Bare Metal](https://gitlab.science.ru.nl/mdessing/noga/-/tree/master/setup/bare_metal.md) (engels).

## Matomo
Om makkelijk en onafhankelijk de juiste omgeving voor Matomo te creëren, gebruiken we een combinatie van verschillende [Docker](https://www.strato.nl/server/docker-tutorial/) containers (software pakketten). Het bouwen en beheren van deze containers wordt gedaan door `docker-compose` - een tool waarmee een specifieke figuratie van virtuele omgevingen kan worden opgeroepen. De configuratie file bevat de instructies voor Docker om de juiste containers op te starten en met elkaar te laten samenwerken. Daarnaast houdt docker-compose ook een oogje in het zeil wat betreft 'gezondheid' van de containers, en worden corrupte container automatisch herstart. Het is dus van belang dat u **docker-compose** geïnstalleerd heeft en dat u toegang heeft tot de command-line-interface van uw server ([installatie instructies]((https://docs.docker.com/compose/install/))). Om uw installatie te testen kunt u het volgende commando uitvoeren:

```bash
docker-compose --version

>> docker-compose version 1.27.4, build 40524192
```

### De database
Om de statistieken van uw website op te slaan is een database nodig, bijvoorbeeld MySQL of MariaDB. In deze tutorial gebruiken we een MySQL docker container voor het beheren van de data. In de gedownloade bestanden vindt u de `setup-db.sql` setup file voor de database. Het is verstandig om een eigen wachtwoord te kiezen. Dit doet u door '#your_secret_password' te vervangen door uw eigen database wachtwoord.

_Let op: in deze tutorial reeks wordt ook gebruik gemaakt van een MySql admin wachtwoord (default='your_password'). Het is verstandig om deze ook te veranderen, kijk daarvoor naar de volgende files: `docker-compose.yml`, `conf/infile/in-file.cnf` en de twee database back-up scripts in `conf/backups`._

```mysql
-- CREATE DATABASE matomo;

CREATE USER 'matomo'@'%' IDENTIFIED WITH mysql_native_password BY '#your_secret_password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON matomo.* TO 'matomo'@'%';
GRANT FILE ON *.* TO 'matomo'@'%';
```

### De webserver
Het wordt aangeraden om een beveiligde verbinding (SSL) te creëren tussen Matomo en de bezoekers van uw website. Zo'n beveiligde verbinding draagt bij aan de privacy van de bezoeker doordat de data versleuteld wordt verstuurd. Voor het aanvragen van een beveiligde verbinding dient u in het bezit te zijn van een eigen domein. Mocht u niet in het bezit zijn van een eigen domein of geeft u de voorkeur aan een opzet zonder SSL ga dan verder naar GEEN SSL.

#### SSL
Met een SSL verbinding worden de gegevens van de bezoeker versleuteld verstuurd. Hierdoor kan niemand behalve Matomo (en de bezoeker zelf) zien welke gegevens er worden uitgewisseld. Om een beveiligde verbinding te creëren heeft u een SSL certificaat nodig. Deze kunt u bij een Certificate Authority aanvragen. In deze tutorial gebruiken we een Dockerized versie van Let's Encrypt's **certbot**. Dit geeft ons de mogelijkheid om met het draaien van een specifieke Docker container een SSL certificaat te verkrijgen. Daarnaast houdt deze container de geldigheid van uw certificaat in de gaten en vraagt het automatisch een vernieuwing aan wanneer dit nodig is. Voor het gebruik van Matomo via een SSL verbinding zijn een aantal andere configuraties nodig. Vervang daarom de `docker-compose.yml` en `nginx.conf` bestanden met onderstaande commando's.

```bash
rm docker-compose.yml nginx/nginx.conf
mv ssl/docker-compose.yml . && mv ssl/nginx.conf nginx
```

Om de server te laten weten welk domein u wilt gebruiken dient u alle voorkomens van 'example.org' in `nginx/nginx.conf` en `ssl/init-letsencrypt.sh` te vervangen door uw eigen domein. Hierna kunt u het SSL script uitvoeren:

```bash
./ssl/init-letsencrypt.sh
```

#### GEEN SSL
Mocht u geen gebruik willen maken van een beveiligde verbinding of wilt u de installatie enkel lokaal testen vervang dan de `server_name` in het `nginx/nginx.conf` bestand door uw host-adres. In dien u de server lokaal wilt uitproberen vult u hier `localhost` in:

```
server_name localhost;
```

### Start de server
U kunt nu de Matomo webserver starten met het docker-compose commando:

```bash
docker-compose up
```

Bezoek de door u ingestelde host (`uw-matomo-website.nl` of `localhost`)

### Matomo Installatie
Als u voorgaande stappen succesvol heeft kunt u nu de welkomstpagina van Matomo zien. U kunt bovenin de gewenste taal kiezen en op 'volgende' klikken. Hierna wordt er een systeem controle uitgevoerd en kunt u de database instellen. Als u niks aan wachtwoorden heeft veranderd vult u in de lege velden het volgende in:

* Inloggen: matomo
* Wachtwoord: #your_secret_password
* Naam database: matomo

Hierna kunt u de 'super user' account aanmaken en een eerste website waarvan u de statistieke wilt bijhouden toevoegen. Er verschijnt nu een `Javascript Tracking Code` die u op uw website kunt plaatsen. Bij elk bezoek aan uw website wordt de code geactiveerd en vindt er een korte communicatie met de Matomo server plaats.

### Proxy
De aangeleverde opzet maakt gebruik Nginx als tussenpersoon tussen Matomo en de gebruiker, hierdoor ziet Matomo alleen het IP-adres van Nginx. Als u het IP-adres van de daadwerkelijk bezoeker wilt zien, dient u Matomo duidelijk te maken dat het dit ergens anders vandaan moet halen. Dit doet u door onderstaande regels aan Matomo's `config/config.php.ini` toe te voegen.

```
[General]
force_ssl = 1
assume_secure_protocol = 1
proxy_client_headers[] = "HTTP_X_FORWARDED_FOR"
proxy_host_headers[] = "HTTP_X_FORWARDED_HOST" 
```

De aangeleverde code bevat een patch waarmee dit automatisch voor u gedaan wordt: 

```bash
./config/proxy-patch
```

### Toestemming van bezoeker
De regelgeving omtrent het plaatsen van cookies kan soms wat lastig te volgen zijn en bevat een aantal uitzonderingen (zie onze blogs: [cookies](https://nogadata.nl/2020/03/09/cookies.html) en [cookies II](https://nogadata.nl/2020/03/09/borgesius-cookies.html)). Officieel is het in Nederland verplicht om bezoekers van uw website te informeren over het gebruik van cookies. Voordat er cookies mogen worden geplaatst dienen gebruikers eerst actief toestemming (consent) te geven. Er geldt echter een uitzondering voor analytics cookies die privacy-vriendelijk zijn.

De standaard configuratie van Matomo anonimiseert de laatste 2 bytes van elk IP-adres en respecteert 'Do Not Track' verzoeken. Als u daarnaast ook nog eens uw eigen server gebruikt, kunt u Matomo op een privacy vriendelijke manier gebruiken. Deze redenatie gaat echter alleen op binnen de Nederlandse wet. Mocht u ook op internationale bezoekers rekenen is een consent formulier wel op zijn plaats. Matomo geeft hier instructies voor in de 'privacy' tab.

### Conclusie
Met bovenstaande instructies heeft u een begin kunnen maken met het opzetten van uw eigen Matomo server. Om de installatieprocedure zo eenvoudig mogelijk te houden, betreft de huidige installatie een absolute basis opzet van Matomo die op veel punten verbeterd kan worden. Een volgende blog zal daarom aandacht besteden aan het verbeteren uw Matomo server doormiddel van automatische archief processen en geografische databases. 


