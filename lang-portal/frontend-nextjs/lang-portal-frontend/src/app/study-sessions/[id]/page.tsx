import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  Card,
  CardContent,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowLeft, ArrowUpDown } from "lucide-react";
import Link from 'next/link';

interface ReviewedWord {
  kanji: string;
  romaji: string;
  english: string;
  correct: number;
  wrong: number;
}

interface SessionDetails {
  activity: string;
  group: string;
  startTime: string;
  reviewItems: number;
}

const StudySessionDetails = () => {
  // This would typically come from an API using the session ID
  const sessionDetails: SessionDetails = {
    activity: "Typing Tutor",
    group: "Core Verbs",
    startTime: "2025-02-08 12:16:18.159792",
    reviewItems: 5,
  };

  const reviewedWords: ReviewedWord[] = [
    {
      kanji: "あげる",
      romaji: "ageru",
      english: "to give",
      correct: 1,
      wrong: 0,
    },
    {
      kanji: "合う",
      romaji: "au",
      english: "to meet; to fit",
      correct: 2,
      wrong: 0,
    },
    {
      kanji: "帰る",
      romaji: "kaeru",
      english: "to return",
      correct: 1,
      wrong: 1,
    },
  ];

  const formatDateTime = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  return (
    <div className="p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Study Session Details</h1>
        <Link href="/sessions">
          <Button variant="outline" className="flex items-center gap-2">
            <ArrowLeft className="h-4 w-4" />
            Back to Sessions
          </Button>
        </Link>
      </div>

      {/* Session Overview */}
      <Card>
        <CardContent className="p-6 grid grid-cols-2 gap-6">
          <div className="space-y-4">
            <div>
              <h3 className="text-sm font-medium text-gray-500">Activity</h3>
              <p className="text-blue-600">{sessionDetails.activity}</p>
            </div>
            <div>
              <h3 className="text-sm font-medium text-gray-500">Start Time</h3>
              <p>{formatDateTime(sessionDetails.startTime)}</p>
            </div>
          </div>
          <div className="space-y-4">
            <div>
              <h3 className="text-sm font-medium text-gray-500">Group</h3>
              <p className="text-blue-600">{sessionDetails.group}</p>
            </div>
            <div>
              <h3 className="text-sm font-medium text-gray-500">Review Items</h3>
              <p>{sessionDetails.reviewItems}</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Words Reviewed Section */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Words Reviewed</h2>
        <Card>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>
                    <div className="flex items-center space-x-1">
                      KANJI
                      <ArrowUpDown className="h-4 w-4" />
                    </div>
                  </TableHead>
                  <TableHead>
                    <div className="flex items-center space-x-1">
                      ROMAJI
                      <ArrowUpDown className="h-4 w-4" />
                    </div>
                  </TableHead>
                  <TableHead>
                    <div className="flex items-center space-x-1">
                      ENGLISH
                      <ArrowUpDown className="h-4 w-4" />
                    </div>
                  </TableHead>
                  <TableHead className="text-center">CORRECT</TableHead>
                  <TableHead className="text-center">WRONG</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {reviewedWords.map((word) => (
                  <TableRow key={word.kanji}>
                    <TableCell className="text-blue-600">{word.kanji}</TableCell>
                    <TableCell>{word.romaji}</TableCell>
                    <TableCell>{word.english}</TableCell>
                    <TableCell className="text-center text-green-500">{word.correct}</TableCell>
                    <TableCell className="text-center text-red-500">{word.wrong}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default StudySessionDetails;