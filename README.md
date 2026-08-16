# 🔎 INDRA

### Industrial Network Discovery and Reconnaissance Assistant

> 🛡️ A passive OT/ICS network reconnaissance and asset discovery framework designed to identify, fingerprint, and map industrial network assets from observed traffic.

---

## 🚀 Overview

**INDRA** is a CLI-first cybersecurity tool for **OT/ICS network visibility and reconnaissance**.

Instead of actively scanning industrial devices, INDRA focuses on **passive traffic analysis** to discover assets and understand how they communicate.

The project follows this pipeline:

```text
🎯 SPAN / TAP
      ↓
📡 Packet Capture
      ↓
🔬 Protocol Analysis
      ↓
🗺️ Network Topology
      ↓
🖥️ Asset Discovery
      ↓
🧬 Asset Fingerprinting
      ↓
📊 Asset Inventory
      ↓
⚠️ Risk & Criticality
```

---

## ✨ Planned Features

### 📡 Passive Packet Capture

Capture traffic from a monitoring interface connected through:

* SPAN / Port Mirroring
* Network TAP
* PCAP files

### 🔍 Network Reconnaissance

Extract information such as:

* Source / destination IP
* Source / destination MAC
* Source / destination ports
* Protocol
* Packet size
* Timestamp
* TCP information

### 🏭 OT Protocol Analysis

Initial protocol support:

* 🔧 Modbus/TCP
* ⚡ IEC 60870-5-104
* 🌐 Ethernet / TCP / UDP

For Modbus/TCP, INDRA will analyze information such as:

* Function Code
* Transaction ID
* Unit ID
* Register address
* Read / Write operations

### 🧬 Asset Fingerprinting

INDRA will combine multiple traffic characteristics to identify likely device types.

Example:

```text
IP            : 192.168.10.20
MAC           : XX:XX:XX:XX:XX:XX
Protocol      : Modbus/TCP
Port          : 502
Device Type   : PLC
Confidence    : 94%
```

### 🗺️ Network Topology

Build a communication map showing relationships between industrial assets.

```text
             ┌─────────┐
             │  SCADA  │
             └────┬────┘
                  │
             Modbus/TCP
                  │
             ┌────▼────┐
             │  PLC-01 │
             └────┬────┘
                  │
                IED-01
```

### 📋 Asset Inventory

Maintain an inventory containing:

| Attribute   | Example       |
| ----------- | ------------- |
| Asset ID    | PLC-01        |
| IP Address  | 192.168.10.20 |
| MAC Address | XX:XX:XX:XX   |
| Device Type | PLC           |
| Protocol    | Modbus/TCP    |
| Port        | 502           |
| Normal Peer | SCADA-01      |
| Confidence  | 94%           |
| Criticality | High          |
| Status      | Active        |

### ⚠️ Unknown Asset Detection

Detect previously unseen devices and flag them for investigation.

```text
⚠️ NEW ASSET DETECTED

IP        : 192.168.10.55
Protocol  : Modbus/TCP
Port      : 502
Type      : Unknown
Confidence: 61%
```

---

## 🖥️ CLI-First Design

INDRA is designed to work like a modern Linux security tool.

Example commands:

```bash
indra --help

indra interfaces
indra sniff -i eth0
indra pcap capture.pcap
indra assets
indra topology
indra fingerprint <IP>
indra protocols
indra baseline
indra report
```

---

## 🏗️ Project Architecture

```text
INDRA
│
├── 📡 capture
│   ├── live.py
│   └── pcap.py
│
├── 🔎 discovery
│   ├── passive.py
│   ├── assets.py
│   └── topology.py
│
├── 🧬 fingerprint
│   ├── device.py
│   ├── plc.py
│   ├── hmi.py
│   └── ied.py
│
├── 🔧 protocols
│   ├── modbus.py
│   ├── iec104.py
│   └── ethernet.py
│
├── 📊 analysis
│   ├── flows.py
│   ├── baseline.py
│   └── anomalies.py
│
├── 💾 database
│   └── inventory.py
│
├── 📄 output
│   ├── terminal.py
│   └── report.py
│
└── 🚀 main.py
```

---

## 🎯 Development Roadmap

### Phase 1 — Traffic Acquisition

* [ ] Interface detection
* [ ] Live packet capture
* [ ] Packet parsing
* [ ] PCAP recording

### Phase 2 — Network Intelligence

* [ ] Flow extraction
* [ ] Protocol identification
* [ ] Communication analysis
* [ ] Passive topology discovery

### Phase 3 — Asset Discovery

* [ ] Asset detection
* [ ] Asset fingerprinting
* [ ] Device classification
* [ ] Confidence scoring
* [ ] Asset inventory

### Phase 4 — OT Intelligence

* [ ] Modbus/TCP analysis
* [ ] IEC 104 analysis
* [ ] Communication baselining
* [ ] Unknown asset detection

### Phase 5 — Security Assessment

* [ ] Asset criticality
* [ ] Risk scoring
* [ ] Baseline deviation detection
* [ ] Security reports

### Phase 6 — Advanced Analysis

* [ ] Network visualization
* [ ] Historical asset tracking
* [ ] Digital Twin integration
* [ ] Cyber-physical correlation

---

## 🧪 Example Use Case

A monitoring machine is connected to an OT switch through a SPAN port.

```text
                 OT NETWORK

        ┌───────────────┐
        │  Managed      │
        │   Switch      │
        └───────┬───────┘
          │     │     │
        PLC    HMI   SCADA
          │
          └──── SPAN ────► 💻 INDRA
```

INDRA observes the mirrored traffic and builds an asset view without participating in the actual SCADA communication.

This passive-first approach is particularly suitable for OT environments where disrupting control traffic is undesirable.

---

## 🛡️ Security Philosophy

INDRA follows a **passive-first** design.

> 👁️ Observe first. Understand the network. Then assess it.

The monitoring system should remain outside the actual control path whenever possible.

This allows the OT communication to continue even if the monitoring system becomes unavailable.

---

## 🧰 Technology Stack

* 🐍 Python
* 📡 Scapy
* 🔧 Modbus/TCP
* 📦 PCAP
* 🗄️ SQLite / database layer
* 🖥️ Linux CLI

Additional technologies may be introduced as development progresses.

---

## 🎓 Project Goals

INDRA aims to provide:

* 🔎 OT network visibility
* 🏭 Industrial asset discovery
* 🧬 Device fingerprinting
* 🗺️ Network topology mapping
* 📋 Asset inventory
* ⚠️ Unknown asset detection
* 📊 Communication baselining
* 🛡️ Security assessment capabilities

---

## ⚠️ Disclaimer

INDRA is intended for **authorized security testing, research, education, and controlled OT/ICS laboratory environments**.

Do not capture or analyze network traffic without proper authorization.
---

## 🌐 Vision

INDRA is designed to evolve from a simple packet-analysis script into a complete **OT/ICS reconnaissance and asset intelligence framework**.

```text
Traffic
   ↓
Understanding
   ↓
Discovery
   ↓
Fingerprinting
   ↓
Topology
   ↓
Asset Intelligence
   ↓
Security Assessment
```

### 🔎 INDRA

**See the industrial network. Understand the assets.**
