Wishlist Backend Web App Readme
This is a simple backend web application for managing a wishlist. The application provides basic CRUD (Create, Read, Update, Delete) functionality for wishlist items.

Technologies Used
Python3: Programming language used for the backend logic.
Flask: Web framework used to build the backend.
Swagger: API documentation and testing tool.
SQLite: Database for storing wishlist items.
How to Run the Application
Make sure you have Python3 installed on your system.

Install the required dependencies using the following command:
$pip install -r requirements.txt

Run the application:
$python app.py
The Flask application will start, and you can access the Swagger UI for testing the API at http://localhost:5000/api/ui/

API Endpoints
The following CRUD operations are available:

Create a Wishlist Item: api/ui/#/Wishlist/wishlist.create
Get All Wishlist Items: api/ui/#/Wishlist/wishlist.read_all
Get a Wishlist Item by ID: api/ui/#/Wishlist/wishlist.read_one
Update a Wishlist Item by ID: api/ui/#/Wishlist/wishlist.update
Delete a Wishlist Item by ID: api/ui/#/Wishlist/wishlist.delete
Please refer to the Swagger UI at http://localhost:5000/api/ui/ for detailed API documentation and testing.

Important Notes
This application currently lacks a front-end user interface. It is recommended to use Swagger for testing the API endpoints.
The SQLite database is used for simplicity. In a production environment, consider using a more robust database system.
Feel free to contribute to the development of this wishlist backend web application. If you encounter any issues or have suggestions for improvements, please open an issue in the repository.
