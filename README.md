# YOGA VIBE

![Yogavibe mockup](docs/readme/mockup.jpeg)

This website is designed for yoga enthusiasts of all levels, from beginners to experienced practitioners. 

Visit the live site: [YogaVibe]()

# Table of contents

- [User Experience (UX)](#User-Experience-UX)
  - [User Stories](#User-Stories)

- [Agile Metodology](#Agile-metodology)

- [Design](#Design)

  - [Flowchart](#Flowchart)
  - [Database Schema](#Database-Schema)
  - [Colour Palette](#Colour-Palette)
  - [Typography](#Typography)
  - [Imagery](#Imagery)
  - [Wireframes](#Wireframes)
  - [Features](#Features)

- [Marketing Stategy](#Marketing-Stategy)
  - [Business model](#Business-model)
  - [Social Media](#Social-Media)
      - [Facebook](#Facebook)
  - [Newsletter](#Newsletter)
      - [Mailchimp](#Mailchimp)

- [Technologies Used](#Technologies-Used)

  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

- [Deployment & Local Development](#Deployment--Local-Development)

  - [Deployment](#Deployment)
  - [Local Development](#Local-Development)
    - [How to Fork](#How-to-Fork)
    - [How to Clone](#How-to-Clone)

- [Testing](#Testing)

- [Credits](#Credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#Acknowledgments)

---

## User Experience (UX)

#### Key information for the site

This section provides insight into the UX process, with a focus on the people who this e-commerce application shop has been created for, the main aims of the project and how it can help users to meet their needs.

**Project goals:**

- The aim of the project is to encourage both beginners and advanced yoga enthusiasts to buy yoga gear.

- To provide an easy and user-friendly web app where users can buy yoga gear and at the same time learn some more about yoga.

### User Stories

|   EPIC                                ||                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**VIEWING AND NAVIGATION**             |  ||
|                                       |  | As a site user, I can view a list of products so that I can select some to purchase. |             
|                                       |AC1| When I navigate to the homepage of the e-commerce site, I should see a visually appealing and organized display of product categories.|
|                                       |AC2| Upon selecting a specific category, I should be able to view a list of products within that category, with each product showing its name, price, and image.|
|                                       |AC3| Each product listing should include a clickable link or button that allows me to view more detailed information about the product, such as description, specifications, and customer reviews etc.|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |  | As a site user, I can register for a new account so that I can have a personal account and be able to view and edit my account.|
|                                       |AC1| Easily login and logout to view and edit my personal information.|
|                                       |AC2| Easily recover password to recover account if password is forgotten.|
|                                       |AC3| Receive an email confirmation after registation.|
|**USER PROFILE**                       |  ||
|                                       |  | As a site user, I can view and manage my user profile so that I can update my personal information and preferences.|
|                                       |AC1| Upon logging into my account, I should be able to access my user profile page, which displays my current personal information such as name, email address, shipping address, and contact information.|
|                                       |AC2| The user profile page should display a history of my past orders, including order dates, order numbers, items purchased, and order statuses (e.g., pending, shipped). I should be able to click on each order to view detailed information about the items ordered and their respective statuses.|
|                                       |AC3| Within the profiles section, there should be a dedicated "Favorites" page where I can view a list of products I have marked as favorites. I should be able to add new products to my favorites list and remove existing ones as needed. The list of favorites should persist across sessions.|                                  
|**PRODUCT REVIEWS**                       |  ||
|                                       |  | As a site user, I can leave reviews for products so that I can share my experience with other customers and help them make informed purchase decisions.|
|                                       |AC1| As a logged-in user, when I navigate to the product details page, I should see a section where I can write a review for the product.|
|                                       |AC2| As a site user, when i press write a review button and am not logged in i will be informed that i need to be logged in in order to leave a product review.|
|                                       |AC3| After submitting a review, it should appear on the product page under the reviews section. The review should display my username, review text, rating, and the date it was submitted.|
|**ADMIN**              |  ||
|                                       |  | As an admin user, I want to have full CRUD functionality for products so that I can effortlessly maintain an up-to-date site and product information.|
|                                       |AC1| As an admin user, I should be able to add new products to the store. The product creation form should include fields for product name, description, price, category, and image upload. Upon submission, the new product should appear immediately in the store's product listings.|
|                                       |AC2| As an admin user, I should be able to edit existing product details. When I navigate to the product section, I should see a list of current products with an option to edit each product. The edit form should allow modification of product name, description, price, category, and image. Changes made should be reflected immediately in the product listings.|
|                                       |AC3| As an admin user, I should be able to remove products from the store. There should be a delete option available next to each product in the product section. Upon deletion, the product should be permanently removed from the store.|
|**PURCHASE & CHECKOUT**                            |  ||
|                                       |  | As a shopper, I want to be able to select products, add them to my cart, and complete the checkout process smoothly and securely.|
|                                       |AC1| As a shopper, I should be able to browse products, view detailed information about each product, and add desired products to my shopping cart. The cart should update dynamically to reflect the added items.|
|                                       |AC2| From the shopping cart page, I should be able to view all products added, their quantities, and prices. I should have options to update quantities and remove products.|
|                                       |AC3| After finalizing my product selection in the cart, I should be able to proceed to the checkout process. There should be a clear and visible "Checkout" button or link that initiates the checkout flow.|
|                                       |AC4| Easily enter payment information|
|                                       |AC5| Upon successful completion of the checkout process, I should receive an order confirmation page and email that includes an order summary, and any other relevant information. The order should also be visible in my account's order history.|
|**SEARCH**              |  ||
|                                       |  | As a site user, I can enter a keyword in the search field, so that I can view all products associated with that keyword.|
|                                       |AC1| When I navigate to the e-commerce site, there should be a clearly visible search field prominently displayed, such as in the header or a designated search bar area.|
|                                       |AC2| Upon entering a keyword in the search, the page should display a list of all products that match the search criteria.|
|                                       |AC3| If the search does not return any results for the entered keyword, the system should display a clear message indicating that no products match the search criteria. The user will then be asked to try again or go back to home page.|
|**RECOMMENDED PRODUCT**              |  ||
|                                       |  | As a User, I can see recommended products, so that I can purchase other useful items that would go along with my main purchase.|
|                                       |AC1| When I view the details of a product on the e-commerce site, I should see a section displaying recommended products.|
|                                       |AC2| Recommended products should be visually distinguishable and clearly presented alongside the main product details. Each recommended product should include its name, image, price, and a link to view more details.|
|                                       |AC3| After completing a purchase and viewing the order confirmation page, there should be a section displaying recommended products related to the items purchased in the order. This allows users to consider additional products they might find useful based on their recent purchase.|
                                      

---

## Agile Metodology

![Github user stories](docs/readme/user-stories.jpeg)

### MoSCoW Prioritization

---

## Design

### Database Schema


### Colour Palette


### Typography

### Imagery

### Wireframes

#### Existing Features

**Logo**

**Fav Icon**

**Nav Bar**

**Footer**

**Hero Image**

**Search**

**Product Display**

**Product CRUD Functionality**

**Allauth**

**User Feedback**

**Reviews**

**Product Favorite**


---

### Features Left to Implement

Many ideas and features are lined up for this project, although they could not be implemented this time, in the future, I would like to:

---

### Marketing Stategy

#### Business model

#### Social Media
##### Facebook

#### Newsletter
##### Mailchimp

---
## Technologies Used

The main technologies used are Python, Javascript, html, css & Django.

### Frameworks, Libraries & Programs Used

## Deployment & Local Development

### Deployment

- This site was deployed by completing the following steps:

####  Django

####  Heroku


####  AWS

### Local Development

#### How to Fork

#### How to Clone

---

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing carried out.

## Credits

### Code Used

- [Code Institue](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentecomm) walkthrough tutorial "Boutique Ado".

- [Stack overflow](https://stackoverflow.com/) helped me to troubleshoot many of the issues and bugs encountered.

- I also researched using [W3 Schools](https://www.w3schools.com/) & [Django Documentation](https://docs.djangoproject.com/en/4.2/).

### Content


### Media

### Acknowledgments
- Tutor support at Code Institute.