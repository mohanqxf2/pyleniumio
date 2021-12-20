
def test_demo(py):
    py.visit('https://weathershopper.pythonanywhere.com/')
    assert py.title() == 'Current Temperature'

    py.get('a[href="/sunscreen"]').click()
    assert py.title() == 'The Best Sunscreens in the World!'

    #add item to cart
    py.get('button[class="btn btn-primary"]').is_displayed()
    py.contains('Add').click()

    #click on the cart button
    py.get('button[class="thin-text nav-link"]').is_displayed()  
    py.contains('Cart - ').click()

    assert py.contains('Checkout').should().be_visible()