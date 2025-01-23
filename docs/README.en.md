# Documentation in English

## Overview

### Problem
Security management companies face challenges in real-time monitoring of distributed security devices. This can result in delays in identifying failures or incidents.

### Solution
We developed a web-based monitoring dashboard that:
- Integrates security devices via API.
- Displays operational status and failure alerts.
- Sends automatic notifications via email or SMS.
- Centralizes event logs for auditing.

## Features
- Real-time monitoring
- Automated notifications
- Intuitive and responsive interface
- Dynamic charts

## Technologies
- Frontend: HTML, CSS, JavaScript
- Backend: Node.js
- Database: MySQL
- API: REST

## How to Run

### Requirements
- Installed Node.js
- Configured MySQL
- Modern browser

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/youruser/security-management-solutions.git
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure the database:
   - Import the `database.sql` file into your MySQL.
   - Update credentials in the `.env` file.

4. Start the server:
   ```bash
   npm start
   ```

5. Access the application in the browser:
   - URL: `http://localhost:3000`

## Contributions
Contributions are welcome! Follow the contribution guide in the `CONTRIBUTING.md` file.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
