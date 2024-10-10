### Database Design for Hodl Up!

**Objective**: As part of Week 5, we focus on designing and implementing the backbone of our crypto alert application, specifically the database.

## Data Model
The database is structured to store essential information related to user accounts, cryptocurrency alert configurations, supported cryptocurrencies, and notifications. Here’s a focused breakdown of the entities and their attributes:

- **Users**: Stores information about users, including their credentials and contact details.  
  _Attributes_: `user_id` (PK), `email`, `phone_number`, `created_at`, `updated_at`.

- **Cryptocurrencies**: Keeps track of the list of supported cryptocurrencies and their market data.  
  _Attributes_: `crypto_id` (PK), `crypto_name`, `market_cap`, `hourly_price`, `time_updated`, `hourly_percentage`.

- **Alerts**: Stores user-defined cryptocurrency price and percentage change alerts.  
  _Attributes_: `alert_id` (PK), `user_id` (FK), `crypto_id` (FK), `threshold_price`, `threshold_percentage`, `condition`, `notification_method`, `created_at`, `updated_at`.

- **Notifications**: Logs every notification sent to the user in response to an alert being triggered.  
  _Attributes_: `notification_id` (PK), `alert_id` (FK), `message`, `notification_method`, `sent_at`.

## Why SQL?
For this activity, we chose **MySQL** as our database for several reasons:

1. **Relational Data**: Our project requires modeling clear relationships between users, alerts, and cryptocurrencies. MySQL is well-suited for these relationships through its use of foreign keys and relational integrity.
2. **Consistency**: MySQL ensures data consistency, which is crucial when handling real-time alerts and notifications for users.
3. **Efficient Queries**: MySQL allows for efficient querying of user-specific data, cryptocurrency prices, and alert configurations, which is essential for delivering timely notifications.
4. **Scalability**: As the user base grows, MySQL offers scalability for handling a larger number of users and alerts.

## Schema Design
We have designed the following schema for MySQL:

- **Users** and **Alerts** tables are related through the `user_id`, while **Alerts** and **Cryptocurrencies** are connected via the `crypto_id`.
- The **Notifications** table logs notifications sent to users, linked by `alert_id`.

This relational design ensures data integrity and smooth interactions between users and their alert configurations.

---

## Setup Instructions for the Database
### Prerequisites
- MySQL installed locally or accessible via a server.
- Database management tool (e.g., MySQL Workbench or a MySQL extension in VS Code).
  
### Steps:

### 1. Clone the repository:
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

