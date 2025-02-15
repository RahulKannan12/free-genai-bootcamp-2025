using System;

public class WordReviewItems
{
    public int WordId { get; set; }
    public int StudySessionId { get; set; }
    public bool Correct { get; set; }
    public DateTime CreatedAt { get; set; }
    public Words Word { get; set; }
    public StudySessions StudySession { get; set; }
}