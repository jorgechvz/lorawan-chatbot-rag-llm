# Glossary

## Activation

### Definition:

Every end device must be registered with a network before sending and receiving messages. This procedure is known as activation. There are two activation methods available: Over-The-Air-Activation (most secure and most flexible) and Activation By Personalization (least secure and least flexible).
### The Opportunity:

Activation is a network-agnostic procedure which allows an end device to join any LoRaWAN network, preventing lock-in and allowing you to use and transfer your devices between networks as you choose.

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

The application server processes application-specific data messages received from end devices. It also generates all the application-layer downlink payloads and sends them to connected end devices through the network server. A LoRaWAN network can have more than one application server.
### The Opportunity:

The application server allows decoupling of the application from the network backend. Collected data can be interpreted, analyzed, or visualized using third party integrations, without revealing application specific keys to the network.

## Bandwidth

### Definition:

Bandwidth is the range of frequencies occupied by the modulated radio frequency signal. The bandwidth is expressed in Hertz (Hz).
### The Opportunity:

Bandwidth impacts time on air and receiver sensitivity. Increasing bandwidth decreases the time needed to transmit, decreasing power consumption, but also reducing receiver sensitivity.

## Coding Rate

### Definition:

The coding rate defines the proportion of bits that actually carry information. For example, the coding rate 4/5 means 4 bits carry information and one bit is used for error correction - a total of 5 bits. LoRa uses the following Coding Rates. CR1: 4/5 (1 error correction bit for 4 information bits) CR2: 4/6 (2 error correction bits for 4 information bits) CR3: 4/7 (3 error correction bits for 4 information bits) CR4: 4/8 (4 error correction bits for 4 information bits)
### The Opportunity:

Coding Rates allow the network to adjust the amount of redundant data that is sent, so that data can be received correctly even when there is interference. When there is little interference, a faster Coding Rate can be used, which transmits less redundant data, allowing for more information carrying bits to be transmitted per second.

## CRC

### Definition:

A Cyclic Redundancy Check (CRC) is an error detecting code used in digital transmission to detect unintended changes to raw data.
### The Opportunity:

CRCs allow us to detect errors in digital data, enabling reliable communication over noisy channels.

## Decibel (dB)

### Definition:

The decibel (dB) is a unit of measurement used to express the ratio between quantities on a logarithmic scale. In radio transmission, it is used most often to refer to gain from an antenna with respect to a fixed reference value, and signal-to-noise ratio.
### The Opportunity:

The decibel scale allows network operators to quickly quantify losses and gains on a signal path, by linearizing the power domain. For example, a 10dB loss and 5dB gain can be quickly seen to sum to a 5dB loss, but calculating this in terms of gain is much more complicated, involving two multiplications.

## Decibel-milliwatts (dBm)

### Definition:

dBm (decibel-milliwatts) is a unit used to indicate that a power level is expressed in decibels (dB) with reference to an input power of 1 mW.
### The Opportunity:

While dBm is not a recognized SI unit, it is incredibly useful for defining standards.

## Device Classes

### Definition:

The LoRaWAN specification defines three device types - Class A (All), Class B (Beacon), and Class C (Continuous). Class A devices open windows to receive downlinks immediately following an uplink. Class B devices add periodic receive windows. Class C devices listen continuously for downlinks. All LoRaWAN devices must implement Class A, whereas Class B and Class C are extensions to the specification of Class A devices.
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

The Join Server processes join-request messages sent by end devices. It stores root keys, generates session keys, and transfers those session keys to the network server and the application server. The Join Server is introduced in LoRaWAN 1.1 and 1.0.4.
### The Opportunity:

The Join Server allows for secure end-device provisioning without network lock-in and without knowing beforehand which network the end-user will select. Manufacturers only need to provide the keys to the end-device in one safe place. The buyer uses a one-click device claiming procedure to transfer ownership in the Join Server. The owner can then configure the device to any LoRaWAN compliant network.

## LoRa

### Definition:

LoRa is a wireless modulation technique derived from chirp spread spectrum technology. It encodes information on radio waves using chirp pulses - similar to the way dolphins and bats communicate!
### The Opportunity:

LoRa is ideal for applications that transmit small chunks of data with low bit rates. LoRa modulated transmission is robust against disturbances and can be received across great distances - up to 5 km in urban areas and 15 km or more in rural areas with line-of-sight. LoRa end devices consume very little power and devices often last up to ten years on a single coin cell battery.

## LoRaWAN®

### Definition:

LoRaWAN is a Media Access Control (MAC) layer protocol built on top of LoRa modulation. It is a software layer which defines how devices use the LoRa hardware, for example when they transmit, and the format of messages. \nThe LoRaWAN protocol is developed and maintained by the LoRa Alliance®.
### The Opportunity:

Like LoRa, LoRaWAN is ideal for applications that transmit small chunks of data with low bit rates. LoRaWAN devices are ultra low power, often lasting up to ten years on a single coin cell battery. LoRaWAN networks are extremely long range, up to 15km in rural areas, and the cost of hardware and running a network is extremely low. LoRaWAN provides built in geolocation, modern security, large capacity, built-in roaming, and operates in the license-free spectrum, so there is no barrier to creating your own network.

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

The preamble is a set of symbols (or chirps) that is used by the receiver to detect a LoRa packet. LoRaWAN uses a series of 8 up-chirps as a preamble.
### The Opportunity:

The preamble signals to a receiver when a LoRaWAN packet is being sent, which allows multiple protocols to operate using the same modulation technique (in this case LoRa) without interfering with each other.

## Received Signal Strength Indicator

### Definition:

The Received Signal Strength Indicator (RSSI) is the received signal power in milliwatts, measured in dBm. This value is used as a measurement of how well the signal is received.
### The Opportunity:

RSSI is used in the ADR feedback loop to determine if a signal is being received with enough power to allow the device to increase its data rate and conserve battery. A high RSSI means the device can reduce transmission power and messages will still be received.

## Signal-to-Noise Ratio

### Definition:

Signal-to-Noise Ratio (SNR) indicates the ratio between the received power signal and the noise floor power level. SNR is expressed in dB.
### The Opportunity:

SNR is used in the ADR feedback loop to determine if a signal is being received with enough power to allow the device to increase its data rate and conserve battery. A high SNR means the device can reduce transmission power and messages will still be received.

## Spreading Factor

### Definition:

The spreading factor defines a spreading pattern applied to the bitstream before modulation, which increases processing gain and aids in decoding of LoRaWAN messages. LoRaWAN defines 6 spreading factors - SF7 to SF12.
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

Uplinks enable your application to collect data from sensors in all sorts of environments - LoRaWAN devices can be battery or mains powered, in dense urban areas or completely off the grid, mobile or stationary - the possibilities are endless, and the limits of your application are up to your creativity.