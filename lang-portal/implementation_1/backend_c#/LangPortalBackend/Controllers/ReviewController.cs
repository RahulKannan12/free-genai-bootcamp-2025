using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class ReviewController : ControllerBase
{
    private readonly AppDbContext _context;

    public ReviewController(AppDbContext context)
    {
        _context = context;
    }

    [HttpPost("study_sessions/{id}/words/{word_id}/review")]
    public IActionResult ReviewWord(int id, int word_id, [FromBody] ReviewRequest reviewRequest)
    {
        var studySession = _context.StudySessions.Find(id);
        if (studySession == null)
        {
            return NotFound(new { message = "Study session not found" });
        }

        var word = _context.Words.Find(word_id);
        if (word == null)
        {
            return NotFound(new { message = "Word not found" });
        }

        var wordReviewItem = new WordReviewItems
        {
            WordId = word_id,
            StudySessionId = id,
            Correct = reviewRequest.Correct,
            CreatedAt = DateTime.UtcNow
        };

        _context.WordReviewItems.Add(wordReviewItem);
        _context.SaveChanges();

        return Ok(new { message = "Review recorded successfully" });
    }
}

public class ReviewRequest
{
    public bool Correct { get; set; }
}