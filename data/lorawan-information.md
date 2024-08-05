# What are LoRa and LoRaWAN?

Welcome to the first chapter of The Things Fundamentals on LoRaWAN. In this section, you’ll learn why LoRaWAN is so awesome, hear about some great LoRaWAN use cases, and learn the difference between LoRa and LoRaWAN.
### LoRa

LoRa is a wireless modulation technique derived from Chirp Spread Spectrum (CSS) technology. It encodes information on radio waves using chirp pulses \- similar to the way dolphins and bats communicate! LoRa modulated transmission is robust against disturbances and can be received across great distances.
Don’t be alarmed about the complex terms; LoRa modulation and Chirp Spread Spectrum technology are simple to understand in practice. In case you are curious, in this video, Richard Wenner explains how Chirp Spread Spectrum technology works:

Video: https://www.youtube.com/embed/dxYY097QNs0

LoRa is ideal for applications that transmit small chunks of data with low bit rates. Data can be transmitted at a longer range compared to technologies like WiFi, Bluetooth or ZigBee. These features make LoRa well suited for sensors and actuators that operate in low power mode.
LoRa can be operated on the license free sub\-gigahertz bands, for example, 915 MHz, 868 MHz, and 433 MHz. It also can be operated on 2\.4 GHz to achieve higher data rates compared to sub\-gigahertz bands, at the cost of range. These frequencies fall into ISM bands that are reserved internationally for industrial, scientific, and medical purposes.
### LoRaWAN

LoRaWAN is a Media Access Control (MAC) layer protocol built on top of LoRa modulation. It is a software layer which defines how devices use the LoRa hardware, for example when they transmit, and the format of messages.
The Things Network is powered by The Things Stack, which is a LoRaWAN network server that receives messages from LoRaWAN devices. Try it and get started building for free here .
The LoRaWAN protocol is developed and maintained by the LoRa Alliance . The first LoRaWAN specification was released in January 2015\. The table below shows the version history of the LoRaWAN specifications. At the time of this writing the latest specifications are 1\.0\.4 (in 1\.0 series) and 1\.1 (1\.1 series).

| **Version** | **Release date** |
| --- | --- |
| 1\.0 | January 2015 |
| 1\.0\.1 | February 2016 |
| 1\.0\.2 | July 2016 |
| 1\.1 | October 2017 |
| 1\.0\.3 | July 2018 |
| 1\.0\.4 | October 2020 |

## Bandwidth vs. Range

LoRaWAN is suitable for transmitting small size payloads (like sensor data) over long distances. LoRa modulation provides a significantly greater communication range with low bandwidths than other competing wireless data transmission technologies. The following figure shows some access technologies that can be used for wireless data transmission and their expected transmission ranges vs. bandwidth.

## Why is LoRaWAN so awesome?

* **Ultra low power** \- LoRaWAN end devices are optimized to operate in low power mode and can last up to 10 years on a single coin cell battery.
* **Long range** \- LoRaWAN gateways can transmit and receive signals over a distance of over 10 kilometers in rural areas and up to 3 kilometers in dense urban areas.
* **Deep indoor penetration** \- LoRaWAN networks can provide deep indoor coverage, and easily cover multi floor buildings.
* **License free spectrum** \- You don’t have to pay expensive frequency spectrum license fees to deploy a LoRaWAN network.
* **Geolocation**\- A LoRaWAN network can determine the location of end devices using triangulation without the need for GPS. A LoRa end device can be located if at least three gateways pick up its signal.
* **High capacity** \- LoRaWAN Network Servers handle millions of messages from thousands of gateways.
* **Public and private deployments** \- It is easy to deploy public and private LoRaWAN networks using the same hardware (gateways, end devices, antennas) and software (UDP packet forwarders, Basic Station software, LoRaWAN stacks for end devices).
* **End\-to\-end security**\- LoRaWAN ensures secure communication between the end device and the application server using AES\-128 encryption.
* **Firmware updates over the air** \- You can remotely update firmware (applications and the LoRaWAN stack) for a single end device or group of end devices.
* **Roaming**\- LoRaWAN end devices can perform seamless handovers from one network to another.
* **Low cost** \- Minimal infrastructure, low\-cost end nodes and open source software.
* **Certification program**\- The LoRa Alliance certification program certifies end devices and provides end\-users with confidence that the devices are reliable and compliant with the LoRaWAN specification.
* **Ecosystem**\- LoRaWAN has a very large ecosystem of device makers, gateway makers, antenna makers, network service providers, and application developers.

## LoRaWAN use cases

Here are a few great LoRaWAN use cases provided by Semtech , to give you some insight into how LoRaWAN can be applied:
* **Vaccine cold chain monitoring** \- LoRaWAN sensors are used to ensure vaccines are kept at appropriate temperatures in transit.
* **Animal conservation** \- Tracking sensors manage endangered species such as Black Rhinos and Amur Leopards.
* **Dementia patients** \- Wristband sensors provide fall detection and medication tracking.
* **Smart farms**\- Real time insights into crop soil moisture and optimized irrigation schedule reduce water use up to 30%.
* **Water conservation**\- Identification and faster repair of leaks in a city’s water network.
* **Food safety**\- Temperature monitoring ensures food quality maintenance.
* **Smart waste bins** \- Waste bin level alerts sent to staff optimize the pickup schedule.
* **Smart bikes**\- Bike trackers track bikes in remote areas and dense buildings.
* **Airport tracking** \- GPS\-free tracking monitors vehicles, personnel, and luggage.
* **Efficient workspaces** \- Room occupancy, temperature, energy usage and parking availability monitoring.
* **Cattle health** \- Sensors monitor cattle health, detect diseases and forecast calves delivery time.
* **LoRa in space** \- Satellites to provide LoRaWAN\-based coverage worldwide.

## LoRa Alliance

The LoRa Alliance® is an open, non\-profit association established in 2015\. It supports development of the LoRaWAN protocol and ensures interoperability of all LoRaWAN products and technologies. Today, the LoRa Alliance has over 500 members around the globe .
The LoRa Alliance provides LoRaWAN certification for end devices. Certified end devices provide users with confidence that the end device is reliable and compliant with the LoRaWAN specification. You can learn more about LoRaWAN certification by visiting the LoRa Alliance website . Certification is only available for device manufacturers that are members of the LoRa Alliance. Once certified, the manufacturer can use the LoRaWAN Certified mark with the product.
## LoRaWAN is now an ITU standard.

As announced by the LoRa Alliance® on December 7, 2021, LoRaWAN® is officially approved as a standard for Low Power Wide Area Networking (LPWAN) by the International Telecommunication Union (ITU).
Read the Lora Alliance® Press Release, LoRaWAN® Formally Recognized as ITU International Standard for Low Power Wide Area Networking for more information.# LoRaWAN Architecture

LoRaWAN networks are deployed in a star\-of\-stars topology.
A typical LoRaWAN network consists of the following elements.

* End Devices \- sensors or actuators send LoRa modulated wireless messages to the gateways or receive messages wirelessly back from the gateways.
.
* Gateways \- receive messages from end devices and forward them to the Network Server.
* Network Server \- a piece of software running on a server that manages the entire network.
* Application servers \- a piece of software running on a server that is responsible for securely processing application data.
* Join Server \- a piece of software running on a server that processes join\-request messages sent by end devices (The Join Server is not shown in the above figure).

End devices communicate with nearby gateways and each gateway is connected to the network server. LoRaWAN networks use an ALOHA based protocol, so end devices don’t need to peer with specific gateways. Messages sent from end devices travel through all gateways within range. These messages are received by the Network Server. If the Network Server has received multiple copies of the same message, it keeps a single copy of the message and discards others. This is known as message deduplication.
Let’s examine each element of the LoRaWAN network in detail.
### End devices

A LoRaWAN end device can be a sensor, an actuator, or both. They are often battery operated. These end devices are wirelessly connected to the LoRaWAN network through gateways using LoRa RF modulation. The following figure shows an end device that consists of sensors like temperature, humidity, and fall detection.

### Gateways

Each gateway is registered (using configuration settings) to a LoRaWAN network server. A gateway receives LoRa messages from end devices and simply forwards them to the LoRaWAN network server. Gateways are connected to the Network Server using a backhaul like Cellular (3G/4G/5G), WiFi, Ethernet, fiber\-optic or 2\.4 GHz radio links.
#### Types of LoRaWAN Gateways

LoRaWAN gateways can be categorized into indoor (picocell) and outdoor (macrocell) gateways.
Indoor gateways are cost\-effective and suitable for providing coverage in places like deep\-indoor locations (spaces covered by multiple walls), basements, and multi\-floor buildings. These gateways have internal antennas or external ‘pigtail’ antennas. However depending on the indoor physical environment some indoor gateways can receive messages from sensors located several kilometers away.
The following figure shows The Things Indoor gateway designed to be directly plugged into an AC power outlet.

Outdoor gateways provide a larger coverage than the indoor gateways. They are suitable for providing coverage in both rural and urban areas. . These gateways can be mounted on cellular towers, the rooftops of very tall buildings, metal pipes (masts) etc. Usually an outdoor gateway has an external antenna (i.e. Fiberglass antenna) connected using a coaxial cable.
If you are good at hacking electronic products, you can convert some indoor gateways to outdoor gateways using water/dust proof enclosures and adding external antennas.
The following figure shows a LoRaWAN outdoor gateway. It has connectors for connecting external LoRaWAN, 3G/4G, and GPS antennas. Can you figure them out?

Usually, the receiver sensitivity of an outdoor gateway is higher than the receiver sensitivity of an indoor gateway.
### Network Server

The Network Server manages gateways, end\-devices, applications, and users in the entire LoRaWAN network.
A typical LoRaWAN Network Server has the following features.
* Establishing secure 128\-bit AES connections for the transport of messages between end\-devices and the Application Server (end\-to\-end security).
* Validating the authenticity of end devices and integrity of messages.
* Deduplicating uplink messages.
* Selecting the best gateway for routing downlink messages.
* Sending ADR commands to optimize the data rate of devices.
* Device address checking.
* Providing acknowledgements of confirmed uplink data messages.
* Forwarding uplink application payloads to the appropriate application servers
* Routing uplink application payloads to the appropriate Application Server.
* Forwarding Join\-request and Join\-accept messages between the devices and the join server
* Responding to all MAC layer commands.

### Application Server

The Application Server processes application\-specific data messages received from end devices. It also generates all the application\-layer downlink payloads and sends them to the connected end devices through the Network Server. A LoRaWAN network can have more than one Application Server. The collected data can be interpreted by applying techniques like machine learning and artificial intelligence to solve business problems.
### Join Server

The Join Server assists in secure device activation, root key storage, and session key generation. The join procedure is initiated by the end device by sending the Join\-request message to the Join Server through the Network Server. The Join\-server processes the Join\-request message, generates session keys, and transfers NwkSKey and AppSKey to the Network server and the Application server respectively.
The Join Server was first introduced with LoRaWAN v1\.1\. It is also availabe in LoRaWAN v1\.0\.4\.# Regional Parameters

##### Info:

 For information on the specific versions of the Regional Parameters check [The Things Stack documentation](https://www.thethingsindustries.com/docs/the-things-stack/concepts/spec-regional-parameters/).

LoRaWAN operates in unlicensed radio spectrum. This means that anyone can use the radio frequencies without having to pay million dollar fees for transmission rights. It is similar to WiFi, which uses the 2\.4GHz and 5GHz ISM bands worldwide. Anyone is allowed to set up WiFi routers and transmit WiFi signals without the need for a license or permit.
LoRaWAN uses lower radio frequencies with a longer range. The fact that frequencies have a longer range also comes with more restrictions, that are often country\-specific. This poses a challenge for LoRaWAN, as it strives to maintain uniformity across various regions of the world. As a result, LoRaWAN is specified for several bands within these regions. These bands are similar enough to support a region\-agnostic protocol but entail various consequences for the implementation of backend systems.
* LoRaWAN has official regional specifications, called Regional Parameters , that you can download from the LoRa Alliance website .
* These LoRaWAN regional specifications do not specify everything either. They only cover a region by specifying the common denominator. For example, the LoRaWAN regional parameters for Asia only specify a common subset of channels \- but there are variations between regulations in Asian countries. Furthermore, each network server operator is free to select additional parameters, such as additional emission channels. We call these parameters Other . For The Things Network, they are defined in this GitHub repository .
* In some countries, more than one frequency plan may be used. For example, in the Netherlands (NL) , both EU868\-870 and EU433 can be used.
* The regional parameters include physical layer parameters such as frequency plans (channel plans), mandatory channel frequencies and data rates for join\-request messages. The Regional Parameters also include LoRaWAN layer parameters such as maximum payload size.

In this chapter you will learn in detail about the EU863\-870 band and US902\-928 ISM band. This chapter also presents some important parameters involved in other frequency plans.
# Frequency Plans

LoRaWAN operates in the unlicensed ISM (Industrial, Scientific, and Medical) bands. The table below lists all the frequency plans and their common names.

| Plan ID | Frequency Plan | Common Name |
| --- | --- | --- |
| 1 | EU863\-870 | EU868 |
| 2 | US902\-928 | US915 |
| 3 | CN779\-787 | CN779 |
| 4 | EU433 | EU433 |
| 5 | AU915\-928 | AU915 |
| 6 | CN470\-510 | CN470 |
| 7 | AS923\-1 | AS923 |
| 8 | AS923\-2 | AS923\-2 |
| 9 | AS923\-3 | AS923\-3 |
| 10 | KR920\-923 | KR920 |
| 11 | IN865\-867 | IN865 |
| 12 | RU864\-870 | RU864 |
| 13 | AS923\-4 | AS923\-4 |

Information about specific countries and frequency plans can be found here:
* [Frequency Plans](/docs/lorawan/frequency-plans/)
* [Frequency Plan by Country](/docs/lorawan/frequencies-by-country/)

##### Note:

 The Things Fundamentals certification exam expects detailed knowledge about the EU863\-870 and US902\-928 frequency plans. However, a basic understanding of other frequency plans is sufficient.

# Default Settings for All Regions

There are a few recommended default settings available that can be applied to all the regions.
* RX1 Delay: **1s**
* RX2 Delay: **2s** (RX1 Delay \+ 1s)
* Join Accept 1 Delay: **5s**
* Join Accept 2 Delay: **6s**

* EU863\-870
* US902\-928
* IN865\-867
* CN470\-510

2. Which bit rate can be achieved with the configuration, SF12 / 125 kHz?

* 250 bit/s
* 440 bit/s
* 980 bit/s
* 1760 bit/s

3. Which country allows the choice of using Listen Before Talk Adaptive Frequency Agility (LBT AFA)?

* Japan
* South Korea
* Australia
* United States of America

4. Which country uses Listen Before Talk (LBT) instead of using duty cycle limitations?

* Japan
* South Korea
* China
* The Neatherlands

5. How many sub\-bands are included in the EU863\-870 frequency plan for LoRaWAN as defined by the ETSI?

* 3
* 4
* 5
* 6

6. What is the maximum application payload size allowed for LoRa: SF12 / 125 kHz in Europe?

* 51 bytes
* 115 bytes
* 242 bytes# LoRaWAN Relay

LoRaWAN relays are suitable for bridging wireless communication gaps in areas where the gateway and end device cannot directly communicate with each other due to weak signal strength caused by factors such as extreme distance or obstacles between them. They are low\-cost, low\-power devices. A relay’s hardware is equivalent to a standard LoRaWAN end device. A single relay can serve up to 16 end devices. For the Network Server, a relay appears as a standard end device.
The following figure shows how a relay helps to forward/relay a message from an end device to the gateway.

Adding a new gateway is a good idea if many devices have a lack of signal reception. But if it’s just a few devices, using a relay is a cheaper solution.
## Relay Requirments

The relay specification requirements are described in the LoRaWAN® Relay Specification TS011\-1\.0\.0 document.
* End device should implement the LoRaWAN stack, precisely TS001\-LoRaWAN L2 1\.0\.4 and Regional Parameters RP2\-1\.0\.3 specifications, and LoRa Basics Modem firmware. The experimental release of the LoRa Basics Modem firmware can be found [here](https://github.com/Lora-net/SWL2001).
* End device should be implemented with SX1261/2, LR1110, LR1120, or LR1121 sub\-GHz LoRa transceiver.
* A LoRaWAN Network Server (e.g., The Things Stack ) supporting the relay specification.

##### Note:

 The gateways do not need to be updated to support relays.

## How Relay Works?

The following steps describe how an end device communicates with the Network Server through a relay.
The end device and the relay know in advance which channels (frequencies) are used for exchanging frames between them.
The end device that wants to use the support of a relay, first sends a Wake\-on\-Radio (WOR) frame. The WOR frame is used to wake up the relay and share the radio parameters like frequency and data rate that will be used in the subsequent uplink frame.
There are two types of WOR frames an end device can send to a relay, whose type can be identified by examining the payload content:
* Relay Join\-Request
* Relay Uplink (Class A uplink)

The relay goes to sleep mode if there is no radio activity. Even if the relay is in sleep mode, it periodically scans the channel for any radio activity in a very low\-power mode. This channel scanning period is called Channel Activity Detection (CAD). The CAD can be 25ms to 1s (default). The duration between two consecutive CAD is called CADPeriodicity. The WOR frame’s preamble has a variable length and can be up to 1s long. This long preamble gives the relay a higher chance of detecting the WOR frame with its very short CAD. If there is no LoRa activity detected during the CAD, the relay goes back to sleep mode.
If the relay detects a LoRa activity during the scan, it switches from CAD to the reception mode. The time taken to switch from CAD to the reception mode is called CadToRx delay. In this mode, the relay demodulates the incoming WOR frame. If the demodulation is successful and the WOR frame is valid, the relay sends the Wake On Radio Acknowledge (WOR\-ACK) frame to the end device.
The end device finds the following information in the payload of the WOR\-ACK frame. These parameters are then used by the end device to align certain settings with the relay.
* CadToRx \- the time required to switch from CAD to the reception mode of WOR
* Forward \- indicates the current state of the relay forward limitations
* RelayDataRate\- the data rate used by the relay to forward the end device payload
* XTALAccuracy \- the crystal frequency accuracy of the relay clock
* CADPeriodicity \- the delay between two consecutive CAD scans performed by the relay on a single channel
* TOffset \- the time, in milliseconds, between the start of the scan and the end of the reception of the WOR frame preamble.

The relay listens for the subsequent uplink LoRaWAN frame from the end device. Upon receiving it, the relay prepends a 6\-byte metadata field to the frame. The resulting frame is called Relay Uplink FRMPayload. Subsequently, the relay creates a new LoRaWAN frame by inserting the Relay Uplink FRMPayload into its payload field. This new frame is then transmitted to the Network Server through the nearby gateways (FPort \= 226\). The Network Server handles the message deduplication.
The relay receives any downlink frame from the Network Server (FPort \= 226\) over RX1 or RX2 slots. Upon receiving it, the relay extracts the actual payload from the LoRaWAN frame and then sends it to the end device over the RXR slot.
## Regional Parameters for Relays

The following regional parameters are applicable to use with relays in different regions.
In EU868, four dedicated channels with a bandwidth of 125 kHz and a spreading factor of 9 are used to communicate between the end device and the relay. Among them, two channels are used to send the WOR frame from the end device to the relay:

| Channel | Frequency |
| --- | --- |
| 0 | 856\.1 MHz |
| 1 | 865\.5 MHz |

Two channels are used to send the WOR\-ACK frame from the relay to the end device:

| Channel | Frequency |
| --- | --- |
| 0 | 865\.3 MHz |
| 1 | 865\.9 MHz |

In US915, four dedicated channels with a bandwidth of 500 kHz and a spreading factor of 10 are used to communicate between the end device and the relay. Among them, two channels are used to send the WOR frame from the end device to the relay:

| Channel | Frequency |
| --- | --- |
| 0 | 916\.7 MHz |
| 1 | 919\.9 MHz |

Two channels are used to send the WOR\-ACK frame from the relay to the end device:

| Channel | Frequency |
| --- | --- |
| 0 | 918\.3 MHz |
| 1 | 918\.3 MHz |

Refer to the Regional Parameters Specification 1\.0\.4 document for channel frequencies, bandwidths, and spreading factors in other regions, such as AU915, CN470, AS923, KR920, IN865, and RU864\.
## Security

The relay has root keys (AppKey and NwkKey) the same as those of the standard end device, which are used to derive session keys (AppSKey and NwkSKey). However, these session keys cannot be used to calculate the MIC and encrypt the payload field of WOR and WOR\-ACK frames. Therefore, a new root key is defined, called the Root Relay Session Key (RootWorSKey), which is used by both the relay and the end device.
The end device derives the RootWorSKey from its NwkSkey (LoRaWAN Version 1\.0\.X) or NwkSEncKey (LoRaWAN Version 1\.1\.X and higher). The relay will also receive a copy of the RootWorSKey from the Network Server.
Based on the RootWorSKey and the DevAddr, two session keys are derived by both the end device and the relay:
* WOR Integrity Session Key (WorSIntKey) \- used by both the end device and the relay to calculate and verify the MIC of the WOR and WOR\-ACK frames
* WOR Encryption Session Key (WorSEncKey) \- used by both the end device and the relay to encrypt/decrypt the payload field of the WOR and WOR\-ACK frames# Message Types

##### Info:

 For information on The Things Stack specific data formats, check [The Things Stack documentation](https://www.thethingsindustries.com/docs/the-things-stack/concepts/data-formats/).

In this chapter, you will learn about different message types used in LoRaWAN 1\.0\.x and 1\.1\. These message types are used to transport MAC commands and application data. The Things Fundamentals Certification exam expects you should have basic knowledge on the following topics with regards to the message types:
* Uplink and downlink messages.
* MAC Message types and their uses.
* Sending MAC commands in the FOpts field.
* Sending MAC commands and application data in the FRMPayload field.
* Keys used to encrypt each field that carries MAC Commands and application data.
* Keys used to calculate the Message Integrity Code (MIC) of each message.

## Uplink and Downlink Messages

LoRa messages can be divided into uplink and downlink messages based on the direction they travel.
Uplink messages \- Uplink messages are sent by end devices to the Network Server relayed by one or many gateways. If the uplink message belongs to the Application Server or the Join Server, the Network server forwards it to the correct receiver.
Downlink messages \- Each downlink message is sent by the Network Server to only one end device and is relayed by a single gateway. This includes some messages initiated by the Application Server and the Join Server too.
## MAC Message Types

LoRaWAN defines several MAC message types.
The following table presents MAC message types that can be found in LoRaWAN 1\.0\.x and 1\.1\.

| **LoRaWAN 1\.0\.x** | **LoRaWAN 1\.1** | **Description** |
| --- | --- | --- |
| Join\-request | Join\-request | An uplink message, used by the over\-the\-air activation (OTAA) procedure |
| Join\-accept | Join\-accept | A downlink message, used by the over\-the\-air activation (OTAA) procedure |
| Unconfirmed Data Up | Unconfirmed Data Up | An uplink data frame, confirmation is not required |
| Unconfirmed Data Down | Unconfirmed Data Down | A downlink data frame, confirmation is not required |
| Confirmed Data Up | Confirmed Data Up | An uplink data frame, confirmation is requested |
| Confirmed Data Down | Confirmed Data Down | A downlink data frame, confirmation is requested |
| RFU | Rejoin\-request | 1\.0\.x \- Reserved for Future Usage 1\.1 \- Uplink over\-the\-air activation (OTAA) Rejoin\-request |
| Proprietary | Proprietary | Used to implement non\-standard message formats |

### Join\-request, Rejoin\-request, and Join\-accept messages

In LoRaWAN 1\.0\.x, two MAC message types are used by the Over\-The\-Air\-Activation (OTAA) procedure:
* Join\-request
* Join\-accept

In LoRaWAN 1\.1, three MAC message types are used by the Over\-The\-Air\-Activation (OTAA) procedure and for roaming purposes:
* Join\-request
* Join\-accept
* Rejoin\-request

#### Join\-request

The Join\-request message is always initiated by an end device and sent to the Network Server. In LoRaWAN versions earlier than 1\.0\.4 the Join\-request message is forwarded by the Network Server to the Application Server. In LoRaWAN 1\.1 and 1\.0\.4\+, the Network Server forwards the Join\-request message to the device’s Join Server. The Join\-request message is not encrypted.
#### Join\-accept

In LoRaWAN versions earlier than 1\.0\.4 the Join\-accept message is generated by the Application Server. In LoRaWAN 1\.1 and 1\.0\.4\+ the Join\-accept message is generated by the Join Server. In both cases the message passes through the Network Server. Then the Network Server routes the Join\-accept message to the correct end\-device. The Join\-accept message is encrypted as follows.
* In LoRaWAN 1\.0, the Join\-accept message is encrypted with the AppKey.
* In LoRaWAN 1\.1, the Join\-accept message is encrypted with different keys as shown in the table below.

| **If triggered by** | **Encryption Key** |
| --- | --- |
| Join\-request | NwkKey |
| Rejoin\-request type 0, 1, and 2 | JSEncKey |

#### Rejoin\-request

The Rejoin\-request message is always initiated by an end device and sent to the Network Server. There are three types of Rejoin\-request messages: Type 0, 1, and 2\. These message types are used to initialize the new session context for the end device. For the Rejoin\-request message, the network replies with a Join\-accept message.
### Data Messages

There are 4 data message types used in both LoRaWAN 1\.0\.x and 1\.1\. These data message types are used to transport both MAC commands and application data which can be combined together in a single message. Data messages can be confirmed or unconfirmed. Confirmed data messages must be acknowledged by the receiver whereas unconfirmed data messages do not need to be acknowledged by the receiver.
A data message is constructed as shown below:

MAC payload of the data messages consists of a frame header (FHDR) followed by an optional port field (FPort) and an optional frame payload (FRMPayload).

| 7 to 22 bytes | 0 to 1 byte | 0 to N bytes |
| --- | --- | --- |
| FHDR | FPort | FRMPayload |

The frame header (FHDR) of the MAC payload consists of the following fields.

| 4 bytes | 1 byte | 2 bytes | 0 to 15 bytes |
| --- | --- | --- | --- |
| DevAddr | FCtrl | FCnt | FOpts |

The maximum length of the MAC Payload field is region and data rate\-specific and can be found in the Regional Parameters chapter .
## Sending MAC Commands and Application\-Specific Data

A data message can contain any sequence of MAC commands. A data message can carry both MAC commands and application data simultaneously in separate fields.
MAC commands can be sent either in the frame options field (FOpts) field or frame payload field (FRMPayload) field of a data message, but not both simultaneously.
Application data can be sent in the frame payload (FRMPayload) field of a data message. The FRMPayload field CAN NOT contain MAC commands and application data simultaneously.
### Sending MAC Commands in FOpts Field

MAC commands can be piggybacked in the FOpts field of a data message for sending. The total length of the MAC commands MUST NOT exceed 15 bytes.
* In LoRaWAN 1\.0\.x, these piggybacked MAC commands are always sent unencrypted.
* In LoRaWAN 1\.1, these piggybacked MAC commands are always sent encrypted using the NwkSEncKey.

### Sending MAC Commands and Application\-specific data in the FRMPayload field

The FRMPayload field can contain MAC Commands or application data. If the FRMPayload field is not empty, the FPort field must be present. If the FPort field is present,
* FPort value `0` indicates that the FRMPayload field contains only MAC commands. The total length of the MAC commands MUST NOT exceed the maximum FRMPayload length (region\-specific).
* FPort value `1-223` indicates that the FRMPayload field contains application data.

The following table shows the possible values for the FPort field depending on what it carries.

| **FPort Value** | **Description** |
| --- | --- |
| 0 | MAC commands only |
| 1 to 223 | Application\-specific data |
| 224 | LoRaWAN MAC layer test protocol |
| 255 | Reserved for Future Use (RFU) |

If the FRMPaylod field contains MAC commands or application data, the FRMPayload field must be encrypted before the Message Integrity Code (MIC) is calculated. This ensures message confidentiality. The following table shows which key is used to encrypt the FRMPayload field in different LoRaWAN versions.

| **FRMPayload** | **Direction** | **FPort** | **1\.0\.x** | **1\.1** |
| --- | --- | --- | --- | --- |
| MAC Commands | Uplink/Downlink | 0 | NwkSKey | NwkSEncKey |
| Application\-specific data | Uplink/Downlink | 1 to 223 | AppSKey | AppSKey |

## Calculating the Message Integrity Code (MIC)

The Message Integrity Code (MIC) ensures the integrity and authenticity of a message. The message integrity code is calculated over all the fields in the message and then added to the message itself. The following list shows what fields are used to calculate the MIC for each message type in LoRaWAN 1\.0\.x and 1\.1\.

| **LoRaWAN version** | **Message Type** | **Fields** |
| --- | --- | --- |
| 1\.0\.x | Join\-request | MHDR \| AppEUI \| DevEUI \| DevNonce |
| 1\.0\.x | Join\-accept | MHDR \| AppNonce \| NetID \| DevAddr \| DLSettings \| RxDelay \| CFList |
| 1\.0\.x | Data messages (up and down) | MHDR \| FHDR \| FPort \| FRMPayload |
| 1\.1 | Join\-request | MHDR \| JoinEUI \| DevEUI \| DevNonce |
| 1\.1 | Join\-accept | MHDR \| JoinNonce \| NetID \| DevAddr \| DLSettings \| RxDelay \| CFList |
| 1\.1 | Rejoin\-request Type 0 and 2 | MHDR \| Rejoin Type \| NetID \| DevEUI \| RJcount0 |
| 1\.1 | Rejoin\-request Type 1 | MHDR \| Rejoin Type \| JoinEUI \| DevEUI \| RJcount1 |
| 1\.1 | Data messages (up and down) | MHDR \| FHDR \| FPort \| FRMPayload |

The following table presents which key is used to calculate the MIC of each message type in LoRaWAN 1\.0\.x and 1\.1\.

| **LoRaWAN version** | **Message Type** | **Key** |
| --- | --- | --- |
| 1\.0\.x | Join\-request | AppKey |
| 1\.0\.x | Join\-accept | AppKey |
| 1\.0\.x | Uplink data message | NwkSKey |
| 1\.0\.x | Downlink data messages | NwkSKey |
| 1\.1 | Join\-request | NwkKey |
| 1\.1 | Join\-accept | JSIntKey |
| 1\.1 | Rejoin\-request Type 0 and 2 | SNwkSIntKey |
| 1\.1 | Rejoin\-request Type 1 | JSIntKey |
| 1\.1 | Uplink data messages | FNwkSIntKey and SNwkSIntKey |
| 1\.1 | Downlink data message | SNwkSIntKey |

When a LoRaWAN 1\.1 device is provisioned with a LoRaWAN 1\.0\.x Network Server, the MIC of each message is calculated as shown in the following table.

| **Message Type** | **Key** |
| --- | --- |
| Join\-request | NwkKey |
| Join\-accept | NwkKey |
| Uplink data messages | FNwkSIntKey |
| Downlink data messages | FNwkSIntKey |

## Practice Questions# Security

## Security Keys

LoRaWAN 1\.0 specifies a number of security keys: NwkSKey , AppSKey and AppKey . All keys have a length of 128 bits.
The algorithm used for this is AES\-128, similar to the algorithm used in the 802\.15\.4 standard.
### Session Keys

When a device joins the network (this is called a join or activation), an application session key AppSKey and a network session key NwkSKey are generated. The NwkSKey is shared with the network, while the AppSKey is kept private. These session keys will be used for the duration of the session.
The Network Session Key ( NwkSKey ) is used for interaction between the Node and the Network Server. This key is used to validate the integrity of each message by its Message Integrity Code (MIC check). This MIC is similar to a checksum, except that it prevents intentional tampering with a message. For this, LoRaWAN uses AES\-CMAC. In the backend of The Things Network this validation is also used to map a non\-unique device address ( DevAddr ) to a unique DevEUI and AppEUI .
The Application Session Key ( AppSKey ) is used for encryption and decryption of the payload. The payload is fully encrypted between the Node and the Handler/Application Server component of The Things Network (which you will be able to run on your own server). This means that nobody except you is able to read the contents of messages you send or receive.
These two session keys ( NwkSKey and AppSKey ) are unique per device, per session. If you dynamically activate your device (OTAA), these keys are re\-generated on every activation. If you statically activate your device (ABP), these keys stay the same until you change them.
### Application Key

The application key ( AppKey ) is only known by the device and by the application. Dynamically activated devices (OTAA) use the Application Key ( AppKey ) to derive the two session keys during the activation procedure. In The Things Network you can have a AppKey which will be used to activate all devices, or customize the AppKey per device.
## Frame Counters

Because we’re working with a radio protocol, anyone will be able to capture and store messages. It’s not possible to read these messages without the AppSKey , because they’re encrypted. Nor is it possible to tamper with them without the NwkSKey , because this will make the MIC check fail. It is however possible to re\-transmit the messages. These so\-called replay attacks can be detected and blocked using frame counters.
When a device is activated, these frame counters ( FCntUp and FCntDown ) are both set to 0 . Every time the device transmits an uplink message, the FCntUp is incremented and every time the network sends a downlink message, the FCntDown is incremented. If either the device or the network receives a message with a frame counter that is lower than the last one, the message is ignored.
This security measure has consequences for development devices, which often are statically activated (ABP). When you do this, you should realize that these frame counters reset to 0 every time the device restarts (when you flash the firmware or when you unplug it). As a result, The Things Network will block all messages from the device until the FCntUp becomes higher than the previous FCntUp . Therefore, you should re\-register your device in the backend every time you reset it.
## Spread Spectrum

Spread Spectrum Radio Transmission was traditionally used, during WW2, to make military communications difficult to monitor \- either by using a technique called ‘frequency hopping’ (FHSS) \- skipping the transmission frequency around in a prearranged manner, causing the enemy to constantly retune (very rapidly) or ‘direct sequence’ (DSSS) where the digital message is added to a much higher bit\-rate, pseudo random (PR) sequence. The code spreads the radio signal over a much wider bandwidth. In fact, so wide that the power may well be dispersed so that the total signal falls down into the background radio noise \- and becomes invisible. Recovery is therefore a matter of i) knowing the original radio frequency ii) the pseudo random code and iii) and the PR code bit rate. Knowing these details means that synchronising receivers is not as difficult as may at first appear. The signal will just ‘pop up’ out of the noise when the correct values are achieved. (‘Processing Gain’)
The technique used in LoRa is ‘ CHIRP ’: Compressed High Intensity Radar Pulse. It is even more complex but simple with current technology. As the name may suggest, the background design requirement, it is not used to hide the radio signal but is employed because of other factors, not just processing gain but interference immunity, channel sharing and resistance to radio reflections (amongst others). It is therefore employed as security against operating conditions not for surveillance resistance. (Hedy Lamarr was a co\-inventor and holds a patent for FHSS).# Device Classes

