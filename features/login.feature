Feature: checking login functionality

    Scenario: view products
        Given Go to the login page
        When I Enter username "dave" and password "dave"
        And Click on login button
        Then user successfully logged in
        