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
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/homepage.png" >
</p>

- __Products__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/products-page.png" >
</p>

- __Product Detail__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/product-detail-page.png" >
</p>

- __Add Product__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/add-product.png" >
</p>
<br>
- Highlighted elements are added dynamically by crispy_forms, since there are no known errors with the page these errors were ignored.
<br>
<br>

- __Edit Product__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/edit-product.png" >
</p>
<br>
- Highlighted elements are added dynamically by crispy_forms, since there are no known errors with the page these errors were ignored.
<br>
<br>

- __Shopping Bag Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/shopping-bag-page.png" >
</p>

- __Checkout Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/checkout.png" >
</p>

- __Blog Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/blog-page.png" >
</p>

- __Blog Detail Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/blog-detail.png" >
</p>

- __Login__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/login.png" >
</p>

- __Register__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/register.png" >
</p>

- __Profile__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/profile-page.png" >
</p>

- __About__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/about.png" >
</p>

- __Contact__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/html-validator-results/contact-page.png" >
</p>
<br>
- Subject field is added dynamically by the Contact models and crispy_forms since this error doesnt cause any problems, the error was ignored.
<br>
<br>



</details>

<details><summary><b>Click here for CSS Validator results</b></summary>

- __CSS Validator Results__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/css-validator-results/css-validator-results.png" >
</p>
</details>

<details><summary><b>Click here for JSHint results</b></summary>

- __JSHint Results__

<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/jshint-results/jshint-results.png" >
</p>

</details>

<details><summary><b>PEP8 Online results</b></summary>

