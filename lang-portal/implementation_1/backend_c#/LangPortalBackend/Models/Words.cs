using System.Collections.Generic;

public class Words
{
    public int Id { get; set; }
    public string Japanese { get; set; }
    public string Romaji { get; set; }
    public string English { get; set; }
    public string Parts { get; set; }
    public ICollection<WordsGroups> WordsGroups { get; set; }
}