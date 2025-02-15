using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class DashboardController : ControllerBase
{
    private readonly AppDbContext _context;

    public DashboardController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet("last_study_session")]
    public IActionResult GetLastStudySession()
    {
        var lastStudySession = _context.StudySessions
            .OrderByDescending(ss => ss.CreatedAt)
            .Select(ss => new
            {
                ss.Id,
                ss.GroupId,
                ss.CreatedAt,
                ss.StudyActivityId,
                GroupName = ss.Group.Name
            })
            .FirstOrDefault();

        if (lastStudySession == null)
        {
            return NotFound();
        }

        return Ok(lastStudySession);
    }

    [HttpGet("study_progress")]
    public IActionResult GetStudyProgress()
    {
        var totalWordsStudied = _context.WordReviewItems.Count();
        var totalAvailableWords = _context.Words.Count();

        var studyProgress = new
        {
            TotalWordsStudied = totalWordsStudied,
            TotalAvailableWords = totalAvailableWords
        };

        return Ok(studyProgress);
    }

    [HttpGet("quick-stats")]
    public IActionResult GetQuickStats()
    {
        var totalStudySessions = _context.StudySessions.Count();
        var totalActiveGroups = _context.Groups.Count();
        var successRate = _context.WordReviewItems
            .Where(wr => wr.Correct)
            .Count() / (double)_context.WordReviewItems.Count() * 100;
        var studyStreakDays = _context.StudySessions
            .GroupBy(ss => ss.CreatedAt.Date)
            .Count();

        var quickStats = new
        {
            SuccessRate = successRate,
            TotalStudySessions = totalStudySessions,
            TotalActiveGroups = totalActiveGroups,
            StudyStreakDays = studyStreakDays
        };

        return Ok(quickStats);
    }
}