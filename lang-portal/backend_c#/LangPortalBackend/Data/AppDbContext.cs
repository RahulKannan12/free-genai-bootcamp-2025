using Microsoft.EntityFrameworkCore;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<Words> Words { get; set; }
    public DbSet<WordsGroups> WordsGroups { get; set; }
    public DbSet<Groups> Groups { get; set; }
    public DbSet<StudySessions> StudySessions { get; set; }
    public DbSet<StudyActivities> StudyActivities { get; set; }
    public DbSet<WordReviewItems> WordReviewItems { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<WordsGroups>()
            .HasKey(wg => new { wg.WordId, wg.GroupId });

        modelBuilder.Entity<WordReviewItems>()
            .HasKey(wr => new { wr.WordId, wr.StudySessionId });
    }
}