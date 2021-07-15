---
layout: "post"
title: "Gebruiksvriendelijkheid van Matomo en Google Analytics"
author: "Alessandra van Veen"
date: "2021-05-11 8:00"
excerpt: "Een vergelijking van gebruiksvriendelijkheid aan de hand van verschillende scenario's"
tags: NoGA Matomo Google Analytics Radboud universiteit pilot
---

In de [vorige blog](/2021/04/12/scenarios-radboud-universiteit.html) werd Matomo en Google Analytics vergeleken aan de hand van verschillende scenario's om te kijken of de resultaten verschillen. Deze keer zullen we kijken naar het verschil in gebruiksvriendelijkheid van de analytics diensten aan de hand van de uitgevoerde scenario's en concluderen of Matomo een goed alternatief is voor Google Analytics op basis hiervan.

## De scenario's

In de vorige blog hebben we naar de volgende vier scenario's gekeken.

## Vergelijking

Over het algemeen waren de scenario's makkelijk uit te voeren op beide systemen, maar soms waren bepaalde dingen wel makkelijker of sneller op het ene systeem vergeleken met de ander.

Bij de eerste twee scenario's moesten we eerst een specifieke pagina zoeken en daar verschillende informatie vandaan halen. Om bij het juiste onderdeel terecht te komen, moet je met Matomo eerst navigeren naar Behavior en dan pages. Via Google Analytics moet er eerst genavigeerd worden naar Site Content en dan All pages.  In Google Analytics staat het volledige pad, bijvoorbeeld `/english/education/masters/`. Om de juiste pagina te vinden kun je de zoekbalk gebruiken. Als je bijvoorbeeld ‘data-science’ intikt, zie je alle pagina's waar data-science in staat. Je kan ook op de juiste pagina daarna klikken om alleen die resultaten te krijgen.  Bij Matomo staan pagina's standaard hiërarchisch, maar het is mogelijk om het flat te weergeven waardoor de structuur soortgelijk is aan dat van Google Analytics. Flat maakt zoeken makkelijker, terwijl hiërarchisch niet altijd alles weergeeft. Bij Matomo is het voor een gebruiker die het voor het eerst gebruikt wel even zoeken naar de settings icoon die onderaan de pagina zit verstopt.  Zodra we onze pagina hadden gevonden, was het triviaal om de meeste data te verzamelen.  Alle data staat er meteen, maar om data te verkrijgen van een specifiek soort bezoeker, is er nog een extra stap nodig. In Google Analytics is dit te doen door een tweede dimensie toe te voegen op basis van het soort visitor. Google verwerkt de data en geeft je de resultaten binnen enkele seconden. In Matomo wordt een segment opgesteld dat alle data filtert, dus ook de data die niet nodig is. Het nadeel hiervan is dat een segment wanneer die voor het eerst wordt opgesteld verwerkt moet worden. Dit kan enkele minuten tot een uur duren afhankelijk van hoe Matomo is opgesteld en hoeveel data het moet verwerken. Als het segment eenmaal bestaat, heb je de resultaten wel altijd binnen enkele seconden.

Scenario drie was erg makkelijk uit te voeren met allebei de diensten. Zowel bij Matomo als Google Analytics was de benodigde data binnen een paar klikken te vinden.  Ook voor scenario vier was het makkelijk om de data te vinden zodra je de juiste pagina had. Wel was er een belangrijk verschil tussen Matomo en Google Analytics op de transitions page. Terwijl Matomo maximaal vijf volgende pagina's aangeeft, geeft Google Analytics er tien. Wel heeft Google Analytics de mogelijkheid om een zoekbalk te gebruiken om te zien of een bepaalde pagina er toch tussen zit. Matomo heeft dit niet. Wel heeft Matomo weer meer categorieën voor transitions zoals downloads en outlinks.

Voor een gebruiker die al wel bekend is met Google Analytics, maar nog niet met Matomo ging het uitzoeken vrij gemakkelijk in bijna alle gevallen. De uitzondering was bijvoorbeeld de instellingen van hoe de paden werden weergegeven en de segmenten die je moet opstellen. De opstelling van beide diensten lijken verder erg op elkaar en ze gebruiken ook vaak soortgelijke of zelfs dezelfde termen, wat het leren van Matomo makkelijker maakt.

## Conclusie

Op basis van de uitgevoerde scenario's is de gebruiksvriendelijkheid van Matomo en Google Analytics voor de meeste doelen vergelijkbaar. Wel vereist Matomo voor sommige doelen iets meer tijd omdat bijvoorbeeld een segment moet worden opgesteld en dan verwerkt moet worden. Ook heeft Matomo een iets hogere leercurve. Hoewel bij Google Analytics en Matomo het meeste snel was te vinden zonder hulp, was bij Matomo niet alles altijd even duidelijk als bij Google Analytics.  Op basis van gebruiksvriendelijkheid is Matomo een goed alternatief voor Google Analytics.  Wel moet de gebruiker rekening houden met het feit dat niet ze niet altijd alle resultaten meteen zullen hebben.
