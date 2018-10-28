# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
from flask import Flask, render_template, request

import stripe

app = Flask(__name__)

secret_key = os.environ['STRIPE_SECRET_KEY']
print(secret_key)

events_prices = {
    'career_insights': 3000,
    'eoy_dinner': 3500,
    'conference': 948,
    'retreat': 19200,
}

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = secret_key

def make_stripe_payment():
    token = request.form['stripeToken']
    event = request.form['event']
    amount = events_prices[event]
    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=token
    )
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='gbp',
        description=f'Payment for {event}',
        metadata={'event': request.form['event']}
    )
    return

@app.route('/')
def home():
    return '<h1>HELLO YDWC!</h1>'

@app.route('/pay', methods=['POST'])
def pay():
    try:
        make_stripe_payment()
    except Exception as e:
        # return jsonify({'result': 'failed', 'reason': str(e)})
        return render_template('basic.html', message="""Failed to process payment. Please contact someone at YDWC.""")

    return render_template('basic.html', message="Your payment was processed successfully.")

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
