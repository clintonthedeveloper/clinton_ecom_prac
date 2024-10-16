class Cart():
	def __init__(self, request):
		self.session = request.session
		
        # Get the current session key if it exists
		cart = self.session.get('session_key')
		
        # if the user is new, no session key! create one!
		cart = self.session['session_key'] = {}
		


        # make sure cart is available in all pages of the site
		self.cart = cart

	def add(self, product):
		product_id = str(product.id)

		# Logic
		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = {'price': str(product.price)}

		self.session.modified = True

	def __len__(self):
		return len(self.cart)		
		
