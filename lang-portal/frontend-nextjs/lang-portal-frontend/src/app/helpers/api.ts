const BASE_URL = 'http://localhost:5057/api'; // Base URL for your API

export const API_ENDPOINTS = {
  getLastStudySession: `${BASE_URL}/Dashboard/last_study_session`,
  getStudyProgress: `${BASE_URL}/dashboard/study_progress`,
  getQuickStats: `${BASE_URL}/dashboard/quick_stats`,
  // Add other endpoints as needed
};