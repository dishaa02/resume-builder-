from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace 'root' with your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Replace '' with your MySQL password
app.config['MYSQL_DB'] = 'pbl2'  # Replace 'your_database_name' with your MySQL database name
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)

# Create table query
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""

# Route to create the table
@app.route('/create_table')
def create_table():
    # Connect to MySQL
    cur = mysql.connection.cursor()
    # Execute the create table query
    cur.execute(create_table_query)
    # Commit changes
    mysql.connection.commit()
    # Close connection
    cur.close()
    return 'Table created successfully!'

if __name__ == '__main__':
    app.run(debug=True)
