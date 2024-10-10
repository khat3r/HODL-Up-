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

---
### 1. Clone this repository or download the source code.

```bash 
git clone https://github.com/khat3r/HODL-Up-.git 
```
---
### 2. Install the required packages:  

```bash
pip install -r requirements.txt
```
---
### 3. Create a .env file and replcae the following placeholders with the acutal SQL connection credentials (included in the lytespace submission). 

```bash
DB_HOST=your_mysql_host
DB_USER=your_mysql_username
DB_PASS=your_mysql_password
DB_NAME=your_database_name
```
---
### 4. Save and close the .env file. Please ensure that it is included in your .gitignore file as it contians sensitive information that cannot be leaked (if you successfully cloned this repository, .env file should be already included in the .gitignore file)  

