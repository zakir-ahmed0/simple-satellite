# Simple Satellite

## Satellite Telemetry & Health Monitoring Simulator

**Status:** In Development

## Overview

Simple Satellite is a Python-based simulation of a
satellite telemetry and health monitoring system.

The application aims to simulate sensor readings from
multiple fictional satellites, evaluate their operating
conditions, detect abnormal measurements and record
telemetry and fault events.

## Planned Features

- Multiple satellite simulation
- Telemetry generation
- Temperature and battery monitoring
- Satellite health status evaluation
- Fault and warning detection
- Telemetry data logging
- Mission health reports
- Automated testing

## Initial Simulation Configuration

Three fictional satellites will be simulated.

Initial monitoring thresholds:

| Measurement | Normal Range |
|---|---|
| Temperature | 0–40 °C |
| Battery | 30–100% |
| Solar output | 0–100 W |
| Signal strength | 0–100% |

Temperature at or above 45 °C will trigger a
critical status and warning.

Battery below 30% will trigger a critical status
and a fault event.

These are illustrative simulation parameters,
not real spacecraft operating specifications.

## Technologies

- Python 3
- Object-Oriented Programming
- CSV and JSON
- Git and GitHub
- Automated Testing

## Project Goals

The goal is to develop a modular, testable and
well-documented satellite telemetry simulation
using Python.

## Disclaimer

This is an educational software simulation.
It is not designed or validated for controlling
real spacecraft or operational aerospace systems.