from crypto_portfolio.products.model_products import Products


def get_product_by_name_and_username(product_slug, username):
    return Products.objects.get(slug=product_slug, product_user__username=username)
