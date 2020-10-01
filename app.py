import os
import sys
import requests
from flask import Flask, jsonify, render_template, redirect, url_for
from flask import request
app = Flask(__name__)
from requests_html import HTMLSession
from scripts import flight as F
from scripts import iata as I
from scripts import iata_detail as ID
from scripts import authenticate as A
from scripts import changepass as CH
from scripts import savepayment as SP


@app.route('/flight')
def flight():
    token = request.args.get('token')
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departureDate = request.args.get('departureDate')
    returnDate = request.args.get('returnDate')
    
    adults = request.args.get('adults')
    children = request.args.get('children')
    infants = request.args.get('infants')
    r = F.flight(origin, destination, departureDate, returnDate, adults, children, infants, token)
    return r 

@app.route('/authenticate')
def auth():
    username = request.args.get('username')
    password = request.args.get('password')
    r = A.authenticate(username, password)
    return r

@app.route('/changepass')
def changepass():
    oldpass = request.args.get('oldpass')
    newpass = request.args.get('newpass')
    token = request.args.get('token')
    r = CH.changePass(oldpass, newpass, token)
    return r

@app.route('/iata')
def iata_codes():
    token = request.args.get('token')
    r = I.getCodes(token)
    return r

@app.route('/iatadetail/<code>')
def iata_details(code):
    token = request.args.get('token')
    r = ID.getDetails(code, token)
    return r

@app.route('/savepayment')
def save_payment():
    holdername = request.args.get('holdername')
    cardnumber = request.args.get('cardnumber')
    cvv = request.args.get('cvv')
    expiration = request.args.get('expiration')
    token = request.args.get('token')
    r = SP.savePayment(holdername, cardnumber, cvv, expiration, token)
    return r

@app.errorhandler(404) 
def not_found(e):
  return render_template("404.html") 

if __name__ == '__main__':
    app.run(debug=True)