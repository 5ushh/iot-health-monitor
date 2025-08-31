# IoT Health Monitoring System

Collects health data from sensors (ESP32 + MAX30100) and streams it to a cloud backend for real-time visualization.

## Structure
- `firmware/` → Embedded code (ESP32/STM32)
- `backend/` → MQTT broker + API (Python FastAPI/Flask)
- `frontend/` → Dashboard (Streamlit/React)
- `docs/` → Diagrams, notes

## Tech Stack
ESP32/STM32, MQTT, Python (FastAPI/Streamlit), React, PostgreSQL/Docker.
