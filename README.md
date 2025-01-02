# Micro-Grid-Simulator

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Installation](#installation)

## Project Overview

The Micro-Grid Simulator is an interactive web-based platform designed to model, analyze, and optimize micro-grid systems. This application enables users to simulate energy flows, resource allocation, and cost analysis within a micro-grid, providing insights into energy efficiency, sustainability, and economic feasibility. Built with modern web technologies, the simulator ensures a responsive and seamless user experience, empowering users to make informed decisions about their energy systems.

Key Features:
- Interactive Visualization: Real-time graphical representation of energy flows and resource utilization within the micro-grid.
- Customizable Scenarios: Users can modify parameters such as energy inputs, consumption patterns, and environmental factors to simulate different grid configurations.
- Data Persistence: Persistent state management ensures simulations are saved for future reference and comparative analysis.
- Optimized Performance: High-performance backend and caching for quick responses to complex simulations.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Vite, ShadCN, Typecript
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Getting Started

### Prerequisites

Make sure you have the following installed on your local machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Node.js](https://nodejs.org/) (for React development)
- Python 3.10

### Installation ()

1. **Clone the repository**
   ```bash
   git clone https://github.com/ethandfmacleod/Micro-Grid-Simulator
   cd Micro-Grid-Simulator

2. **Run Containers**
   ```bash
   docker compose up -d

3. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt

4. **Run Migrations**
   ```bash
   python manage.py migrate

5. **Run Local Server**
   ```bash
   python manage.py runserver 8001

6. **Run Front-end**
   ```bash
   cd ../frontend
   npm install
   npm run dev