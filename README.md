# Bokning - API
## Project description
Bokning is a web app to help people book an apartment. The application consists of the React app and an API.
This is the Django Rest Framework API project section.

## User stories
| Category  | as | I want to                               | so that I can                                                                                    | mapping API feature                              |
| --------- | -------- | --------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| auth      | visitor  | register for an account           | have a personal profile with a picture                                                           | dj-rest-auth<br>Create profile (signals)         |
| auth      | visitor  | register for an account           | create, edit and delete bookings                                                                 | Create booking<br>Edit booking<br>Delete booking |
| booking   | visitor  | view a list of bookings           | see what dates are available                                                                     | List/ Filter posts                               |
| booking   | visitor  | scroll through a list of bookings | browse bookings by filtering a specific date                                                     | List/ Filter posts                               |
| booking   | user     | edit and delete my booking        | correct or hide any mistakes                                                                     | Update property<br>Destroy property              |
| booking   | user     | create a booking                  | share my moments with others                                                                     | Create post                                      |
| profiles  | user     | view a profile                    | see a user's username, profile picture and bio                                                   | Retrieve profile                                 |
| profiles  | user     | edit a profile                    | update my profile information                                                                    | Update profile                                   |

## Entity Relationship Diagram
![ERD](https://res.cloudinary.com/dgjrrvdbl/image/upload/v1649155000/moments-api-erd_aw81vx.png)

## Models and CRUD breakdown
| model     | endpoints                    | create        | retrieve | update | delete | filter                   | text search |
| --------- | ---------------------------- | ------------- | -------- | ------ | ------ | ------------------------ | ----------- |
| admin     | admin/<br>admin/             | yes           | yes      | yes    | no     | no                       | no          |
| profiles  | profiles/<br>profiles/:pk/   | yes (signals) | yes      | yes    | no     | no                       | no          |
| bookings  | bookings/<br>bookings/:pk/   | yes           | yes      | yes    | yes    | date<br>desc             | yes         |
| comments  | comment/<br>comment/:pk/   | yes           | yes      | yes    | yes    | profile<br>date          | no          |

## Tests

### Testing is done manually by the following steps: 

- Bookings app:
    - logged out users can list bookings
    - logged in users can book a date
    - logged out users can't book a date
    - logged out users can retrieve a post with a valid id
    - logged out users can't retrieve a post with an invalid id
    - logged in users can update a post they own
    - logged in users can't update a post they don't own

## Deployment steps
- set the following environment variables:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY
- installed the following libraries to handle database connection:
    - psycopg2
	- dj-database-url
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS:
	- set allowed_origins
- set default renderer to JSON
- added Procfile with release and web commands
- gitignored the env&#46;py file
- generated requirements.txt
- deployed to Heroku

