import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { ArrowRight, Clock, Activity, Trophy } from 'lucide-react';
import { GetServerSideProps } from 'next';
import { API_ENDPOINTS} from '@/app/helpers/api';

interface StudySession {
  type: string;
  date: string;
  correct: number;
  wrong: number;
}

interface DashboardData {
  lastStudySession: StudySession;
  totalWords: number;
  wordsStudied: number;
  masteryProgress: number;
  successRate: number;
  studySessions: number;
  activeGroups: number;
  studyStreak: number;
}

const Dashboard = async () => {
  // This would typically come from an API or state management
  const res = await fetch(API_ENDPOINTS.getLastStudySession);
  const data = await res.json();
    

  const dashboardData: DashboardData = {
    lastStudySession: {
      type: "Typing Tutor",
      date: "2/8/2025",
      correct: 4,
      wrong: 1
    },
    totalWords: 124,
    wordsStudied: 3,
    masteryProgress: 0,
    successRate: 80,
    studySessions: 1,
    activeGroups: 1,
    studyStreak: 1
  };

  return (
    <div className="p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <button className="bg-blue-500 text-white px-4 py-2 rounded-lg flex items-center gap-2">
          Start Studying
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Last Study Session */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Clock className="w-5 h-5" />
              Last Study Session
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <h3 className="font-medium">{dashboardData.lastStudySession.type}</h3>
              <p className="text-sm text-gray-500">{dashboardData.lastStudySession.date}</p>
              <div className="flex gap-4">
                <span className="text-green-500">✓ {dashboardData.lastStudySession.correct} correct</span>
                <span className="text-red-500">✗ {dashboardData.lastStudySession.wrong} wrong</span>
              </div>
              <button className="text-blue-500 text-sm flex items-center gap-1">
                View Group
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </CardContent>
        </Card>

        {/* Study Progress */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Activity className="w-5 h-5" />
              Study Progress
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <div className="flex justify-between mb-2">
                  <span>Total Words Studied</span>
                  <span>{dashboardData.wordsStudied} / {dashboardData.totalWords}</span>
                </div>
                <Progress 
                  value={(dashboardData.wordsStudied / dashboardData.totalWords) * 100} 
                  className="h-2"
                />
              </div>
              <div>
                <div className="flex justify-between mb-2">
                  <span>Mastery Progress</span>
                  <span>{dashboardData.masteryProgress}%</span>
                </div>
                <Progress 
                  value={dashboardData.masteryProgress} 
                  className="h-2"
                />
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Quick Stats */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Trophy className="w-5 h-5" />
              Quick Stats
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex justify-between">
                <span>Success Rate</span>
                <span className="font-medium">{dashboardData.successRate}%</span>
              </div>
              <div className="flex justify-between">
                <span>Study Sessions</span>
                <span className="font-medium">{dashboardData.studySessions}</span>
              </div>
              <div className="flex justify-between">
                <span>Active Groups</span>
                <span className="font-medium">{dashboardData.activeGroups}</span>
              </div>
              <div className="flex justify-between">
                <span>Study Streak</span>
                <span className="font-medium">{dashboardData.studyStreak} days</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

// export const getServerSideProps: GetServerSideProps = async () => {
//     const res = await fetch(API_ENDPOINTS.getLastStudySession);
//     const data = await res.json();
//     console.log(data);
//     return {
//       props: { data }, // This data will be passed to your component as props
//     };
//   };

export default Dashboard;