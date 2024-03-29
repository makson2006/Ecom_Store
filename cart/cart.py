from store.models import Product

class Cart():
    def __init__(self,request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new no session key. Create one.
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

            # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        return products


    def get_quants(self):
        quantites = self.cart
        return quantites

    def delete(self,product):
        product_id = str(product)
        # Delete from dic
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart

        total = 0
        for key,value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total


    # def cart_total(self):
    #     product_ids = self.cart.keys()
    #     products = Product.objects.filter(id__in=product_ids)
    #     quantities = self.cart
    #
    #     total = 0
    #     for key,value in quantities.items():
    #         key = int(key)
    #         for product in products:
    #             if product.id == key:
    #                 total = total + (product.price * value)
    #
    #     return total