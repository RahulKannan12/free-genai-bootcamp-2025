using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Linq;
using System.IO;
using Newtonsoft.Json;

public static class DatabaseInitializer
{
    public static void Initialize(IServiceProvider serviceProvider)
    {
        using (var context = new AppDbContext(
            serviceProvider.GetRequiredService<DbContextOptions<AppDbContext>>()))
        {
            context.Database.Migrate();

            // Look for any existing data.
            if (context.Words.Any())
            {
                return;   // DB has been seeded
            }

            // Seed initial data from JSON files
            SeedDataFromJson(context);

            context.SaveChanges();
        }
    }

    private static void SeedDataFromJson(AppDbContext context)
    {
        var wordsJson = File.ReadAllText("Data/SeedData/words.json");
        var words = JsonConvert.DeserializeObject<List<Words>>(wordsJson);
        context.Words.AddRange(words);

        var groupsJson = File.ReadAllText("Data/SeedData/groups.json");
        var groups = JsonConvert.DeserializeObject<List<Groups>>(groupsJson);
        context.Groups.AddRange(groups);

        var studySessionsJson = File.ReadAllText("Data/SeedData/study_sessions.json");
        var studySessions = JsonConvert.DeserializeObject<List<StudySessions>>(studySessionsJson);
        context.StudySessions.AddRange(studySessions);

        var studyActivitiesJson = File.ReadAllText("Data/SeedData/study_activities.json");
        var studyActivities = JsonConvert.DeserializeObject<List<StudyActivities>>(studyActivitiesJson);
        context.StudyActivities.AddRange(studyActivities);

        var wordReviewItemsJson = File.ReadAllText("Data/SeedData/word_review_items.json");
        var wordReviewItems = JsonConvert.DeserializeObject<List<WordReviewItems>>(wordReviewItemsJson);
        context.WordReviewItems.AddRange(wordReviewItems);
    }
}