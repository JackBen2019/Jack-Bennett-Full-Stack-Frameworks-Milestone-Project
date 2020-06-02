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

# Testing

[![Build Status](https://travis-ci.org/JackBen2019/Jack-Bennett-Full-Stack-Frameworks-Milestone-Project.svg?branch=master)](https://travis-ci.org/JackBen2019/Jack-Bennett-Full-Stack-Frameworks-Milestone-Project)

A lot of the testing was done by me and without the assistance of other online tools, but the tools that were used can be found in the **Technologies Used** section. The manual tests completed were as follows:

### Login, Logout and Registration



### Password Reset



### Browser and Mobile Responsiveness



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

# Technologies Used

### Frameworks, Libraries, Version Control and Testing:

- Django: Used as the core framework for this project.
- Bootstrap: Used 
- Font Awesome: 
- Heroku:
- GitHub:
- Travis: 
- W3 HTML & CSS Validator:

### Languages:

- HTML5
- CSS3
- JavaScript
- Python3

### Extra Technologies:

- 

# Features



# Database

I decided to use Postgres as the database for this project, which is built into the Django framework. Postgres can be easily accessed and updated by simply using the Django admin panel. This reason alone made it the viable choice over other databases such as MongoDB, as it was easily accessible and was within the framework I was using.

# Credits

- [Dennis Ivy](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) - A massive thanks to Dennis Ivy and his Django tutorials, which helped me to overcome a few obstacles with my website.
- Image used on About Us page: This [link](https://unsplash.com/photos/KE0nC8-58MQ) is for the free to use image that was added to the About Us page.
- 