#!/usr/bin/env python
from flask import Flask
from flask_svgbarcode import svg_barcode
app=Flask(__name__)
api = svg_barcode(app, "/api/barcode")

if __name__ == "__main__":
    app.run()

