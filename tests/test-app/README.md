#Test App
It would behoove you to run this in a virtualenv.

```bash
cd test_app
virtualenv venv
source venv/bin/activate
(venv) pip install git+https://github.com/lysdexia/flask-svg-barcode
(venv) ./app.py
```

Browse to http://localhost:5000 and groove on the stripey bits.

Have a look at ```tests/test-app/static/js/test-barcode.js``` for some bright
ideas on how to use this. The innerHTML technique is kind of crappy, but it should be fine for displaying your coupon.
