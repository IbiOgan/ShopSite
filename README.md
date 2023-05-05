# My Render URL

https://customer-subscription-site.onrender.com/

# My Data Source(Customer Subscription Data)

https://www.kaggle.com/datasets/gsagar12/dspp1?select=customer_product.csv

# Introduction

The project is developed to apply my knowledge of Flask Python framework in building a web application. This application is built on open source data from Kaggle.com. The data contains tables with products, customer info, customer subscription and support cases. Here’s a link to the data set on Kaggle.

# Web App Development

Here are some snippets of code I used while setting up this virtual environment.

```python
cd MyWebApp/
pyenv install 3.9.0
pyenv local 3.9.0
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install flask
```

Running of App. Here are some snippets of code I used while setting up this flask application.

```python
export FLASK_APP=server.py
export FLASK_DEBUG=True
python3 -m flask run --host=0.0.0.0
```

Here are some snippets of code I used while setting up the GitHub repo.

```python
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin <git url>
git push -u origin main
```

I also choose to use GitHub for version control and code maintenance. From my experience using GitHub, I got more familiar with running commands in the terminal. I also felt less anxiety about my work being lost because it was stored in a remote repository online. Over time I built the habit of committing and pushing my code to the repository frequently. Using GitHub gave me confidence to experiment with my codebase because I could easily restore a previous save point from the git repository. I learnt to use “branch” command to create another branch where I could attempt to implement different HTML and python features. I will definitely be using git for all my projects in the future.
Here are some snippets of code I used while using the GitHub branch.

```python
git branch
git checkout -b experiment-with-html-tables
git push --set-upstream origin experiment-with-html-tables
git checkout main
git merge experiment-with-html-tables
```

# Maintenance/Testing

Create features folder. Create driver folder and download chrome driver. Create features file. Sample code below.
Create product.feature:

```python
Feature: Product Page
"""
Confirm that we can browse the Product related page on our site
"""
Scenario: success for visiting index(Home) and Product pages
Given I navigate to the index page
When I click on the link to Product
Then I should see the table for Products
Create steps folder. Create product.py
from behave import given, when, then
@given(u'I navigate to the home page')
def nav(context):
"""
Navigate to the index page
"""
context.browser.get('http://localhost:5000')
@when(u'I click on the link to product')
def click(context):
"""
Find the desired link
"""
context.browser.find_element_by_id('product').click()
@then(u'I should see the table for products')
def details(context):
"""
if successful, then we should be directed to the product page
"""
# use print(context.browser.page_source) to aid debugging
print(context.browser.page_source)
assert context.browser.current_url == 'http://localhost:5000/product'
assert 'Product ID' in context.browser.page_source
```

run behave command in terminal to do testing.
