from Pages.Subscription.subcription_home import SubscriptionHome


def test_subscriptionHome(page):
    subHome=SubscriptionHome(page)
    subHome.subscription_home("ij@gmail.com")
    subHome.subscription_cart("ij@gmail.com")

def test_subscriptionCart(page):
    subCart=SubscriptionHome(page)
    subCart.subscription_cart("ij@gmail.com")
