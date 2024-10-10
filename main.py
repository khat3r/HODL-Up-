import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_connection():
    connection = None
    try:
        # Print connection details (be careful with this in production!)
        print(f"Attempting to connect to:")
        print(f"Host: {os.getenv('DB_HOST')}")
        print(f"User: {os.getenv('DB_USER')}")
        print(f"Database: {os.getenv('DB_NAME')}")
        
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        print("Successfully connected to the database")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print(f"Error Code: {e.errno}")
        print(f"SQL State: {e.sqlstate}")
        print(f"Error Message: {e.msg}")
    return connection

def create_table(connection):
    create_users_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        phone_nunmber VARCHAR(20), 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """
    
    create_cryptocurrencies_table_query = """
    CREATE TABLE IF NOT EXISTS cryptocurrencies (
        crypto_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        market_cap DECIMAL(18, 2),
        hourly_price DECIMAL(18, 2),
        hourly_percentage DECIMAL(5, 2),
        time_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    create_alerts_table_query = """
    CREATE TABLE IF NOT EXISTS alerts (
        alert_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        crypto_id INT,
        threshold_price DECIMAL(18, 2),
        threshold_percentage DECIMAL(5, 2),
        method ENUM('above', 'below') NOT NULL,
        notification_method ENUM('email', 'sms', 'push') NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (crypto_id) REFERENCES cryptocurrencies(crypto_id) ON DELETE CASCADE
    )
    """

    create_notifications_table_query = """
    CREATE TABLE IF NOT EXISTS notifications (
        notification_id INT AUTO_INCREMENT PRIMARY KEY,
        alert_id INT,
        message TEXT,
        notification_method ENUM('email', 'sms', 'push') NOT NULL,
        sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (alert_id) REFERENCES alerts(alert_id) ON DELETE CASCADE
    )
    """
    # error handling for users table 
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_users_table_query)
            connection.commit()
            print("Table 'users' created successfully")
    except Error as e:
        print(f"Error creating 'users' table: {e}")
    
    #error handling for cryptocurrencies table 
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_cryptocurrencies_table_query)
            connection.commit()
            print("Table 'cryptocurrencies' created successfully")
    except Error as e:
        print(f"Error creating 'cryptocurrencies' table: {e}")
    
    #error handling for alerts table 
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_alerts_table_query)
            connection.commit()
            print("Table 'alerts' created successfully")
    except Error as e:
        print(f"Error creating 'alerts' table: {e}")
    
     #error handling for notifications table 
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_notifications_table_query)
            connection.commit()
            print("Table 'notification' created successfully")
    except Error as e:
        print(f"Error creating 'notification' table: {e}")
        

def main():
    connection = create_connection()
    if connection is None:
        return
    
    create_table(connection)
    
    connection.close()
    print("Goodbye!")
    
if __name__ == "__main__":
    main()
    
