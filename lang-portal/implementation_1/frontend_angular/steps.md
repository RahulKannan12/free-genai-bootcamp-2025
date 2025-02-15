# Frontend Implementation Steps

## Project Setup

- [x] Create a new Angular project using Angular CLI
- [x] Add necessary dependencies (e.g., Angular Material, HttpClientModule)
- [x] Set up project structure (Components, Services, Models, etc.)

## Pages

### Dashboard `/dashboard`

- [x] Create the Dashboard component
- [x] Implement the Last Study Session component
- [x] Implement the Study Progress component
- [x] Implement the Quick Stats component
- [x] Implement the Start Studying Button
- [x] Integrate with the backend API endpoints
  - [x] GET /api/dashboard/last_study_session
  - [x] GET /api/dashboard/study_progress
  - [x] GET /api/dashboard/quick_stats

### Study Activities Index `/study_activities`

- [ ] Create the Study Activities Index component
- [ ] Implement the Study Activity Card component
- [ ] Integrate with the backend API endpoint
  - [ ] GET /api/study_activities

### Study Activity Show `/study_activities/:id`

- [ ] Create the Study Activity Show component
- [ ] Implement the Study Activities Paginated List component
- [ ] Integrate with the backend API endpoints
  - [ ] GET /api/study_activities/:id
  - [ ] GET /api/study_activities/:id/study_sessions

### Study Activities Launch `/study_activities/:id/launch`

- [ ] Create the Study Activities Launch component
- [ ] Implement the Launch form
- [ ] Integrate with the backend API endpoint
  - [ ] POST /api/study_activities

### Words Index `/words`

- [ ] Create the Words Index component
- [ ] Implement the Paginated Word List component
- [ ] Integrate with the backend API endpoint
  - [ ] GET /api/words

### Word Show `/words/:id`

- [ ] Create the Word Show component
- [ ] Implement the Study Statistics component
- [ ] Implement the Word Groups component
- [ ] Integrate with the backend API endpoint
  - [ ] GET /api/words/:id

### Word Groups Index `/groups`

- [ ] Create the Word Groups Index component
- [ ] Implement the Paginated Group List component
- [ ] Integrate with the backend API endpoint
  - [ ] GET /api/groups

### Group Show `/groups/:id`

- [ ] Create the Group Show component
- [ ] Implement the Group Statistics component
- [ ] Implement the Words in Group component
- [ ] Implement the Study Sessions component
- [ ] Integrate with the backend API endpoints
  - [ ] GET /api/groups/:id
  - [ ] GET /api/groups/:id/words
  - [ ] GET /api/groups/:id/study_sessions

### Study Sessions Index `/study_sessions`

- [ ] Create the Study Sessions Index component
- [ ] Implement the Paginated Study Session List component
- [ ] Integrate with the backend API endpoint
  - [ ] GET /api/study_sessions

### Study Session Show `/study_sessions/:id`

- [ ] Create the Study Session Show component
- [ ] Implement the Study Session Details component
- [ ] Implement the Words Review Items component
- [ ] Integrate with the backend API endpoints
  - [ ] GET /api/study_sessions/:id
  - [ ] GET /api/study_sessions/:id/words

### Settings Page `/settings`

- [ ] Create the Settings component
- [ ] Implement the Theme Selection component
- [ ] Implement the Reset History Button
- [ ] Implement the Full Reset Button
- [ ] Integrate with the backend API endpoints
  - [ ] POST /api/reset_history
  - [ ] POST /api/full_reset

## Final Steps

- [ ] Review and refactor code
- [ ] Perform thorough testing
- [ ] Deploy the frontend application