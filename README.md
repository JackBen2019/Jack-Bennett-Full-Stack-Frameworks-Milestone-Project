# Jack-Bennett Full Stack Frameworks Milestone Project

![JB:Marketing Logo](https://user-images.githubusercontent.com/52998869/83530842-32342b80-a4e4-11ea-9abe-101ec2c56688.png)

Are you looking for the perfect place to buy and sell marketing and website services? Then [JB:Marketing](https://jb-full-stack-frameworks.herokuapp.com/) is the place to go!

We, just like you, are always striving to be better everyday and we are always pushing for the next amazing opportunity. We live by the motto to always do more and that's something we hope we you can live by with us.

To always do more is a broad term. To do more does not simply mean spending hours, or even days working on something that will provide minimum value. To do more means you are being more efficient with your time, therefore getting more done. That's where we come in.

Whether you're someone who is looking to promote their marketing or web services, or someone who is looking to buy those services, JB:Marketing is the place to be. As a registered user you'll have the option to both list your services and/or purchase other services already listed on the website.

# How the website functions

JB:Marketing was built with the assistance of the Django3 framework. Django3 helps to put a lot of the structure and functionality in place, which in turns allows you to focus on the more important things about your website, such as the content and making it as user friendly as possible.

Throughout the building of this website, it has had consistent version control with the use of GitHub and GitPod. This is to ensure that if any issues were to occur during the building phase, we would be able to revert back to an older version of the website. When I reached the point of completion on this website, I then deployed it to Heroku.

To ensure the security of the website, all non user-friendly files such as enviroment variables and secret keys have been stored inside a seperate file, which has then been hidden with the use a .gitignore file.

All images and other static files have been stored externally with AWS S3. Whenever these files needed to be updated, I updated them on my local repository and then sent to AWS S3 by running the "python3 manage.py collectstatic" command.

**Profile Page Functionality**: The profile page will display a page that contains your email address and username, as well as the total amount of orders and an option to edit your details. Once you have made an order, the page will update and display your most recent order(s).

# Testing

[![Build Status](https://travis-ci.org/JackBen2019/Jack-Bennett-Full-Stack-Frameworks-Milestone-Project.svg?branch=master)](https://travis-ci.org/JackBen2019/Jack-Bennett-Full-Stack-Frameworks-Milestone-Project)

A lot of the testing was done by me and without the assistance of other online tools, but the tools that were used can be found in the **Technologies Used** section. The manual tests completed were as follows:

### Login, Logout and Registration

**Registration**: To test this, I visited the website in the position of a user who was visiting for the first time. I first clicked on the 'Register' button in the navigation menu. Once the registration page opened, I then proceeded to enter my registration details. To test this further, I first added a username and email that I knew was already taken to ensure that it would not let me register it. I was able to confirm that it gave me an error. After that test, I entered some new details and then clicked 'Register'. This registered me successfully and I was then able to access pages such as services, forum, profile and cart.

**Login**: To test this, I visited my website in the position of a recently registered user. Once on the website, I then proceeded to click on the 'Login' button in the navigation menu. After that, I then proceeded to enter the details I originally registered with. This then successfully logged me in.

**Logout**: To test this, I simply clicked on the 'Logout' button the navigation menu after I had logged in. This then successfully logged me out.

**Password Reset**: To test this, I first ensured that I was logged out of the website. Once I was sure of that, I proceeded to click on the 'Login' button in the navigation menu. Once the login page loaded, I clicked on the 'Forgotton your password?' link at the bottom of the login form. This then took me to another page, where I was able to enter my registered email address and have a password reset sent to my email. I successfully recieved the email and was able to update my password. Finally, I went back onto the website, loaded up the login page, added my new login details and successfully logged in.

### Browser and Mobile Responsiveness

I tested the browser and mobile responsiveness in a couple of ways. The main method I used to test the responsiveness was by inspecting all the pages on Google Chrome and using the 'Toggle device toolbar' option. Using this tool I was able to test a variaty of different screen sizes and how the page would look on specific mobile devices.

The second method I used was simply opening the website on 4 different devices and ensuring it looked user-friendly.

- My PC (21" Monitor)
- Samsung Galaxy S8
- iPhone 8
- iPad Pro

### Checkout

When testing the checkout process, you will be prompted to enter your payment details in order to complete payment. Please use the card numbers mentioned in this [link](https://stripe.com/docs/testing#cards) to test this.

During my testing of the checkout process, I used the following test details:

- **Card Number**: 4242424242424242
- **CVC**: Any 3 digits
- **Date**: Any future date

# UX

### Design

When designing a website, I like to keep it clean and simple. Not too many contrasting colours and with a simple, easy to navigate structure. From my experience, I am very easily deterred from any website that I instantly have issues with, even if those issues are very minor. Which is why I try to keep things simple.

**Structure**: The structure of my website has been created with the use of Bootstrap4. Bootstrap provides you with an entire library of helpful CSS that can be incredibly helpful when creating the structure of your website. So, with the use of Bootstrap I can be much more certain that my website will be user-friendly on just about any device.

**Colours**: As mentioned previously, I like to keep the colours simple, but I still of course like them to be appealing. Which is why I've gone for various different shades of Grey. While Grey is often seen as a fairly dull colour, I feel it complements the site well and keeps the look simple.

- Navigation and footer colour: ![#f2f2f2](https://via.placeholder.com/15/f2f2f2/000000?text=+) `#f2f2f2`
- Secondary footer colour: ![#ebeced](https://via.placeholder.com/15/ebeced/000000?text=+) `#ebeced`
- Main font colour: ![#212529](https://via.placeholder.com/15/212529/000000?text=+) `#212529`
- Secondary font colour: ![#6c757d](https://via.placeholder.com/15/6c757d/000000?text=+) `#6c757d`

**Font Family**: The font family used on this website was the same throughout. Again, I didn't feel the need to add potentially contrasting fonts throughout the website.

- -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";

**Logo**: The logo of my website was created with the use of [Wix's free logo creator](https://www.wix.com/logo/maker). The logo has the brand name (JB:Marketing) added alongside a graph that is scaling upwards. The reason I chose to add this graph was to demonstrate that my website is here to help people level up their businesses.

### User Stories

**Generic**:

- All page elements must be well presented on screens as small as 360 pixels wide and as big as 3840 pixels wide.
- All links that are external must be automatically opened in a new tab to avoid closing down the current window.
- All important/relevant pages must be easy to reach either through the navigation or other clearly visible links.

**General Visitors**:

- As a visitor, I want to have the option to register on the website.
- As a visitor, I want to be able to instantly read something that gives me an understanding of what the website's purpose is e.g. on an About page.
- As a visitor, I want to be able to contact the site admins/support team to ask any questions, or raise any issues.
- As a visitor, I want to be able to view any social media associated with the website to get an understanding of the company.

**Registered Users**:

- As a registered user, I want to be able to easily locate a logout option.
- As a registered user, I want to be able to login back in using the details I registered with.
- As a registered user, I want to be able to add my products/servics to the website.
- As a registered user, I want to be able to add and see the products/services that are in my cart.
- As a registered user, I want to be able to purchase any products/servics that are on the website.
- As a registered user, I want to be able to add posts into the forum.
- As a registered user, I want to be able to edit or delete anything I have added to the website.

**Admins**:

- As an admin, I need to be able to edit user details and/or remove them if necessary.
- As an admin, I need to ensure that I can easily login into the admin panel and access orders, users, posts and products.
- As an admin, I need to be able to remove posts and/or products if necessary.

# Wireframes and Templates



# Technologies Used

### Frameworks, Libraries, Version Control and Testing:

- **Django 3**: Used as the core framework for this website.
- **Bootstrap 4**: Used for the structure for the website, as well as making it more user-friendly.
- **Font Awesome**: Used to add icons, such as social media,
- **Heroku**: Used for the final deployment of this website.
- **GitHub**: Used for version control.
- **Travis**: Used for testing purposes.
- **W3 HTML & CSS Validator**: Used to test that all HTML and CSS was valid.

### Languages:

- **HTML5**
- **CSS3**
- **JavaScript**
- **Python3**

# Features



# Bugs / Issues

1. Password reset email: When creating the password reset form, there were no issues/bugs to be noted and everything seemed to be working fine. It was only when you went to your email inbox and noticed that no email had actually been sent.

**Solution**: 

2. Travis implementation: One of the very first things that was implemented for this website was Travis. I felt it was key that Travis was implemented early on so all issues could be picked up on quickly. The issue that kept occuring was that Travis didn't seem to understand the script I was trying to pass in the file. I was trying to direct it to a SECRET KEY, but I had no luck in getting it to work.

**Solution**: After some online research, I found that you could add "script: pip install -U pytest" instead of trying to run the script to the SECRET KEY.

**BEFORE:**
```
language: python
python:
    - "3.4"
install: "pip3 install -r requirements.txt"
script:
- SECRET_KEY="whatever" ./manage.py test 
```
**AFTER:**
```
language: python
python:
  - "3.6"
install:
  - pip install -r requirements.txt
script: pip install -U pytest
```

3. Adding a single product to the cart: The original plan for the website was to allow users to add multiple of any product to the basket. But, after some thought, I felt this wouldn't work well it's services that are being sold, rather than physical products. So, I then came across an issue as I wasn't quite sure how to only allow for a single product to be added to the basket, when I had previously allowed for multiple.

**Solution**: After some time spent looking at the way the 'add_to_cart' functionality was setup, I was able to understand that simply removing any reference of quantity would solve the issue.

**BEFORE:**
```
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))
```
**AFTER:**
```
def add_to_cart(request, id):
    """Add a specified product to the cart"""

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 1)

    request.session['cart'] = cart
    return redirect(reverse('products'))
```

4. Removing a single product from the cart: Following on from the previous issue, I then had the issue of being able to remove a single product from the basket. I managed to quite easily add functionality which cleared the entire contents of the basket, but I then needed to find a way to remove a single product.

**Solution**: After raising the issue online, I was able to get some feedback which helped me resolve the issue. I was informed that simply adding 'cart.pop' would remove a single product. Credit for this can be found [here](https://stackoverflow.com/questions/62027473/removing-a-single-product-from-the-cart-in-django/62027585#62027585).

```
def remove_from_cart(request, id):
    """Remove a specified product from the cart"""

    cart = request.session.get('cart', {})
    cart.pop(id, None)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
```

5. Adding user restrictions on who can edit/delete posts/services: I needed to ensure that only the creator of a post/service would be able to edit/delete their work. I had some trouble with this and often found that rather than hiding the edit/delete button from other users, it hid it from everyone. Including the creator.

**Solution**: 

# Database

I decided to use Postgres as the database for this project, which is built into the Django framework. Postgres can be easily accessed and updated by simply using the Django admin panel. This reason alone made it the viable choice over other databases such as MongoDB, as it was easily accessible and was within the framework I was using.

# Credits

- [Dennis Ivy](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) - A massive thanks to Dennis Ivy and his Django tutorials, which helped me to overcome a few obstacles with my website.
- Image used on About Us page: This [link](https://unsplash.com/photos/KE0nC8-58MQ) is for the free to use image that was added to the About Us page.
- Full Stack Frameworks module: A lot of the code added was inspired/assisted by following along with this module.