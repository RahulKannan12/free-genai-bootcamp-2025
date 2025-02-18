# Backend API Implementation Steps

## Project Setup

- [x] Create a new C# project using .NET Core
- [x] Add necessary dependencies (Entity Framework Core, SQLite, ASP.NET Core WebAPI)
- [x] Set up project structure (Controllers, Models, Data, Services, etc.)

## Database Setup

- [x] Create the SQLite database `words.db` in the root of the project folder
- [x] Define the Entity Framework Core models for the database schema
  - [x] Words
  - [x] WordsGroups
  - [x] Groups
  - [x] StudySessions
  - [x] StudyActivities
  - [x] WordReviewItems
- [x] Configure the DbContext for Entity Framework Core
- [x] Use the code-first approach to create and migrate the database

## API Endpoints

### Dashboard Endpoints

- [x] Implement GET /api/dashboard/last_study_session
- [x] Implement GET /api/dashboard/study_progress
- [x] Implement GET /api/dashboard/quick-stats

### Study Activities Endpoints

- [x] Implement GET /api/study_activities/:id
- [x] Implement GET /api/study_activities/:id/study_sessions
- [x] Implement POST /api/study_activities

### Words Endpoints

- [x] Implement GET /api/words
- [x] Implement GET /api/words/:id

### Groups Endpoints

- [x] Implement GET /api/groups
- [x] Implement GET /api/groups/:id
- [x] Implement GET /api/groups/:id/words
- [x] Implement GET /api/groups/:id/study_sessions

### Study Sessions Endpoints

- [x] Implement GET /api/study_sessions
- [x] Implement GET /api/study_sessions/:id
- [x] Implement GET /api/study_sessions/:id/words

### Reset Endpoints

- [x] Implement POST /api/reset_history
- [x] Implement POST /api/full_reset

### Review Endpoint

- [x] Implement POST /api/study_sessions/:id/words/:word_id/review

## Entity Framework Related Tasks

- [x] Implement task to initialize the database
- [x] Implement task to migrate the database
- [x] Implement task to seed data from JSON files

## Unit Tests

- [x] Set up xUnit for unit testing
- [x] Write unit tests for each API endpoint
- [x] Write unit tests for database operations
- [x] Write unit tests for service layer

## Documentation

- [x] Document API endpoints with request and response examples
- [x] Document database schema and relationships
- [x] Document setup and usage instructions

## Final Steps

- [ ] Review and refactor code
- [ ] Perform thorough testing
- [ ] Deploy the backend API