The LoRaWAN specification defines three device types: Class A , Class B , and Class C . All LoRaWAN devices must implement Class A, whereas Class B and Class C are extensions to the specification of Class A devices. All device classes support bi\-directional communication (uplink and downlink). During firmware upgrades over\-the\-air (FUOTA), a device must be switched to Class B or Class C.

##### Note:

 End devices can’t send uplink messages while they receive downlink messages.

## Class A

All LoRaWAN end\-devices must support Class A implementation. A Class A device can send an uplink message at any time. Once the uplink transmission is completed, the device opens two short receive windows for receiving downlink messages from the network. There is a delay between the end of the uplink transmission and the start of each receive window, known as RX1 Delay and RX2 Delay, respectively. If the network server does not respond during these two receive windows, the next downlink will be scheduled immediately after the next uplink transmission.

The network server can respond during the first receive window (RX1\) or the second receive window (RX2\), but does not use both windows. Let’s consider three situations for downlink messages as illustrated below.

Class A end devices have very low power consumption. Therefore, they can operate with battery power. They spend most of their time in sleep mode and usually have long intervals between uplinks. Additionally, Class A devices have high downlink latency, as they require sending an uplink to receive a downlink.
The following are some of the use cases for Class A end devices:
* Environmental monitoring
* Animal tracking
* Forest fire detection
* Water leakage detection
* Smart parking
* Asset tracking
* Waste management

## Class B

Class B devices extend Class A capabilities by periodically opening receive windows called ping slots to receive downlink messages. The network broadcasts a time\-synchronized beacon (unicast and multicast) periodically through the gateways, which is received by the end devices. These beacons provide a timing reference for the end devices, allowing them to align their internal clocks with the network. This allows the network server to know when to send a downlink to a specific device or a group of devices. The time between two beacons is known as the beacon period .
After an uplink, the two short receive windows, RX1 and RX2 will open similar to Class A devices.

Class B end devices have low latency for downlinks compared to Class A end devices because they periodically open ping slots. However, they have much higher latency than the Class C end devices. Class B devices are often battery powered. The battery life is shorter in Class B compared to Class A because the devices spend more time in active mode due to receiving beacons and having open ping slots. Because of the low latency for downlinks, Class B mode can be used in devices that require medium\-level critical actuation, such as utility meters.
The following are some of the use cases for Class B end devices:
* Utility meters (electrical meters, water meters, etc)
* Street lights

Class B devices can also operate in Class A mode.
## Class C

Class C devices extend Class A capabilities by keeping the receive windows open unless transmitting an uplink, as shown in the figure below. Therefore, Class C devices can receive downlink messages at almost any time, thus having very low latency for downlinks. These downlink messages can be used to activate certain functions of a device, such as reducing the brightness of a street light or turning on the cut\-off valve of a water meter.
Class C devices open two receive windows, RX1 and RX2, similar to Class A. However, the RX2 receive window remains open until the next uplink transmission. After the device sends an uplink, a short RX2 receive window opens, followed by a short RX1 receive window, and then the continuous RX2 receive window opens. This RX2 receive window remains open until the next uplink is scheduled. Uplinks are sent when there is no downlink in progress.

Compared to Class A and Class B devices, Class C devices have the lowest latency. However, they consume more power due to the need for opening continuous receive slots. As a result, these devices cannot be operated with batteries for long time therefore they are often mains powered.
The following are some of the use cases for Class C end devices:
* Utility meters (electrical meters, water meters, etc)
* Street lights
* Beacon lights
* Alarms

Class C devices can also operate in Class A mode.

1. Which end device class consumes the lowest power?
	* Class A
	* Class B
	* Class C
2. Which end device class consumes the highest power?
	* Class A
	* Class B
	* Class C
3. Which end device class usually runs on mains power?
	* Class A
	* Class B
	* Class C
4. What does RX1 Delay mean?
	* The delay between the end of the uplink transmission and the start of the RX1 receive window.
	* The delay between the end of the uplink transmission and the start of the RX2 receive window.
	* The delay between the end of the RX1 and the end of the RX2 receive windows.
	* The delay between the start of the RX1 and the start of the RX2 receive windows.
5. Which device class has the lowest downlink latency?
	* Class A
	* Class B
	* Class C
6. Which device class has the highest downlink latency?
	* Class A
	* Class B
	* Class C
7. Which device class is synchronized to the network using periodic beacons?
	* Class A
	* Class B
	* Class C
8. Which device class only can receive a downlink message after sending an uplink message?
	* Class A
	* Class B
	* Class C# End Device Activation

Every end device must be registered with a network before sending and receiving messages. This procedure is known as activation . There are two activation methods available:
* **Over\-The\-Air\-Activation (OTAA)** \- the most secure and recommended activation method for end devices. Devices perform a join procedure with the network, during which a dynamic device address is assigned and security keys are negotiated with the device.
* **Activation By Personalization (ABP)** \- requires hardcoding the device address as well as the security keys in the device. ABP is **less secure** than OTAA and also has the downside that devices can not switch network providers without manually changing keys in the device.

The join procedure for LoRaWAN 1\.0\.x and 1\.1 is slightly different. The following two sections describe the join procedure for LoRaWAN 1\.0\.x and 1\.1 separately.

