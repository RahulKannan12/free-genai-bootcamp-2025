using System;
using System.Collections.Generic;

public class StudySessions
{
    public int Id { get; set; }
    public int GroupId { get; set; }
    public DateTime CreatedAt { get; set; }
    public int StudyActivityId { get; set; }
    public Groups Group { get; set; }
    public ICollection<WordReviewItems> WordReviewItems { get; set; }
}