using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class ResetController : ControllerBase
{
    private readonly AppDbContext _context;

    public ResetController(AppDbContext context)
    {
        _context = context;
    }

    [HttpPost("reset_history")]
    public IActionResult ResetHistory()
    {
        var wordReviewItems = _context.WordReviewItems.ToList();
        _context.WordReviewItems.RemoveRange(wordReviewItems);
        _context.SaveChanges();

        return Ok(new { message = "History reset successfully" });
    }

    [HttpPost("full_reset")]
    public IActionResult FullReset()
    {
        var wordReviewItems = _context.WordReviewItems.ToList();
        var studySessions = _context.StudySessions.ToList();
        var studyActivities = _context.StudyActivities.ToList();

        _context.WordReviewItems.RemoveRange(wordReviewItems);
        _context.StudySessions.RemoveRange(studySessions);
        _context.StudyActivities.RemoveRange(studyActivities);
        _context.SaveChanges();

        return Ok(new { message = "Full reset successfully" });
    }
}