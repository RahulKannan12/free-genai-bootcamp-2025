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

- [ ] Implement GET /api/dashboard/last_study_session
- [ ] Implement GET /api/dashboard/study_progress
- [ ] Implement GET /api/dashboard/quick-stats

### Study Activities Endpoints

- [ ] Implement GET /api/study_activities/:id
- [ ] Implement GET /api/study_activities/:id/study_sessions
- [ ] Implement POST /api/study_activities

### Words Endpoints

- [ ] Implement GET /api/words
- [ ] Implement GET /api/words/:id

### Groups Endpoints

- [ ] Implement GET /api/groups
- [ ] Implement GET /api/groups/:id
- [ ] Implement GET /api/groups/:id/words
- [ ] Implement GET /api/groups/:id/study_sessions

### Study Sessions Endpoints

- [ ] Implement GET /api/study_sessions
- [ ] Implement GET /api/study_sessions/:id
- [ ] Implement GET /api/study_sessions/:id/words

### Reset Endpoints

- [ ] Implement POST /api/reset_history
- [ ] Implement POST /api/full_reset

### Review Endpoint

- [ ] Implement POST /api/study_sessions/:id/words/:word_id/review

## Entity Framework Related Tasks

- [ ] Implement task to initialize the database
- [ ] Implement task to migrate the database
- [ ] Implement task to seed data from JSON files

## Unit Tests

- [ ] Set up JUnit for unit testing
- [ ] Write unit tests for each API endpoint
- [ ] Write unit tests for database operations
- [ ] Write unit tests for service layer

## Documentation

- [ ] Document API endpoints with request and response examples
- [ ] Document database schema and relationships
- [ ] Document setup and usage instructions

## Final Steps

- [ ] Review and refactor code
- [ ] Perform thorough testing
- [ ] Deploy the backend API