- __PEP8 Online Results__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/pep8-results/pep8-compliance.png" >
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

  #### Navbar - PASS

  - All links are working, and takes the user where they want to go.
  - Search bar is working, and lets user search through products, categories, and product details. If user input doesnt match any results, "You didn't enter any search criteria!" message is shown.

  #### Homepage - PASS

  - CTA button is working as expected, and directs users to Products page.

  #### Register - PASS

  - Form inputs work as expected and stores the data in the database, and registers user.
  - Form validations work as expected, and gives feedback upon unmatched format, invalid data, or for existing user.
  - Submit button works as expected and submits data successfully, and send verification e-mail for users.

  #### Login - PASS

  - Form inputs works perfectly, and form validations work as expected and gives feedback upon unmatched format or incorrect username/email and password, or if user doesn't exist in the database.
  - Submit button works as expected and submits data successfully, and redirects user to homepage with a success toast message.
  - Forgot password link works as expected and directs user to password recovery page.

  #### Logout - PASS

  - Logout functionality works perfectly, logs out user, and removes session cookies.

  #### Profile - PASS

  - All recent purchases are shown in the Order History tab.
  - All recent purchase links works as expected and open in a new page with the past order information.
  - User details form works as expected, and successfully updates user details.

  #### Products - PASS

  - Products page works as expected, and renders all the products in the database.
  - Category badges work as expected, and sorts items by specified categories.
  - Sort menu works as expected and sorts products by A-Z, Price High - Low, and by Category.
  - Edit and Remove buttons for products are visible for Admin user, and works as expected.

  #### Product Detail - PASS

  - Page works as expected, renders the specified product.
  - Quantity input buttons work as expected, adds specified amount and any quantity between 1-99 is restricted.
  - Item Grind selector fields work as expected and adds the specified Coffee Grind, Grind field is invisible if the current product doesn't have `has_grind` attribute.
  - Keep shopping button works as expected and redirects user back to Products page.
  - Add to Bag button works as expected, and adds the specified item, quantity, and grind into the shopping bag, with a success message.

  #### Product Management Add/Edit - PASS

  - Page works as expected and renders product management form.
  - Form successfully Adds new product to specified category, along with its data, and images.
  - Form successfully Edits specified product, along with its data, and images.
  - Submit button works as expected and submits data.
  #### Bag - PASS

  - Page works as expected, and renders all the items in the bag with their details.
  - Remove, and Update buttons work as expected and Removes or Updates specified product, or item grind.
  - Grand total, and delivery treshold are visible, and accurate.
  - Keep shopping button works as expected and redirects user back to Products page.
  - Secure Checkout button works as expected and directs user to the Checkout Page.

  #### Checkout - PASS

  - Page works as expected and renders all the items in bag with their details in order summary section.
  - Checkout form works as expected and successfully submits data for payment.
  - Checkout form validation works as expected and gives feedback upon unmatched format, and incorrect input.
  - Upon successful payment, a confirmation e-mail is sent to user with their order details.

  #### Checkout Success - PASS

  - Page works as expected, renders, and summarizes the order history for customers with their confirmation number.

  #### Blog - PASS

  - Page works as expected, and renders all the blog data from the database.
  - All post images, titles, and read more links work as expected and takes the user to the post page.
  - Pagination works as expected, and only shows 4 posts per page.

  #### Blog Detail - PASS

  - Successfully renders all the data including the post image.
  - Comment section works as expected and shows all the current comments, with a comment counter. If there are no comments on the post, a message is shown to the user if they would like to add one.
  - Comment form works as expected and submits user comment data, forwards it to Admin for moderation before posting.
  - Comment success alert message works as expected.

  #### About - PASS

  - Page works as expected and renders all the About text and images.

  #### Contact - PASS

  - Page works as expected and renders the contact form.
  - Contact form works as expected and gives feedback upon umatched format, or empty fields.
  - Submit button works as expected and submits the form data, and sends an email to the Admin user.

  #### Footer - PASS

  - Footer is present on all pages.
  - Products links work as expected, and redirects user to specified category.
  - Quick links work as expected, and redirects user to the specified page.
  - Social, and external links on the footer works as expected, and all the links open in a new tab.

  #### Error 400 - PASS

  - Works as expected, successfuly captures and handles bad request error.
  - Go back button on error page works as expected and redirects user back to the homepage.

  #### Error 403 - PASS

  - Works as expected, successfuly captures and handles forbidden error.
  - Go back button on error page works as expected and redirects user back to the homepage.

  #### Error 404 - PASS

  - Works as expected, successfuly captures and handles page not found error.
  - Go back button on error page works as expected and redirects user back to the homepage.

  #### Error 500 - PASS

  - Works as expected, successfuly captures and handles internal server error.
  - Go back button on error page works as expected and redirects user back to the homepage.

  #### Stripe Webhooks - PASS

  - Webhooks works as expected, and gives 200 code.
  <p align="center">
    <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/webhooks/webhooks.png" >
  </p>


### Google Lighthouse Testing

  - All pages were tested for web quality using Google's Lighthouse.

  <details><summary><b>Click here for Lighthouse results</b></summary>

- __Homepage__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/homepage-lighthouse.png" >
</p>

- __Login__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/login-lighthouse.png" >
</p>

- __Register__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/register-lighthouse.png" >
</p>

- __Contact__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/contact-lighthouse.png" >
</p>

- __Profile__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/profile-lighthouse.png" >
</p>

- __About__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/about-page-lighthouse.png" >
</p>

- __Products__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/products-page-lighthouse.png" >
</p>

- __Product Detail__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/product-detail-lighthouse.png" >
</p>

- __Product Management__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/product-detail-lighthouse.png" >
</p>

- __Shopping Bag Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/shopping-bag-lighthouse.png" >
</p>

- __Checkout Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/checkout-lighthouse.png" >
</p>

- __Blog Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/blog-page-lighthouse.png" >
</p>

- __Blog Detail Page__
<p align="center">
  <img src="https://github.com/yigitaksoy/Rebel-Beans/blob/master/documentation/lighthouse-scores/blog-detail-lighthouse.png" >
</p>

  </details>

  #### __back to [Contents Table](#contents-table)__
