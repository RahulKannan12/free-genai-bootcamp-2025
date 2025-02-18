using System;
using System.Collections.Generic;

public class StudyActivities
{
    public int Id { get; set; }
    public int StudySessionId { get; set; }
    public int GroupId { get; set; }
    public DateTime CreatedAt { get; set; }
    public StudySessions StudySession { get; set; }
    public Groups Group { get; set; }
}