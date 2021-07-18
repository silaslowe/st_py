# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.

import os
import stripe

from flask.views import MethodView
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stripe.api_key = ''


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session(self):
    price_id = '{{PRICE_ID}}'

    session = stripe.checkout.Session.create(
        success_url='https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://example.com/canceled.html',
        payment_method_types=['card'],
        mode='subscription',
        line_items=[{
            'price': price_id,
            # For metered billing, do not pass quantity
            'quantity': 1
        }],
    )

    # return redirect(session.url, code=303)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class SubscriptionPage(MethodView):

    def get(self):
        return render_template('subscription.html')


app.add_url_rule('/subscription', view_func=SubscriptionPage.as_view('subscription_page'))
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

if __name__ == '__main__':
    app.run(port=4242)
