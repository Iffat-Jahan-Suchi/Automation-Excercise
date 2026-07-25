from Pages.Subscription.subcription_home import SubscriptionHome


def test_subscriptionHome(page):
    subHome=SubscriptionHome(page)
    subHome.subsciption_home("ij@gmail.com")