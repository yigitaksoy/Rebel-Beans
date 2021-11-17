<h2 align="center">
 Rebel Beans Application Testing
</h2>

<div align="center">


<br><br>

[You can view the live project here](https://rebelbeans.herokuapp.com)

</div>
<br>

Please refer to seperate [README.md](https://github.com/yigitaksoy/Rebel-Beans/blob/master/README.md) file for more information about the project.

<br>

## Contents Table

1. [**Testing User Stories from UX Design Section**](#user-stories)
    - [**First Time Visitor Goals**](#first-time-visitor-goals)
    - [**Registered Visitor Goals**](#registered-visitor-goals)
    - [**Admin User Goals**](#admin-user-goals)

2. [**Testing**](#testing)
    - [**W3C Markup Validator Results**](#html-validator-results)
    - [**W3C CSS Validator Results**](#html-validator-results)
    - [**JSHint Results**](#jshint-results)
    - [**PEP8 Online Validator Results**](#pep8-validator-results)
    - [**Debugging**](#debugging)

3. [**Further Manual Testing**](#further-manual-testing)





### Testing User Stories from UX Design Section

#### First Time Visitor Goals

* **I want to understand the main purpose of the website.**
    - When users enter the website a jumbotron text and a CTA button is presented for the visitors, which clearly states the main purpose of the website.
* **I want to easily navigate through the website.**
    - At the top of the page a sticky navigation bar is present, displaying all the links for users to easily navigate through the website.
* **I want to be able to easily see the products on the website.**
    - On the navigation bar a Shop link, and on the Main page of the website a Shop Now button for users to easily navigate to products page. 
* **I want to be able to search through the products on the website.**
    - On the navigation bar, there is a search bar present for users to easily search for products.  
* **I want to be able to easily sort products by category.**
    - On the navigation bar users can hover over the Shop link and sort through the products by category. Sorting is also available on the products page, on the right hand side, with dropdown menu which is present for users to easily sort products by category, price or by name.
* **I want to be able to get more details about a certain product on the website.**
    - On the products page, users can get more details about a specific product by clicking on the product image.
* **I want to find out how I can register for the website.**
    - On the main and mobile top header, My Account link is present for users to easily register fot the website. 
* **I want to be able to easily edit, remove or update products in my shopping bag.**
    - On the shopping bag page remove and update buttons with quantity indicators are present for users.
* **I want to easily be able to purchase a product from the website.**
    - On the shopping bag page, at the right bottom side, there is a Secure Checkout button present which directs users to the checkout page. 
    
#### Registered Visitor Goals

* **I want to find out how I can login to my account, or recover my password on the website.**
    - On the main and mobile top header, My Account button which contains a Login link is presented for registered users, which takes them to Login page.
* **I want to find out how I can see my past orders on the website.**
    - On the main and mobile top header, My Account button which contains a link to Users Profile page is present, where registered users can see their past orders.
* **I want to find out how I can save my address, and contact details so I can use them later.**
    - On the main and mobile top header, My Account button which contains a link to Users Profile page is present, where registered users can update their contact details.
* **I want to get more information about the brand, and their mission.**
    - On the navigation bar there is a About link present where users can go and get more information about the company.
* **I want to find out how I can leave comments on the website's blog posts.**
    - On each blog post page, underneath the blog post content, there is a comment form present for registered users to add comments on current posts.
* **I want to find out how I can contact the site owner.**
    - On the navigation bar there is a link for the Contact page where users can contact the website Admin using the contact form. 

#### Admin User Goals

* **I want to be able to easily Add/Edit/Delete products.**
    - On the Admin backend, under Products tab, Admin user can easily Add/Edit/Delete products. Admin user can also easily Add products using the Product Management tab under My Profile link. Edit/Delete product options are also available on the Products and Product Detail pages for the Admin user.
* **I want to be able to easily Add/Edit/Delete categories.**
    - On the Admin backend, under Categories tab, Admin user can easily Add/Edit/Delete categories.
* **I want my customers to make purchases with ease of mind, and have secure payments.**
    - Website uses the Stripe Payments infrastruce which allows al all the transactions on the website to be 100% secure. 
* **I want to be able to easily Add/Edit/Delete posts on my Blog.**
    - On the Admin backend, under the Posts tab, Admin user can easily Add/Edit/Delete posts, and can save Blog posts as drafts for later.
* **I want to be able to moderate each comment on Blog posts.**
    - On the Admin backend, under the Comments tab, Admin user easily moderate each user comment before they are publish, allowing admin user to be in total control.
* **I want to be able to see and manage current orders on the website.**
    - On Admin backend, under the Orders tab, admin user can easily see and manage current orders.
* **I want to be able to see and manage current users on the website.**
    - On Admin backend, under the Users tab, admin user can easily see and manage current users.

### Testing

- The W3C Markup Validator and W3C CSS Validator Services were used to validate the HTML & CSS code in the project to ensure there were no syntax errors. JSHint was used to check the quality of the Javascript and PEP8 Online was used for checking the python code.

<details><summary><b>Click here for HTML Validator results</b></summary>

- __Homepage__
<p align="center">
  <img src="#" >
</p>

- __Products__
<p align="center">
  <img src="#" >
</p>

- __Product Detail__
<p align="center">
  <img src="#" >
</p>

- __Product Management__
<p align="center">
  <img src="#" >
</p>

- __Checkout Page__
<p align="center">
  <img src="#" >
</p>

- __Blog Page__
<p align="center">
  <img src="#" >
</p>

- __Blog Detail Page__
<p align="center">
  <img src="#" >
</p>

- __Login__
<p align="center">
  <img src="#" >
</p>

- __Register__
<p align="center">
  <img src="#" >
</p>

- __Profile__
<p align="center">
  <img src="#" >
</p>

- __About__
<p align="center">
  <img src="#" >
</p>

- __Contact__
<p align="center">
  <img src="#" >
</p>



</details>

<details><summary><b>Click here for CSS Validator results</b></summary>

- __CSS Validator Results__
<p align="center">
  <img src="#" >
</p>
</details>

<details><summary><b>Click here for JSHint results</b></summary>

- __JSHint Results__
<p align="center">
  <img src="#" >
</p>
</details>

<details><summary><b>PEP8 Online results</b></summary>

- __PEP8 Online Results__
<p align="center">
  <img src="#" >
</p>
</details>

### Debugging



### Further Manual Testing

#### Responsive Design - PASS

- All pages were tested locally, and on Heroku using Chrome, Firefox, IE, and Safari. 
- All pages tested for responsiveness in different device sizes using Google Chrome Developer Tools, and Google Chrome Responsive Viewer extension;
  - Desktop 
  - iPhone 5/6/7/8/X 
  - iPad 1/2/3/Pro 
  - Galaxy Android phones
- All the pages were also tested manually using;
  - iPhone 5s/6s/8/X/XS/11/
  - Samsung Galaxy S8/Note 10+
  - iPad Air 2 
  - iPad Pro 3
  
### Functionality Testing
  

  
  
  
### Google Lighthouse Testing 
  
  - All pages were tested for web quality using Google's Lighthouse.
  
  <details><summary><b>Click here for Lighthouse results</b></summary>
  
- __Homepage__
<p align="center">
  <img src="#" >
</p>

- __Login__
<p align="center">
  <img src="#" >
</p>

- __Register__
<p align="center">
  <img src="#" >
</p>

- __Contact__
<p align="center">
  <img src="#" >
</p>

- __Profile__
<p align="center">
  <img src="#" >
</p>

- __About__
<p align="center">
  <img src="#" >
</p>

- __Products__
<p align="center">
  <img src="#" >
</p>

- __Product Detail__
<p align="center">
  <img src="#" >
</p>

- __Product Management__
<p align="center">
  <img src="#" >
</p>

- __Checkout Page__
<p align="center">
  <img src="#" >
</p>

- __Blog Page__
<p align="center">
  <img src="#" >
</p>

- __Blog Detail Page__
<p align="center">
  <img src="#" >
</p>

  </details>
  
  #### __back to [Contents Table](#contents-table)__ 