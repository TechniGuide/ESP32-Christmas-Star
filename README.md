# 🎄 ESP32 Christmas Star

Turning an ordinary battery-powered Christmas decoration into a smart, programmable device using an ESP32-C5.

![Status](https://img.shields.io/badge/Status-Prototype-orange)
![Platform](https://img.shields.io/badge/Platform-ESP32--C5-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 About the Project

This project explores how a simple Christmas decoration can be upgraded using modern microcontroller technology.

The goal is to develop a compact, programmable and eventually rechargeable Christmas star.

This repository documents the entire development process, including experiments, measurements, mistakes and improvements.

## 🎬 YouTube Series

### Episode 01 – Building the Prototype

- Analyzing the original decoration
- Measuring current consumption
- Designing the circuit using Falstad
- Building a breadboard prototype
- AI-assisted ESP32 programming
- Testing the first prototype

YouTube video coming soon.

## 🔧 Hardware

- ESP32-C5 development board
- LED Christmas star
- Transistor
- Resistors
- Breadboard
- Jumper wires
- USB-C power supply

## ⚡ Circuit Diagram

The circuit was designed using the Falstad Circuit Simulator.

![Circuit Diagram](schematics/circuit.png)

### Circuit Files

- [Download Falstad Circuit](schematics/circuit.txt)
- [View Circuit Diagram](schematics/circuit.png)
- [Open Falstad Simulator](https://www.falstad.com/circuit/)

### Circuit Overview

- Supply voltage: 3.3 V
- Current-limiting resistors: 2 × 10 Ω
- Total series resistance: 20 Ω
- Base resistor: 1 kΩ
- NPN transistor for switching
- ESP32-C5 GPIO 10 as control signal

## 💻 Firmware

The ESP32 firmware was developed with AI assistance.

Source code and setup instructions will be available here.

## 🗺️ Roadmap

- [x] Analyze original decoration
- [x] Measure current consumption
- [x] Design prototype circuit
- [x] Build breadboard prototype
- [x] Develop initial firmware
- [x] Test first prototype
- [ ] Publish firmware and circuit diagram
- [ ] Optimize power consumption
- [ ] Integrate rechargeable LiPo battery
- [ ] Design custom 3D-printed enclosure
- [ ] Build final version

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 About TechniGuide

Electronics, engineering, programming and DIY projects.

Building things, making mistakes and learning along the way.

---

Made by **TechniGuide**
