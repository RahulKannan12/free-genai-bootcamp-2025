using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class StudySessionsController : ControllerBase
{
    private readonly AppDbContext _context;

    public StudySessionsController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public IActionResult GetStudySessions(int page = 1, int pageSize = 100)
    {
        var studySessions = _context.StudySessions
            .OrderByDescending(ss => ss.CreatedAt)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .Select(ss => new
            {
                ss.Id,
                ss.GroupId,
                ss.CreatedAt,
                ss.StudyActivityId
            })
            .ToList();

        var totalItems = _context.StudySessions.Count();
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

    [HttpGet("{id}")]
    public IActionResult GetStudySession(int id)
    {
        var studySession = _context.StudySessions
            .Where(ss => ss.Id == id)
            .Select(ss => new
            {
                ss.Id,
                ss.GroupId,
                ss.CreatedAt,
                ss.StudyActivityId
            })
            .FirstOrDefault();

        if (studySession == null)
        {
            return NotFound();
        }

        return Ok(studySession);
    }

    [HttpGet("{id}/words")]
    public IActionResult GetStudySessionWords(int id)
    {
        var words = _context.WordReviewItems
            .Where(wr => wr.StudySessionId == id)
            .Select(wr => new
            {
                wr.Word.Id,
                wr.Word.Japanese,
                wr.Word.Romaji,
                wr.Word.English,
                wr.Word.Parts,
                wr.Correct,
                wr.CreatedAt
            })
            .ToList();

        if (!words.Any())
        {
            return NotFound();
        }

        return Ok(words);
    }
}