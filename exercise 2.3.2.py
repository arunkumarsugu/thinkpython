""" Suppose the cover price of a book is $24.95,but book stores get a 40% discount.
Shipping costs $3 for the ﬁrst copy and 75 cents for each additional copy.
What is the total wholesale cost for 60 copies? """
cost_price = 24.95
discount = (cost_price/100)*40
cost_price_with_discount_onebook = cost_price-discount
no_of_books = 60
cost_price_all_book = cost_price_with_discount_onebook * no_of_books
shipping_cost = 3 + .75* (no_of_books-1)
final_price = cost_price_all_book + shipping_cost
print(final_price)