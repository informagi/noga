---
layout: "post"
title: "Matomo opzetten II"
author: "Pepijn Boers"
date: "2020-12-01 12:00"
excerpt: "Uitbreiding van matomo installatie"
tags: NoGA Matomo setup opzetten cronjob docker-compose GeoIP backup
---

De voorgaande blog beschreef het gebruik van docker-compose voor het opzetten van een basis versie van Matomo. Deze blog gaat daarop verder en bespreekt een aantal verbeterpunten voor de huidige opzet. Denk hierbij aan het automatisch genereren van rapporten, het opslaan van reservekopieën of het koppelen van geografische informatie aan IP-adressen. Als u nog geen werkende Matomo server heeft, volg dan eerst de [basis setup](https://nogadata.nl/2020/11/23/matomo-opzetten.html) alvorens u doorgaat met deze blog.

## Archiveren van rapporten
Met de verzamelde website data bouwt Matomo een grote variatie aan rapporten. Het bouwen van die rapporten kost rekenkracht en kan op sommige momenten uw server wat vertragen. Hierom raadt Matomo beheerders van middel tot grote websites aan om het ter plekken genereren van rapporten uit te schakelen en te vervangen door automatisch gegenereerde rapporten op vaste tijdstippen. Het directe gevolg is dat er niet elke keer dat er naar een rapport wordt gekeken meteen een nieuw rapport wordt gebouwd. Hierdoor bespaar je rekenkracht voor andere processen.

Het automatisch genereren van rapporten gaat in twee stappen. Zorg er eerst voor dat er elke X uur een nieuw rapport wordt gearchiveerd, door het aanroepen van onderstaand commando. Dit kan via een [cronjob](https://nl.wikipedia.org/wiki/Cronjob) of taakplanner applicatie. Verder dient u in uw Matomo installatie aan te geven dat u het automatisch genereren van rapporten wilt uitschakelen. De optie vindt u onder Algemene instellingen > Archiveringsinstellingen.

```bash
docker exec -i matomo-compose_app_1 /var/www/html/console core:archive --url=<jouw-site>
```

## Reservekopieën
### Matomo server
Voor het maken van een reservekopie van uw Matomo installatie is het van belang dat u de `config` en de `plugin` folder opslaat. Deze bevatten alle persoonlijke configuratie informatie over uw Matomo server. Aangezien we een reservekopie maken door bestanden uit een docker container te kopiëren dient uw server aan te staan tijdens het uitvoeren van de volgende commando's.

Een back-up kan worden gemaakt met:

```bash
docker cp matomo-compose_app_1:/var/www/html/config config
docker cp matomo-compose_app_1:/var/www/html/plugins plugins
tar -zcvf backup.tar.gz plugins config 
rm -rf config plugins
```

Een back-up kan weer worden teruggezet terug via: 

```bash
tar -zxvf backup.tar.gz
docker cp config matomo-compose_app_1:/var/www/html/config
docker cp plugins matomo-compose_app_1:/var/www/html/plugins
```

Kant-en-klare backup en restore scripts zijn beschikbaar in `conf/backups`. Een back-up maken en terugzetten doet u met volgende commando's:

```bash
./conf/backups/backup-matomo
./conf/backup/restore-matomo <uw-matomo-backup.tar.gz>
```
### Matomo database
Een back-up van uw Matomo configuratie is pas compleet met een back-up van de database. De database bevat namelijk alle gebruikers logs en Matomo accounts. Uw kunt een back-up maken met:

```bash
docker exec -i matomo-compose_db_1 mysqldump \
    --hex-blob \
    --single-transaction \
    --quick \
    --lock-tables=false \
    --password="your_password" \
    matomo | gzip > db.sql.gz
```

Of maak gebruik van de kant-en-klare backup scripts:

```bash
./conf/backups/backup-db
./conf/backups/restore-db <back-up-naam.sql.gz>
```
## Geografische locatie bepaling
Om inzichten te krijgen in de geografische locatie van uw bezoekers kunt u een GeoIP database downloaden. Hierin staan toewijzingen van IP-adressen aan geografische locaties. Hoe accuraat deze locaties zijn hangt af van de database die u gebruikt. Erg nauwkeurige pakketten kosten meestal geld, maar met zogenoemde 'light' versies krijgt u een globaal idee van de locaties van uw bezoekers (hoe globaler hoe privacy vriendelijker). Matomo biedt [hier](https://matomo.org/docs/geo-locate/) uitleg over Matomo en geolocatie databases.

Een simpele IP naar stad database is [hier](https://db-ip.com/db/download/ip-to-city-lite) te downloaden. Na het downloaden dient u de database uit te pakken en van naam te veranderen (verander naar `DBIP-City.mmdb`) en in de juiste folder te zetten, zodat Matomo de database herkent. 

Kopiëren van database naar matomo's `misc` folder:

```bash
docker cp <GeoIP-database> matomo-compose_app_1:/var/www/html/misc/
```

Nu kunt u via Systeem > Geolocatie > Locatie Provider de DBIP/GeoIP 2 (php) optie selecteren en opslaan.

## Conclusie
Met het doorvoeren van bovenstaande instructies heeft u uw Matomo server verder verbeterd. Als laatste test kunt u een systeem controle uitvoeren door naar Diagnose > systeemcontrole te gaan. Als bovenstaande stappen succesvol zijn afgerond zult u hier de volgende tekst aantreffen: "Hoera! Er zijn geen problemen met je Matomo setup. Geef jezelf een schouderklopje."