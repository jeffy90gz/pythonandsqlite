from flask import Flask, request, jsonify
import sqlite3


conn = sqlite3.connect('invoices.db')
print("open database connection successfully");


conn.execute(''' CREATE TABLE invoices
(ID            INTEGER PRIMARY KEY,
invoice_name     Text NOT NULL,
invioce_amount   INT NOT NULL);''')
print("table created successfully")

conn.close()