##### Info:

 For more information on the differences between OTAA and ABP, check the [The Things Stack documentation](https://www.thethingsindustries.com/docs/the-things-stack/concepts/data-formats/).

## Over The Air Activation in LoRaWAN 1\.0\.x

In LoRaWAN 1\.0\.x, the join procedure requires two MAC messages to be exchanged between the end device and the Network Server:
* Join\-request \- from end device to the Network Server
* Join\-accept \- from Network Server to the end device

Before activation, the AppEUI , DevEUI , and AppKey should be stored in the end device. The AppKey is an AES\-128 bit secret key known as the root key . The same AppKey should be provisioned onto the network where the end device is going to register. The AppEUI and DevEUI are not secret and are visible to everyone.

##### Note:

 The **AppKey** is **never sent** over the network.

The following steps describe the Over\-The\-Air\-Activation (OTAA) procedure.

##### Step 1

The join procedure is always initiated by the end device. The end device sends the Join\-request message to the network that is going to be joined. The Join\-request message consists of the following fields.

| **8 bytes** | **8 bytes** | **2 bytes** |
| --- | --- | --- |
| AppEUI | DevEUI | DevNonce |

* **AppEUI** – a 64\-bit globally unique application identifier in IEEE EUI64 address space that uniquely identifies the entity able to process the Join\-req frame.
* **DevEUI** – a 64\-bit globally unique device identifier in IEEE EUI64 address space that uniquely identifies the end\-device.
* **DevNonce** – a unique, random, 2\-byte value generated by the end device. The Network Server uses the DevNonce of each end\-device to keep track of their join requests. If an end device sends a Join\-request with a previously used DevNonce (this situation is known as a replay attack), the Network Server **rejects** the Join\-request and does not allow that end device to register with the network.

The Message Integrity Code (MIC) is calculated over all the fields in the Join\-request message using the AppKey . The calculated MIC is then added to the Join\-request message.

##### Note:

 The **AppKey** is not sent with the **Join\-request** message, and the **Join\-request** message is **not encrypted**.

The Join\-request message can be transmitted using any data rate and using one of the region\-specific join channels. For example, in Europe an end device can transmit the Join\-request message by randomly choosing among 868\.10 MHz, 868\.30 MHz, or 868\.50 MHz. The Join\-request message travels through one or more gateways to the Network Server.
##### Step 2

The Network Server processes the Join\-request message. The Network Server will generate two session keys (NwkSKey and AppSKey) and the Join\-accept message if the end\-device is permitted to join a network.
The Join\-accept message consists of the following fields.

| **3 bytes** | **3 bytes** | **4 bytes** | **1 bytes** | **1 bytes** | **16 bytes (optional)** |
| --- | --- | --- | --- | --- | --- |
| AppNonce | NetID | DevAddr | DLSettings | RXDelay | CFList |

* **AppNonce** – a random value or unique ID provided by the Network Server. The AppNonce is used by the end device to derive the two session keys, **AppSKey** and **NwkSKey**.
* **NetID** – consists of the network identifier (NwkID), the most significant 7 bits.
* **DevAddr** – a 32\-bit device address assigned by the Network Server to identify the end device within the current network.
* **DLSettings** – a 1\-byte field consisting of downlink settings which the end device should use.
* **RxDelay** – contains the delay between TX and RX.
* **CFList** – an optional list of channel frequencies for the network the end\-device is joining. These frequencies are region\-specific.

The Message Integrity Code (MIC) is calculated over all the fields in the Join\-accept message using the AppKey . The calculated MIC is then added to the Join\-accept message.
The Join\-accept message itself is then encrypted with the AppKey . The Network Server uses an AES decrypt operation in ECB mode to encrypt the Join\-accept message.
##### Step 3

The Network Server sends the encrypted Join\-accept message back to the end device as a normal downlink.

##### Note:

 No response is given to the end\-device if the **Join\-request** message is not accepted by the Network Server.

##### Step 4

The Network Server keeps the NwkSKey and distributes the AppSKey to the Application Server.
##### Step 5

The end device decrypts the Join\-accept message using AES encrypt operation. The end device uses the AppKey and AppNonce to derive the two session keys, the Network Session Key (NwkSKey) and the Application Session Key (AppSKey) .
The end device is now activated on the Network.
After activation, the following additional information is stored in the end device.
* **DevAddr** \- a 32\-bit device address assigned by the Network Server to identify the end device within the current network.
* **NwkSKey** \- the network session key is used by the end device and Network Server to calculate and verify the Message Integrity Code (MIC) of all data messages for ensuring message integrity. The NwkSKey is also used to encrypt and decrypt payloads with MAC commands.
* **AppSKey** \- the application session key is used to encrypt and decrypt application payloads in data messages for ensuring message confidentiality.

## Over\-The\-Air\-Activation in LoRaWAN 1\.1

In LoRaWAN 1\.0\.x, the join procedure requires two MAC messages to be exchanged between the end device and the Join Server:
* Join\-request \- from end device to the Join Server
* Join\-accept \- from Join Server to the end device

Before activation, the JoinEUI , DevEUI , AppKey , and NwkKey should be stored in the end device. The AppKey and NwkKey are AES\-128 bit secret keys known as root keys . The matching AppKey , NwkKey , and DevEUI should be provisioned onto the Join Server that will assist in the processing of the join procedure and session key derivation. The JoinEUI and DevEUI are not secret and visible to everyone.

##### Note:

 The **AppKey** and **NwkKey** are never sent over the network.

The following steps describe the Over\-The\-Air\-Activation (OTAA) procedure.

##### Step 1

The join procedure is always initiated by the end device. The end device sends the Join\-request message to the network that is going to be joined. The Join\-request message consists of the following fields.

| **8 bytes** | **8 bytes** | **2 bytes** |
| --- | --- | --- |
| JoinEUI | DevEUI | DevNonce |

* **JoinEUI** – a 64\-bit global application identifier in IEEE EUI64 address space that uniquely identifies the **Join Server** that can assist in the processing of the Join\-request and derivation of the session keys.
* **DevEUI** – a 64\-bit global device identifier in IEEE EUI64 address space that uniquely identifies the end\-device.
* **DevNonce** – a 2\-byte counter, starting at 0 when the device is initially powered up and incremented with every **Join\-request**. The DevNonce value is used to prevent **replay attacks**.

##### Note:

 In LoRaWAN 1\.1 **AppEUI** is replaced with the **JoinEUI**.

The MIC is calculated over all the fields in the Join\-request message using the NwkKey . The calculated MIC is then added to the Join\-request message.

##### Note:

 The **NwkKey** is not sent with the **Join\-request** message, and the **Join\-request** message is not encrypted but sent as plain text.

The Join\-request message can be transmitted using any data rate and using one of the region\-specific join channels. For example, in Europe an end device can transmit the Join\-request message by randomly choosing among 868\.10 MHz, 868\.30 MHz, or 868\.50 MHz. The Join\-request message travels through one or more gateways to the Network Server.

##### Note:

 No response is given to the end\-device if the **Join\-request** is not accepted.

##### Step 2

The Network Server forwards the Join\-request message to the corresponding Join Server.
##### Step 3

The Join Server processes the Join\-request message. The Join Server will generate all the session keys (AppSKey, FNwkSIntKey, SNwkSIntKey, and NwkSEncKey) if the end\-device is permitted to join the network.
##### Step 4

If the above step gets success, the Network Server generates the Join\-accept message. The Join\-accept message consists of the following fields.

| **1 byte** | **3 bytes** | **4 bytes** | **1 bytes** | **1 bytes** | **16 bytes** |
| --- | --- | --- | --- | --- | --- |
| JoinNonce | NetID | DevAddr | DLSettings | RXDelay | CFList |

* **JoinNonce** – a device specific counter value provided by the Join Server and used by the end device to derive the session keys, **FNwkSIntKey**, **SNwkSIntKey**, **NwkSEncKey**, and **AppSKey**.
* **NetID** – a 24\-bit unique network identifier.
* **DevAddr** – a 32\-bit device address assigned by the Network Server to identify the end device within the current network.
* **DLSettings** – a 1\-byte field consisting of downlink settings which the end device should use.
* **RxDelay** – contains delay between TX and RX
* **CFList** – an optional list of channel frequencies for the network the end\-device is joining. These frequencies are region\-specific.

The Message Integrity Code (MIC) is calculated over all the fields in the Join\-accept message using NwkKey (for LoRaWAN 1\.0 devices) or JSIntKey (for LoRaWAN 1\.1 devices) . The calculated MIC is then added to the Join\-accept message.
The Join\-accept message itself is then encrypted with the NwkKey. The Network Server uses an AES decrypt operation in ECB mode to encrypt the join\-accept message.
The Join\-accept message is encrypted with the NwkKey (if triggered by Join\-request) or JSEncKey (if triggered by Rejoin\-request).
Then the Network Server sends the encrypted Join\-accept message back to the end device as a normal downlink.

##### Note:

 No response is given to the end\-device if the **Join\-request** message is not accepted by the Network Server.

##### Step 5

The Join Server sends the AppSKey to the Application Server and the three network session keys (FNwkSIntKey, SNwkSIntKey, and NwkSEncKey) to the Network Server.
##### Step 6

The end\-device decrypts the Join\-accept message using AES encrypt operation. The end device uses AppKey, NwkKey, and JoinNonce to generate session keys.
For LoRaWAN 1\.0\.x devices,
* AppSKey is derived from the NwkKey.
* FNwkSIntKey, SNwkSIntKey, and NwkSEncKey are derived from the NwkKey.

For LoRaWAN 1\.1 devices,
* AppSKey is derived from AppKey.
* FNwkSIntKey, SNwkSIntKey, and NwkSEncKey are derived from the NwkKey.

The end device is now activated on the Network.
After activation, the following additional information is stored in the end device.
* **DevAddr** \- a 32\-bit device address assigned by the Network Server to identify the end device within the current network.
* **FNwkSIntKey** \- a network session key that is used by the end device to calculate the MIC (partially) of all uplink data messages for ensuring message integrity.
* **SNwkSIntKey** \- a network session key that is used by the end device to calculate the MIC (partially) of all uplink data messagse and calculate the MIC of all downlink data messages for ensuring message integrity.
* **NwkSEncKey** \- a network session key that is used to encrypt and decrypt the payloads with MAC commands of the uplink and downlink data messages for ensuring message confidentiality.
* **AppSKey** \- a session key used by both the Application Server and the end device to encrypt and decrypt the application data in the data messages for ensuring message confidentiality.

## Activation By Personalization

Activation By Personalization (ABP) directly ties an end\-device to a pre\-selected network, bypassing the over\-the\-air\-activation procedure. Activation by Personalization is the less secure activation method, and also has the downside that devices can not switch network providers without manually changing keys in the device. A Join Server is not involved in the ABP process.
An end device activated using the ABP method can only work with a single network and keeps the same security session for its entire lifetime.
### Activation By Personalisation in LoRaWAN 1\.0\.x

The DevAddr and the two session keys NwkSKey and AppSKey are directly stored into the end\-device instead of the DevEUI, AppEUI, and the AppKey. Each end device should have a unique set of NwkSKey and AppSkey. The same DevAddr and NwkSKey should be stored in the Network Server and the AppSKey should be stored in the Application Server

### Activation By Personalisation in LoRaWAN 1\.1

The DevAddr and the four\-session keys FNwkSIntKey , SNwkSIntKey , NwkSEncKey , and AppSKey are directly stored into the end device instead of the DevEUI, JoinEUI, AppKey, and NwkKey. The same DevAddr , FNwkSIntKey , SNwkSIntKey , and NwkSEncKey should be stored in the Network Server and the and AppSKey should be stored in the Application Server.# Spreading Factors

LoRa is based on Chirp Spread Spectrum (CSS) technology, where chirps (also known as symbols) are the carrier of data.
The spreading factor controls the chirp rate, and thus controls the speed of data transmission. Lower spreading factors mean faster chirps and therefore a higher data transmission rate . For every increase in spreading factor, the chirp sweep rate is halved, and so the data transmission rate is halved.
For a visual explanation, see this video on LoRa chirps.
Lower spreading factors reduce the range of LoRa transmissions, because they reduce the processing gain and increase the bit rate. Changing spreading factor allows the network to increase or decrease data rate for each end device at the cost of range.
The network also uses spreading factors to control congestion. Spreading factors are orthogonal, so signals modulated with different spreading factors and transmitted on the same frequency channel at the same time do not interfere with each other.
### Influence of Spreading Factors

LoRa modulation has a total of 6 spreading factors from SF7 to SF12\. Spreading factors influence data rate, time\-on\-air, battery life, and receiver sensitivity, as described here.
#### Data rate

Compared to a higher spreading factor, a lower spreading factor provides a higher bit rate for a fixed bandwidth and coding rate. For example, SF7 provides a higher bit rate than SF12\.
Doubling the bandwidth also doubles the bit rate for a fixed spreading factor and coding rate.
The following table presents bit rates calculated with the SF7 and Coding Rate (CR) \= 1 for bandwidths, 125, 250, and 500 kHz.

| **Spreading Factor** | **Bandwidth** | **Bit rate (kbits/s)** |
| --- | --- | --- |
| 7 | 125 | 5\.5 |
| 7 | 250 | 10\.9 |
| 7 | 500 | 21\.9 |

#### Distance

Larger spreading factors mean larger processing gain, and so a signal modulated with a larger spreading factor can be received with less errors compared to a signal with a lower spreading factor, and therefore travel a longer distance. For example, a signal modulated with the SF12 can travel a longer distance than a signal modulated with the SF7\.
#### Time\-On\-Air

Compared to a lower spreading factor, sending a fixed amount of data (payload) with a higher Spreading Factor and a fixed bandwidth needs longer time\-on\-air.
The Things Network’s LoRaWAN airtime calculator can be used to calculate the time\-on\-air using input bytes (payload size), bandwidth, and spreading factor. TTN’s LoRaWAN airtime calculator can be accessed here .
#### Receiver Sensitivity

Higher spreading factors provide higher receiver sensitivity. Usually, LoRa uses higher spreading factors when the signal is weak.
The following table shows how spreading factors impact the receiver sensitivity.

| **Spreading factor** | **Receiver sensitivity for bandwidth fixed at 125 kHz** |
| --- | --- |
| SF7 | \-123 dBm |
| SF8 | \-126 dBm |
| SF9 | \-129 dBm |
| SF10 | \-132 dBm |
| SF11 | \-134\.5 dBm |
| SF12 | \-137 dBm |

#### Battery Life

The battery life of an end device is highly dependent on the spreading factor used. Higher spreading factors result in longer active times for the radio transceivers and shorter battery life.

* SF9
* SF10
* SF11
* SF12

2. Which spreading factor provides the highest bit rate?

* SF7
* SF8
* SF9
* SF10

3. Which spreading factor provides the longest battery life for an end device?

* SF7
* SF8
* SF9
* SF10

4. For the same amount of data and bandwidth, which spreading factor results in the longest time\-on\-air?

* SF7
* SF8
* SF9
* SF10# Adaptive Data Rate

Adaptive Data Rate (ADR) is a mechanism for optimizing data rates, airtime and energy consumption in the network.
The ADR mechanism controls the following transmission parameters of an end device.
* Spreading factor
* Bandwidth
* Transmission power

ADR can optimize device power consumption while ensuring that messages are still received at gateways. When ADR is in use, the network server will indicate to the end device that it should reduce transmission power or increase data rate. End devices which are close to gateways should use a lower spreading factor and higher data rate, while devices further away should use a high spreading factor because they need a higher link budget.
ADR should be enabled whenever an end device has sufficiently stable RF conditions. This means that it can generally be enabled for static devices. If the static end device can determine that RF conditions are unstable (for example, when a car is parked on top of a parking sensor), ADR should (temporarily) be disabled.
Mobile end devices should be able to detect when they are stationary for a longer times, and enable ADR during those times. End devices decide if ADR should be used or not, not the application or the network.
## ADR in The Things Stack

##### Info:

 Check [The Things Stack documentation](https://www.thethingsindustries.com/docs/reference/adr/#how-adr-works) for more specifics on how ADR works on the The Things Stack.

To determine the optimal data rate, the network needs some measurements (uplink messages). Currently The Things Stack takes the 20 most recent uplinks, starting at the moment the ADR bit is set. These measurements contains the frame counter, signal\-to\-noise ratio (SNR) and number of gateways that received each uplink. When a device unsets the ADR bit (because it knows it is moving or it knows RF conditions are unstable), previous measurements are discarded. As soon as the ADR bit is set again, the network starts measuring again.
For each of these measurements, we take the SNR of the best gateway, and we calculate the so\-called “margin”, which is the measured SNR minus the required SNR to demodulate a message given the data rate. This margin is used to determine how much we can increase the data rate or lower the transmit power. For example, when the network receives a message with data rate SF12BW125 and SNR 5\.0 , that message has a margin of 25 dB. This is a waste of valuable airtime and energy. If we would increase the data rate to SF7BW125 we would still have a margin of 12\.5 dB, but that would be many times more airtime\- and energy efficient. We could even lower the transmit power to save even more energy and cause less interference.
There are a several moments when an ADR request is scheduled or sent:

ADR requests are no longer scheduled or sent if the device refused several ADR requests. This could either mean a bad implementation of the device, or a version mismatch between the device and the server.
The algorithm used in The Things Network is based on Semtech’s recommended algorithm for rate adaptation. The following diagram outlines the ADR flow as implemented in The Things Stack:

1. The Adaptive Data Rate is suitable for
	* Static end devices
	* Mobile end devices
2. The end devices located close to a gateway should use a
	* Lower data rate
	* Higher data rate
3. The end devices located several kilometers from a gateway should use a
	* Lower data rate
	* Higher data rate
4. A higher data rate means,
	* A lower spreading factor
	* A higher spreading factor
5. Which of the following end devices should not implement ADR?
	* Environmental sensor
	* Water leakage detector
	* Pet tracker
	* Gas detector# Limitations

LoRaWAN is not suitable for every use\-case, so it is important that you understand the limitations. Here’s a quick overview:
#### Suitable use\-cases for LoRaWAN:

* **Long range** \- multiple kilometers
* **Low power** \- can last years on a battery
* **Low cost** \- less than 20€ CAPEX per node, almost no OPEX
* **Low bandwidth** \- between 250bit/s and 11kbit/s in Europe using LoRa modulation (depending on the spreading factor)
* **Coverage everywhere** \- you are the network! Just install your own gateways
* **Secure** \- 128bit end\-to\-end encrypted

#### Not Suitable for LoRaWAN:

* **Realtime data** \- you can only send small packets every couple of minutes
* **Phone calls** \- you can do that with GPRS/3G/LTE
* **Controlling lights in your house** \- check out ZigBee or BlueTooth
* **Sending photos, watching Netflix** \- check out WiFi

## Sending data from a Node to your Application (uplink)

We want you to create products that are as efficient as possible. This will get the most out of your battery, and doesn’t require you to buy many gateways. If you follow these recommendations, you’ll definitely build an amazing product!
* **Payload** should be as small as possible. This means that you **should not send JSON or plain (ASCII) text**, but instead encode your data as binary data. This is made really easy with the [Cayenne Low Power Payload](/docs/devices/arduino/api/cayennelpp/) format which is fully supported by The Things Network.
* **Interval** between messages should be in the range of **several minutes**, so be smart with your data. You could for example transmit a `min|avg|max` every 5 minutes, or you could only transmit when you sensor value changed more than a certain threshold or have it triggered by motion or another event.
* **Data Rate** should be as fast as possible to minimize your airtime. `SF7BW125` is usually a good place to start, as it consumes the least power and airtime. If you need more range, you can slowly increase until you have enough. You can also enable adaptive data rate (ADR), the network will then be able to automatically optimize your data rate.

## Sending responses from your Application to your Node (downlink)

We want to be able to handle as many Nodes as possible per Gateway. But as full\-duplex radios are not widely available yet, a Gateway is not able to receive transmissions from Nodes while it is transmitting. This means that if a gateway is transmitting 10% of the time, it’s not able to receive anything for that 10% of the time. This is even worse when you realize that a gateway can receive at 8 channels simultaneously. Except when it’s transmitting. So while an idle gateway can receive transmissions from 8 devices, those 8 devices are worthless when the gateway is transmitting.
We want to build a network that offers high reliability. If your device transmits, the gateway should receive it. In order to keep the gateway availability as high as we can, we ask you to follow these recommendations.
* **Data Rate** should be, just as with uplink, as efficient as possible. The downlink data rate is based on the uplink data rate, so if you send efficient uplinks, the network will respond with efficient downlinks.
* **Downlink** messages should be avoided if possible, and if you send downlink, keep the payload small.
* **Confirmed Uplink** is often not necessary. Try to make your application work without confirmations.# Frequency Plans by Country

This document is only a summary of radio regulations, and the appropriate frequency plans that should be used for The Things Network in the respective countries. This is in no way an official document; gateway owners are still obliged to find, study and adhere to their own country’s regulations. You can also read the LoRa Alliance LoRaWAN Regional Parameters . Some countries also expect you to register your gateway, or obtain a license. In that case you are using a “free band”, not a “license free band”. In some countries it is also necessary that the gateway is certified (CE, FCC, …) if you allow other people to also communicate via it.
For discussions about the frequency plans in different countries, see the posts on the forum tagged with Country/Frequency\-Plan .

### A

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Afghanistan |  |  |
| Albania | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Algeria |  | [CONDITIONS D’UTILISATION DES EQUIPEMENTS D’IDENTIFICATION PAR RADIOFREQUENCES \- RFID](http://www.anf.dz/pdf/caf/RFID.pdf) |
| Andorra | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Angola | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Antigua and Barbuda |  |  |
| Argentina | AU915\-928 | [RESOL\-2018\-581\-APN\-MM](https://www.enacom.gob.ar/multimedia/normativas/2018/res581MM.pdf) |
| Armenia |  | EN 302 208 |
| Australia | AU915\-928 |  |
| Austria | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Azerbaijan | unknown, no CEPT | EN 302 208, CEPT Rec. 70\-03 |

### B

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Bahamas |  |  |
| Bahrain | EU863\-870EU433 | [Kingdom Of Bahrain National Frequency Plan](http://www.tra.org.bh/media/document/The%202009%20National%20Frequency%20Plan.pdf) |
| Bangladesh |  |  |
| Barbados |  |  |
| Belarus | unknown, limited CEPT | CEPT Rec. 70\-03 |
| Belgium | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Belize |  |  |
| Benin |  |  |
| Bhutan |  |  |
| Bolivia | US902\-928 |  |
| Bosnia and Herzegovina | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Botswana | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Brazil | AU915\-928 | [National Telecommunications Agency (ANATEL) Resolution No. 680, from June 27, 2017 \- Portuguese only](http://www.anatel.gov.br/legislacao/resolucoes/2017/936-resolucao-680), Article 10  [National Telecommunications Agency (ANATEL) Act No. 14448, from December 4, 2017 \- Portuguese only](http://www.anatel.gov.br/legislacao/atos-de-requisitos-tecnicos-de-certificacao/2017/1139-ato-14448) Section 10\.3 |
| Brunei | AS923\-925 (“AS2”) |  |
| Bulgaria | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Burkina Faso |  |  |
| Burundi |  |  |

### C

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Cabo Verde |  |  |
| Cambodia | AS923\-925 (“AS2”) |  |
| Cameroon |  |  |
| Canada | US902\-928 |  |
| Central African Republic (CAR) |  |  |
| Chad |  |  |
| Chile | AU915\-928 | [FIJA NORMA TECNICA DE EQUIPOS DE ALCANCE REDUCIDO](https://www.leychile.cl/Consulta/m/norma_plana?org=&idNorma=240404) |
| China | CN470\-510CN779\-787 |  |
| Colombia | US902\-928 |  |
| Comoros |  |  |
| Democratic Republic of the Congo | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Republic of the Congo |  |  |
| Costa Rica | US902\-928 |  |
| Cote d’Ivoire |  |  |
| Croatia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Cuba |  |  |
| Curaçao |  | [Ministeriële regeling vrijstelling telecommunicatiemachtiging 2015](http://btnp.org/images/stories/pdf/telecom/PB_20153.pdf) |
| Cyprus | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Czech Republic | EU863\-870EU433 | CEPT Rec. 70\-03 |

### D

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Denmark | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Djibouti |  |  |
| Dominica |  |  |
| Dominican Republic | US902\-928 |  |

### E

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Ecuador | AU915\-928 | [Plan Nacional de Frecuencia 2021 (p.59\)](https://www.arcotel.gob.ec/wp-content/uploads/2021/10/PNF-V.6.0_14-07-21_v.1.pdf) ARCOTEL |
| Egypt |  |  |
| El Salvador |  |  |
| Equatorial Guinea |  |  |
| Eritrea |  |  |
| Estonia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Eswatini (formerly Swaziland) | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Ethiopia |  |  |

### F

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Fiji |  |  |
| Finland | EU863\-870EU433 | CEPT Rec. 70\-03 |
| France | EU863\-870EU433 | CEPT Rec. 70\-03 |

### G

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Gabon |  |  |
| Gambia |  |  |
| Georgia | unknown, limited CEPT | CEPT Rec. 70\-03 |
| Germany | EU863\-870EU433 | [Non\-specific Short Range Devices (SRD) regulations](http://www.bnetza.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Allgemeinzuteilungen/2018_05_SRD_pdf.html), CEPT Rec. 70\-03 |
| Ghana |  |  |
| Greece | EU863\-870EU433 | [Radio frequency regulations](http://www.eett.gr/opencms/export/sites/default/admin/downloads/Announcments/AP399_034.pdf), [433MHz SRD regulations](http://www.eett.gr/opencms/export/sites/default/EETT/Electronic_Communications/Radio_Communications/TelecommunicationsEquipment/104v2.pdf), [868MHz SRD regulations](http://www.eett.gr/opencms/export/sites/default/EETT/Electronic_Communications/Radio_Communications/TelecommunicationsEquipment/105v2.pdf), CEPT Rec. 70\-03 |
| Grenada |  |  |
| Guatemala |  |  |
| Guinea |  |  |
| Guinea\-Bissau |  |  |
| Guyana | US902\-928 |  |

### H

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Haiti |  |  |
| Honduras |  |  |
| Hong Kong (different than China) | AS923\-925 (“AS2”) |  |
| Hungary | EU863\-870EU433 | CEPT Rec. 70\-03 |

### I

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Iceland | EU863\-870EU433 | CEPT Rec. 70\-03 |
| India | IN865\-867 | [Use of low power wireless equipments in the frequency band 865\-867MHz for RFID](http://www.wpc.gov.in/WriteReadData/userfiles/file/RFID%20Delicensing.doc) |
| Indonesia | AS923\-925 (“AS2”) |  |
| Iran |  | EN 302 208 |
| Iraq |  |  |
| Ireland | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Israel |  | EN 302 208 |
| Italy | EU863\-870EU433 | CEPT Rec. 70\-03 |

### J

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Jamaica |  |  |
| Japan | AS920\-923 (“AS1”) | [ARIB STD\-T108](https://www.arib.or.jp/english/html/overview/doc/5-STD-T108v1_0-E1.pdf) |
| Jordan |  |  |

### K

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Kazakhstan |  |  |
| Kenya |  |  |
| Kiribati |  |  |
| Kosovo |  |  |
| Kuwait |  |  |
| Kyrgyzstan |  |  |

### L

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Laos | AS923\-925 (“AS2”) |  |
| Latvia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Lebanon |  |  |
| Lesotho | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03, [Radio Spectrum Management Guidelines and Procedures 2014](http://www.lca.org.ls/images/documents/Radio%20Spectrum%20Management%20Guidelines%20and%20Procedures_2014.pdf) |
| Liberia |  |  |
| Libya |  |  |
| Liechtenstein | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Lithuania | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Luxembourg | EU863\-870EU433 | CEPT Rec. 70\-03 |

### M

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Madagascar | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Malawi | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Malaysia | AS920\-923 (“AS1”) |  |
| Maldives |  |  |
| Mali |  |  |
| Malta | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Marshall Islands |  |  |
| Mauritania |  |  |
| Mauritius | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Mexico | US902\-928 |  |
| Micronesia |  |  |
| Moldova | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Monaco |  |  |
| Mongolia |  |  |
| Montenegro | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Morocco |  | [Decision ANRT/DG/Nº08/13 \- 20th June 2013](https://www.anrt.ma/sites/default/files/2013-08-13-condit-tech-install-radioelect-app-faible-puissance-fr.pdf) |
| Mozambique | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Myanmar (Burma) |  |  |

### N

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Namibia | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Nauru |  |  |
| Nepal |  |  |
| Netherlands | EU863\-870EU433 | [Regeling gebruik van frequentieruimte zonder vergunning en zonder meldingsplicht 2015](http://wetten.overheid.nl/BWBR0036378/2016-12-28), CEPT Rec. 70\-03 |
| New Zealand | AU915\-928 | [Radio Spectrum Management](https://www.rsm.govt.nz/about-rsm/spectrum-policy/gazette/gurl/short-range-devices) |
| Nicaragua |  |  |
| Niger |  |  |
| Nigeria |  |  |
| North Macedonia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| North Korea |  |  |
| Norway | unknown, limited CEPT | CEPT Rec. 70\-03 |

### O

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Oman |  | EN 302 208 |

### P

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Pakistan |  |  |
| Palau |  |  |
| Palestine |  |  |
| Panama | US902\-928 |  |
| Papua New Guinea |  |  |
| Paraguay | US902\-928 |  |
| Peru | US902\-928 |  |
| Philippines | EU863\-870EU433 | **NOTE:** This is not a license free band. If you connect to a commercial telecoms operator you are however allowed to use thier frequencies. Please check the rules and obtain a license before running a gateway. |
| Poland | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Portugal | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Puerto Rico | US902\-928 |  |

### Q

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Qatar |  |  |

### R

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Romania | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Russia | EU863\-870EU433 | CEPT Rec. 70\-03, [Decision ГКРЧ 07\-20\-03\-001](http://minsvyaz.ru/ru/documents/4039/), Appendix 10 |
| Rwanda |  |  |

### S

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Saint Kitts and Nevis |  |  |
| Saint Lucia |  |  |
| Saint Vincent and the Grenadines |  |  |
| Samoa |  |  |
| San Marino |  |  |
| Sao Tome and Principe |  |  |
| Saudi Arabia | EU863\-870EU433 | [National frequency plan in the kingdom of Saudi Arabia](http://www.citc.gov.sa/en/RulesandSystems/RegulatoryDocuments/FrequencySpectrum/Documents/SM%20002%20E-NFP.pdf) |
| Senegal |  |  |
| Serbia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Seychelles | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Sierra Leone |  |  |
| Singapore | AS920\-923 (“AS1”) |  |
| Slovakia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Slovenia | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Solomon Islands |  |  |
| Somalia |  |  |
| South Africa | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03, [The Radio Frequency Spectrum Regulations 2015](https://www.icasa.org.za/uploads/files/Radio-Frequency-Spectrum-Regulations-2015.pdf), [Amendment December 2021](https://www.gov.za/sites/default/files/gcis_document/202112/45690gen737.pdf) |
| South Korea | KR920\-923 |  |
| South Sudan |  |  |
| Spain | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Sri Lanka |  |  |
| Sudan |  |  |
| Suriname | US902\-928 |  |
| Sweden | EU863\-870EU433 | [Svenska frekvensplanen](https://etjanster.pts.se/radio/frekvensplanen), CEPT Rec. 70\-03 |
| Switzerland | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Syria |  |  |

### T

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Taiwan | AS923\-925 (“AS2”) | [LP0002 2016](http://www.rootlaw.com.tw/Attach/L-Doc/A040110071000200-1050823-1000-001.pdf) or [LP0002 2011](http://www.ncc.gov.tw/chinese/law_detail.aspx?site_content_sn=3441&is_history=0&sn_f=1807), section 4, “Radio Frequency Identification, RFID” |
| Tajikistan |  |  |
| Tanzania | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Thailand | AS923\-925 (“AS2”) |  |
| Timor\-Leste |  |  |
| Togo |  |  |
| Tonga |  |  |
| Trinidad and Tobago |  |  |
| Tunisia |  | EN 302 208 |
| Turkey | EU863\-870EU433 | CEPT Rec. 70\-03 |
| Turkmenistan |  |  |
| Tuvalu |  |  |

### U

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Uganda |  |  |
| Ukraine | unknown, limited CEPT | CEPT Rec. 70\-03 |
| United Arab Emirates (UAE) | EU863\-870EU433 | EN 302 208, [TRA Regulations](https://www.tra.gov.ae/assets/YXsb1a9i.pdf.aspx) |
| United Kingdom (UK) | EU863\-870EU433 | [Forum thread about requirements](https://www.thethingsnetwork.org/forum/t/uk-legal-requirements-for-equipment/6239), CEPT Rec. 70\-03 |
| United States of America (USA) | US902\-928 |  |
| Uruguay | US902\-928 |  |
| Uzbekistan |  |  |

### V

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Vanuatu |  |  |
| Vatican City (Holy See) | EU863\-870EU433 |  |
| Venezuela | US902\-928 |  |
| Vietnam | AS923\-925 (“AS2”) |  |

### Y

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Yemen |  |  |

### Z

| Country | Frequency Plan | Regulatory document |
| --- | --- | --- |
| Zambia | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |
| Zimbabwe | EU863\-870EU433 | CRASA follows CEPT Rec. 70\-03 |

### Regulatory Documents

CEPT/ERC Recommendation 70\-03 relating to the use of short range devices (SRD)
Already implemented in: Albania, Andorra, Austria, Belgium, Bosnia \& Herzegovina, Bulgaria, Cyprus, Czech Republic, Germany, Denmark, Spain, Estonia, France, Finland, United Kingdom, Hungary, Netherlands, Croatia, Italy, Ireland, Iceland, Liechtenstein, Lithuania, Luxembourg, Latvia, Moldova, Former Yugoslav Republic of Macedonia, Malta, Montenegro, Poland, Portugal, Romania, Sweden, Serbia, Switzerland, Slovak Republic, Slovenia, Turkey
Limited implementation: Belarus, Georgia(433\), Greece, Norway, Russian Federation, Ukrain
Not implemented in: Azerbaijan, Georgia(868\)

---

Communications Regulators' Association of Southern Africa (CRASA) Harmonised Frequency Bands For SRD Applications
Angola, Botswana, Democratic Republic of Congo, Lesotho, Malawi, Mauritius, Mozambique, South Africa, Namibia, Swaziland, Tanzania, Zambia, Zimbabwe.
Even though there is an overlap between the Southern African Development Community (SADC) and CRASA, the Seychelles and Madagascar are not members of CRASA. They are however included in the SADC Frequency allocation plan: SADC Frequency Allocation Plan# Frequency Plans

This is a list of frequency plan definitions used in The Things Network. These frequency plans are based on what is specified in the LoRaWAN regional parameters document. To know which frequency plan to use in your country, see the list of frequency plans by country list .
## EU863\-870

Uplink:

Downlink:
* Uplink channels 1\-9 (RX1\)
* **869\.525** \- SF9BW125 (RX2\)

##### Note:

 The Things Network uses the non\-standard SF9BW125 data rate for RX2 in Europe. If your devices use OTAA, this will be configured automatically when they join. If your devices use ABP, you will need to program this RX2 data rate into the devices in order to make them work with TTN.

## EU433

> No frequency plan yet. Submit a proposal!

## US902\-928

Used in USA, Canada and South America
Uplink:
1. **903\.9** \- SF7BW125 to SF10BW125
2. **904\.1** \- SF7BW125 to SF10BW125
3. **904\.3** \- SF7BW125 to SF10BW125
4. **904\.5** \- SF7BW125 to SF10BW125
5. **904\.7** \- SF7BW125 to SF10BW125
6. **904\.9** \- SF7BW125 to SF10BW125
7. **905\.1** \- SF7BW125 to SF10BW125
8. **905\.3** \- SF7BW125 to SF10BW125
9. **904\.6** \- SF8BW500

Downlink:
1. **923\.3** \- SF7BW500 to SF12BW500 (RX1\)
2. **923\.9** \- SF7BW500 to SF12BW500 (RX1\)
3. **924\.5** \- SF7BW500 to SF12BW500 (RX1\)
4. **925\.1** \- SF7BW500 to SF12BW500 (RX1\)
5. **925\.7** \- SF7BW500 to SF12BW500 (RX1\)
6. **926\.3** \- SF7BW500 to SF12BW500 (RX1\)
7. **926\.9** \- SF7BW500 to SF12BW500 (RX1\)
8. **927\.5** \- SF7BW500 to SF12BW500 (RX1\)
9. **923\.3** \- SF12BW500 (RX2\)

## CN470\-510

Used in China
Uplink:
1. **486\.3** \- SF7BW125 to SF12BW125
2. **486\.5** \- SF7BW125 to SF12BW125
3. **486\.7** \- SF7BW125 to SF12BW125
4. **486\.9** \- SF7BW125 to SF12BW125
5. **487\.1** \- SF7BW125 to SF12BW125
6. **487\.3** \- SF7BW125 to SF12BW125
7. **487\.5** \- SF7BW125 to SF12BW125
8. **487\.7** \- SF7BW125 to SF12BW125

Downlink:
1. **506\.7** \- SF7BW125 to SF12BW125 (RX1\)
2. **506\.9** \- SF7BW125 to SF12BW125 (RX1\)
3. **507\.1** \- SF7BW125 to SF12BW125 (RX1\)
4. **507\.3** \- SF7BW125 to SF12BW125 (RX1\)
5. **507\.5** \- SF7BW125 to SF12BW125 (RX1\)
6. **507\.7** \- SF7BW125 to SF12BW125 (RX1\)
7. **507\.9** \- SF7BW125 to SF12BW125 (RX1\)
8. **508\.1** \- SF7BW125 to SF12BW125 (RX1\)
9. **505\.3** \- SF12BW125 (RX2\)

## CN779\-787

Not used by The Things Network
## AU915\-928

Uplink:
1. **916\.8** \- SF7BW125 to SF12BW125
2. **917\.0** \- SF7BW125 to SF12BW125
3. **917\.2** \- SF7BW125 to SF12BW125
4. **917\.4** \- SF7BW125 to SF12BW125
5. **917\.6** \- SF7BW125 to SF12BW125
6. **917\.8** \- SF7BW125 to SF12BW125
7. **918\.0** \- SF7BW125 to SF12BW125
8. **918\.2** \- SF7BW125 to SF12BW125
9. **917\.5** \- SF8BW500

Downlink:
1. **923\.3** \- SF7BW500 to SF12BW500 (RX1\)
2. **923\.9** \- SF7BW500 to SF12BW500 (RX1\)
3. **924\.5** \- SF7BW500 to SF12BW500 (RX1\)
4. **925\.1** \- SF7BW500 to SF12BW500 (RX1\)
5. **925\.7** \- SF7BW500 to SF12BW500 (RX1\)
6. **926\.3** \- SF7BW500 to SF12BW500 (RX1\)
7. **926\.9** \- SF7BW500 to SF12BW500 (RX1\)
8. **927\.5** \- SF7BW500 to SF12BW500 (RX1\)
9. **923\.3** \- SF12BW500 (RX2\)

> Note that The Things Network uses 2nd Sub\-Band only (channels 8 to 15 and 65\). You’ll need to program the specific channels into the devices in order to make them work with TTN.

## AS923

We use two frequency plans, depending on the country. OTAA devices use two common channels: 923\.2MHz and 923\.4MHz. They will receive the additional channels on a successful join.
### AS920\-923 (“AS1”)

Used in Japan, Malaysia, Singapore
Uplink:
1. **923\.2** \- SF7BW125 to SF12BW125
2. **923\.4** \- SF7BW125 to SF12BW125
3. **922\.2** \- SF7BW125 to SF12BW125
4. **922\.4** \- SF7BW125 to SF12BW125
5. **922\.6** \- SF7BW125 to SF12BW125
6. **922\.8** \- SF7BW125 to SF12BW125
7. **923\.0** \- SF7BW125 to SF12BW125
8. **922\.0** \- SF7BW125 to SF12BW125
9. **922\.1** \- SF7BW250
10. **921\.8** \- FSK

Downlink:
* Uplink channels 1\-10 (RX1\)
* **923\.2** \- SF10BW125 (RX2\)

### AS923\-925 (“AS2”)

Used in Brunei, Cambodia, Hong Kong, Indonesia, Laos, Taiwan, Thailand, Vietnam
Uplink:
1. **923\.2** \- SF7BW125 to SF12BW125
2. **923\.4** \- SF7BW125 to SF12BW125
3. **923\.6** \- SF7BW125 to SF12BW125
4. **923\.8** \- SF7BW125 to SF12BW125
5. **924\.0** \- SF7BW125 to SF12BW125
6. **924\.2** \- SF7BW125 to SF12BW125
7. **924\.4** \- SF7BW125 to SF12BW125
8. **924\.6** \- SF7BW125 to SF12BW125
9. **924\.5** \- SF7BW250
10. **924\.8** \- FSK

Downlink:
* Uplink channels 1\-10 (RX1\)
* **923\.2** \- SF10BW125 (RX2\)

## KR920\-923

Uplink:
1. **922\.1** \- SF7BW125 to SF12BW125
2. **922\.3** \- SF7BW125 to SF12BW125
3. **922\.5** \- SF7BW125 to SF12BW125
4. **922\.7** \- SF7BW125 to SF12BW125
5. **922\.9** \- SF7BW125 to SF12BW125
6. **923\.1** \- SF7BW125 to SF12BW125
7. **923\.3** \- SF7BW125 to SF12BW125
8.

Downlink:
* Uplink channels 1\-7
* **921\.9** \- SF12BW125 (RX2; SF12BW125 might be changed to SF9BW125\)

## IN865\-867

Uplink:
1. **865\.0625** \- SF7BW125 to SF12BW125
2. **865\.4025** \- SF7BW125 to SF12BW125
3. **865\.9850** \- SF7BW125 to SF12BW125

Downlink:
* Uplink channels 1\-3 (RX1\)
* **866\.550** \- SF10BW125 (RX2\)# Duty Cycle

Duty Cycle indicates the fraction of time a resource is busy.
When a single device transmits on a channel for 2 every 10 , this device has a duty cycle of 20%.
However, if we also consider , things get a bit more complicated. When we have a device that transmits on 3 channels instead of one, each individual is still occupied for 2 every 10 (so 20%). However, the is now transmitting for 6 every 10 , giving it a duty cycle of 60%.
In our European frequency plan, we have channels in different , so when considering the duty cycle, we also have to consider these. Let’s say the 3 channels we used before, are in 2 different . Each separate still has a duty cycle of 20%, the still has a duty cycle of 60%, but we now see that is in use for 2 every 10 (20%), while is in use for 4 every 10 (40%).
## Maximum Duty Cycle

The duty cycle of radio devices is often regulated by government. If this is the case, the duty cycle is commonly set to 1%, but make sure to check the regulations of your local government to be sure.
In Europe, duty cycles are regulated by section 4\.3\.3 of the ETSI EN300\.220\-2 V3\.2\.1 (2018\-06\) standard. This standard defines the following sub\-bands and their duty cycles:
* **K** (863 MHz \- 865 MHz): 0\.1%
* **L** (865 MHz \- 868 MHz): 1%
* **M** (868 MHz \- 868\.6 MHz): 1%
* **N** (868\.7 MHz \- 869\.2 MHz): 0\.1%
* **P** (869\.4 MHz \- 869\.65 MHz): 10%
* **Q** (869\.7 MHz \- 870 MHz): 1%

Additionally, the LoRaWAN specification specifies duty cycles for the join frequencies, which are used for over\-the\-air activations (OTAA) by every LoRaWAN\-compliant end device. In most regions, the duty cycle for these frequencies is set to 1% .
#### Fair Use Policy

On The Things Network’s The Things Stack Sandbox a Fair Use Policy applies which limits the uplink airtime to 30 seconds per day (24 hours) per node and the downlink messages to 10 messages per day (24 hours) per node . If you use a private network, these limits do not apply, but you still have to be compliant with the governmental and LoRaWAN limits.
## Compliance

Every radio device must be compliant with the regulated duty cycle limits. This applies to both nodes and gateways .
In practice, this means that you should program your nodes in such a way, that they stay within the limits. The easiest way to do this, is to calculate how much each message consumes using one of the many airtime calculators and use that information to choose a good transmit interval.
Some radio modules (such as the RN2483\) also enforce the duty cycle limits. If you exceed the limits, the module will complain with a message no\_free\_ch . Specifically, the RN2483 limits the duty cycle on a per\-channel basis. This means that if you only have 1 channel configured, the module will start enforcing the duty cycle after the first message.

In the European band, a transmission on a channel within a frequency band, also influences the other frequencies in that band.

As a per\-channel duty cycle limit is easier to implement, you can also divide the sub\-band duty cycle over the number of channels in that sub\-band. So for example, in a sub\-band with 8 channels and a duty cycle of 1%, each channel has a duty cycle of 1/8% (that’s 0\.125%).
This method is also implemented by the RN2483 module, and as a result, instead of seeing the no\_free\_ch when you send too quickly after the first message you can send multiple messages before all 8 channels are “blocked” and the duty cycle is enforced.# Glossary

## Activation

### Definition:

Every end device must be registered with a network before sending and receiving messages. This procedure is known as activation. There are two activation methods available: Over\-The\-Air\-Activation (most secure and most flexible) and Activation By Personalization (least secure and least flexible).
### The Opportunity:

Activation is a network\-agnostic procedure which allows an end device to join any LoRaWAN network, preventing lock\-in and allowing you to use and transfer your devices between networks as you choose.

## Activation by Personalisation

### Definition:

This is the less secure method of activation. Matching keys must be manually programmed in a device and entered in the network. To change networks, physical access to the device is necessary, to reprogram keys.
### The Opportunity:

Activation by Personalisation is sometimes useful during demos when you do not want to wait for an uplink slot to complete activation

## Adaptive Data Rate

### Definition:

Adaptive Data Rate (ADR) is a mechanism for optimizing data rates, airtime and energy consumption in the network. The ADR mechanism controls the following transmission parameters of an end device: Spreading factor Bandwidth Transmission power
### The Opportunity:

ADR can optimize device power consumption while ensuring that messages are still received at gateways. When ADR is in use, the network server will indicate to the end device that it should reduce transmission power or increase data rate. End devices which are close to gateways should use a lower spreading factor and higher data rate, while devices further away should use a high spreading factor because they need a higher link budget.

## Application Server

### Definition:

The application server processes application\-specific data messages received from end devices. It also generates all the application\-layer downlink payloads and sends them to connected end devices through the network server. A LoRaWAN network can have more than one application server.
### The Opportunity:

The application server allows decoupling of the application from the network backend. Collected data can be interpreted, analyzed, or visualized using third party integrations, without revealing application specific keys to the network.

## Bandwidth

### Definition:

Bandwidth is the range of frequencies occupied by the modulated radio frequency signal. The bandwidth is expressed in Hertz (Hz).
### The Opportunity:

Bandwidth impacts time on air and receiver sensitivity. Increasing bandwidth decreases the time needed to transmit, decreasing power consumption, but also reducing receiver sensitivity.

## Coding Rate

### Definition:

The coding rate defines the proportion of bits that actually carry information. For example, the coding rate 4/5 means 4 bits carry information and one bit is used for error correction \- a total of 5 bits. LoRa uses the following Coding Rates. CR1: 4/5 (1 error correction bit for 4 information bits) CR2: 4/6 (2 error correction bits for 4 information bits) CR3: 4/7 (3 error correction bits for 4 information bits) CR4: 4/8 (4 error correction bits for 4 information bits)
### The Opportunity:

Coding Rates allow the network to adjust the amount of redundant data that is sent, so that data can be received correctly even when there is interference. When there is little interference, a faster Coding Rate can be used, which transmits less redundant data, allowing for more information carrying bits to be transmitted per second.

## CRC

### Definition:

A Cyclic Redundancy Check (CRC) is an error detecting code used in digital transmission to detect unintended changes to raw data.
### The Opportunity:

CRCs allow us to detect errors in digital data, enabling reliable communication over noisy channels.

## Decibel (dB)

### Definition:

The decibel (dB) is a unit of measurement used to express the ratio between quantities on a logarithmic scale. In radio transmission, it is used most often to refer to gain from an antenna with respect to a fixed reference value, and signal\-to\-noise ratio.
### The Opportunity:

The decibel scale allows network operators to quickly quantify losses and gains on a signal path, by linearizing the power domain. For example, a 10dB loss and 5dB gain can be quickly seen to sum to a 5dB loss, but calculating this in terms of gain is much more complicated, involving two multiplications.

## Decibel\-milliwatts (dBm)

### Definition:

dBm (decibel\-milliwatts) is a unit used to indicate that a power level is expressed in decibels (dB) with reference to an input power of 1 mW.
### The Opportunity:

While dBm is not a recognized SI unit, it is incredibly useful for defining standards.

## Device Classes

### Definition:

The LoRaWAN specification defines three device types \- Class A (All), Class B (Beacon), and Class C (Continuous). Class A devices open windows to receive downlinks immediately following an uplink. Class B devices add periodic receive windows. Class C devices listen continuously for downlinks. All LoRaWAN devices must implement Class A, whereas Class B and Class C are extensions to the specification of Class A devices.
### The Opportunity:

Device classes provide a suitable LoRaWAN solution for many different use cases. Class A devices maximize battery life by listening for downlinks only after an uplink, and spending most of their time in sleep. For applications which do not need guaranteed downlink latency, Class A provides years of battery life on a single cell. Class B devices add guaranteed latency at the cost of some battery life. Class C devices can receive downlinks anytime, but are typically mains powered.

## Downlink message

### Definition:

A downlink message is sent by the network server (or application server) to an end device and is relayed by a single gateway.
### The Opportunity:

Downlinks allow you to update or configure your device, for example to update signage, change the temperature in a room, or blink a light to notify users something has happened. Downlinks may also contain firmware or security updates for your device.

## Effective Isotropic Radiated Power

### Definition:

The Effective Isotropic Radiated Power (EIRP) is the total power radiated by a hypothetical isotropic antenna in a single direction. EIRP is expressed in dBm or Watts. The maximum allowed EIRP differs between regions.
### The Opportunity:

Antenna power provides a tradeoff between range and battery life, and is one of the components of ADR. Power can be increased for devices which need to transmit longer distances, and decreased to save power when they are nearer to gateways.

## End Device

### Definition:

An end device is a sensor or an actuator that is wirelessly connected to the LoRaWAN network.
### The Opportunity:

There are countless LoRaWAN use cases, but here are some great existing applications for LoRaWAN end devices: Vaccine cold chain monitoring Animal conservation Smart farming Food safety Smart waste bins Smart parking Facility management

## Forward Error Correction

### Definition:

Forward error correction is a way of controlling error in noisy data transmission by adding redundant data. The receiver can check the integrity of the data based on the redundant information, and only accepts data which appears to be correct.
### The Opportunity:

Error correction allows for detection and in some cases correction of data that has been affected by interference. Adding redundant data increases the ability of the receiver to detect or correct errors, but results in a lower effective data rate. See Coding Rate for more information.

## Frequency

### Definition:

The frequency of a radio wave is the number of times the wave oscillates per second, measured in hertz. The radio spectrum has frequencies from 30 Hz to 300 GHz. To prevent interference between different users, the generation and transmission of radio waves across the frequency band is strictly regulated by national laws.
### The Opportunity:

LoRa operates in the license free frequency spectrum range, so you don’t have to pay expensive frequency spectrum license fees to deploy a LoRaWAN network.

## Frequency Plan

### Definition:

A Frequency Plan defines data rates and channels which comply with the LoRaWAN Regional Parameters for a band or geographical area. Devices are configured for a particular Frequency Plan as part of activation, and can use any Frequency Plan within a supported band
### The Opportunity:

LoRa operates in the license free spectrum, which has different frequencies in every geographical area. The regional parameters document defines recommended frequency plans to allow standardization of LoRaWAN devices across geographical areas.

## Join Server

### Definition:

The Join Server processes join\-request messages sent by end devices. It stores root keys, generates session keys, and transfers those session keys to the network server and the application server. The Join Server is introduced in LoRaWAN 1\.1 and 1\.0\.4\.
### The Opportunity:

The Join Server allows for secure end\-device provisioning without network lock\-in and without knowing beforehand which network the end\-user will select. Manufacturers only need to provide the keys to the end\-device in one safe place. The buyer uses a one\-click device claiming procedure to transfer ownership in the Join Server. The owner can then configure the device to any LoRaWAN compliant network.

## LoRa

### Definition:

LoRa is a wireless modulation technique derived from chirp spread spectrum technology. It encodes information on radio waves using chirp pulses \- similar to the way dolphins and bats communicate!
### The Opportunity:

LoRa is ideal for applications that transmit small chunks of data with low bit rates. LoRa modulated transmission is robust against disturbances and can be received across great distances \- up to 5 km in urban areas and 15 km or more in rural areas with line\-of\-sight. LoRa end devices consume very little power and devices often last up to ten years on a single coin cell battery.

## LoRaWAN®

### Definition:

LoRaWAN is a Media Access Control (MAC) layer protocol built on top of LoRa modulation. It is a software layer which defines how devices use the LoRa hardware, for example when they transmit, and the format of messages. \\nThe LoRaWAN protocol is developed and maintained by the LoRa Alliance®.
### The Opportunity:

Like LoRa, LoRaWAN is ideal for applications that transmit small chunks of data with low bit rates. LoRaWAN devices are ultra low power, often lasting up to ten years on a single coin cell battery. LoRaWAN networks are extremely long range, up to 15km in rural areas, and the cost of hardware and running a network is extremely low. LoRaWAN provides built in geolocation, modern security, large capacity, built\-in roaming, and operates in the license\-free spectrum, so there is no barrier to creating your own network.

## Network Server

### Definition:

The Network Server manages the LoRaWAN network. It receives uplink messages from gateways as IP traffic, and routes downlink messages for end devices. The Network Server is also responsible for end device activation, message deduplication, message acknowledgement, geolocation of end devices, and adaptive data rate control of the network.
### The Opportunity:

The network server enables the LoRaWAN network.

## Noise Floor

### Definition:

The noise floor is the sum of all noise sources in a measurement system. It is typically the size of the smallest unit that can be measured by the system.
### The Opportunity:

LoRa and other spread spectrum technologies can detect signals below the noise floor, by spreading information in the frequency spectrum across the entire signal bandwidth.

## Over the Air Activation

### Definition:

This is the most secure activation method for end devices. Devices perform a join procedure with the network, during which a dynamic device address is assigned and security keys are negotiated with the device.
### The Opportunity:

Over the Air Activation provides maximum security and maximum flexibility. Keys are negotiated securely between the network and device, and the device can easily be transferred to another network by registering it in another network server, even without physical access to the device.

## Packet Forwarder

### Definition:

A Packet Forwarder is a program running on a Gateway that receives and transmits LoRa packets, and forwards these packets to and from a Network Server. There are two popular packet forwarders: the legacy Semtech UDP packet forwarder, and the modern LoRa Basics™ Station packet forwarder. The UDP packet forwarder is ubiquitous, but uses unsecured UDP packets. LoRa Basics Station adds a centralized update and configuration server, TLS authentication, and centralized frequency plan management.
### The Opportunity:

Packet forwarders are packet agnostic programs that forward all LoRaWAN packets received on a gateway to the network, decoupling their implementation completely from the application. Packet forwarders can run on basic, low cost hardware, which allows for easy expansion of LoRaWAN network coverage simply by adding more gateways.

## Preamble

### Definition:

The preamble is a set of symbols (or chirps) that is used by the receiver to detect a LoRa packet. LoRaWAN uses a series of 8 up\-chirps as a preamble.
### The Opportunity:

The preamble signals to a receiver when a LoRaWAN packet is being sent, which allows multiple protocols to operate using the same modulation technique (in this case LoRa) without interfering with each other.

## Received Signal Strength Indicator

### Definition:

The Received Signal Strength Indicator (RSSI) is the received signal power in milliwatts, measured in dBm. This value is used as a measurement of how well the signal is received.
### The Opportunity:

RSSI is used in the ADR feedback loop to determine if a signal is being received with enough power to allow the device to increase its data rate and conserve battery. A high RSSI means the device can reduce transmission power and messages will still be received.

## Signal\-to\-Noise Ratio

### Definition:

Signal\-to\-Noise Ratio (SNR) indicates the ratio between the received power signal and the noise floor power level. SNR is expressed in dB.
### The Opportunity:

SNR is used in the ADR feedback loop to determine if a signal is being received with enough power to allow the device to increase its data rate and conserve battery. A high SNR means the device can reduce transmission power and messages will still be received.

## Spreading Factor

### Definition:

The spreading factor defines a spreading pattern applied to the bitstream before modulation, which increases processing gain and aids in decoding of LoRaWAN messages. LoRaWAN defines 6 spreading factors \- SF7 to SF12\.
### The Opportunity:

The spreading factor allows the network to increase the transmission bit rate and decrease power consumption for an end device at the cost of range. Controlling spreading factor also allows the network to control congestion, as messages sent using different spreading factors on the same channel do not interfere with each other.

## Time on Air

### Definition:

The time a transmitter is on, i.e the time needed to complete a transmission. In LoRa, this is the preamble duration and payload duration. The spreading factor and coding rate determine the length of time needed to transmit a given payload, and play a critical role in how much data a device can send.
### The Opportunity:

National and international governing bodies set strict limits on the amount of time devices can spend transmitting, to prevent congestion of public frequencies. In addition, network operators often impose additional restrictions on the amount of time devices can spend transmitting, called “Fair Access Policy.” These regulations must be respected to give everyone an opportunity to share airtime in the license free spectrum.

## Uplink message

### Definition:

An uplink message is sent by an end device to the network server and is relayed by one or more gateways.
### The Opportunity:

Uplinks enable your application to collect data from sensors in all sorts of environments \- LoRaWAN devices can be battery or mains powered, in dense urban areas or completely off the grid, mobile or stationary \- the possibilities are endless, and the limits of your application are up to your creativity.# Modulation \& Data Rate

In most cases LoRaWAN uses LoRa modulation. LoRa modulation is based on Chirp spread\- spectrum technology, which makes it work well with channel noise, multipath fading and the Doppler effect, even at low power.
The data rate depends on the used bandwidth and spreading factor. LoRaWAN can use channels with a bandwidth of either 125 kHz, 250 kHz or 500 kHz, depending on the region or the frequency plan. The spreading factor is chosen by the end\-device and influences the time it takes to transmit a frame.

> The Data Rate Story : There are three knobs you can turn: transmission power , bandwidth and spreading factor . If you lower the tx power, you’ll save battery, but the range of the signal will obviously be shorter. The other two knobs combined form the data rate. This determines how fast bytes are transmitted. If you increase the data rate (make the bandwidth wider or the spreading factor lower) you can transmit those bytes in a shorter time. For those, the calculation is approximately as follows: Making the bandwidth 2x wider (from BW125 to BW250\) allows you to send 2x more bytes in the same time. Making the spreading factor 1 step lower (from SF10 to SF9\) allows you to send 2x more bytes in the same time. Lowering the spreading factor makes it more difficult for the gateway to receive a transmission, as it will be more sensitive to noise. You could compare this to two people taking in a noisy place (a bar for example). If you’re far from each other, you have to talk slow (SF10\), but if you’re close, you can talk faster (SF7\)

# Airtime Calculator

Don’t waste your airtime. Be mindful about the spreading factors and aim for a high transmission speed as this leads to longer battery life and less gateway utilization.
Visit the Airtime Calculator# Addressing \& Activation

## Addressing

LoRaWAN knows a number of identifiers for devices, applications and gateways.
* `DevEUI` \- 64 bit end\-device identifier, EUI\-64 (unique)
* `DevAddr` \- 32 bit device address (non\-unique)
* `AppEUI` \- 64 bit application identifier, EUI\-64 (unique)
* `GatewayEUI` \- 64 bit gateway identifier, EUI\-64 (unique)

### Devices

The Things Network Foundation has received a 7\-bit device address prefix from the LoRa Alliance. This means that all TTN device addresses will start with 0x26 or 0x27 (although addresses that start with these might also belong to other networks with the same prefix). Within TTN, we assign device address prefixes to “regions” (for example, device addresses in the eu region start with 0x2601 ). Within a region, the NetworkServer is responsible for assigning device addresses. We are using prefixes here too for different device classes (for example, ABP devices in the eu region start with 0x26011 ) or to shard devices over different servers, see .
The NetworkServer assigns device addresses to devices (based on configuration). For ABP devices you have to request an address from the NetworkServer (the console or ttnctl will do this for you). For OTAA devices, the NetworkServer will assign an address when the device joins.
When a device joins the network, it receives a dynamic (non\-unique) 32\-bit address ( DevAddr ). It’s good to keep in mind that device addresses are not unique. We can (and probably will) give hundreds of devices the same address. Finding the actual device that belongs to that address is done by matching the cryptographic signature (MIC) of the message to a device in the database.
### Applications

Applications in LoRaWAN and The Things Network have a 64 bit unique identifier ( AppEUI ). When you create an application, The Things Network’s account server allocates an AppEUI from the address block of The Things Network Foundation. This means that every application has at least an AppEUI that starts with 70B3D57ED . If you have your own AppEUI s, you can also add those to your application.
### Gateways

Gateways are manufactured with an embedded EUI, which can then be used to register the gateway on The Things Network. Although the configuration files of some gateways suggest that you can just choose an EUI for the gateway, this is not true . If your gateway did not come with an embedded EUI, you can use another EUI that you own, or configure an AppEUI that is registered to your account. You may also use an MQTT\-based forwarder, which only needs a GatewayID (that you can choose yourself) instead of a GatewayEUI .
## Activation

LoRaWAN devices have a 64 bit unique identifier ( DevEUI ) that is assigned to the device by the chip manufacturer. However, all communication is done with a dynamic 32 bit device address ( DevAddr ) of which 7 bits are fixed for The Things Network, leaving 25 bits that can be assigned to individual devices, a procedure called Activation .
### Over\-the\-Air Activation (OTAA)

Over\-the\-Air Activation (OTAA) is the preferred and most secure way to connect with The Things Network. Devices perform a join\-procedure with the network, during which a dynamic DevAddr is assigned and security keys are negotiated with the device.
### Activation by Personalization (ABP)

In some cases you might need to hardcode the DevAddr as well as the security keys in the device. This means activating a device by personalization (ABP). This strategy might seem simpler, because you skip the join procedure, but it has some downsides related to security.# Academic Research

A lot of research is conducted on LoRa and LoRaWAN. This page is created to better share the conducted academic research and created scientific articles.

| Title | Author | Journal/Proceedings | Year |
| --- | --- | --- | --- |
| [Modeling Communication Reliability in LoRa Networks with Device\-level Accuracy](https://ieeexplore.ieee.org/document/9488783) | V. Toro\-Betancur; G. Premsankar; M. Slabicki; M. Di Francesco | IEEE INFOCOM | 2021 |
| [A Communication Infrastructure for the Health and Social Care Internet of Things: Proof\-of\-Concept Study](https://medinform.jmir.org/2020/2/e14583) | V.Della Mea V, M.h. Popescu, D.Gonano, T.Petaros, I.Emili, M.G.Fattori | JMIR Medical Informatics | 2020 |
| [A comparative study of LPWAN technologies for large\-scale IoT deployment](http://www.sciencedirect.com/science/article/pii/S2405959517302953) | K.Mekki, E.Bajic, F.Chaxel, F.Meyer | ICT Express | 2019 |
| [City Scale Particulate Matter Monitoring Using LoRaWAN Based Air Quality IoT Devices](https://www.mdpi.com/1424-8220/19/1/209) | S.J.Johnston, P.J.Basford, F.M.Bulot, M.Apetroaie\-Cristea, N.H.Easton, C.Davenport C, et al | Sensors (Basel) | 2019 |
| [Tracking and Monitoring System Based on LoRa Technology for Lightweight Boats](https://www.mdpi.com/2079-9292/8/1/15) | Sanchez\-Iborra R, G. Liaño I, Simoes C, Couñago E, Skarmeta A | Electronics | 2019 |
| [Characterization of LoRa Point\-to\-Point Path\-Loss: Measurement Campaigns and Modeling Considering Censored Data](https://ieeexplore.ieee.org/document/8902126) | G. Callebaut, and L. van der Perre | IEEE Internet of Things Journal | 2019 |
| [Cross\-layer framework and optimization for efficient use of the energy budget of IoT Nodes](https://ieeexplore.ieee.org/document/8885739) | G. Callebaut, G. Ottoy and L. van der Perre | IEEE Wireless Communications and Networking Conference (WCNC), Marrakesh, Morocco, 2019, pp. 1\-6 | 2019 |
| [A Deployable LPWAN Platform for Low\-Cost and Energy\-Constrained IoT Applications](https://www.mdpi.com/1424-8220/19/3/585) | B. Thoen, G. Callebaut, G. Luus and S. Wielandt | Sensors \- Internet of Things and Ubiquitous Sensing | 2019 |
| [Collision Resolution Protocol for Delay and Energy Efficient LoRa Networks](https://ieeexplore.ieee.org/document/8678478) | N. El Rachkidy, A. Guitton and M. Kaneko | IEEE Transactions on Green Communications and Networking | 2019 |
| [A Survey on LoRa Networking: Research Problems, Current Solutions and Open Issues](https://ieeexplore.ieee.org/document/8883217) | Jothi Prasanna Shanmuga Sundaram, Wan Du, Zhiwei Zhao | IEEE Communications Surveys and Tutorials | 2019 |
| [On the LoRa Modulation for IoT: Waveform Properties and Spectral Analysis](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8723130) | M. Chiani and A. Elzanaty | IEEE Internet of Things Journal | 2019 |
| [LoRaWAN Network: Radio Propagation Models and Performance Evaluation in Various Environments in Lebanon](http://samer.lahoud.fr/pub-pdf/jiot-19.pdf) | R. El Chall, S. Lahoud, M. El Helou | IEEE Internet of Things Journal | 2019 |
| [IoT agriculture system based on LoRaWAN](https://ieeexplore.ieee.org/document/8402368) | D.Davcev, K.Mitreski, S.Trajkovic, V.Nikolovski, N.Koteli | IEEE International Workshop on Factory Communication Systems (WFCS) | 2018 |
| [A Community\-Based IoT Personalized Wireless Healthcare Solution Trial](https://ieeexplore.ieee.org/document/8355907) | Catherwood PA, Steele D, Little M, Mccomb S, Mclaughlin J | IEEE Journal of Translational Engineering in Health and Medicine | 2018 |
| [Emerging Distributed Programming Paradigm for Cyber\-Physical Systems Over LoRaWANs](https://doi.org/10.1109/glocomw.2018.8644518) | D. Pianini, A. Elzanaty, A. Giorgetti, M. Chiani | 2018 IEEE Globecom Workshops (GC Wkshps) | 2018 |
| [How Agile is the Adaptive Data Rate Mechanism of LoRaWAN?](https://ieeexplore.ieee.org/document/8647469) | S. Li, U. Raza, A. Khan | IEEE Global Communications Conference (GLOBECOM) | 2018 |
| [Analysis and Performance Optimization of LoRa Networks With Time and Antenna Diversity](https://doi.org/10.1109/ACCESS.2018.2839064) | A. Hoeller\-Jr, R.D. Souza, O.L. Alcaraz\-López, H. Alves, M. Noronha\-Neto, G. Brante | IEEE ACCESS Journal | 2018 |
| [Exploiting Time Diversity of LoRa Networks Through Optimum Message Replication](https://doi.org/10.1109/ISWCS.2018.8491203) | A. Hoeller\-Jr, R.D. Souza, O.L. Alcaraz\-López, H. Alves, M. Noronha\-Neto, G. Brante | 15th International Symposium on Wireless Communication Systems (ISWCS) | 2018 |
| [Analysis and assessment of LoRaWAN](https://ieeexplore.ieee.org/document/8325799) | Kieu\-Ha Phung , Hieu Tran , Quan Nguyen , Truong Thu Huong , Thanh\-Long Nguyen | 2nd International Conference on Recent Advances in Signal Processing, Telecommunications \& Computing (SigTelCom) | 2018 |
| [Throughput, coverage and scalability of LoRa LPWAN for Internet of Things](http://people.ucalgary.ca/~mghaderi/docs/iwqos18-lora.pdf) | A. M. Yousuf, E. M. Rochester, B. Ousat and M. Ghaderi | Proc. IEEE/ACM International Symposium on Quality of Service (IWQoS) | 2018 |
| [A low\-cost LoRaWAN testbed for IoT: Implementation and measurements](https://ieeexplore.ieee.org/document/8355180) | A. M. Yousuf, E. M. Rochester and M. Ghaderi. | Proc. IEEE World Forum on Internet of Things (WF\-IoT), pp. 361\-366 | 2018 |
| [Integration of LoRaWAN and 4G/5G for the Industrial Internet of Things](https://ieeexplore.ieee.org/document/8291115/) | Navarro\-Ortiz, J., Sendra, S., Ameigeiras, P., Lopez\-Soler, J.M. | IEEE Communications Magazine, Vol. 56(2\), pp. 60\-67 | 2018 |
| [A Fair Adaptive Data Rate Algorithm for LoRaWAN](https://arxiv.org/abs/1801.00522) | Abdelfadeel, K.Q., Cionca, V. and Pesch, D. | arXiv preprint arXiv:1801\.00522 | 2018 |
| [Resource Efficiency in Low\-Power Wide\-Area Networks for IoT Applications](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8254800) | Z. Qin and J. McCann. | IEEE Global Communications Conference (GLOBECOM), pp. 1\-7\. | 2017 |
| [LoRaWAN as an e\-health communication technology](https://ieeexplore.ieee.org/document/8029947) | Buyukakkaslar MT, Erturk MA, Aydin MA, Vollero L. | IEEE 41st Annual Computer Software and Applications Conference (COMPSAC) | 2017 |
| [IoT\-based health monitoring via LoRaWAN](https://ieeexplore.ieee.org/document/8011165) | Mdhaffar A, Chaari T, Larbi K, Jmaiel M, Freisleben B | IEEE EUROCON 2017 \-17th International Conference on Smart Technologies | 2017 |
| [Analysis of the use of LoRaWan technology in a large\-scale smart city demonstrator](https://ieeexplore.ieee.org/document/8125011) | M.Loriot, A.Aljer and I.Shahrour | IEEE Conf. Sensors Networks Smart and Emerging Technologies (SENSET) | 2017 |
| [Modelling and analysis of low\-power wide\-area networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7996589) | Z. Qin, y. Liu, G. Y. Li, and J. McCann. | IEEE International Conference on Communications (ICC), pp. 1\-7\. | 2017 |
| [Understanding the Limits of LoRaWAN](https://arxiv.org/pdf/1607.08011.pdf) | Adelantado, F., Vilajosana, X., Tuset\-Peiro, P., Martinez, B., Melia\-Segui, J. and Watteyne, T. | IEEE Communications Magazine Vol. 55(9\), pp. 34\-40 | 2017 |
| [LoRa protocol performance assessment in critical noise conditions](https://www.researchgate.net/publication/321462429_LoRa_Protocol_Performance_Assessment_in_Critical_Noise_Conditions) | Angrisani, L., Arpaia, P., Bonavolontà, F., Conti, M. and Liccardo, A. | Research and Technologies for Society and Industry (RTSI), 2017 IEEE 3rd International Forum on, pp. 1\-5 | 2017 |
| [Mathematical model of LoRaWAN channel access](https://ieeexplore.ieee.org/document/7974300) | Bankov, D., Khorov, E. and Lyakhov, A. | A World of Wireless, Mobile and Multimedia Networks (WoWMoM), 2017 IEEE 18th International Symposium on, pp. 1\-3 | 2017 |
| [LoRaWAN in the wild: Measurements from the things network](https://arxiv.org/abs/1706.03086) | Blenn, N. and Kuipers, F. | arXiv preprint arXiv:1706\.03086 | 2017 |
| [LoRa transmission parameter selection](https://ieeexplore.ieee.org/document/8271941) | Bor, M. and Roedig, U. | Proceedings of the 13th IEEE International Conference on Distributed Computing in Sensor Systems (DCOSS), Ottawa, ON, Canada, pp. 5\-7 | 2017 |
| [Modeling the Energy Performance of LoRaWAN](http://www.mdpi.com/1424-8220/17/10/2364) | Casals, L., Mir, B., Vidal, R. and Gomez, C. | Sensors | 2017 |
| [An Experimental Evaluation of the Reliability of LoRa Long\-Range Low\-Power Wireless Communication](https://www.mdpi.com/2224-2708/6/2/7) | Cattani, M., Boano, C.A. and Römer, K. | Journal of Sensor and Actuator Networks Vol. 6(2\), pp. 7 | 2017 |
| [Empowering Low\-Power Wide Area Networks in Urban Settings](https://dl.acm.org/doi/10.1145/3098822.3098845) | Eletreby, R., Zhang, D., Kumar, S. and Yağan, O. | Proceedings of the Conference of the ACM Special Interest Group on Data Communication, pp. 309\-321 | 2017 |
| [Low power wide area network analysis: Can LoRa scale?](https://ieeexplore.ieee.org/document/7803607) | Georgiou, O. and Raza, U. | IEEE Wireless Communications Letters Vol. 6(2\), pp. 162\-165 | 2017 |
| [Effects of Shadowing on LoRa LPWAN Radio Links](http://ijece.iaescore.com/index.php/IJECE/article/view/8664) | Habaebi, M.H., Chowdhury, I.J., Islam, M.R. and Zainal, N.A.B. | International Journal of Electrical and Computer Engineering (IJECE) Vol. 7(6\), pp. 2970\-2976 | 2017 |
| [Proposal of Adaptive Data Rate Algorithm for LoRaWAN\-Based Infrastructure](https://ieeexplore.ieee.org/document/8114467) | Hauser, V. and Hégr, T. | Future Internet of Things and Cloud (FiCloud), 2017 IEEE 5th International Conference on, pp. 85\-90 | 2017 |
| [LoRa indoor coverage and performance in an industrial environment: Case study](https://ieeexplore.ieee.org/abstract/document/8247601) | Haxhibeqiri, J., Karaağaç, A., Van den Abeele, F., Joseph, W., Moerman, I. and Hoebeke, J. | IEEE ETFA2017, the 22nd IEEE International Conference on Emerging Technologies And Factory Automation, pp. 1\-8 | 2017 |
| [LoRa scalability: A simulation model based on interference measurements](https://www.mdpi.com/1424-8220/17/6/1193) | Haxhibeqiri, J., Van den Abeele, F., Moerman, I. and Hoebeke, J. | Sensors Vol. 17(6\), pp. 1193 | 2017 |
| [LoRa from the city to the mountains: Exploration of hardware and environmental factors](https://dl.acm.org/doi/10.5555/3108009.3108091) | Iova, O., Murphy, A., Picco, G.P., Ghiro, L., Molteni, D., Ossi, F. and Cagnacci, F. | Proceedings of the 2017 International Conference on Embedded Wireless Systems and Networks | 2017 |
| [Internet of Things and LoRa™ Low\-Power Wide\-Area Networks: A survey](https://ieeexplore.ieee.org/document/8034915) | Lavric, A. and Popa, V. | Signals, Circuits and Systems (ISSCS), 2017 International Symposium on, pp. 1\-5 | 2017 |
| [DaRe: Data recovery through application layer coding for LoRaWAN](https://ieeexplore.ieee.org/document/7946866) | Marcelis, P.J., Rao, V.S. and Prasad, R.V. | Internet\-of\-Things Design and Implementation (IoTDI), 2017 IEEE/ACM Second International Conference on, pp. 97\-108 | 2017 |
| [On LoRaWAN scalability: Empirical evaluation of susceptibility to inter\-network interference](https://ieeexplore.ieee.org/document/7980757) | Mikhaylov, K., Petäjäjärvi, J. and Janhunen, J. | Networks and Communications (EuCNC), 2017 European Conference on, pp. 1\-6 | 2017 |
| [Performance of a low\-power wide\-area network based on LoRa technology: Doppler robustness, scalability, and coverage](https://journals.sagepub.com/doi/full/10.1177/1550147717699412) | Petäjäjärvi, J., Mikhaylov, K., Pettissalo, M., Janhunen, J. and Iinatti, J. | International Journal of Distributed Sensor Networks Vol. 13(3\), pp. 1550147717699412 | 2017 |
| [Does bidirectional traffic do more harm than good in LoRaWAN based LPWA networks?](https://arxiv.org/abs/1704.04174) | Pop, A.\-I., Raza, U., Kulkarni, P. and Sooriyabandara, M. | arXiv preprint arXiv:1704\.04174 | 2017 |
| [Power and spreading factor control in low power wide area networks](https://ieeexplore.ieee.org/document/7996380) | Reynders, B., Meert, W. and Pollin, S. | Communications (ICC), 2017 IEEE International Conference on, pp. 1\-6 | 2017 |
| [uLoRa: Ultra Low\-Power, Low\-Cost and Open Platform for the LoRa Networks](https://dl.acm.org/doi/10.1145/3127882.3127890) | Sallouha, H., Van den Bergh, B., Wang, Q. and Pollin, S. | Proceedings of the 4th ACM Workshop on Hot Topics in Wireless, pp. 43\-47 | 2017 |
| [Comparison of LoRaWAN classes and their power consumption](https://ieeexplore.ieee.org/document/8240313) | San Cheong, P., Bergs, J., Hawinkel, C. and Famaey, J. | Communications and Vehicular Technology (SCVT), 2017 IEEE Symposium on, pp. 1\-6 | 2017 |
| [A survey on LPWA technology: LoRa and NB\-IoT](https://www.sciencedirect.com/science/article/pii/S2405959517300061) | Sinha, R.S., Wei, Y. and Hwang, S.\-H. | ICT Express Vol. 3(1\), pp. 14\-21 | 2017 |
| [Analysis of Latency and MAC\-layer Performance for Class A LoRaWAN](https://ieeexplore.ieee.org/document/7954020) | Sørensen, R.B., Kim, D.M., Nielsen, J.J. and Popovski, P. | IEEE Wireless Communications Letters Vol. 6(5\), pp. 566\-569 | 2017 |
| [LoRa backscatter: Enabling the vision of ubiquitous connectivity](https://dl.acm.org/doi/10.1145/3130970) | Talla, V., Hessar, M., Kellogg, B., Najafi, A., Smith, J.R. and Gollakota, S. | Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies Vol. 1(3\), pp. 105 | 2017 |
| [Scalability analysis of large\-scale LoRaWAN networks in ns\-3](https://ieeexplore.ieee.org/abstract/document/8090518) | Van den Abeele, F., Haxhibeqiri, J., Moerman, I. and Hoebeke, J. | IEEE Internet of Things Journal Vol. 4(6\), pp. 2186\-2198 | 2017 |
| [Capacity limits of LoRaWAN technology for smart metering applications](https://ieeexplore.ieee.org/document/7996383) | Varsier, N. and Schwoerer, J. | Communications (ICC), 2017 IEEE International Conference on, pp. 1\-6 | 2017 |
| [Interference impact on coverage and capacity for low power wide area IoT networks](https://ieeexplore.ieee.org/document/7925510) | Vejlgaard, B., Lauridsen, M., Nguyen, H., Kovács, I.Z., Mogensen, P. and Sorensen, M. | Wireless Communications and Networking Conference (WCNC), 2017 IEEE, pp. 1\-6 | 2017 |
| [Range and coexistence analysis of long range unlicensed communication](https://ieeexplore.ieee.org/document/7500415) | Reynders, B., Meert, W. and Pollin, S. | Telecommunications (ICT), 2016 23rd International Conference on, pp. 1\-6 | 2016 |
| [Comparison of 6LoWPAN and LPWAN for the Internet of Things](https://www.researchgate.net/publication/316236998_Comparison_of_6LoWPAN_and_LPWAN_for_the_Internet_of_Things) | Al\-Kashoash, H. and Kemp, A.H. | Australian Journal of Electrical and Electronics Engineering Vol. 13(4\), pp. 268\-274 | 2016 |
| [Mitigating inter\-network interference in lora networks](https://dl.acm.org/doi/10.5555/3108009.3108093) | Voigt, T., Bor, M., Roedig, U. and Alonso, J. | arXiv preprint arXiv:1611\.00688 | 2016 |
| [Evaluation of LoRa and LoRaWAN for wireless sensor networks](https://ieeexplore.ieee.org/abstract/document/7808712) | Wixted, A.J., Kinnaird, P., Larijani, H., Tait, A., Ahmadinia, A. and Strachan, N. | Sensors, 2016 IEEE, pp. 1\-3 | 2016 |
| [A study of LoRa: Long range \& low power networks for the internet of things](https://www.mdpi.com/1424-8220/16/9/1466) | Augustin, A., Yi, J., Clausen, T. and Townsley, W.M. | Sensors Vol. 16(9\), pp. 1466 | 2016 |
| [On the limits of LoRaWAN channel access](https://ieeexplore.ieee.org/document/7810745) | Bankov, D., Khorov, E. and Lyakhov, A. | Engineering and Telecommunication (EnT), 2016 International Conference on, pp. 10\-14 | 2016 |
| [LoRa for the Internet of Things](https://eprints.lancs.ac.uk/id/eprint/77615/1/MadCom2016_LoRa_MAC.pdf) | Bor, M., Vidler, J.E. and Roedig, U. | Proceedings of the 2016 International Conference on Embedded Wireless Systems and Networks | 2016 |
| [Do LoRa low\-power wide\-area networks scale?](https://www.researchgate.net/publication/310200794) | Bor, M.C., Roedig, U., Voigt, T. and Alonso, J.M. | Proceedings of the 19th ACM International Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems, pp. 59\-67 | 2016 |
| [Long\-range communications in unlicensed bands: The rising stars in the IoT and smart city scenarios](https://ieeexplore.ieee.org/document/7721743) | Centenaro, M., Vangelista, L., Zanella, A. and Zorzi, M. | IEEE Wireless Communications Vol. 23(5\), pp. 60\-67 | 2016 |
| [Indoor signal propagation of LoRa technology](https://ieeexplore.ieee.org/document/7827865) | Gregora, L., Vojtech, L. and Neruda, M. | Mechatronics\-Mechatronika (ME), 2016 17th International Conference on, pp. 1\-4 | 2016 |
| [Experimental evaluation of LoRa(WAN) in indoor and outdoor environments](http://essay.utwente.nl/71133/) | Hakkenberg, C. | University of Twente | 2016 |
| [Decoding LoRa: Realizing a modern LPWAN with SDR](https://pubs.gnuradio.org/index.php/grcon/article/view/8) | Knight, M. and Seeber, B. | Vol. 1(1\)Proceedings of the GNU Radio Conference | 2016 |
| [Analysis of capacity and scalability of the LoRa low power wide area network technology](https://ieeexplore.ieee.org/document/7499263) | Mikhaylov, K., Petaejaejaervi, J. and Haenninen, T. | European Wireless 2016; 22th European Wireless Conference; Proceedings of, pp. 1\-6 | 2016 |
| [Indoor deployment of low\-power wide area networks (LPWAN): A LoRaWAN case study](https://ieeexplore.ieee.org/abstract/document/7763213) | Neumann, P., Montavont, J. and Noël, T. | Wireless and Mobile Computing, Networking and Communications (WiMob), 2016 IEEE 12th International Conference on, pp. 1\-8 | 2016 |
| [Vibrations powered LoRa sensor: An electromechanical energy harvester working on a real bridge](http://ieeexplore.ieee.org/document/7808752/authors) | Orfei, F | Department of Physics and Geology, Università degli Studi di Perugia | 2016 |
| [Evaluation of LoRa LPWAN technology for remote health and wellbeing monitoring](https://ieeexplore.ieee.org/document/7498898) | Petäjäjärvi, J., Mikhaylov, K., Hämäläinen, M. and Iinatti, J. | Medical Information and Communication Technology (ISMICT), 2016 10th International Symposium on, pp. 1\-5 | 2016 |
| [On the coverage of LPWANs: range evaluation and channel attenuation model for LoRa technology](https://ieeexplore.ieee.org/abstract/document/7377400) | Petajajarvi, J., Mikhaylov, K., Roivainen, A., Hanninen, T. and Pettissalo, M. | ITS Telecommunications (ITST), 2015 14th International Conference on, pp. 55\-59 | 2015 |
| [Long\-range IoT technologies: The dawn of LoRa™](https://link.springer.com/chapter/10.1007/978-3-319-27072-2_7) | Vangelista, L., Zanella, A. and Zorzi, M. | Future Access Enablers of Ubiquitous and Intelligent Infrastructures, pp. 51\-58 | 2015 |# Antenna Connectors

LoRaWAN gateways and end devices use different types of connectors including U.FL, SMA, RP\-SMA, Type\-N, and Type\-N PR for connecting antennas and interface cables.
## U.FL

U.FL (‘U’ stands for ultra\-small and ‘FL’ is just a series name assigned by Hirose ) connectors are commonly used in gateways and end devices where space is of critical concern (similar: I\-PEX, IPX, etc).
There are two types:
* U.FL Male \- These connectors are surface\-mounted and soldered directly to the printed circuit board.
* U.FL Female \- These connectors come as part of a pigtail, usually an ultra\-fine coaxial (fluorinated resin insulated) cable.

U.FL Male and U.FL Female connectors provide a very tight snap\-in connection. They are lightweight, require a small mounting area, and feature a very small mated height. When mating, the tactile click sensation confirms the complete electrical and mechanical connection.

The following table shows some of their applications:

| Application | Description |
| --- | --- |
|  | Interface Cable: SMA to U.FL. |
|  | Interface Cable: RP\-SMA to U.FL. |
|  | A half\-wave antenna with U.FL termination. |
|  | U.FL Male connector is soldered onto a PCB |
|  | Interface cable: I\-PEX to N\-Type cable. |
|  | I\-PEX to N\-Type Cables are used to provide an interface for connecting external antennas such as LoRa, WiFi, GPS, and LTE. |

## SMA

SMA connectors use a screw\-type coupling mechanism to create strong mechanical connections.
There are two types:
* SMA Male
* SMA Female

SMA Male connectors have a center pin and inner threads whereas SMA Female connectors have a center sleeve and outer threads.

Variations: The Reverse Polarity (RP) SMA connectors use the same outer shell, but change the gender of the inner pin. However, the signal polarity is not reversed. These reverse polarity connectors do not mate with SMA connectors.
There are two types:
* RP\-SMA Male
* RP\-SMA Female

RP\-SMA Male connectors have a center sleeve and inner threads whereas RP\- SMA Female connectors have a center pin and outer threads.

The following table shows some of their applications.

| Application | Description |
| --- | --- |
|  | An SMA Female Edge\-Mount connector is soldered onto a PCB. |
|  | Interface Cable: SMA to U.FL. |
|  | Interface Cable: RP\-SMA to U.FL. |
|  | An omni\-directional rubber ducky antenna with SMA connector. |

## N Type

N Type connectors are threaded, waterproof, medium\-size RF connectors that can be used to connect antennas (LoRa, LTE, GPS, WiFi, etc) directly or using cables.
There are two types:
* **N Type Male** \- these connectors have a center pin and inner threads. There is a ferrule between the center pin and the inner threads.

* **N Type Female** \- these connectors have a center sleeve and outer threads.

Variation: Like SMA connectors, N Type connectors have reverse polarity variations known as RP\-N Type connectors.
There are two types:
* **RP\-N Male** \- these connectors have a center sleeve and inner threads. There is a ferrule between the center pin and the inner threads.

* **RP\-N Female** \- these connectors have a center pin and outer threads.

The following table shows some of their applications.

| Application | Description |
| --- | --- |
|  | An antenna feeder line which consists of N Type Male (right) and N Type Female (left) connectors. |
|  | RAK7249 WisGate Edge Max uses 4 N\-Type connectors for connecting LoRa, LTE, GPS, and 2\.4G WiFi antennas. |# Antenna Types

In this tutorial, you will learn about some of the popular antenna types used with LoRaWAN end devices and gateways.
## Wire Antenna

Wire antennas are low\-cost and easy to build and work well in indoor environments. They are usually quarter\-wave antennas. Different frequencies need different wire lengths (calculated for quarter\-wave), for example, 3\.25 inches or 8\.2 cm for 868 MHz and 3 inches or 7\.8 cm for 915 MHz. Suitable for DIY projects. You must keep the antenna wire as vertical as possible for better performance.
Image courtesy of SparkFun Electronics
## PCB Antenna

These antennas are made from a copper trace drawn directly onto a PCB. Great for high volume production and suitable for indoor use.
Image courtesy of DesignSpark
## Spring Antenna

Spring antennas (also known as coil/helical antennas) are made from coiled wires (usually copper or aluminium) that reduce the antenna’s length. These antennas are suitable for use with LoRa modules with low transmission power (up to 100mW) and are also perfect for end devices with space constraints.

## Rubber Duck Antenna

These antennas are made from rubber/plastic (housing) and copper/aluminium (actual antenna). Rubber duck antennas are usually half wave or quarter wave. They terminated with SMA or RP\-SMA connector for directly connecting with the gateway/end device or for connecting through a pigtail. Ideal for LoRa nodes and indoor gateways.
Image courtesy of SparkFun Electronics
## Collinear Antenna

These high\-performance antennas are made from copper (actual antenna) and fiberglass (protective enclosure). A Collinear antenna is an array of dipoles made from copper wires in a straight line (some collinear antennas are made from coaxial cables). The radiating dipoles sum up all radiation intensities for providing higher performance and gain. These antennas are ideal for use with heavy\-duty, high\-power LoRaWAN outdoor gateways. However, they can be used with LoRaWAN nodes as well. They have Type N termination for connecting with gateways directly or through an interface cable. Collinear antennas can be vertically pole mounted. Suitable for harsh outdoor conditions because most of them are IP67 rated.
Image courtesy of HB Radiofrequency
The following figure shows a LoRaWAN collinear antenna wire with loops. The straight end of the antenna is connected to a Type N connector for termination. Then the looped copper wire is enclosed in high\-density fiberglass.
Image courtesy of IRNAS# dB, dBm, dBi and dBd

In this chapter briefly discuss some units that are used to measure the performance of transceivers (gateways and end devices) and antennas
## dB (decibel)

The decibel can be used to express the ratio of two physical quantities such as power, sound intensity, sound pressure, voltage, and current on a logarithmic scale. In LoRaWAN we use decibel to express the ratio between two power levels usually given in watt (W) or milliwatt (mW).
The power ratio, can be expressed in decibel using the formula,
N \= 10 log 10 (P out /P in ) dB
where P out is the output power and P in is the input power.

##### Note:

 When we are dealing with the power levels we use 10log units.

For example, if an amplifier turns a 1 W signal into a 1000 W signal, its power ratio can be expressed as:
N \= 10 log 10 (P out /P in ) \= 10 log 10 (1000/1\) \= 30 dB
Decibel doesn’t provide an absolute value. By looking at the decibel value you can’t say the input and output power of a device or cable etc, but you can say whether it offers a gain or a loss.
A power ratio greater than 0 dB is treated as a gain. For example, if an amplifier turns a 2 W signal into a 10 W signal, the power ratio is:
N \= 10 log 10 (P out /P in ) \= 10 log 10 (10/2\) \= 10 log 10 (5\) \= 6\.9 dB (gain)
A power ratio less than 0 dB is treated as a loss (negative gain or attenuation). For example, if 10 W of power is fed into a cable but only 8 W is measured at the output, the power ratio is:
N \= 10 log 10 (P out /P in ) \= 10 log 10 (8/10\) \= 10 log 10 (0\.8\) \= \-0\.9 dB (loss)
The power ratio of 0 dB means there is no gain or loss.
## dBm (decibel per milliwatt)

If you use the reference input power (P in ) of 1 mW the power ratio, can be expressed in dBm:
N \= 10 log 10 (P out / 1\) dBm
By using the above formula, P out can be expressed in mW which is an absolute value.
P out /P in \= 10 (N/ 10\)
P out \= 10 (N/ 10\) mW
For example, if a LoRaWAN gateway has an output power of 22 dBm, how much power does it generate in W?
P out \= 10 (N / 10\) \= 10 (22 / 10\) \= 10 (2\.2\) \= 158\.48 mW \= 0\.158 W
## Rule of 10s and 3s

By using only 10s and 3s, one can easily convert a dBm value to its corresponding absolute power value without using the logarithmic scale.
* 10 dB \= x10 (makes output power 10 times as the input power, for example, input\=10 W and output\=100 W)
* \-10 dB \= ÷10 (makes output power 1/10 times as the input power, for example, input\=100 W and output\=10 W)
* 3 dB \= x2 (doubles the power, for example, input\=5 W and output\=10 W)
* \-3 dB \= ÷2 (halves the power, for example, input\=10 W and output\=5 W)

For example, if you want to convert 1 dBm its corresponding absolute power value, 1 can be written as, 10 \-3 \-3 \-3\.
Then apply the rule:
1 dB \= 10 dB \-3 dB \-3 dB \-3 dB \= x10 ÷2 ÷2 ÷2 \= 1\.25
Remember P in is always 1 mW and ’m' in dBm stands for milliwatt. So we multiply the above answer by 1 mW.
1 dBm \= 1 mW x 1\.25 \= 1\.25 mW
When you write any dBm value using 10s and 3s remember,
* If possible avoid using 3s
* Never use more than five 3s

Let’s take another example:
For example, if a LoRaWAN gateway has an output power of 17 dBm, how much power does it generate in mW?
17 can be written as, 10 \+10 \-3
Then apply the rule:
17 dB \= 10 dB \+10 dB \-3 dB \= x10 x10 ÷2 \= 50
17 dBm \= 1 mW x 50 \= 50 mW
## Antenna gains

The units dBi and dBd are used to express antenna gains.
### dBi (decibel relative to isotropic)

The gain of an antenna can be measured relative to an isotropic antenna and is expressed in dBi. An isotropic antenna is a hypothetical antenna that radiates power uniformly in all directions. The gain of an isotropic antenna is 0 dB which means it has no gain or loss.
### dBd (decibel relative to dipole)

The gain of an antenna can be measured relative to a reference dipole antenna and is expressed in dBd. A reference dipole antenna offers a fixed 2\.15 dB of gain over an isotropic antenna.
The following equation represents the relationship between dBi and dBd:
dBi \= dBd \+ 2\.15 dB

X dBd \= X dBi \- 2\.15 \= 5 \- 2\.15 \= 2\.85 dBd
2. Convert 2 dBd to dBi.

X dBi \= X dBd \+ 2\.15 \= 2 \+ 2\.15 \= 4\.15 dBi# EIRP and ERP

LoRaWAN gateways and end devices consist of radios (also called transceivers) that are capable of transmitting and receiving LoRa modulated radio signals. A radio needs an antenna to transmit or receive signals. The connection between the radio and the antenna is usually made by a piece of cable (for some devices it is a PCB trace). When transmitting, radio (transmitter) and antenna provide signal gain while antenna cable and connectors affect signal loss.
## EIRP

EIRP (Effective Isotropic Radiated Power) is the total power radiated by an isotropic antenna in a single direction. In this case, the antenna gain must be expressed in dBi.

The EIRP of a unit that consists of a transmitter, an antenna, and a cable can be calculated using the formula,
EIRP \= Transmitter output power (dBm) \+ Antenna gain (dBi) \- Cable loss (dB)
where the transmitter power in dBm, antenna gain in dBi, and cable loss in dB.
Question: Calculate the EIRP value of the following unit that consists of a LoRaWAN gateway, an antenna cable, and an antenna.

EIRP \= Transmitter output power (dBm) \+ Antenna gain (dBi) \- Cable loss (dB)
EIRP \= 20 \+3 \-7 \= 16 dBm
## ERP

Sometimes, the maximum output power is measured in ERP (Effective Radiated Power) instead of the EIRP.
ERP is the total power radiated by an actual antenna relative to a half\-wave dipole antenna. In this case, the antenna gain must be expressed in dBd.

The ERP of a unit that consists of a transmitter, an antenna, and a cable can be calculated using the formula,
ERP \= Transmitter output power (dBm) \+ Antenna gain (dBd) \- Cable loss (dB)
where the transmitter power in dBm, antenna gain in dBd, and cable loss in dB.
ERP is also expressed in dBm.
Question: Calculate the ERP value of the following unit that consists of an end device, an antenna cable, and an antenna.

ERP \= Transmitter output power (dBm) \+ Antenna gain (dBd) \- Cable loss (dB)
ERP \= 20 \+0\.85 \-7 \= 13\.85 dBm
## Conversion between EIRP and ERP

You can easily convert EIRP to ERP and vice versa using the following equation:
EIRP (dBm) \= ERP (dBm) \+ 2\.15
Question: Convert the EIRP value 16 dBm to ERP.
ERP (dBm) \= EIRP (dBm) \- 2\.15
ERP (dBm) \= 16 \-2\.15 \= 13\.85 dBm
## dBm to watts conversion

EIRP or ERP values can be converted to watts (W) or milliwatts (mW), for example, EIRP 16 dBm is equivalent to 40 mW.
Read the section Rule of 10s and 3s in our guide dB, dBm, dBi and dBd to learn how to convert dBm to watts or milliwatts.
If you want to quickly convert dBm to watts or milliwatts without calculating by hand, an online tool is available at RapidTables
## Regulations

The maximum transmission power of a gateway or an end device is region specific and is regulated by the respective regulatory authorities. For example, in Europe, it is 25 mW ERP (\+16 dBm EIRP) and is regulated by ETSI (European Telecommunications Standards Institute).
Read the LoRaWAN® Regional Parameters 1\.0\.3 to find the maximum allowed EIRP in other regions.
Adjust the following parameters to prevent EIRP/ERP/milliwatts thresholds from being exceeded.
* Transmitter output power
* Cable and connector attenuation
* Antenna gain# Forward Error Correction and Code Rate

Forward Error Correction is a process of adding redundant bits to the data to be transmitted. During the transmission, data may get corrupted by interference (changes from 0 to 1 / 1 to 0\). These error correction bits are used at the receivers for restoring corrupted bits.
The Code Rate of a forward error correction expresses the proportion of bits in a data stream that actually carry useful information.
There are 4 code rates used in LoRaWAN:
* 4/5
* 4/6
* 5/7
* 4/8

For example, if the code rate is 5/7, for every 5 bits of useful information, the coder generates a total of 7 bits of data, of which 2 bits are redundant.# LoRa Physical Layer Packet Format

LoRa uses two types of packet formats for data transmission: explicit and implicit.
In explicit mode, a LoRa packet includes the following elements:
* Preamble is used to synchronize the receiver with the transmitter. It MUST consist of 8 symbols for all regions as mentioned in the LoRaWAN Regional Parameters document. However, the radio transmitter will add another 4\.25 symbols resulting in a final preamble length of 8 \+ 4\.25 \= 12\.25 symbols.
* PHDR (Physical Header) is an optional element only present in the explicit mode that contains information about payload size and CRC (Cyclic Redundancy Check).
* PHDR\_CRC (Header CRC) is an optional field that contains an error detecting code for correcting errors in header.

The PHDR and PHDR\_CRC are encoded with the Coding Rate of 4/8\.
* PHYPayload contains the complete frame generated by the MAC layer. The maximum payload size varies by DR (Data Rate) and is region\-specific.
* CRC is an optional field that contains an error detecting code for correcting errors in the payload of uplink messages.

The PHYPayload and CRC are encoded with one of the Coding Rates (4/5, 4/6, 4/7, or 4/8\). The complete frame is then sent using one of the Spreading Factors (SF \= 7 to 12\).
The following figure shows the physical layer structure of uplink and downlink packets that uses explicit mode.

In implicit mode, the header is removed from the packet where the payload size and Coding Rate are fixed or known in advance.
Beacons use LoRa radio packet implicit mode for sending time synchronizing information from gateways to the end devices.
The following figure shows the structure of a LoRa packet that uses the implicit mode.# LoRaWAN® Concentrators

Semtech’s LoRa concentrators power all LoRa communication.
Semtech has produced four LoRa concentrators and all LoRaWAN gateways use one of these devices to receive and transmit LoRa messages.
Read about all of Semtech’s LoRa products on their LoRa product page .
Additionally, RAK Wireless provides a great breakdown of available LoRa hardware .
This page provides a quick description of each of the LoRa concentrators.
## SX1301

The SX1301 is Semtech’s first outdoor LoRaWAN concentrator, designed to provide worldwide LoRaWAN gateway capability in ISM bands. It is the first digital baseband chip to integrate Semtech’s LoRa Concentrator IP.
* Up to \-142\.5dBm sensitivity with SX1257 Tx/Rx front\-end
* 70 dB CW interferer rejection at 1 MHz offset
* Able to operate with negative SNR, CCR up to 9dB
* Emulates 49x LoRa demodulators and 1x (G)FSK demodulator
* Dual digital TX\&RX radio front\-end interfaces
* 10 programmable parallel demodulation paths
* Dynamic data\-rate (DDR) adaptation
* True antenna diversity or simultaneous dual\-band operation

The SX1301 is succeeded by the SX1302\.
Read more about the SX1301 on Semtech’s SX1301 product page .
## SX1302

The SX1302 succeeds the SX1301\. It reduces current consumption, has better thermal capability, is cheaper, and can handle more traffic than its predecessor.
* Up to \-141 dBm sensitivity with SX1250 Tx/Rx front\-end
* 125 kHz LoRa reception with:
	+ 8 x 8 channels LoRa® packet detectors
	+ 8 x SF5\-SF12 LoRa® demodulators
	+ 8 x SF5\-SF10 LoRa® demodulators
* 125 / 250 / 500 kHz LoRa® demodulator
* (G)FSK demodulator
* Direct interface to Semtech transceivers
* SX1255, SX1257 and SX1250
* Single 32 MHz clock

The SX1302 is succeeded by the SX1303\.
Read more about the SX1302 on Semtech’s SX1302 product page .
## SX1303

The SX1303 succeeds the SX1302, and is Semtech’s most modern LoRa concentrator. It is pin and size compatible to its predecessor, and further reduces current, improves thermal capability, and is cheaper. In addition, it supports Time Difference of Arrival (TDOA) geolocation via a new Fine Timestamp capability.
* Fine Timestamp
* Up to \-141dBm sensitivity with SX1250 Tx/Rx front\-end
* 125kHz LoRa reception with:
	+ 8 x 8 channels LoRa packet detectors
	+ 8 x SF5\-SF12 LoRa demodulators
	+ 8 x SF5\-SF10 LoRa demodulators
	+ Up to 8 packets can be received simultaneously when Fine Timestamp is enabled
* 125/250/500kHz LoRa demodulator
* (G)FSK demodulator
* Direct interface to Semtech transceivers
* SX1255, SX1257 and SX1250
* Single 32MHz clock

Read more about the SX1303 on Semtech’s SX1303 product page .
## SX1308

The SX1308 is a less sensitive concentrator than the SX1301/2/3\. It is designed for indoor gateways.
* Up to \-139dBm sensitivity with SX1257 or SX1255 Tx/Rx front\-end
* 70dB CW interferer rejection at 1MHz offset
* Able to operate with negative SNR
	+ CCR up to 9dB
* Emulates 49x LoRa demodulators and 1x (G)FSK demodulator
* Dual digital Tx \& Rx radio front\-end interfaces
* 10 programmable parallel demodulation paths
* Dynamic data\-rate adaptation (ADR)
* True antenna diversity or simultaneous dual\-band operation

Read more about the SX1308 on Semtech’s SX1308 product page .# LoRaWAN® Transceivers

Besides gateway chips described in the LoRaWAN Concentrators section, an important part of the LoRa portfolio are transceiver chips.
Semtech has produced a few series of LoRa Core™ sub\-GHz transceiver chips, like SX127x, SX126x and LLCC68\. Recently, Semtech has also produced the LR1110 solution that includes a LoRa transceiver as part of the LoRa Edge™ platform.
This page provides a quick description of the most commonly used LoRa transceivers.
## SX127x

The SX127x series transceivers were one of the first LoRa transceivers on the market, providing ultra\-long range spread spectrum communication and high interference immunity, while minimizing current consumption. All chips from this series have similar characteristics. The main difference is that the SX1272/73 transceivers operate in the 860\-1000MHz, while the SX1276/77/78/79 operate in the 137\-1020MHz frequency band.
* LoRa Modem
* 157dB maximum link budget for SX1272/73, 168dB for SX1276/77/78/79
* \+20dBm at 100mW constant RF output vs V supply
* Up to \+14dBm TX power using high efficiency power amplifier (PA)
* Programmable bit rate up to 300kbps for FSK
* High sensitivity, down to \-137dBm for SX1272/73, \-148dBm for SX1276/77/78/79
* Bullet\-proof front end, with IIP3 \= \-12\.5dBm for SX1272/73, IIP3\= \-11dBm for SX1276/77/78/79
* Excellent blocking immunity
* Low RX current of 10mA and 100nA register retention for SX1272/73, 9\.9mA and 200nA register retention for for SX1276/77/78/79
* Fully integrated synthesizer with a resolution of 61Hz
* FSK, GFSK, MSK, GMSK, LoRa and OOK modulation
* Built\-in bit synchronizer for clock recovery
* Preamble detection
* 127dB Dynamic Range RSSI
* Automatic RF Sense and Channel Activity Detection (CAD) with ultra\-fast Automatic Frequency Control (AFC)
* Packet engine up to 256 bytes with CRC
* Built\-in temperature sensor and low battery indicator

Read more about the SX127x transceiver series on Semtech’s product page .
## SX126x

The successor of the SX127x is the SX126x series. All chips from the SX126x series are very similar, half\-duplex transceivers for long range wireless applications. Their main features are low consumption for long battery life, and high TX power thanks to the highly efficient integrated PAs. Besides LoRa modulation, they support (G)FSK modulation for legacy use cases. The main difference between these devices is in the last stage of the transmit chain, where the difference in the maximum TX power arises. The SX1261 and SX1262 have a global frequency coverage, while the SX1268 operates in China frequency bands.
* LoRa and FSK Modem
* 170 dB maximum link budget for SX1262 and SX1268
* Maximum TX power \+15 dBm for SX1261 (using DC\-DC converter or LDO), \+22 dBm for SX1261 and SX1268 (under the battery supply)
* Low RX current of 4\.2 mA
* Integrated DC\-DC converter and LDO
* Programmable bit rate up to 62\.5 kbps for LoRa and 300 kbps for FSK
* High sensitivity, down to \-148 dBm for LoRa
* 88 dB blocking immunity at 1 MHz offset for LoRa
* Co\-channel GMSK rejection of up to 19 dB for LoRa
* FSK, GFSK, MSK, GMSK and LoRa modulation, plus Long Range FHSS modulations for SX1262
* Automatic CAD with ultra\-fast AFC

Read more about the SX126x transceiver series on Semtech’s product page .
## LLCC68

Semtech’s LLCC68 is a sub\-GHz LoRa RF transceiver, intended for medium range indoor, and indoor to outdoor smart home wireless applications. It is pin\-to\-pin compatible with SX1262 and their features are very similar. The main difference is that the LLCC68 can transmit up to \+22 dBm using highly integrated PAs, the maximum link budget it provides is 151 dB and its sensitivity can go down to \-129 dBm. Also, it does not support all LoRaWAN rates \- the supported ones include SF7 to SF9 at 125kHz, SF7 to SF10 at 250kHz, and SF7 to SF11 at 500kHz.
Read more about the LLCC68 transceiver on Semtech’s product page .
## LR1110

The LR1110 is a solution that integrates a high sensitivity half\-duplex LoRa transceiver, long range FHSS modulator, multi\-constellation scanner and passive Wi\-Fi AP MAC address scanner.
The main features of the transceiver:
* LoRa and (G)FSK modulation support
* Worldwide ISM frequency bands support in the range 150\-960MHz
* Low Noise Figure RX front\-end for enhanced LoRa/(G)FSK sensitivity
* High power PA path \+22dBm
* High efficiency PA path \+15dBm
* Long Range FHSS modulator
* Integrated PA regulator supply selector to simplify dual power \+15/\+22dBm with one board implementation
* Able to support worldwide multi\-region bill of materials, the circuit adapts to matching network to satisfy regulatory limits
* Fully compatible with SX126x devices and the LoRaWAN® standard defined by the LoRa Alliance®

The main features of the multi\-purpose radio front\-end that targets geolocation capabilities:
* GNSS (GPS, BeiDou, geostationary) low\-power scanning
* 802\.11b/g/n Wi\-Fi ultra\-low\-power passive scanning
* 150\-2700MHz continuous frequency synthesizer range
* High bandwidth RX ADC (up to 24MHz Double Side Band)
* Digital baseband processing# NetID and DevAddr Prefix Assignments

| **NetID** | **DevAddr Prefix** | **DevAddr Range** | **Operator** | **Region** |
| --- | --- | --- | --- | --- |
| `000000` | `00000000/7` | `00000000` \- `01FFFFFF` | Private/experimental nodes | Local |
| `000001` | `02000000/7` | `02000000` \- `03FFFFFF` | Private/experimental nodes | Local |
| `000002` | `04000000/7` | `04000000` \- `05FFFFFF` | Actility | World |
| `000003` | `06000000/7` | `06000000` \- `07FFFFFF` | Proximus | Europe |
| `000004` | `08000000/7` | `08000000` \- `09FFFFFF` | Swisscom | World |
| `000005` | `0A000000/7` | `0A000000` \- `0BFFFFFF` |  |  |
| `000006` | `0C000000/7` | `0C000000` \- `0DFFFFFF` |  |  |
| `000007` | `0E000000/7` | `0E000000` \- `0FFFFFFF` | Bouygues Telecom | World |
| `000008` | `10000000/7` | `10000000` \- `11FFFFFF` | Orbiwise | World |
| `000009` | `12000000/7` | `12000000` \- `13FFFFFF` | SENET | World |
| `00000A` | `14000000/7` | `14000000` \- `15FFFFFF` | KPN | Europe |
| `00000B` | `16000000/7` | `16000000` \- `17FFFFFF` | EveryNet | Russia |
| `00000C` | `18000000/7` | `18000000` \- `19FFFFFF` |  |  |
| `00000D` | `1A000000/7` | `1A000000` \- `1BFFFFFF` | SK Telecom | World |
| `00000E` | `1C000000/7` | `1C000000` \- `1DFFFFFF` | SagemCom | World |
| `00000F` | `1E000000/7` | `1E000000` \- `1FFFFFFF` | Orange | World |
| `000010` | `20000000/7` | `20000000` \- `21FFFFFF` | A2A Smart City | World |
| `000011` | `22000000/7` | `22000000` \- `23FFFFFF` |  |  |
| `000012` | `24000000/7` | `24000000` \- `25FFFFFF` | Kerlink | World |
| `000013` | `26000000/7` | `26000000` \- `27FFFFFF` | **The Things Network** | World |
| `000014` | `28000000/7` | `28000000` \- `29FFFFFF` |  |  |
| `000015` | `2A000000/7` | `2A000000` \- `2BFFFFFF` | Cisco Systems | World |
| `000016` | `2C000000/7` | `2C000000` \- `2DFFFFFF` |  |  |
| `000017` | `2E000000/7` | `2E000000` \- `2FFFFFFF` | MultiTech Systems | World |
| `000018` | `30000000/7` | `30000000` \- `31FFFFFF` | Loriot | World |
| `000019` | `32000000/7` | `32000000` \- `33FFFFFF` | NNNCo | World |
| `00001A` | `34000000/7` | `34000000` \- `35FFFFFF` |  |  |
| `00001B` | `36000000/7` | `36000000` \- `37FFFFFF` |  |  |
| `00001C` | `38000000/7` | `38000000` \- `39FFFFFF` |  |  |
| `00001D` | `3A000000/7` | `3A000000` \- `3BFFFFFF` |  |  |
| `00001E` | `3C000000/7` | `3C000000` \- `3DFFFFFF` |  |  |
| `00001F` | `3E000000/7` | `3E000000` \- `3FFFFFFF` | Axatel | Italy |
| `000020` | `40000000/7` | `40000000` \- `41FFFFFF` |  |  |
| `000021` | `42000000/7` | `42000000` \- `43FFFFFF` |  |  |
| `000022` | `44000000/7` | `44000000` \- `45FFFFFF` | Comcast | World |
| `000023` | `46000000/7` | `46000000` \- `47FFFFFF` | Ventia | World |
| `000024` | `48000000/7` | `48000000` \- `49FFFFFF` |  |  |
| `000025` | `4A000000/7` | `4A000000` \- `4BFFFFFF` |  |  |
| `000026` | `4C000000/7` | `4C000000` \- `4DFFFFFF` |  |  |
| `000027` | `4E000000/7` | `4E000000` \- `4FFFFFFF` |  |  |
| `000028` | `50000000/7` | `50000000` \- `51FFFFFF` |  |  |
| `000029` | `52000000/7` | `52000000` \- `53FFFFFF` |  |  |
| `00002A` | `54000000/7` | `54000000` \- `55FFFFFF` |  |  |
| `00002B` | `56000000/7` | `56000000` \- `57FFFFFF` |  |  |
| `00002C` | `58000000/7` | `58000000` \- `59FFFFFF` |  |  |
| `00002D` | `5A000000/7` | `5A000000` \- `5BFFFFFF` |  |  |
| `00002E` | `5C000000/7` | `5C000000` \- `5DFFFFFF` |  |  |
| `00002F` | `5E000000/7` | `5E000000` \- `5FFFFFFF` |  |  |
| `000030` | `60000000/7` | `60000000` \- `61FFFFFF` | SoftBank | World |
| `000031` | `62000000/7` | `62000000` \- `63FFFFFF` |  |  |
| `000032` | `64000000/7` | `64000000` \- `65FFFFFF` |  |  |
| `000033` | `66000000/7` | `66000000` \- `67FFFFFF` |  |  |
| `000034` | `68000000/7` | `68000000` \- `69FFFFFF` |  |  |
| `000035` | `6A000000/7` | `6A000000` \- `6BFFFFFF` | Shenzhen Tencent Computer Systems Company Limited | China |
| `000036` | `6C000000/7` | `6C000000` \- `6DFFFFFF` | Netze BW GmbH | World |
| `000037` | `6E000000/7` | `6E000000` \- `6FFFFFFF` | Tektelic | World |
| `000038` | `70000000/7` | `70000000` \- `71FFFFFF` | Charter Communicaton | USA |
| `000039` | `72000000/7` | `72000000` \- `73FFFFFF` | Amazon | World |
| `600000` | `E0000000/15` | `E0000000` \- `E001FFFF` | RESERVED |  |
| `600001` | `E0020000/15` | `E0020000` \- `E003FFFF` | Digita | Finland |
| `600002` | `E0040000/15` | `E0040000` \- `E005FFFF` | Netmore | Europe |
| `600003` | `E0060000/15` | `E0060000` \- `E007FFFF` | QuaeNet Inc. | World |
| `600004` | `E0080000/15` | `E0080000` \- `E009FFFF` | eleven\-x | North and South America |
| `600005` | `E00A0000/15` | `E00A0000` \- `E00BFFFF` | IoT Network AS | World |
| `600006` | `E00C0000/15` | `E00C0000` \- `E00DFFFF` |  |  |
| `600007` | `E00E0000/15` | `E00E0000` \- `E00FFFFF` | EDF | World |
| `600008` | `E0100000/15` | `E0100000` \- `E011FFFF` | Unidata | Italy |
| `600009` | `E0120000/15` | `E0120000` \- `E013FFFF` |  |  |
| `60000A` | `E0140000/15` | `E0140000` \- `E015FFFF` | Öresundskraft | Scandinavia |
| `60000B` | `E0160000/15` | `E0160000` \- `E017FFFF` |  |  |
| `60000C` | `E0180000/15` | `E0180000` \- `E019FFFF` |  |  |
| `60000D` | `E01A0000/15` | `E01A0000` \- `E01BFFFF` |  |  |
| `60000E` | `E01C0000/15` | `E01C0000` \- `E01DFFFF` | Spark | World |
| `60000F` | `E01E0000/15` | `E01E0000` \- `E01FFFFF` |  |  |
| `600010` | `E0200000/15` | `E0200000` \- `E021FFFF` | Senet | World |
| `600011` | `E0220000/15` | `E0220000` \- `E023FFFF` |  |  |
| `600012` | `E0240000/15` | `E0240000` \- `E025FFFF` |  |  |
| `600013` | `E0260000/15` | `E0260000` \- `E027FFFF` | Actility | World |
| `600014` | `E0280000/15` | `E0280000` \- `E029FFFF` | Kerlink | World |
| `600015` | `E02A0000/15` | `E02A0000` \- `E02BFFFF` |  |  |
| `600016` | `E02C0000/15` | `E02C0000` \- `E02DFFFF` | Cisco | World |
| `600017` | `E02E0000/15` | `E02E0000` \- `E02FFFFF` | Schneider Electric | Global |
| `600018` | `E0300000/15` | `E0300000` \- `E031FFFF` | Minol ZENNER Connect GmbH | Global |
| `600019` | `E0320000/15` | `E0320000` \- `E033FFFF` |  |  |
| `60001A` | `E0340000/15` | `E0340000` \- `E035FFFF` | NEC Corporation | Japan |
| `60001B` | `E0360000/15` | `E0360000` \- `E037FFFF` | Shenzhen Tencent Computer Systems Company Limited | China |
| `60001C` | `E0380000/15` | `E0380000` \- `E039FFFF` | MachineQ/Comcast | World |
| `60001D` | `E03A0000/15` | `E03A0000` \- `E03BFFFF` | NTT (Nippon Telephone and Telegraph) | Japan |
| `60001E` | `E03C0000/15` | `E03C0000` \- `E03DFFFF` |  |  |
| `60001F` | `E03E0000/15` | `E03E0000` \- `E03FFFFF` | KPN | Europe |
| `600020` | `E0400000/15` | `E0400000` \- `E041FFFF` | Spectrum | USA |
| `600021` | `E0420000/15` | `E0420000` \- `E043FFFF` | Microshare Inc. | World |
| `600022` | `E0440000/15` | `E0440000` \- `E045FFFF` |  |  |
| `600023` | `E0460000/15` | `E0460000` \- `E047FFFF` |  |  |
| `600024` | `E0480000/15` | `E0480000` \- `E049FFFF` | Netze BW GmbH | World |
| `600025` | `E04A0000/15` | `E04A0000` \- `E04BFFFF` | Tektelic | World |
| `600026` | `E04C0000/15` | `E04C0000` \- `E04DFFFF` |  |  |
| `600027` | `E04E0000/15` | `E04E0000` \- `E04FFFFF` | Birdz | World |
| `600028` | `E0500000/15` | `E0500000` \- `E051FFFF` | Charter Communication | USA |
| `600029` | `E0520000/15` | `E0520000` \- `E053FFFF` | Machines Talk | Saudi Arabia |
| `60002A` | `E0540000/15` | `E0540000` \- `E055FFFF` | Neptune Technology Group | North America |
| `60002B` | `E0560000/15` | `E0560000` \- `E057FFFF` | Amazon | World |
| `60002C` | `E0580000/15` | `E0580000` \- `E059FFFF` | myDevices | World |
| `60002D` | `E05A0000/15` | `E05A0000` \- `E05BFFFF` | Decentralized Wireless Foundation Inc | World |
| `60002E` | `E05C0000/15` | `E05C0000` \- `E05DFFFF` | Eutelsat S.A. | World |
| `C00000` | `FC000000/22` | `FC000000` \- `FC0003FF` | RESERVED |  |
| `C00001` | `FC000400/22` | `FC000400` \- `FC0007FF` |  |  |
| `C00002` | `FC000800/22` | `FC000800` \- `FC000BFF` | ResIOT | World |
| `C00003` | `FC000C00/22` | `FC000C00` \- `FC000FFF` | SYSDEV | World |
| `C00004` | `FC001000/22` | `FC001000` \- `FC0013FF` |  |  |
| `C00005` | `FC001400/22` | `FC001400` \- `FC0017FF` | Macnica | Japan |
| `C00006` | `FC001800/22` | `FC001800` \- `FC001BFF` |  |  |
| `C00007` | `FC001C00/22` | `FC001C00` \- `FC001FFF` |  |  |
| `C00008` | `FC002000/22` | `FC002000` \- `FC0023FF` | Definium Technologies | World |
| `C00009` | `FC002400/22` | `FC002400` \- `FC0027FF` |  |  |
| `C0000A` | `FC002800/22` | `FC002800` \- `FC002BFF` | SenseWay | Japan |
| `C0000B` | `FC002C00/22` | `FC002C00` \- `FC002FFF` | 3S | Tunisia |
| `C0000C` | `FC003000/22` | `FC003000` \- `FC0033FF` |  |  |
| `C0000D` | `FC003400/22` | `FC003400` \- `FC0037FF` | Packetworx | Philippines |
| `C0000E` | `FC003800/22` | `FC003800` \- `FC003BFF` |  |  |
| `C0000F` | `FC003C00/22` | `FC003C00` \- `FC003FFF` | Antenna Hungaria Co | Hungary |
| `C00010` | `FC004000/22` | `FC004000` \- `FC0043FF` |  |  |
| `C00011` | `FC004400/22` | `FC004400` \- `FC0047FF` |  |  |
| `C00012` | `FC004800/22` | `FC004800` \- `FC004BFF` | Netmore | Europe |
| `C00013` | `FC004C00/22` | `FC004C00` \- `FC004FFF` | Lyse AS | Norway |
| `C00014` | `FC005000/22` | `FC005000` \- `FC0053FF` | VTC Digicom | Vietnam |
| `C00015` | `FC005400/22` | `FC005400` \- `FC0057FF` | Machines Talk | Saudi Arabia |
| `C00016` | `FC005800/22` | `FC005800` \- `FC005BFF` | Schneider Electric | Global |
| `C00017` | `FC005C00/22` | `FC005C00` \- `FC005FFF` | Connexin | UK |
| `C00018` | `FC006000/22` | `FC006000` \- `FC0063FF` | Minol ZENNER Connect GmbH | Global |
| `C00019` | `FC006400/22` | `FC006400` \- `FC0067FF` | Telekom Srbija | Serbia |
| `C0001A` | `FC006800/22` | `FC006800` \- `FC006BFF` | REQUEA | World |
| `C0001B` | `FC006C00/22` | `FC006C00` \- `FC006FFF` | Sensor Network Services | Austria |
| `C0001C` | `FC007000/22` | `FC007000` \- `FC0073FF` |  |  |
| `C0001D` | `FC007400/22` | `FC007400` \- `FC0077FF` | Boston Networks Limited | Europe |
| `C0001E` | `FC007800/22` | `FC007800` \- `FC007BFF` |  |  |
| `C0001F` | `FC007C00/22` | `FC007C00` \- `FC007FFF` | mcf88 SRL | World |
| `C00020` | `FC008000/22` | `FC008000` \- `FC0083FF` | NEC Corporation | Japan |
| `C00021` | `FC008400/22` | `FC008400` \- `FC0087FF` | Hiber | World |
| `C00022` | `FC008800/22` | `FC008800` \- `FC008BFF` |  |  |
| `C00023` | `FC008C00/22` | `FC008C00` \- `FC008FFF` |  |  |
| `C00024` | `FC009000/22` | `FC009000` \- `FC0093FF` | NTT (Nippon Telephone and Telegraph) | Japan |
| `C00025` | `FC009400/22` | `FC009400` \- `FC0097FF` | International Centre for Free and Open Source Software (ICFOSS) | India |
| `C00026` | `FC009800/22` | `FC009800` \- `FC009BFF` |  |  |
| `C00027` | `FC009C00/22` | `FC009C00` \- `FC009FFF` |  |  |
| `C00028` | `FC00A000/22` | `FC00A000` \- `FC00A3FF` | Lacuna Space | World |
| `C00029` | `FC00A400/22` | `FC00A400` \- `FC00A7FF` | Andorra Telecom | Principality of Andorra |
| `C0002A` | `FC00A800/22` | `FC00A800` \- `FC00ABFF` | Xiamen Milesight IoT Co., Ltd. | World |
| `C0002B` | `FC00AC00/22` | `FC00AC00` \- `FC00AFFF` | Grenoble Alps University | France |
| `C0002C` | `FC00B000/22` | `FC00B000` \- `FC00B3FF` |  |  |
| `C0002D` | `FC00B400/22` | `FC00B400` \- `FC00B7FF` |  |  |
| `C0002E` | `FC00B800/22` | `FC00B800` \- `FC00BBFF` | Spectrum | USA |
| `C0002F` | `FC00BC00/22` | `FC00BC00` \- `FC00BFFF` | Afnic | France |
| `C00030` | `FC00C000/22` | `FC00C000` \- `FC00C3FF` |  |  |
| `C00031` | `FC00C400/22` | `FC00C400` \- `FC00C7FF` |  |  |
| `C00032` | `FC00C800/22` | `FC00C800` \- `FC00CBFF` | Microshare Inc. | World |
| `C00033` | `FC00CC00/22` | `FC00CC00` \- `FC00CFFF` | HEIG\-VD | Switzerland |
| `C00034` | `FC00D000/22` | `FC00D000` \- `FC00D3FF` |  |  |
| `C00035` | `FC00D400/22` | `FC00D400` \- `FC00D7FF` |  |  |
| `C00036` | `FC00D800/22` | `FC00D800` \- `FC00DBFF` |  |  |
| `C00037` | `FC00DC00/22` | `FC00DC00` \- `FC00DFFF` | Alperia Fiber | Italy |
| `C00038` | `FC00E000/22` | `FC00E000` \- `FC00E3FF` | First Snow Co., Ltd | Republic of Korea |
| `C00039` | `FC00E400/22` | `FC00E400` \- `FC00E7FF` | Acklio | World |
| `C0003A` | `FC00E800/22` | `FC00E800` \- `FC00EBFF` |  |  |
| `C0003B` | `FC00EC00/22` | `FC00EC00` \- `FC00EFFF` | Meshed Pty Ltd | Australia, New Zealand |
| `C0003C` | `FC00F000/22` | `FC00F000` \- `FC00F3FF` | Birdz | World |
| `C0003D` | `FC00F400/22` | `FC00F400` \- `FC00F7FF` | Arthur D Riley \& Co Ltd | Asia Pacific |
| `C0003E` | `FC00F800/22` | `FC00F800` \- `FC00FBFF` | Komro GmbH | Germany, Austria, Switzerland |
| `C0003F` | `FC00FC00/22` | `FC00FC00` \- `FC00FFFF` | RSAWEB | South Africa |
| `C00040` | `FC010000/22` | `FC010000` \- `FC0103FF` | Ceske Radiokomunikace | Czech Republic |
| `C00041` | `FC010400/22` | `FC010400` \- `FC0107FF` | CM Systems LLC | World |
| `C00042` | `FC010800/22` | `FC010800` \- `FC010BFF` | MIOT Melita.io Technology GmbH | Germany |
| `C00043` | `FC010C00/22` | `FC010C00` \- `FC010FFF` | PROESYS S.r.l. | World |
| `C00044` | `FC011000/22` | `FC011000` \- `FC0113FF` | MeWe, Inc | World |
| `C00045` | `FC011400/22` | `FC011400` \- `FC0117FF` | Alpha\-Omega Technology GmbH \& Co. KG | Europe |
| `C00046` | `FC011800/22` | `FC011800` \- `FC011BFF` | SSE Contracting Limted t/a Mayflower Smart Control | UK, Ireland |
| `C00047` | `FC011C00/22` | `FC011C00` \- `FC011FFF` | VEGA Grieshaber KG | World |
| `C00048` | `FC012000/22` | `FC012000` \- `FC0123FF` | Afghan Wireless Communication Company | Afghanistan |
| `C00049` | `FC012400/22` | `FC012400` \- `FC0127FF` | API\-K | Europe |
| `C0004A` | `FC012800/22` | `FC012800` \- `FC012BFF` | Decstream LLC | Russian Federation |
| `C0004B` | `FC012C00/22` | `FC012C00` \- `FC012FFF` | Nova Track Ltd | World |
| `C0004C` | `FC013000/22` | `FC013000` \- `FC0133FF` | IMT Atlantique | France |
| `C0004D` | `FC013400/22` | `FC013400` \- `FC0137FF` | Machines Talk | Saudi Arabia |
| `C0004E` | `FC013800/22` | `FC013800` \- `FC013BFF` | Yosensi Sp. z o.o. | World |
| `C0004F` | `FC013C00/22` | `FC013C00` \- `FC013FFF` | The Saira 2\.0, LLC dba The IoT Solutions | Guam, USA |
| `C00050` | `FC014000/22` | `FC014000` \- `FC0143FF` | Neptune Technology Group | North America |
| `C00051` | `FC014400/22` | `FC014400` \- `FC0147FF` | myDevices | World |
| `C00052` | `FC014800/22` | `FC014800` \- `FC014BFF` | Savoie Mont Blanc University | France |
| `C00053` | `FC014C00/22` | `FC014C00` \- `FC014FFF` | Decentralized Wireless Foundation Inc | World |
| `C00054` | `FC015000/22` | `FC015000` \- `FC0153FF` | X\-Telia Group Inc | Americas |
| `C00055` | `FC015400/22` | `FC015400` \- `FC0157FF` | Deviceroy | World |
| `C00056` | `FC015800/22` | `FC015800` \- `FC015BFF` | Eutelsat S.A. | World |
| `C00057` | `FC015C00/22` | `FC015C00` \- `FC015FFF` | Bejing Dingtek Technology Corp. Ltd | World |
| `C00058` | `FC016000/22` | `FC016000` \- `FC0163FF` | The Things Network Foundation | World |
| `C00059` | `FC016400/22` | `FC016400` \- `FC0167FF` | Quandify AB | Europe and USA |
| `C0005A` | `FC016800/22` | `FC016800` \- `FC016BFF` | Hutchison Drei Austria GmbH | Europe |
| `C0005B` | `FC016C00/22` | `FC016C00` \- `FC016FFF` | Agrology, PBC | North America |
| `C0005C` | `FC017000/22` | `FC017000` \- `FC0173FF` | mHascaro GmbH | Germany |
| `E00000` | `FE000000/25` | `FE000000` \- `FE00007F` | RESERVED |  |
| `E00010` | `FE000800/25` | `FE000800` \- `FE00087F` | RESERVED |  |
| `E00020` | `FE001000/25` | `FE001000` \- `FE00107F` | Techtenna b.v. | World |
| `E00030` | `FE001800/25` | `FE001800` \- `FE00187F` | LNX Solutions | South Africa |
| `E00040` | `FE002000/25` | `FE002000` \- `FE00207F` | Cometa Sas | France |# Preparing for The Things Certified Fundamentals

In this section, you’ll learn how to prepare for The Things Certification: The Things Certified Fundamentals .
## What is The Things Certification?

The Things Certification was first announced at The Things Conference 2021\. It consists of four exams: The Things Certified Fundamentals , The Things Certified Advanced , The Things Certified Security , and The Things Certified Network Management . The Things Certification is the only certification program currently available for testing your LoRaWAN knowledge.
## Who Should Take The Things Certified Fundamentals Exam?

The Things Certified Fundamentals exam is intended for everyone who wants to officially validate their skills, and fundamental knowledge around the LoRaWAN protocol.
## What Knowledge is Tested?

You will be tested on
* [LoRaWAN Basics](https://www.thethingsnetwork.org/docs/lorawan/what-is-lorawan/)
* [LoRaWAN architecture](https://www.thethingsnetwork.org/docs/lorawan/architecture/)
* [Frequency plans](https://www.thethingsnetwork.org/docs/lorawan/regional-parameters/)
* [Device classes](https://www.thethingsnetwork.org/docs/lorawan/classes/)
* [Message types](https://www.thethingsnetwork.org/docs/lorawan/message-types/)
* [Spreading factors](https://www.thethingsnetwork.org/docs/lorawan/spreading-factors/)
* [Adaptive Data Rate (ADR)](https://www.thethingsnetwork.org/docs/lorawan/adaptive-data-rate/)
* [Activation methods](https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/)
* [Basic security](https://www.thethingsnetwork.org/docs/lorawan/security/)
* [Limitations of LoRaWAN](https://www.thethingsnetwork.org/docs/lorawan/limitations/)

Understanding the exam format and what question types will be coming will make it easier for you to answer them.
## How Many Questions Are On The Exam And What Are The Question Types?

The Things Certified Fundamentals exam contains 25 questions. These questions fall into two types: multiple\-choice and true/false. Multiple\-choice questions have only one correct answer and several incorrect answers. True/false questions are only composed of a statement. You should select whether it is true or false.
## How Much Time Do I Have to Complete the Exam?

You must answer all the questions within 15 minutes . However, if you don’t know the correct answer for a particular question, you can skip that question and proceed with the next one. You can also go back and answer those questions later within the exam time, or you can submit your exam along with the unanswered questions.
## What Is A Passing Score?

The Things Fundamentals exam is scored out of 100\. You need a 70 or higher to pass the exam and gain your Things Fundamentals certificate.
## How Much Does The Exam Cost?

The Things Certified Fundamentals exam fee is 25 Euro . However, the exam is free for The Things Conference visitors and members of our Developer Success Program.
## Study Materials

Here is a list of study materials you need to prepare for the exam. The Things Certification is based on the LoRaWAN® specification 1\.0\.3 , 1\.1 , and the LoRaWAN® Regional Parameters 1\.0\.3 . You can download these documents from the LoRa Alliance resource hub .
We highly recommend you follow The Things Network Learn section and follow the LoRaWAN fundamentals course on Udemy \- both are free. You can also read the security resources that can be found on the LoRa Alliance website.
## How Do I Register For The Exam?

First, you need The Things ID. Registration for The Things ID is free and it only takes a few minutes.
To get one, visit thethingsnetwork.org and click on the Sign up button.
On the Create an account page, provide a username, your email address, and a password, and click on the Create account button. Once created, you will receive an email for activating your account.
To take the exam, go to The Things Certifications . Then choose your certification (The Things Certified Fundamentals) and click Get this certificate .
You will be redirected to the payment page if you are not a The Things Conference visitor or a member of our Developer Success Program. Here you can enter your payment details and make the payment for the exam.
You will be redirected to the exam starting page. However, you can skip it and take the exam anytime.
Once you finish answering questions, you can submit your answers by clicking on the Finish now button. You will receive the result immediately. If you have passed the exam, you will receive a link to download your certificate (in PDF format).

The certificate shows the certification title, your name, marks, and the date you have taken the exam.
## Practice Questions

Here are some questions you will likely get in The Things Certified Fundamentals exam. We occasionally post these questions through polls on our LinkedIn.
### Which end device class is the most energy\-efficient and results in the longest battery life?

* **Class A**
* Class B
* Class C

Skill measured:
These three device classes open ‘receive windows’ in 3 different ways.
Class A devices open two short receive windows after sending an uplink message.

Class B devices open two short receive windows after sending an uplink similar to Class A devices. In addition to that, Class B devices periodically receive a beacon from the network for aligning its internal clock with the network. Based on the beacon timing reference, they can open additional receive windows periodically called ping slots.

Class C devices open two short receive windows after sending an uplink similar to Class A devices. But Class C devices do not close the second receive window until it sends the next uplink.

When a receive window is opened, an end\-device consumes much more battery power than when it is in sleep mode. By looking at the number of ‘receive windows’ and how long they open, the class C devices consume a lot more energy than the other two classes.
If you rank the device classes from lowest to the highest energy consumption, the lowest is class A, then class B and the highest is class C. So, the correct answer for this question is Class A device.
### Which frequency range is allowed in Australia?

* 863 – 870 MHz
* 902 – 928 MHz
* **915 – 928 MHz**
* 470 – 510 MHz

Skill measured:
So, let’s look at the given options one by one. The first option is 863\-870 MHz. This frequency range is allowed to be used in Europe – the most famous frequency range in LoRaWAN. The second option is 902\-928 MHz. This frequency range is allowed to be used in USA. The third option is 915\-928 MHz This frequency range is allowed to be used in Australia – yeah. We got the answer. The fourth option is 470\-510 MHz, and it is allowed to be used in China. All this information can be found in the LoRaWAN regional parameters document. So, the correct answer for this question is 915 – 928 MHz.
### What activation method is more secure?

* **Over The Air Activation (OTAA)**
* Activation By Personalisation (ABP)

Skill measured:
LoRaWAN uses two methods for activating end devices.
The first one is called over\-the\-air\-activation \- abbreviated as OTAA. For over\-the\-air\-activation, root keys must be stored securely in the LoRaWAN end device, and also the same root keys must be provisioned on the network side at the Join Server. The Join Server which is part of the backend interface provides a secure and trusted storage for root keys and assists in the processing of the join procedure. The root keys are used to derive session keys during the join procedure to activate the end\-device within a network.
The second one is called activation by personalization \- abbreviated as ABP.
Activation By Personalization directly ties an end\-device to a pre\-selected network bypassing the over\-the\-air\-activation procedure. No Join Server is involved in generating session keys. The DevAddr and the four\-session keys FNwkSIntKey, SNwkSIntKey, NwkSEncKey, and AppSKey are directly stored into the end\-device instead of being derived from the root keys. Also, the NwkSKey and the AppSKey should be stored in the Network Server and Application Server respectively. Activation by Personalization is the less secure activation method, and also has the downside that devices cannot switch network providers without manually changing session keys.
So, the correct answer for this question is Over\-the\-air\-activation (OTAA).
### LoRaWAN is operated in an unlicensed spectrum

* **True**
* False

Skill measured:
LoRaWAN operates on both licensed and unlicensed spectrum. If you carefully read the question, it doesn’t say LoRaWAN is operated only in an unlicensed spectrum. So, the correct answer is True.
### Using a higher data rate results in \_\_\_\_.

* **Less time\-on\-air**
* More time\-on\-air

Skills measured:
In LoRaWAN the data rate depends on the spreading factor (SF) used. The lower the spreading factor the higher the data rate, and the higher the spreading factor the lower the data rate.
With regards to the time\-on\-air, the higher the data rate the lower the time\-on\-air, and the lower the data rate the higher the time\-on\-air.
Therefore, using a higher data rate results in less time\-on\-air.
### Where does an uplink message start?

* **End\-device**
* Gateway
* Network Server
* Application Server

Skill measured:
Let’s look at what is the role of each network element with regards to the uplink and downlink messages.
End device – uplink messages are always initiated by an end device
Gateway – gateways receive messages from end devices and simply forward them to the network server
Network server \- initiates downlink messages
Application server \- initiates downlink messages
So, the correct answer for this question is End\-device.
### The AppSKey encrypts and decrypts the application payload.

* **True**
* False

Skill measured:
For example, if an end device sends a data message containing an application payload, the message travels from the end device to the application server. At the end device side, the AppSKey is used to encrypt the application payload. Once encrypted, no one can’t read the payload. At the application server\-side the AppSKey is used to decrypt the application payload. The AppSKey also ensures message confidentiality.
So, for this question, the correct answer is True.
### Using the lowest spreading factor provides longer battery life

* **True**
* False

Skills measured:
The LoRaWAN uses spreading factors (SF) ranging from 7 to 12\. If you carefully read the question the lowest spreading factor means the SF7\. The SF7 provides the highest data rate while the SF12 provides the lowest data rate. As the lower spreading factors provide a higher data rate, the time\-on\-air would be less. Less time\-on\-air means the amount of time the lora radio turned on is also less.
Therefore, the lowest spreading factor provides a longer battery life.
For this question, the correct answer is True.
### How many default channels MUST be implemented in every EU868MHz end\-device?

* **3**
* 8
* 4
* 16

Skills measured:
The LoRaWAN regional parameters document clearly states that there are 3 default channels that MUST be implemented in every EU868 end\-device. The default channels are 868\.10 MHz, 868\.30 MHz, and 868\.50 MHz. Among these three channels, a randomly chosen channel is used to broadcast the Join\-request message. The EU868 gateways always listen on these three default channels.
So, the correct answer is 3\.
### Where are the root keys stored in LoRawan 1\.1 (assume that the servers are not co\-existed)?

* End device and the network server
* End device and the application server
* **End device and the Join Server**
* End device and the Gateway server

Skills measured:
In LoRaWAN 1\.1 root keys are stored in the end device and also the same set of root keys are stored in the Join server. See the image below:

So, the correct answer for this question is End device and the Join Server.
### What element in a LoRaWAN network is responsible for the deduplication of messages?

* Gateway
* **Network Server**
* Application Server
* Join Server

Skills measured:
A network can have more than one gateway. When a device sends a message, all the gateways within the range can receive that message. Each gateway forwards the message to the network server. Once received, the Network Server keeps only one message and discards all other copies. This is known as the deduplication of messages.
So, the correct answer is Network Server.
### Which payload and data rate combination provides the longest battery life for an end device?

* **20 byte payload at SF7**
* 20 byte payload at SF8
* 20 byte payload at SF10
* 20 byte payload at SF12

Skills measured:
The power consumption of an end device depends on the payload size and the spreading factor used.
You can see all answers contain the same payload size which is 20 bytes. So, we should consider the spreading factor used in each option.
The lower spreading factors use less power than the higher spreading factors.
By looking at the spreading factors used in each option, the lowest spreading factor is 7\.
So, the correct answer is 20\-byte payload at SF7\.
### What is not included in every uplink data message?

* FCnt (Frame Counter)
* FPort (Port field)
* DevAddr
* **NwkSKey**

Skills measured:
First, let’s have a look at the structure of a data message. You can see the frame header consists of the frame counter, port field, and device address. But the NwkSKey is not sent with a data message. It is only used to encrypt the MAC commands.
So, the correct answer is NwkSKey.# Regional Limitations of RF Use in LoRaWAN

The sub\-gigahertz ISM (Industrial, Scientific, and Medical) band is a range of radio frequencies between 902 MHz and 928 MHz in the United States , and between 868 MHz and 870 MHz in Europe , that is available for unlicensed use. The frequencies mentioned are commonly used for wireless communications in industrial, scientific, and medical applications, and are also used in LoRaWAN networks.
# Europe (863\-870 MHz)

In Europe, LoRaWAN uses a range of 24 to 80 channels with either 125 kHz or 250 kHz bandwidth, where 250 kHz bandwidth can be achieved only using DR (Data Rate) 6\.
All LoRaWAN end devices are required to operate at least on channels 868\.10 MHz, 868\.30 MHz, and 868\.50 MHz. These channels must have a bandwidth of 125 kHz at DR0 to DR5, and be restricted to a maximum duty cycle of 1%. These three channels are used for sending join\-requests, so all gateways should listen on these channels too.
The LoRa Alliance® recommends a duty cycle limitation of 1% in the European band which means that a device can transmit for no more than 1% of the time while ensuring the maximum EIRP (Effective Isotropic Radiated Power) of \+16 dBm. The purpose of the duty cycle limitation is to ensure that devices operating in the ISM band do not cause harmful interference to other devices operating in the same band.
The EIRP of 16 dBm is equal to 40 mW and is equivalent to an ERP of 14 dBm, which is equal to 25 mW. To learn more about EIRP and ERP, you can refer to the LoRaWAN® section.
However, ETSI (European Telecommunications Standards Institute) has segmented the European ISM frequency band into 6 sub\-bands (K, L, M, N, P, Q) and imposes additional restrictions on the duty cycle and maximum ERP for some sub\-bands (see pages 21\-22 of the ETSI EN300\.220 V3\.2\.1 (2018\-06\) document ).
* K (863 MHz \- 865 MHz): 0\.1%, 25 mW ERP
* L (865 MHz \- 868 MHz): 1%, 25 mW ERP
* M (868 MHz \- 868\.6 MHz): 1%, 25 mW ERP
* N (868\.7 MHz \- 869\.2 MHz): 0\.1%, 25 mW ERP
* P (869\.4 MHz \- 869\.65 MHz): 10%, 500 mW ERP
* Q (869\.7 MHz \- 870 MHz): 1%, 25 mW ERP

For example, devices operating in the 869\.4\-869\.65 MHz range, which is sub\-band P, have a duty cycle limitation of 10%, which means that a device can transmit for no more than 10% of the time.
Usually, the limitations of sub\-bands K, L, M, N and Q are applied for uplink transmissions and the limitations of sub\-band P are mainly applied for downlink transmissions. Usually, a number of end devices in a LoRaWAN network is way higher than a number of gateways. Gateways can therefore run into their duty cycle limit quicker than end devices. LoRaWAN’s RX2 channel is normally chosen to fall into sub\-bad P in order to benefit from the higher duty cycle limit, and provide 10x more downlinks to gateways instead of end devices.
By default, the RX1 receive window for downlinks uses the same frequency as the preceding uplink, while the RX2 receive window uses a fixed frequency, with the default being 869\.525 MHz at DR0 using SF12 with 125 kHz.
In Europe 869\.525 MHz is used for Class B beacon transmissions and ping slots .
# US (902\-928 MHz)

The following regulations are applied to the USA, Canada, and all other countries in ITU Region 2 adopting the entire FCC (Federal Communications Commission) 47 CFR (Code of Federal Regulations) Part 15 in the 902\-928 ISM band.
In the United States, the ISM band is divided into 80 channels : 72 for uplink and 8 for downlink.
* There are **64 uplink channels**, numbered from 0 to 63, each with a bandwidth of 125 kHz. These channels start at a center frequency at 902\.3 MHz and increment linearly by 200 kHz up to 914\.9 MHz.
* There are **8 uplink channels**, numbered from 64 to 71, each with a bandwidth of 500 kHz. These channels start at a center frequency at 903\.0 MHz and increment linearly by 1\.6 MHz up to 914\.2 MHz.
* There are **8 downlink channels**, numbered from 0 to 7, each with a bandwidth of 500 kHz. These channels start at a center frequency at 923\.3 MHz and increment linearly by 600 kHz up to 927\.5 MHz.

The end devices must have the capability to store parameters for the 72 uplink channels mentioned above.
The dwell time for LoRaWAN in the US902\-928 band refers to the amount of time that a device spends on a specific channel before switching to the next channel. The dwell time is an important parameter for LoRaWAN devices as it helps to ensure that devices are able to successfully transmit data while avoiding interference with other devices.
For the US ISM band, the dwell time for transmitting a LoRaWAN message must not exceed 400 ms. It is important to consider this dwell time limitation when designing and operating devices. For example, if a device is transmitting data at a high rate, it may need to use a faster hopping rate in order to comply with the 400 ms dwell time limitation.
Both end devices and gateways are also limited to a maximum EIRP of \+30 dBm. The maximum EIRP can be maintained by adjusting the transmitter power, antenna gain, or cable loss.
The downlink channel for the RX1 receive window is based on the uplink channel that was used to send the preceding uplink. The default downlink channel for the RX2 receive window is 923\.3 MHz with a data rate of DR8\.
Class B beacon transmissions and ping slots in the US utilize eight frequencies: 923\.3, 923\.9, 924\.5, 925\.1, 925\.7, 926\.3, 926\.9, and 927\.5 MHz. These frequencies are rotated starting at 923\.3 MHz.
## Additional Regulatory Requirements and Certifications

It is important to note that there may be additional regulatory requirements and certifications that must be met to legally operate in the ISM band, such as obtaining approval or certification from organizations such as FCC, ICASA, RED, R\&TTE, etc . Getting your LoRaWAN end device certified by the LoRa Alliance® before releasing it to the market is also highly recommended.# RSSI and SNR

In wireless communication, a receiver needs a good signal strength and a signal\-to\-noise ratio to separate the original signal from the modulated carrier. This section contains information about two most commonly used signal strength indicators \- RSSI and SNR.
## RSSI

RSSI (Received Signal Strength Indicator) is a relative measurement that helps you determine if the received signal is strong enough to get a good wireless connection from the transmitter. Since LoRaWAN supports bi\-directional communication, RSSI is an important measurement for both gateways and end devices. RSSI is measured in dBm and its value is a negative form. The closer the RSSI value is to zero, the received signal is stronger.
Apart from the output power of the transmitter, the following factors mainly influence the RSSI:
* Path loss
* Antenna gain
* Cable/connector loss

## SNR

SNR (Signal\-to\-Noise Ratio), often written as S/N, is the ratio of the received signal power to the noise floor. SNR is commonly used to determine the quality of the received signal.
SNR can be calculated using the following formula and is often expressed in decibels (dB):
SNR (dB) \= P received\_signal (dBm) \- P noise (dBm)
If the RSSI is above the noise floor the receiver can easily demodulate the signal.
Here is a good example of a positive SNR:

By looking at the above graph you can see that the RSSI is about \-65 dBm and the noise floor is about \-90 dBm. By using these values you can calculate the SNR as follows:
SNR (dB) \= P received\_signal (dBm) \- P noise (dBm)
SNR (dB) \= \-65 dBm \-(\-90 dBm) \= 25 dB
The positive SNR means that the signal power is greater than the noise power, i.e. the receiver will be able to demodulate the signal.
If the RSSI is below the noise floor, it is impossible to demodulate the signal. However, LoRa can demodulate signals that are below the noise floor. The minimum SNR required for demodulation at different spreading factors is shown in the table below:

Here is a good example of a negative SNR:

By looking at the above graph you can see that the RSSI is about \-120 dBm and the noise floor is about \-90 dBm. Now calculate the SNR as follows:
SNR (dB) \= P received\_signal (dBm) \- P noise (dBm)
SNR (dB) \= \-120 dBm \-(\-90 dBm) \= \-30 dB
The negative SNR means that the signal power is less than the noise power. The value of \-30 dB is below the minimum SNR of \-20 dBm @ SF12, so it does not guarantee that the receiver will be able to demodulate the signal.# The Things Certified Security

This study guide has been written for students who are planning to take The Things Certified Security exam. It explains the following fundamental properties that support LoRaWAN security in detail:
* Mutual authentication
* Integrity protection
* Confidentiality
* End\-to\-end security

In addition to that, we briefly discuss the following security mechanisms:
* Replay protection
* Eavesdropping
* Spoofing
* Securing communication between network elements (backend interfaces)

We hope that you will find this study material useful and that the knowledge you acquire will help you pass The Things Certified Security exam.
## Understanding Message Types

LoRaWAN networks use several MAC message types for different purposes.
There are three MAC messages used for the device activation/registration:
* Join\-request
* Join\-accept
* Rejoin\-request

There are four MAC messages used to carry MAC commands and application data (together or separately), known as data messages :
* Unconfirmed data uplink
* Unconfirmed data downlink
* Confirmed data uplink
* Confirmed data downlink

It is worth knowing the MAC message format before learning how the LoRaWAN security is implemented. A MAC message format breakdown is shown on the image below.

MAC Message Breakdown

MAC messages carry a payload. The messages used for the join procedure have the following payloads, which consist of several fields:
* Join\-request
* Join\-accept
* Rejoin\-request

The payload carried by the data message is called MACPayload (MAC Payload). The term payload refers to the actual data in a packet, e.g. application data and/or MAC commands. Headers are appended to the payload for transport and then discarded at the message destination.
The MACPayload consists of FHDR (Frame Header), FPort (Port Field), and the FRMPayload (Frame Payload) fields. Only the FRMPayload field and FOpts field can carry information. The PHYPayload is created by adding MHDR (MAC Header) and MIC (Message Integrity Code) to the MACPayload .
## Join Procedure

LoRaWAN provides two end device activation methods:
* ABP (Activation\-by\-Personalisation) \- has some security vulnerabilities
* OTAA (Over\-The\-Air\-Activation) \- highly recommended

OTAA is the most secure way to activate an end device on a network. It ensures that only authorized end devices can access the LoRaWAN network by proving that both the end device and the network have the knowledge of root keys . This concept is also known as mutual authentication .
Root keys used in this procedure are unique 128\-bit AES (Advanced Encryption Standard) symmetric keys.
The following keys and identifiers must be stored in an OTAA end device:
* **Root keys** \- LoRaWAN v1\.0\.x uses a single root key called **AppKey**. LoRaWAN v1\.1 uses two root keys called **AppKey** and **NwkKey**.
* **DevEUI** \- a globally unique 64\-bit end device identifier, assigned by the device manufacturer or device owner. Root key/s for a given end device are identified by its DevEUI.

The matching root keys should be stored on the network side. In LoRaWAN v1\.0\.x AppKey is stored in the Network Server, while in LoRaWAN v1\.1 AppKey and NwkKey are stored in the Join Server. The process of storing root keys and identifiers on both ends is known as provisioning .
The join procedure is started by sending a Join\-request message by an end device. The Join\-request message consists of the following fields:
* AppEUI/JoinEUI
* DevEUI
* DevNonce

Note that LoRaWAN v1\.1 and v1\.0\.4 use term JoinEUI instead of AppEUI.
The Join\-request message is not encrypted, i.e. it is sent in plain text. However, it has its integrity protected by computing the MIC (Message Integrity Code). The MIC enables the network to check if the AppKey (1\.0\.x) and NwkKey (1\.1\) are correct. The MIC is computed over all message fields using AES\-CMAC (AES Cipher\-based Message Authentication Code) algorithm together with the root keys. The computed MIC is then added to the message itself. See images explaining this process below:
LoRaWAN v1\.0\.x
LoRaWAN v1\.1
The following two subsections describe how the network processes the Join\-request message.
### In LoRaWAN v1\.0\.x

After the Join\-request frame is received, the Network Server (assume that the Network Server and the Application Server are co\-located) computes the MIC over all message fields (except the MIC field) using AES\-CMAC algorithm with the AppKey.
Then the computed MIC is compared to the MIC field in the Join\-request frame. If these MICs are matched, the Network Server will authenticate the Join\-request frame, otherwise the Join\-request message gets discarded. This ensures that the Join\-request message was not altered by any malicious actor during its journey.
If the end device is allowed to join the network and the MIC is correct, the Network Server prepaires a Join\-accept message. The Join\-accept message consists of the following fields:
* **AppNonce** \- 3 bytes, random value
* **NetID** \- 3 bytes, network ID
* **DevAddr** \- 3 bytes, device address
* **DLSettings** \- 1 byte, downlink parameters
* **RxDelay** \- 1 byte, delay between TX and RX
* **CFList** \- 16 bytes, optional list of channel frequencies

The MIC is calculated over the following Join\-accept message fields using the AES\-CMAC algorithm with the AppKey:
* `cmac = aes128_cmac(AppKey, MHDR | AppNonce | NetID | DevAddr | DLSettings | RxDelay | CFList)`
* `MIC = cmac[0..3]`

The calculated MIC is then added to the Join\-accept message.
The payload of the Join\-accept message is encrypted using AES decrypt operation in ECB (Electronic Code Book) mode with the AppKey, so that the end device can use the AES encrypt operation to decrypt the message:
* `aes128_decrypt(AppKey, AppNonce | NetID | DevAddr | DLSettings | RxDelay | CFList | MIC)`

Finally the Network Server sends the Join\-accept message to the end device.
After the end device receives the Join\-accept message, it derives two session keys locally, NwkSKey and AppSKey using AES encrypt:
* `NwkSKey = aes128_encrypt(AppKey, 0x01 | AppNonce | NetID | DevNonce | pad16)`
* `AppSKey = aes128_encrypt(AppKey, 0x02 | AppNonce | NetID | DevNonce | pad16)`

Similarly, the Network Server derives session keys based on the root key and fields in the Join\-request and Join\-accept messages using AES encrypt:
* `NwkSKey = aes128_encrypt(AppKey, 0x01 | AppNonce | NetID | DevNonce | pad16)`
* `AppSKey = aes128_encrypt(AppKey, 0x02 | AppNonce | NetID | DevNonce | pad16)`

Finally, the Network Server keeps the NwkSkey and shares the AppSKey with the Application Server. Note that the AppSKey is not visible to the Network Server, and that the NwkSKey is not visible to the Application Server.
### In LoRaWAN v1\.1

After the Join\-request frame is received, the Join Server computes the MIC over all message fields (except the MIC field) using AES\-CMAC algorithm with the NwkKey.
Then the computed MIC is compared to the MIC field in the Join\-request message. If these MICs are matched, the Join Server will authenticate the Join\-request message, otherwise the Join\-request message gets discarded. This ensures that the Join\-request message was not altered by any malicious actor during its journey.
If the end device is allowed to join the network and the MIC is correct, the network sends a Join\-accept message. The Join\-accept message consists of the following fields.
* **JoinNonce** \- 3 bytes, device\-specific counter value
* **NetID** \- 3 bytes, network identifier
* **DevAddr** \- 4 bytes, end device address
* **DLSettings** \- 1 byte, downlink parameters
* **RxDelay** \- 1 byte, delay between TX and RX
* **CFList** \- 16 bytes, optional list of channel frequencies

The MIC is calculated over the following Join\-accept message fields using the AES\-CMAC algorithm with the JSIntKey:
* `cmac = aes128_cmac(JSIntKey, JoinReqType | JoinEUI | DevNonce | MHDR | JoinNonce | NetID | DevAddr | DLSettings | RxDelay | CFList)`
* `MIC = cmac[0..3]`

If a LoRaWAN v1\.1 device is provisioned with a LoRaWAN v1\.0\.x Network Server, the MIC of the Join\-accept message is computed using the NwkKey.
* `cmac = aes128_cmac(NwkKey, MHDR | JoinNonce | NetID | DevAddr | DLSettings | RxDelay | CFList)`
* `MIC = cmac[0..3]`

The calculated MIC is then added to the Join\-accept message.
Then the payload of the Join\-accept message is encrypted using AES decrypt operation in ECB (Electronic Code Book) mode with the NwkKey (if triggered by the Join\-request) or JSEncKey (if triggered by the Rejoin\-request type 0, 1, and 2\) so that the end device can use AES encrypt operation to decrypt the message.
* `aes128_decrypt(NwkKey or JSEncKey, JoinNonce | NetID | DevAddr | DLSettings | RxDelay | CFList | MIC)`

After the end device receives the Join\-accept message it derives session keys locally.
The following 3 network session keys are derived using the NwkKey:
* `FNwkSIntKey = aes128_encrypt(NwkKey, 0x01 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `SNwkSIntKey = aes128_encrypt(NwkKey, 0x03 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `NwkSEncKey = aes128_encrypt(NwkKey, 0x04 | JoinNonce | JoinEUI | DevNonce | pad16)`

The AppSKey is derived using the AppKey:
* `AppSKey = aes128_encrypt(AppKey, 0x02 | JoinNonce | JoinEUI | DevNonce | pad16)`

The OptNeg field (can be found in the DLSettings field) is used to indicate whether the network supports LoRaWAN v1\.0\.x (unset) or v1\.1 and later (set).
If the OptNeg is unset, the device reverts to the LoRaWAN v1\.0 and the session keys are derived from the NwkKey as follow:
* `FNwkSIntKey = SNwkSIntKey = NwkSEncKey = aes128_encrypt(NwkKey, 0x01 | JoinNonce | NetID | DevNonce | pad16)`
* `AppSKey = aes128_encrypt(NwkKey, 0x02 | JoinNonce | NetID | DevNonce | pad16)`

If the OptNeg is set, the AppSKey is derived from AppKey and the network session keys are derived from the NwkKey as follow:
* `AppSKey = aes128_encrypt(AppKey, 0x02 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `FNwkSIntKey = aes128_encrypt(NwkKey, 0x01 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `SNwkSIntKey = aes128_encrypt(NwkKey, 0x03 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `NwkSEncKey = aes128_encrypt(NwkKey, 0x04 | JoinNonce | JoinEUI | DevNonce | pad16)`

The Join Server also derives session keys based on the root keys and fields in the Join\-request and Join\-accept messages.
* `FNwkSIntKey = aes128_encrypt(NwkKey, 0x01 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `SNwkSIntKey = aes128_encrypt(NwkKey, 0x03 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `NwkSEncKey = aes128_encrypt(NwkKey, 0x04 | JoinNonce | JoinEUI | DevNonce | pad16)`
* `AppSKey = aes128_encrypt(AppKey, 0x02 | JoinNonce | JoinEUI | DevNonce | pad16)`

Finally, the Join Server shares the network session keys (FNwkSIntKey, SNwkSIntKey, NwkSEncKey) with the Network Server and the AppSKey with the Application Server. Note that the AppSKey is not visible to the Network Server, and that the FNwkSIntKey, SNwkSIntKey, and NwkSEncKey are not visible to the Application Server.
Since both the end device and the network have session keys, from now all the messages will be encrypted using the AppSKey, and the integrity will be protected with the NwkSKey.
## Encrypting the FRMPayload field

The MACPayload of the data message contains a field called FRMPayload which is capable of carrying either a sequence of MAC commands (between the end device and the Network Server) or application data (between the end device and the Application Server). The FRMPayload field is encrypted using AES encrypt operation in CCM mode (counter with cipher block chaining message authentication code; counter with CBC\-MAC). The encryption key used to encrypt the FRMPayload field depends on what it contains. Note that LoRaWAN uses a minor variation of the CCM, named CCM\*.

## Encrypting FOpts Field

The FOpts (Frame Options) field can carry a series of MAC commands that are piggybacked onto the data frame.
The FOpts field is encrypted using AES encrypt operation in CCM\* mode.
The following keys are used to encrypt the FOpts field in the MACPayload in different LoRaWAN versions for both uplink and downlink data messages.

## Computing MIC

The MIC is calculated after encrypting the payload. The MIC is computed for each packet (entire PHYPayload) using the AES\-CMAC.
The following table presents which key is used to calculate the MIC of each data message type in LoRaWAN 1\.0\.x and 1\.1\.

When a LoRaWAN 1\.1 device is provisioned with a LoRaWAN 1\.0\.x Network Server, the MIC of the uplink and downlink data messages are computed with the FNwkSIntKey.
## End\-to\-end Security

LoRaWAN provides end\-to\-end encryption for application payload exchange between end devices and the Application Server. Application payload refers to the data contained in the FRMPayload field. The Network Server also verifies the DevAddr for authenticating received messages.
## Replay Protection

Replay protection ensures that the receiver does not accept a frame that has already been received.
### Join\-request Messages

The replay protection of the Join\-request messages is protected using DevNonce. The DevNonce field is used when computing the MIC.
In LoRaWAN 1\.0\.x, DevNonce is a random value. It is used to keep track of the Join\-request messages. The network server keeps track of a certain number of DevNonce values for each end device. It ignores any Join\-requests that include a previously recorded DevNonce value.
In LoRaWAN v1\.1, DevNonce is a counter starting at 0\. It is used to keep track of the Join\-request messages. The DevNonce value is incremented with every Join\-request. The Network Server keeps track of the last DevNonce value used by the end device and ignores Join\-requests if DevNonce is not incremented.
Similarly, the replay protection for the ReJoin\-request messages is implemented with the RJcount0 (for ReJoin\-request Type 0 or 2 messages) or RJcount1 (for ReJoin\-request Type 1 messages).
### Data Messages

The replay protection of the data messages is implemented with the frame counters.
In LoRaWAN 1\.0\.x two frame counters are used to keep track of uplink and downlink messages:
* **FCntUp** \- keeps track of the number of data messages sent from the end device to the Network Server.
* **FCntDown** \- keeps track of the number of data messages sent from the Network Server to the end device.

These frame counters are stored in both the end device and the Network Server. Frame counters are initially set to 0 and incremented by the value 1 with each transmission.
If either the device or the network receives a message with a frame counter that is lower than the last one, the message is discarded.
In LoRaWAN 1\.1 each end device maintains three frame counters to keep track of uplink and downlink data messages:
* **Uplink** \- The frame counter, **FCntUp** is used to keep track of the data messages sent from the end device to the Network Server.
* **Downlink** \- two frame counter schemes are available.
	+ **Single counter scheme** \- all ports share the same downlink frame counter **FCntDown** when the device operates as a v1\.0 device.
	+ **Two\-counter scheme** \- **NFCntDown** is managed by the Network Server, whereas the **AFCntDown** is managed by the Application Server.
		- **NFCntDown** is used to keep track of data messages that transports MAC commands on port 0 and when the FPort field is missing (which means no FRMPayload field).
		- **AFCntDown** is used to keep track of data messages on all other ports (1 \- 223\) when the device operates as a LoRaWAN 1\.1 device.

## Eavesdropping

Since LoRaWAN provides two layers of security, the MAC payload is encrypted between the end device and the Network Server whereas the application payload is encrypted between the end device and the Application Server. This ensures only the authorised parties (end device, Network Server, Application Server) that hold the security keys (NwkSKey and AppSKey) can decrypt the payload and read the plain text content.
## Spoofing

The MACPayload in the data message is origin\-authenticated and integrity protected with the MIC. This ensures only the authorised parties (end device, Network Server, Application Server) that hold the security keys (NwkSKey and AppSKey) can generate valid data frames.
## Securing Communication Between Network Elements

LoRaWAN uses HTTPS and VPN for securing communication among network elements (backend interfaces) such as the Network Server, Application Servers, and the Join Server.
## Secure Elements

The secure element is a small chip, for example Microchip’s hardware secure element ATECC608B\-TNGLORA , that is used to securely store root keys and for performing cryptographic operations. The root keys are securely stored in the secure elements during the manufacturing process. Once stored, it is extremely difficult to read the root keys from the chip. Simultaneously, the matching root key/s for each secure element are provisioned on the Global Join Server .
Device manufacturers can easily integrate these secure element chips with their LoRaWAN end devices. During the join procedure, the secure element generates an identical pair of session keys from the root key/s, the same way the Join Server does it.
The Global Join Server allows the end\-user to transfer these root keys anytime to a third\-party Join Server. Once transferred, the end device generates new root keys using the rekeying procedure.