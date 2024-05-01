```python
# DatabaseAccess.py
# This module simulates accessing and extracting data from an unencrypted database in the Tiān Wǎng cloud banking system.
# It is used after gaining initial access through other exploits.

import sqlite3
import os

def access_database(db_path):
    """
    Simulates accessing the unencrypted database and extracting customer data.
    
    Args:
    db_path (str): The path to the database file.

    Returns:
    list: A list of tuples containing the extracted customer data.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        # Query to extract all customer data
        query = "SELECT * FROM customers"
        cursor.execute(query)
        
        # Fetch all the results
        data = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        connection.close()
        
        print("Database access successful. Data extracted.")
        return data
    except sqlite3.Error as e:
        print(f"Failed to access database: {e}")
        return []

def save_data_to_file(data, file_path):
    """
    Saves the extracted data to a file.
    
    Args:
    data (list): The data to save.
    file_path (str): The path to the file where the data should be saved.
    """
    try:
        with open(file_path, 'w') as file:
            for row in data:
                file.write(f"{row}\n")
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Failed to save data to file: {e}")

if __name__ == "__main__":
    # Example database path (this would be replaced with the actual database path in a real scenario)
    db_path = "path_to_tianwang_db.sqlite"
    # Example file path to save data
    file_path = "extracted_customer_data.txt"
    
    # Access the database and extract data
    data = access_database(db_path)
    
    # Save the extracted data to a file
    save_data_to_file(data, file_path)
```
