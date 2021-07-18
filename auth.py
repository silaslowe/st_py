import stripe

stripe.api_key = ''

print(stripe.Customer.list())