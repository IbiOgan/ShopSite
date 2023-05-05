Feature: checking cart

    Scenario: view products
        Given Go to the index page
        When Click on the cart link
        Then Then it loads

    Scenario: add to cart
        Given Go to the store page
        When Click on add to cart button
        Then add one item to cart