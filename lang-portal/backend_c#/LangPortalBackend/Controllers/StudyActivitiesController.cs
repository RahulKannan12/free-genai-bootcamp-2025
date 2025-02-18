using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class StudyActivitiesController : ControllerBase
{
    private readonly AppDbContext _context;

    public StudyActivitiesController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet("{id}")]
    public IActionResult GetStudyActivity(int id)
    {
        var studyActivity = _context.StudyActivities
            .Where(sa => sa.Id == id)
            .Select(sa => new
            {
                sa.Id,
                sa.StudySessionId,
                sa.GroupId,
                sa.CreatedAt
            })
            .FirstOrDefault();

        if (studyActivity == null)
        {
            return NotFound();
        }

        return Ok(studyActivity);
    }

    [HttpGet("{id}/study_sessions")]
    public IActionResult GetStudySessions(int id, int page = 1, int pageSize = 100)
    {
        var studySessions = _context.StudySessions
            .Where(ss => ss.StudyActivityId == id)
            .OrderByDescending(ss => ss.CreatedAt)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .Select(ss => new
            {
                ss.Id,
                ActivityName = ss.StudyActivityId,
                GroupName = ss.Group.Name,
                ss.CreatedAt,
                ReviewItemsCount = ss.WordReviewItems.Count
            })
            .ToList();

        var totalItems = _context.StudySessions.Count(ss => ss.StudyActivityId == id);
        var totalPages = (int)Math.Ceiling(totalItems / (double)pageSize);

        var response = new
        {
            Items = studySessions,
            Pagination = new
            {
                CurrentPage = page,
                TotalPages = totalPages,
                TotalItems = totalItems,
                ItemsPerPage = pageSize
            }
        };

        return Ok(response);
    }

    [HttpPost]
    public IActionResult CreateStudyActivity([FromBody] StudyActivities studyActivity)
    {
        if (studyActivity == null)
        {
            return BadRequest();
        }

        _context.StudyActivities.Add(studyActivity);
        _context.SaveChanges();

        return CreatedAtAction(nameof(GetStudyActivity), new { id = studyActivity.Id }, studyActivity);
    }
}