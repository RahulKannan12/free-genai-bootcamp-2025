import React, { useState } from 'react';
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
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { ArrowUpDown, ChevronDown } from "lucide-react";
import { Input } from "@/components/ui/input";

interface Word {
  kanji: string;
  romaji: string;
  english: string;
  correct: number;
  wrong: number;
}

const WordsList = () => {
  const [searchTerm, setSearchTerm] = useState('');

  // This would typically come from an API
  const words: Word[] = [
    { kanji: "あげる", romaji: "ageru", english: "to give", correct: 1, wrong: 0 },
    { kanji: "いい", romaji: "ii", english: "good", correct: 0, wrong: 0 },
    { kanji: "おいしい", romaji: "oishii", english: "tasty", correct: 0, wrong: 0 },
    { kanji: "する", romaji: "suru", english: "to do", correct: 0, wrong: 0 },
    { kanji: "つける", romaji: "tsukeru", english: "to turn on", correct: 0, wrong: 0 },
    { kanji: "もらう", romaji: "morau", english: "to receive", correct: 0, wrong: 0 },
    { kanji: "下車する", romaji: "geshasuru", english: "to get off (vehicle)", correct: 0, wrong: 0 },
    { kanji: "乗る", romaji: "noru", english: "to ride", correct: 0, wrong: 0 },
    { kanji: "休む", romaji: "yasumu", english: "to rest", correct: 0, wrong: 0 },
    { kanji: "会う", romaji: "au", english: "to meet", correct: 0, wrong: 0 },
    { kanji: "低い", romaji: "hikui", english: "low", correct: 0, wrong: 0 },
    { kanji: "作る", romaji: "tsukuru", english: "to make", correct: 0, wrong: 0 },
  ];

  const filteredWords = words.filter(word => 
    word.kanji.toLowerCase().includes(searchTerm.toLowerCase()) ||
    word.romaji.toLowerCase().includes(searchTerm.toLowerCase()) ||
    word.english.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Words</h1>
        <div className="flex gap-4">
          <Input
            placeholder="Search words..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-64"
          />
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline">
                Filter
                <ChevronDown className="ml-2 h-4 w-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem>All Words</DropdownMenuItem>
              <DropdownMenuItem>Studied</DropdownMenuItem>
              <DropdownMenuItem>Not Studied</DropdownMenuItem>
              <DropdownMenuItem>Mastered</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>

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
              {filteredWords.map((word) => (
                <TableRow key={word.kanji}>
                  <TableCell>
                    <span className="text-blue-600 hover:underline cursor-pointer">
                      {word.kanji}
                    </span>
                  </TableCell>
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
  );
};

export default WordsList;