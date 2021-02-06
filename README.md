# Project: Bewegingssensor

# Context

Dankzij de huidige Corona-crisis zijn velen van ons bijna constant binnen wat ten koste gaat van een heel belangrijk aspect van ons leven: beweging. Daarom heb ik ervoor gekozen om een systeem te maken die ervoor zorgt dat je toch wel even je benen gaat strekken.

# Doel

Het doel van dit project is om de gebruiker aan te sturen om regelmatig te gaan bewegen. Dit wordt gedaan door de gebruiker om de 45 minuten een notificatie op mobiel te sturen. Het is de bedoeling dat de gebruiker daardoor uit zijn kamer gaat stappen, om even te pauzeren.

Het uiteindelijke doel is dat de gebruiker hiervan gewoonte maakt en uit zichzelf, zonder de nood van de notificaties gaat bewegen.

# Gebruik

Het apparaat werkt door middel van een PIR Motion sensor die gericht is op een deur; het kan detecteren of de deur wordt geopend.
 Er zit een interne timer in het apparaat van 45 minuten. **Als er 45 minuten lang geen beweging is gedetecteerd, krijgt de gebruiker via de Pushbullet service een notificatie**. Pushbullet heeft een Android app, maar je kan notificaties ook zien op een browser. **Als er wel beweging is gedetecteerd wordt de timer gereset.** In beide gevallen wordt er ook informatie gestuurd naar ThingSpeak.

Flowchart van de algoritme:

![flowchart](https://github.com/nikolasaratlija/door-monitor/blob/main/documents/images/flowchart.png?raw=true)

## Dubbel Registreren Voorkomen

Als je een gebruiker de deur uitgaat, zal hij uiteindelijk weer terugkomen. **Hoe kan het voorkomen worden dat de terugkomst ook wordt meegeteld als beweging?**
 De bewegingssensor heeft een mechanisme die ervoor zorgt dat het signaal voor een bepaalde tijd aan blijft staan nadat beweging is gedetecteerd, ondanks dat er misschien geen beweging meer is. Je kan de duur bepalen met een potentiometer, in dit project zal het worden ingesteld op 5 minuten.

Dankzei dit mechanisme worden alle bewegingen na het initiële signaal voor een bepaalde tijd genegeerd. Aangezien alleen de initiële signaal belangrijk is, is dit een goede oplossing voor het probleem.

# Data en Informatie

Naast de timer functionaliteit zullen ook statistieken/data over Wi-Fi worden gestuurd naar een middleware, namelijk ThingSpeak. Op ThingSpeak kunnen gegevens worden verzameld en betekenis worden aangegeven. Daarbij kan er ook een grafische representatie worden gezien van deze gegevens.

Uit de gegevens kan je misschien zien dat de gebruiker na een bepaald periode uit zich/haarzelf is begonnen met bewegen en dat het alarm haast niet meer aan gaat. Dat betekent dat het project daadwerkelijk werkt en zijn doel heeft bereikt.

# Gebruikte Onderdelen/ Technologieën

- Python 3.7 of hoger
- Raspberry Pi 3 Model B+
- HC-SR501 PIR Motion sensor
- 3x Female to Female Jumper Cables
- [ThingSpeak](https://thingspeak.com/channels/1297027)
- [GitHub](https://github.com/nikolasaratlija/door-monitor)
- Pushbullet

Het prototype was gemaakt met behulp van het volgende artikel: [freva.com](https://www.freva.com/nl/2019/05/21/hc-sr501-pir-bewegingssensor-met-raspberry-pi-gebruiken/)
![f](https://github.com/nikolasaratlija/door-monitor/blob/main/documents/images/prototype_diagram.png?raw=true)

Dit diagram was gebruikt voor het maken van het prototype. (freva.com)

# IoT Pipeline


![pipeline](https://github.com/nikolasaratlija/door-monitor/blob/main/documents/images/pipeline.png?raw=true)