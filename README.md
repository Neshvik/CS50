# DOG HOUSE
#### Video Demo:  <https://www.youtube.com/watch?v=dEWMa9YfDxM>
#### Description: This is a web application related to dogs. The search for a suitable dog breed, the training videos and links to the next things you could buy for the dog. Admin access or registered users can also add dog breeds into the database to give other users an option.

**Templates**
I created a HTML page for each of the following,
1) Addbreed.html
In Addbreed.html, I created a navigation bar. The navigation title, directs users to the index page upon clicking. The navigation is designed to direct users to all the other html pages within this website.

After the navigation, I created a form for the user to fill out with the details of the dog that they wish to add to database. This includes size, temperament, activity level, shedding level, grooming needs, training needs, compatible with children, compatible with other pets, the space needed to house the dog, if the dog is recommended for first time dog owners, and the maximun time (in hours) that the dog can be left alone. Inputs in the form is required to update the database and no fields will be left blank.

The last part of this form requires an address of the dog image that the user is trying to add. It is best that the photo is publicaly available in the web.

Subsequently, the submit button at the end will update the database, name Dogs, with the phython and sql commands.

This page requires user authentication (@login_required).
Handles both GET and POST requests.
If a GET request, renders the "addbreed.html" template.
If a POST request, extracts form data (dog breed details) and inserts them into a database table named "Dogs."
Redirects to the "indexafterlogin.html" template upon successful submission.


2) Buydogstuff.html
Buydogstuff.html is an easier html page. I copied the template over for style and navigation from addbreed.tml and also added a link to Amazon Dog stuff, where user can buy dog stuff by linking to their Amazon account.

3) Choosedog.html
Choosedog.html was a challenging component to the website. First of all, using SQL commands, all the dogs in the database will show in this page with the image and breed name. The user can then use the forms, similar to addbreed.html to filter the search based on the requirement they have for the dog they want. The html page will then show only the dogs that fit the criteria stated by the user. I have used Javascript for this by creating 3 functions.

In the JavaScript section:

Event Listeners:
Listens for changes in the filter form dropdowns.

Filtering Logic:
Updates the display of dog cards based on user-selected filter criteria.
Uses data attributes associated with each dog card to determine visibility.

Initial Display:
Calls the updateDogCards function to display all dogs initially.

Known Issue
Image Display Issue:
The link provided by user is not checked for validity or error. As such, the form will accept any URL and store it in the database as a string. This can be further improved so that the invalid URLs can be flagged up.

4) Index.html
Index.html is the page that users are directed to initially. This page contains a big dog picture and is also design with the navigation bar to direct users to all other html pages.

5) indexafterlogin.html
Indexafterlogin is the page that users will see after logging in when they click on the pages that are tagged as login_required. What is different now is that the option to log out is available to users in the index page.

6) login.html, register.html
This pages are templates taken from week 8 problem set. Basically, the register.html requests users to key in a username, password and confirm password. These data is then extracted through flask to input into a database called users. The password is run through another hash function so that the stored password is a hash rather than the actual password.
The login.html receives the inputs of username and password and checks for validity and authenticates which will then allow users to add a dog breed into the database.

7) traindog.html
This page is basically a collection of Youtube videos that new dog owners might need to watch with regards to dog training. There is also a playlist after the basic videos.

**Dogs.db and Users.db**
02 databases created and managed using SQL.
Dogs.db is used to capture the data about the new breed added to the site.
Users.db is used to store information about registered users to the site.
