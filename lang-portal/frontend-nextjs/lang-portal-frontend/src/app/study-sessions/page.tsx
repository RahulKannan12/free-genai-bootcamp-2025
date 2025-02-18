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
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { ChevronDown, ArrowUpDown } from "lucide-react";

interface StudySession {
  id: number;
  activityName: string;
  groupName: string;
  startTime: string;
  endTime: string;
  reviewItems: number;
}

const StudySessions = () => {
  // This would typically come from an API
  const sessions: StudySession[] = [
    {
      id: 1,
      activityName: "Typing Tutor",
      groupName: "Core Verbs",
      startTime: "2025-02-08 12:16:18.159792",
      endTime: "2025-02-08 12:16:18.159792",
      reviewItems: 5,
    },
  ];

  const formatDateTime = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  return (
    <div className="p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Study Sessions</h1>
        
        {/* Optional: Add filters or additional controls here */}
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline">
              Filter
              <ChevronDown className="ml-2 h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent>
            <DropdownMenuItem>All Sessions</DropdownMenuItem>
            <DropdownMenuItem>Today</DropdownMenuItem>
            <DropdownMenuItem>This Week</DropdownMenuItem>
            <DropdownMenuItem>This Month</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>

      <Card>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="w-16">ID</TableHead>
                <TableHead>
                  <div className="flex items-center space-x-1">
                    ACTIVITY NAME
                    <ArrowUpDown className="h-4 w-4" />
                  </div>
                </TableHead>
                <TableHead>
                  <div className="flex items-center space-x-1">
                    GROUP NAME
                    <ArrowUpDown className="h-4 w-4" />
                  </div>
                </TableHead>
                <TableHead>
                  <div className="flex items-center space-x-1">
                    START TIME
                    <ArrowUpDown className="h-4 w-4" />
                  </div>
                </TableHead>
                <TableHead>
                  <div className="flex items-center space-x-1">
                    END TIME
                    <ArrowUpDown className="h-4 w-4" />
                  </div>
                </TableHead>
                <TableHead className="text-right"># REVIEW ITEMS</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {sessions.map((session) => (
                <TableRow key={session.id}>
                  <TableCell>{session.id}</TableCell>
                  <TableCell className="font-medium">{session.activityName}</TableCell>
                  <TableCell>{session.groupName}</TableCell>
                  <TableCell>{formatDateTime(session.startTime)}</TableCell>
                  <TableCell>{formatDateTime(session.endTime)}</TableCell>
                  <TableCell className="text-right">{session.reviewItems}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
};

export default StudySessions;