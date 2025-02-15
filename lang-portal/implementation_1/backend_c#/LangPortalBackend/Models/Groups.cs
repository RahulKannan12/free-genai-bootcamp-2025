using System.Collections.Generic;

public class Groups
{
    public int Id { get; set; }
    public string Name { get; set; }
    public ICollection<WordsGroups> WordsGroups { get; set; }
    public ICollection<StudySessions> StudySessions { get; set; }
}