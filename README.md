# Jack-Bennett Full Stack Frameworks Milestone Project

![JB:Marketing Logo](https://user-images.githubusercontent.com/52998869/83530842-32342b80-a4e4-11ea-9abe-101ec2c56688.png)

Are you looking for the perfect place to buy and sell marketing and website services? Then [JB:Marketing](https://jb-full-stack-frameworks.herokuapp.com/) is the place to go!

We, just like you, are always striving to be better everyday and we are always pushing for the next amazing opportunity. We live by the motto to always do more and that's something we hope we you can live by with us.

To always do more is a broad term. To do more does not simply mean spending hours, or even days working on something that will provide minimum value. To do more means you are being more efficient with your time, therefore getting more done. That's where we come in.

Whether you're someone who is looking to promote their marketing or web services, or someone who is looking to buy those services, JB:Marketing is the place to be. As a registered user you'll have the option to both list your services and/or purchase other services already listed on my website.

# How my website functions

The bulk of the functionality was made possible with the use of the Django3 framework. Django3 is a Python run application and helps to put a lot of the structure and functionality in place, which in turns allows you to focus on the more important things about your website, such as the content and making it as user friendly as possible.

There are many benefits to using the Djnago3 framework, but the biggest one in my opinion is having instant access to an admin panel. The admin panel allows you to create, view, update and/or delete and record, whether it's a post, user or even just a specific category for one of your products.

**Profile Page Functionality**: The profile page will display a page that contains your email address and username, as well as the total amount of orders and an option to edit your details. Once you have made an order, the page will update and display your most recent order(s).

# Deployment

The development of this project was completed with the use of GitPod, with regular version control being added with the use of GitHub.

Throughout the building of this website, it has had consistent version control with the use of GitHub and GitPod. This is to ensure that if any issues were to occur during the building phase, I would be able to revert back to an older version of my website. When I reached the point of completion on this website, I then deployed it to Heroku.

To ensure the security of my website, all non user-friendly files such as enviroment variables and secret keys have been stored inside a seperate env.py file, which has then been hidden with the use a .gitignore file.

All images and other static files have been stored externally with AWS S3. Whenever these files needed to be updated, I updated them on my local repository and then sent to AWS S3 by running the "python3 manage.py collectstatic" command.

**Deployment Process**

1. The first stage in the deployment process was to create an app on Heroku and then sync that app to my GitHub repository.
2. Staying on Heroku, I then added all relevant Config Vars such as the database url and any secret keys.
3. The third stage in the final deployement was doing a push of my finished code to GitHub and Heroku.
4. As there were no errors after the final code had been pushed, my website was successfully deployed to both GitHub and Heroku.

# Testing

[![Build Status](https://travis-ci.org/JackBen2019/Jack-Bennett-Full-Stack-Frameworks-Milestone-Project.svg?branch=master)](https://travis-ci.org/JackBen2019/Jack-Bennett-Full-Stack-Frameworks-Milestone-Project)

A lot of the testing was done by me and without the assistance of other online tools, but the tools that were used can be found in the **Technologies Used** section. The manual tests completed were as follows:

### General Website Functionality Tests

**Registration**: To test this, I visited my website in the position of a user who was visiting for the first time. I first clicked on the 'Register' button in the navigation menu. Once the registration page opened, I then proceeded to enter my registration details. To test this further, I first added a username and email that I knew was already taken to ensure that it would not let me register it. I was able to confirm that it gave me an error. After that test, I entered some new details and then clicked 'Register'. This registered me successfully and I was then able to access pages such as services, forum, profile and cart.

**Login**: To test this, I visited my website in the position of a recently registered user. Once on my website, I then proceeded to click on the 'Login' button in the navigation menu. After that, I then proceeded to enter the details I originally registered with. This then successfully logged me in.

**Logout**: To test this, I simply clicked on the 'Logout' button the navigation menu after I had logged in. This then successfully logged me out.

**Password Reset**: To test this, I first ensured that I was logged out of my website. Once I was sure of that, I proceeded to click on the 'Login' button in the navigation menu. Once the login page loaded, I clicked on the 'Forgotton your password?' link at the bottom of the login form. This then took me to another page, where I was able to enter my registered email address and have a password reset sent to my email. I successfully recieved the email and was able to update my password. Finally, I went back onto my website, loaded up the login page, added my new login details and successfully logged in.

**User Restrictions on Editing/Deleting Posts/Service**: To ensure that only the user who added a post or service would be able to edit/delete that post or service, I needed to add some user restrictions directly into the templates, which is what I did. To test this, I created a post and a service from 2 seperate accounts. I then viewed both posts and services from different accounts to ensure that I was unable to see an edit or delete button if the post or service wasn't mine. This was the case on both accounts and this test was successful.

### Browser and Mobile Responsiveness

I tested the browser and mobile responsiveness in a couple of ways. The main method I used to test the responsiveness was by inspecting all the pages on Google Chrome and using the 'Toggle device toolbar' option. Using this tool I was able to test a variaty of different screen sizes and how the page would look on specific mobile devices.

The second method I used was simply opening my website on 4 different devices and ensuring it looked user-friendly.

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

**Font Family**: The font family used on this website was the same throughout. Again, I didn't feel the need to add potentially contrasting fonts throughout my website.

- -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";

**Logo**: The logo of my website was created with the use of [Wix's free logo creator](https://www.wix.com/logo/maker). The logo has the brand name (JB:Marketing) added alongside a graph that is scaling upwards. The reason I chose to add this graph was to demonstrate that my website is here to help people level up their businesses.

### Defensive Design

As a visitor to my own website, I wanted to make it as user friendly as possible. This meant that it had to be easy to navigate, have easy to use features and functionality and also make it impossible to become lost at any point while browsing the site.

Below are the design procedures I put in place:

- Success and error messages have been added wherever necessary. For example, if a user's card details are incorrect, a message will pop up to confirm that the payment could not be processed.
- At no point is the website less functional on a smaller device than it is on a larger design. My website has been thoroughly checked and tested to ensure everyone has the same experience.
- If a user tries to purchase an item with incorrect card details, they will instanly be met with a helpful error message to assist them.
- All external pages on my site will automatically be opened in a new window, rather than closing down the current tab.
- If a user opens up one of the category pages on the forum, they can easily go back to the main forum by clicking on the 'Back to Forum' button on every category page.
- If a user opens up a post, they can easily go back to the main forum by clicking on the 'Back to Forum' button on every post.
- If a user opens up a service, they can easily go back to the main forum by clicking on the 'Back to Forum' button on every service.

### User Stories

**Generic**:

- All page elements must be well presented on screens as small as 360 pixels wide and as big as 3840 pixels wide.
- All links that are external must be automatically opened in a new tab to avoid closing down the current window.
- All important/relevant pages must be easy to reach either through the navigation or other clearly visible links.

**General Visitors**:

- As a visitor, I want to have the option to register on my website.
- As a visitor, I want to be able to instantly read something that gives me an understanding of what my website's purpose is e.g. on an About page.
- As a visitor, I want to be able to contact the site admins/support team to ask any questions, or raise any issues.
- As a visitor, I want to be able to view any social media associated with my website to get an understanding of the company.

**Registered Users**:

- As a registered user, I want to be able to easily locate a logout option.
- As a registered user, I want to be able to login back in using the details I registered with.
- As a registered user, I want to be able to add my products/servics to my website.
- As a registered user, I want to be able to add and see the products/services that are in my cart.
- As a registered user, I want to be able to purchase any products/servics that are on my website.
- As a registered user, I want to be able to add posts into the forum.
- As a registered user, I want to be able to edit or delete anything I have added to my website.

**Admins**:

- As an admin, I need to be able to edit user details and/or remove them if necessary.
- As an admin, I need to ensure that I can easily login into the admin panel and access orders, users, posts and products.
- As an admin, I need to be able to remove posts and/or products if necessary.

# Wireframes and Template Descriptions

As with almost any webite I build, the first mock ups of the wireframes tend to differ from the final product. So, with this in mind I always start creating some very basic mock ups on Microsoft Word and then once I am set on the designs I want, I create them in full detail using [Balsamiq](https://balsamiq.com/).

**Base Template**

The base template was used to store all the code that would be re-used across my entire website. This included sections such as the navigation and the footer, as these were likely to never change. The base template was also used to store all links to any external files such as Stylesheets, as well as adding content blocks for page titles and general body content.

The navigation was created with the use of Bootstrap4 and this was to assist in adding a dropdown menu for all smaller devices. The navigation link options will also change dependant on whether you are logged in or not.

<details><summary>Base Template Wireframe</summary>
<p>

![Base Template - Desktop View](https://user-images.githubusercontent.com/52998869/83656886-05e9df00-a5b8-11ea-8edd-87ada5fe81d7.png)
![Base Template - Mobile View](https://user-images.githubusercontent.com/52998869/83656954-1c903600-a5b8-11ea-9107-ee993208b765.png)

</p>
</details>

**Login Template**

The login template was the first template on my website to make use of 'bootstrap_tags'. With the use of bootstrap_tags, I was able to use a pre-generated login form which contained a username and password field.

I also added the option for the user to reset their password if they were to forget it.

<details><summary>Login Template Wireframe</summary>
<p>

![Login Template - Desktop View](https://user-images.githubusercontent.com/52998869/83770421-f2eb1380-a678-11ea-9259-78faa371f9a3.png)
![Login Template - Mobile View](https://user-images.githubusercontent.com/52998869/83656954-1c903600-a5b8-11ea-9107-ee993208b765.png)

</p>
</details>

**Registration Template**

The registration template was the second template to make use of 'bootstrap_tags'. With the use of bootstrap_tags, I was able to use a pre-generated login form which contained an email address, username, password and password confirmation field.

I also added the option to login if you already had an account on the site.

<details><summary>Registration Template Wireframe</summary>
<p>

![Registration Template - Desktop View](https://user-images.githubusercontent.com/52998869/83772080-e4056080-a67a-11ea-9c12-cebd31eab1ff.png)
![Registration Template - Mobile View](https://user-images.githubusercontent.com/52998869/83772210-1020e180-a67b-11ea-9bfc-af553180da2f.png)

</p>
</details>

**About Us Template**

The about us page is actually used as the main home page of my website. As you can only access the main content of my website when your logged in, I felt it would be a good idea for people to get an understanding of my website as soon as they landed on the site.

At the bottom of the about page are two fairly large buttons. One button leads you to the registration page, while the other leads you to the login page.

<details><summary>About Us Template Wireframe</summary>
<p>

![About Us Template - Desktop View](https://user-images.githubusercontent.com/52998869/83663837-1b173b80-a5c1-11ea-93d7-b236f0153643.png)
![About Us Template - Mobile View](https://user-images.githubusercontent.com/52998869/83663961-44d06280-a5c1-11ea-9183-13b93e8ccc40.png)

</p>
</details>

**All Services Template**

The services page is where all the products/services are listed. All registered users have the option to list thier own website or marketing services on my website. This can be done by clicking on the 'Add new service' button at the top of the page. They will be asked to add a service title, description, category, price and image.

The products are listed in rows of 3 on full width screens, but will drop down to just one product per row on smaller screens.

<details><summary>All Services Template Wireframes</summary>
<p>

**Services**

![Services Template - Desktop View](https://user-images.githubusercontent.com/52998869/83784812-7bbd7b80-a688-11ea-9b86-cc171cfd6859.png)
![Services Template - Mobile View](https://user-images.githubusercontent.com/52998869/83784967-89730100-a688-11ea-91e1-9b29e1b272f2.png)

**Add a Service**

![Add a Service Template - Desktop View](https://user-images.githubusercontent.com/52998869/83791300-79abea80-a691-11ea-9434-6f0ad73b363a.png)
![Add a Service Template - Mobile View](https://user-images.githubusercontent.com/52998869/83791322-86304300-a691-11ea-82ff-ce3179fcebc0.png)

</p>
</details>

**All Forum Templates**

The forum page is where all the community posts are added. It has been split up into seperate categories so it is easy for the user to navigate and find specific posts they want to see.

Each category on the forum has a maximum of 4 posts that can be shown and if you would like to see the rest of the posts for that category, you will need to click the link that takes you to the seperate category page.

<details><summary>All Forum Template Wireframes</summary>
<p>

**Forum**

![Forum Template - Desktop View](https://user-images.githubusercontent.com/52998869/83861081-0c8f6800-a718-11ea-8cf1-cd13ee78c450.png)
![Forum Template - Mobile View](https://user-images.githubusercontent.com/52998869/83861107-17e29380-a718-11ea-97c4-e6edb5c30137.png)

**Add a Post Template**

![Add a Post Template - Desktop View](https://user-images.githubusercontent.com/52998869/83859547-fe404c80-a715-11ea-9571-e54cf791337c.png)
![Add a Post Template - Mobile View](https://user-images.githubusercontent.com/52998869/83859576-08624b00-a716-11ea-918b-4cb4ea3df952.png)

**Category Page Default Template**

![Category Page Template - Desktop View](https://user-images.githubusercontent.com/52998869/83861857-0e0d6000-a719-11ea-861e-cb8d65d7ecb9.png)
![Category Page Template - Mobile View](https://user-images.githubusercontent.com/52998869/83862211-88d67b00-a719-11ea-8a4f-a9cfe450b84e.png)

</p>
</details>

**All Profile Template**

The profile page is where the user can find personal information such as their account details and the orders they have placed.

I have added an if statement onto the profile link so that the page will alternate dependant on whether they have made an order or not. If they have made an order, then it will show on their total number of orders and they will also be able to see the order details at the bottom of the page. If they haven't made an order, then the order count will be 0 and the order details section will be completed removed.

<details><summary>All Profile Template Wireframes</summary>
<p>

**Profile With No Orders**

![Profile With No Orders Template - Desktop View](https://user-images.githubusercontent.com/52998869/83865028-7eb67b80-a71d-11ea-8724-90f47d056978.png)
![Profile With No Orders Template - Mobile View](https://user-images.githubusercontent.com/52998869/83865222-cf2dd900-a71d-11ea-8442-af7df231d706.png)

**Profile With Orders Made**

![Profile With Orders Made Template - Desktop View](https://user-images.githubusercontent.com/52998869/83865963-f638da80-a71e-11ea-9af9-0d926d6a2961.png)
![Profile With Orders Made Template - Mobile View](https://user-images.githubusercontent.com/52998869/83865990-0355c980-a71f-11ea-8d55-873a64fea254.png)

</p>
</details>

**Cart Template**

The cart template gives the user a full breakdown of all the items they have added to thier cart. This includes the service name, service type and price.

The user will also have the option to remove indiviudal items from the cart should they wish to do so.

<details><summary>Cart Template Wireframe</summary>
<p>

![Cart Template - Desktop View](https://user-images.githubusercontent.com/52998869/83973172-7f494080-a8dc-11ea-9b42-9398b26584d2.png)
![Cart Template - Mobile View](https://user-images.githubusercontent.com/52998869/83973492-adc81b00-a8de-11ea-91f6-739b6309276f.png)

</p>
</details>

**Checkout Template**

The checkout template is used as the final page before the user completes their order. On this page, the user will asked to add their personal details such as address, name and number, as well as their payment details.

Once the user has made an order, the payment will be handled by Stripe and an order success message will appear. The details of that order will also appear on their profile page.

<details><summary>Checkout Template Wireframe</summary>
<p>

![Checkout Template - Desktop View](https://user-images.githubusercontent.com/52998869/83974428-27630780-a8e5-11ea-91ae-4565cfc48951.png)
![Checkout Template - Mobile View](https://user-images.githubusercontent.com/52998869/83974474-6a24df80-a8e5-11ea-88a9-f3048609bba8.png)

</p>
</details>

# Technologies Used

### Frameworks, Libraries, Version Control and Testing:

- **Django 3**: Used as the core framework for this website.
- **Bootstrap 4**: Used for the structure for my website, as well as making it more user-friendly.
- **Font Awesome**: Used to add icons, such as social media logo's.
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

My website has been made fully responsive and as user friendly as possible to ensure that all features can used effectively. As mentioned previously, Bootstrap4 was often used to assist with the responsiveness of my website.

The main features used on my site can be seen below:

**General**

- Login, Logout and Registration options
- Navigation menu displays more options when the user is registered/logged in
- If the user forgets their password, they can reset it via an external link on the login page
- Stripe functionality is used to allows users to pay for any services they would like

**Profile**

- All of the users orders can be seen in the Profile page (this includes an order count)
- Users can update their details in the Profile page

**Forum**

- Segmented forum (posts are split into categories on the forum)
- Add a post button, allowing users to add their own posts to the forum

**Services**

- Option to search for services on the services page
- Add a service button, allowing users to add their own services to the services page
- The user has the option of finding out more about any of the services available
- The user has the choice to add a service to their cart if they like it

**Contact Form**

- The user can use the contact form to send a message to the site admin

### Future Features:

- Allow for more profile features such as a profile picture
- Allow users to view thier posts in the Profile page
- Allow users to view the services they have listed in the Profile page
- Allow users to delete thier posts (currently they would need to use the contact form and request for it to be deleted)
- Allow users to delete thier services (currently they would need to use the contact form and request for it to be deleted)
- Allow users to add reviews to services they've bought
- Show a number counts of total posts
- Show a number count of total comments on each post

# Bugs / Issues

1. Travis implementation: One of the very first things that was implemented for this website was Travis. I felt it was key that Travis was implemented early on so all issues could be picked up on quickly. The issue that kept occuring was that Travis didn't seem to understand the script I was trying to pass in the file. I was trying to direct it to a SECRET KEY, but I had no luck in getting it to work.

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

2. Adding a single product to the cart: The original plan for my website was to allow users to add multiple of any product to the basket. But, after some thought, I felt this wouldn't work well it's services that are being sold, rather than physical products. So, I then came across an issue as I wasn't quite sure how to only allow for a single product to be added to the basket, when I had previously allowed for multiple.

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

3. Removing a single product from the cart: Following on from the previous issue, I then had the issue of being able to remove a single product from the basket. I managed to quite easily add functionality which cleared the entire contents of the basket, but I then needed to find a way to remove a single product.

**Solution**: After raising the issue online, I was able to get some feedback which helped me resolve the issue. I was informed that simply adding 'cart.pop' would remove a single product. Credit for this can be found [here](https://stackoverflow.com/questions/62027473/removing-a-single-product-from-the-cart-in-django/62027585#62027585).

```
def remove_from_cart(request, id):
    """Remove a specified product from the cart"""

    cart = request.session.get('cart', {})
    cart.pop(id, None)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
```

4. Adding user restrictions on who can edit/delete posts/services: I needed to ensure that only the creator of a post/service would be able to edit/delete their work. I had some trouble with this and often found that rather than hiding the edit/delete button from other users, it hid it from everyone. Including the creator.

**Solution**: To fix this issue, I simply needed to add 'creator_id=request.user' into the 'create_forum_post' view so that the the creator id was always the id the of user who created it.

Once the view had been updated, I was then able to add the following if statement into the post details page `{% if request.user == post.creator_id %}` to ensure that only the post creator could edit the post.

```
def create_forum_post(request, pk=None):
    """ Create a view that allows us to create a post """

    post = get_object_or_404(Post, pk=pk) if pk else None
    if not post:
        post = Post.objects.create(creator_id=request.user)
    if request.method == "POST":
        form = ForumPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
        return redirect('forum_post_details', post.pk)
    else:
        form = ForumPostForm(instance=post)
    return render(request, 'forum_post_form.html', {'form': form})
```

# Database

I decided to use Postgres as the database for this project, which is built into the Django framework. Postgres can be easily accessed and updated by simply using the Django admin panel. This reason alone made it the viable choice over other databases such as MongoDB, as it was easily accessible and was within the framework I was using.

In order to ensure that all created models and apps were correctly implemented, `python3 manage.py makemigrations` was run in the command line and this gave a breakdown of everything that was going to be migrated, as well creating an inital migration. To finalise the migration, `python3 manage.py migrate` was run in the command line shortly after.

# Credits

- [Dennis Ivy](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) - A massive thanks to Dennis Ivy and his Django tutorials, which helped me to create a profile page.
- [Max Goodridge](https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj) - Thanks to Max Goodridge and his tutorial on updating user details from the profile page.
- [LearnDjango](https://learndjango.com/tutorials/django-email-contact-form) - Thanks to this tutorial from LearnDjango for helping me complete the contact form.
- Image used on About Us page: This [link](https://unsplash.com/photos/KE0nC8-58MQ) is for the free to use image that was added to the About Us page.
- Full Stack Frameworks module: A lot of the code added was inspired/assisted by following along with this module.
- All images used on the Services page are from [Pixabay](https://pixabay.com/). See list below:
    1. [E-Commerce-Store](https://pixabay.com/illustrations/ecommerce-online-shopping-e-commerce-1992280/)
    2. [Online-Store-Renovation](https://pixabay.com/illustrations/online-store-business-buy-internet-1673585/)
    3. [Web-Traffic](https://pixabay.com/illustrations/seo-google-search-engine-896175/)
    4. [Increase-Website-Traffic](https://pixabay.com/illustrations/analytics-google-analytics-1925495/)
    5. [Social-Media-Management](https://pixabay.com/illustrations/icon-polaroid-blogger-rss-app-2486501/)
    6. [Organic-Instagram-Followers](https://pixabay.com/vectors/instagram-social-network-urges-1594387/)
- Privacy policy generated with [GetTerms](https://getterms.io/)