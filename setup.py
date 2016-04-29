"""
Flask-SVGBarcode
    flask module providing tissue thin wrapper around pybarcode
    http://pythonhosted.org/pyBarcode/
"""

from setuptools import setup

setup(
    name="Flask-SVGBarcode",
    version="0.1",
    license="BSD",
    author="Doug Shawhan",
    author_email="doug.shawhan@gmail.com",
    url="https://github.com/lysdexia/flask-svg-barcode",
    description="flask module providing tissue thin wrapper around pybarcode",
    long_description=__doc__,
    packages=["flask_svg_barcode"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "Flask",
        "pyBarcode",
        "Flask-RESTful",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
