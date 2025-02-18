import { useState } from 'react';
import Link from 'next/link';
import { ChevronUp, ChevronDown } from 'lucide-react';

interface WordGroup {
  id: string;
  name: string;
  wordCount: number;
}

interface SortConfig {
  key: 'name' | 'wordCount';
  direction: 'asc' | 'desc';
}

const WordGroupsPage = () => {
  // State for sorting
  const [sortConfig, setSortConfig] = useState<SortConfig>({
    key: 'name',
    direction: 'asc',
  });

  // Mock data - in real app, fetch from API
  const [wordGroups, setWordGroups] = useState<WordGroup[]>([
    { id: '1', name: 'Core Adjectives', wordCount: 64 },
    { id: '2', name: 'Core Verbs', wordCount: 60 },
  ]);

  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = 1;

  const handleSort = (key: 'name' | 'wordCount') => {
    setSortConfig((prevConfig) => ({
      key,
      direction:
        prevConfig.key === key && prevConfig.direction === 'asc' ? 'desc' : 'asc',
    }));

    // Sort the data
    const sortedGroups = [...wordGroups].sort((a, b) => {
      if (key === 'name') {
        return sortConfig.direction === 'asc'
          ? b.name.localeCompare(a.name)
          : a.name.localeCompare(b.name);
      } else {
        return sortConfig.direction === 'asc'
          ? b.wordCount - a.wordCount
          : a.wordCount - b.wordCount;
      }
    });

    setWordGroups(sortedGroups);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Word Groups</h1>

      {/* Table */}
      <div className="bg-white rounded-md shadow">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th 
                className="px-6 py-3 text-left cursor-pointer hover:bg-gray-50"
                onClick={() => handleSort('name')}
              >
                <div className="flex items-center space-x-1">
                  <span className="text-gray-600 font-medium">NAME</span>
                  {sortConfig.key === 'name' && (
                    sortConfig.direction === 'asc' ? 
                    <ChevronUp className="w-4 h-4" /> : 
                    <ChevronDown className="w-4 h-4" />
                  )}
                </div>
              </th>
              <th 
                className="px-6 py-3 text-left cursor-pointer hover:bg-gray-50"
                onClick={() => handleSort('wordCount')}
              >
                <div className="flex items-center space-x-1">
                  <span className="text-gray-600 font-medium">WORD COUNT</span>
                  {sortConfig.key === 'wordCount' && (
                    sortConfig.direction === 'asc' ? 
                    <ChevronUp className="w-4 h-4" /> : 
                    <ChevronDown className="w-4 h-4" />
                  )}
                </div>
              </th>
            </tr>
          </thead>
          <tbody>
            {wordGroups.map((group) => (
              <tr 
                key={group.id}
                className="border-b hover:bg-gray-50 cursor-pointer"
                onClick={() => {
                  // Handle navigation to group details
                  console.log(`Navigate to group ${group.id}`);
                }}
              >
                <td className="px-6 py-4">
                  <Link href={`/word-groups/${group.id}`} className="text-blue-600 hover:text-blue-800">
                    {group.name}
                  </Link>
                </td>
                <td className="px-6 py-4 text-gray-600">
                  {group.wordCount}
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* Pagination */}
        <div className="flex justify-end items-center px-6 py-3 border-t">
          <div className="flex items-center space-x-2">
            <button
              className="px-3 py-1 text-gray-600 hover:bg-gray-100 rounded disabled:opacity-50"
              disabled={currentPage === 1}
              onClick={() => setCurrentPage(currentPage - 1)}
            >
              Previous
            </button>
            <span className="text-gray-600">
              Page {currentPage} of {totalPages}
            </span>
            <button
              className="px-3 py-1 text-gray-600 hover:bg-gray-100 rounded disabled:opacity-50"
              disabled={currentPage === totalPages}
              onClick={() => setCurrentPage(currentPage + 1)}
            >
              Next
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WordGroupsPage;