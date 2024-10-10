# Hodl Up!
### Your Ultimate Crypto Companion

**Hold up—crypto’s on the move! Get instant alerts and stay ahead of the market**

## Project Description
Hodl Up! is a crypto alert application designed to help users stay ahead of the market by allowing them to set custom alerts for price thresholds and percentage changes in cryptocurrencies. Users receive notifications via their preferred communication platforms, such as Telegram, Slack, or Discord.

This project features a frontend built with **JavaScript** and **React**, a backend powered by **Python**, and data managed using **MySQL**, which stores user accounts, alert configurations, cryptocurrency data, and historical notifications.

---

## Data Model
The database is structured to store information about users, their cryptocurrency alert configurations, available cryptocurrencies, and historical notifications. Here's an overview of the tables:

- **Users**: Stores user information including usernames, emails, and passwords.  
  _Columns_: `user_id` (PK), `email`, `phone_number`, `created_at`, `updated_at`.
  
- **Cryptocurrencies**: Stores the list of supported cryptocurrencies and their current prices.  
  _Columns_: `crypto_id` (PK), `crypto_name`, `market_cap`, `hourly_price`, `time_updated`, `hourly_percentage`.

- **Alerts**: Stores user-set price threshold and percentage change alerts.  
  _Columns_: `alert_id` (PK), `user_id` (FK), `crypto_id` (FK), `threshold_price`, `threshold_percentage`, `condition`, `notification_method`, `created_at`, `updated_at`.

- **Notifications**: Logs each alert notification sent to the user.  
  _Columns_: `notification_id` (PK), `alert_id` (FK), `message`, `notification_method` (e.g., Slack, Telegram), `notification_confirmation`, `sent_at`.

---

## Why SQL?
We chose **SQL (MySQL)** for this project because of its relational data management capabilities, consistency, and querying power. MySQL is ideal for:
1. **Relational Data**: Modeling relationships between users, their alerts, and cryptocurrencies.
2. **Consistency**: Ensuring data integrity and reliability, especially when processing and logging notifications.
3. **Efficient Queries**: Easily filter, track, and analyze alerts and user data.
4. **Scalability**: Well-suited for handling an increasing number of users and alerts.

---

## Tech Stack
- **Frontend**: JavaScript, React
- **Backend**: Python
- **Database**: MySQL

---

## Setup Instructions
### Prerequisites
- MySQL installed on your local machine or accessible server.
- A database management tool (like MySQL Workbench or MySQL extension installed in your VS Code).
- Python (for the backend API connection).
- Node.js and npm (for the frontend React application).
---
### 1. Install MySQL
You can download and install MySQL from the official website: [MySQL Download](https://dev.mysql.com/downloads/). Ensure that MySQL is running.

---
### 2. Connect to the Database
You can connect using MySQL Workbench or through a command line:

```bash
mysql -u hold -p -h ip_address -P 3306
```
---
### 3. Create the Database and Tables
---

### 4. Connect the Database to the Python Backend
Use the following Python code to connect your backend to the MySQL database. Ensure you load your credentials securely (e.g., using environment variables from a `.env` file).
```bash
pip install mysql-connector-python
```

Then, in your Python script `(backend.py)`, connect to the database:
```bash
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
```
---
### 5. Frontend Setup (React)
To set up the frontend:

1. Ensure Node.js and npm are installed on your system.
2. Navigate to your frontend project directory and run:
```bash
npm install
```
3. Start the React development server:
```bash
npm start
```
---
### 6. Running the Application
- Ensure MySQL is running and the database is set up.
- Run the backend Python API to handle requests and manage alerts.
- The React frontend can be accessed via localhost:3000 once the development server is started.
---
### 7. Testing the Application
- Create sample users and alerts.
- Test notifications by simulating price thresholds or percentage changes.
- Verify that notifications are delivered via your chosen third-party integrations (Telegram, Slack, etc.).
