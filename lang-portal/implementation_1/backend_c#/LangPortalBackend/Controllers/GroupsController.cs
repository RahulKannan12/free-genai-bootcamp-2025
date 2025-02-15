using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class GroupsController : ControllerBase
{
    private readonly AppDbContext _context;

    public GroupsController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public IActionResult GetGroups()
    {
        var groups = _context.Groups
            .Select(g => new
            {
                g.Id,
                g.Name
            })
            .ToList();

        return Ok(groups);
    }

    [HttpGet("{id}")]
    public IActionResult GetGroup(int id)
    {
        var group = _context.Groups
            .Where(g => g.Id == id)
            .Select(g => new
            {
                g.Id,
                g.Name
            })
            .FirstOrDefault();

        if (group == null)
        {
            return NotFound();
        }

        return Ok(group);
    }

    [HttpGet("{id}/words")]
    public IActionResult GetGroupWords(int id)
    {
        var words = _context.WordsGroups
            .Where(wg => wg.GroupId == id)
            .Select(wg => new
            {
                wg.Word.Id,
                wg.Word.Japanese,
                wg.Word.Romaji,
                wg.Word.English,
                wg.Word.Parts
            })
            .ToList();

        if (!words.Any())
        {
            return NotFound();
        }

        return Ok(words);
    }

    [HttpGet("{id}/study_sessions")]
    public IActionResult GetGroupStudySessions(int id)
    {
        var studySessions = _context.StudySessions
            .Where(ss => ss.GroupId == id)
            .Select(ss => new
            {
                ss.Id,
                ss.CreatedAt,
                ss.StudyActivityId
            })
            .ToList();

        if (!studySessions.Any())
        {
            return NotFound();
        }

        return Ok(studySessions);
    }
}