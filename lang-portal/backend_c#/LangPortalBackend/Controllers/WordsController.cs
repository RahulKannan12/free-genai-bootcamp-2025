using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class WordsController : ControllerBase
{
    private readonly AppDbContext _context;

    public WordsController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public IActionResult GetWords(int page = 1, int pageSize = 100)
    {
        var words = _context.Words
            .OrderBy(w => w.Id)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .Select(w => new
            {
                w.Japanese,
                WrongCount = _context.WordReviewItems.Count(wr => wr.WordId == w.Id && !wr.Correct)
            })
            .ToList();

        var totalItems = _context.Words.Count();
        var totalPages = (int)Math.Ceiling(totalItems / (double)pageSize);

        var response = new
        {
            Items = words,
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
    public IActionResult GetWord(int id)
    {
        var word = _context.Words
            .Where(w => w.Id == id)
            .Select(w => new
            {
                w.Japanese,
                w.Romaji,
                w.English,
                w.Parts
            })
            .FirstOrDefault();

        if (word == null)
        {
            return NotFound();
        }

        return Ok(word);
    }
}