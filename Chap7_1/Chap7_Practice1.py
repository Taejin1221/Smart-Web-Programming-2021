# Chap7_Practice1.py
from flask import Flask

app = Flask( __name__ )

@app.route( '/' )
def hello( ):
	return "Hello, World!"