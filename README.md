# python-oauth2-additions
This repo tracks my custom additions to the [python-oauth2 repo by joestump](https://github.com/joestump/python-oauth2 "python-oauth2 repo by joestump") repo.

##To Use
To use this signature method simply clone this repo or copy the code from p_oauth_signatures.py. Import the class `SignatureMethod_HMAC_SHA256` and replace your use of SignatureMethod_HMAC_SHA1 with it. Below is a basic example.

    import oauth2 as oauth
	from p_oauth_signatures import SignatureMethod_HMAC_SHA256
	import requests
	
	token = oauth.Token(key=TOKEN_KEY, secret=TOKEN_SECRET)
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	realm = REALM

	params = {
		'oauth_version': "1.0",
		'oauth_nonce': oauth.generate_nonce(),
		'oauth_timestamp': str(int(time.time())),
		'oauth_token': token.key,
		'oauth_consumer_key': consumer.key
	}
	
	req = oauth.Request(method=HTTP_METHOD, url=URL, parameters=params)
	# Custom signature for OAuth from p_oauth lib
	# Note the replacement of SignatureMethod_HMAC_SHA1()
	signature_method = SignatureMethod_HMAC_SHA256()
	req.sign_request(signature_method, consumer, token)
	header = req.to_header(realm)
	headery = header['Authorization'].encode('ascii', 'ignore')
	headerx = {"Authorization": headery, "Content-Type":"application/json"}

	# headerx can now be used in the header of requests
    