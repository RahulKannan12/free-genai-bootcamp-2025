import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

interface WordDetails {
  japanese: string;
  romaji: string;
  english: string;
  studyStats: {
    correctAnswers: number;
    wrongAnswers: number;
  };
  wordGroups: string[];
}

interface WordDetailsResponse {
  word: WordDetails;
  isLoading: boolean;
  error: string | null;
}

const WordDetailsPage = () => {
  // In a real implementation, you'd fetch this data from an API
  // using useEffect or a data fetching library like React Query
  const { word, isLoading, error }: WordDetailsResponse = {
    word: {
      japanese: 'あげる',
      romaji: 'ageru',
      english: 'to give',
      studyStats: {
        correctAnswers: 1,
        wrongAnswers: 0,
      },
      wordGroups: ['Core Verbs'],
    },
    isLoading: false,
    error: null,
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Word Details</h1>
        <button 
          onClick={() => window.history.back()} 
          className="text-blue-600 hover:text-blue-800"
        >
          Back to Words
        </button>
      </div>

      <div className="space-y-6">
        {/* Language Details */}
        <section className="space-y-4">
          <div>
            <h2 className="text-lg font-semibold text-gray-700">Japanese</h2>
            <p className="text-2xl">{word.japanese}</p>
          </div>

          <div>
            <h2 className="text-lg font-semibold text-gray-700">Romaji</h2>
            <p className="text-xl">{word.romaji}</p>
          </div>

          <div>
            <h2 className="text-lg font-semibold text-gray-700">English</h2>
            <p className="text-xl">{word.english}</p>
          </div>
        </section>

        {/* Study Statistics */}
        <Card>
          <CardHeader>
            <CardTitle>Study Statistics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <h3 className="text-sm text-gray-600">Correct Answers</h3>
                <p className="text-2xl font-semibold text-green-500">
                  {word.studyStats.correctAnswers}
                </p>
              </div>
              <div>
                <h3 className="text-sm text-gray-600">Wrong Answers</h3>
                <p className="text-2xl font-semibold text-red-500">
                  {word.studyStats.wrongAnswers}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Word Groups */}
        <section>
          <h2 className="text-lg font-semibold text-gray-700 mb-3">Word Groups</h2>
          <div className="flex gap-2">
            {word.wordGroups.map((group) => (
              <Badge key={group} variant="secondary">
                {group}
              </Badge>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
};

export default WordDetailsPage;