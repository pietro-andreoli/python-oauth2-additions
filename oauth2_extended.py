import binascii
import hmac
from hashlib import sha256

import oauth2 as oauth

"""
This module is dedicated to the custom oauth implementation by Pietro Andreoli.
It has been named p_oauth.

This module contains a class that extends the python-oauth2 module's SignatureMethod to get the same functionaliy,
but with SHA256 encoding.
See SignatureMethod_HMAC_SHA1 for another example
https://github.com/joestump/python-oauth2/blob/master/oauth2/__init__.py
"""

class SignatureMethod_HMAC_SHA256(oauth.SignatureMethod):
	name = 'HMAC-SHA256'

	def signing_base(self, request, consumer, token):
		if (not hasattr(request, 'normalized_url') or request.normalized_url is None):
			raise ValueError("Base URL for request is not set.")

		sig = (
			oauth.escape(request.method),
			oauth.escape(request.normalized_url),
			oauth.escape(request.get_normalized_parameters()),
		)

		key = '%s&' % oauth.escape(consumer.secret)
		if token:
			key += oauth.escape(token.secret)
		raw = '&'.join(sig)
		return key.encode('ascii'), raw.encode('ascii')

	def sign(self, request, consumer, token):
		"""Builds the base signature string."""
		key, raw = self.signing_base(request, consumer, token)

		hashed = hmac.new(key, raw, sha256)

		# Calculate the digest base 64.
		return binascii.b2a_base64(hashed.digest())[:-1]
