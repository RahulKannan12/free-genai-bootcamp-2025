public class WordsGroups
{
    public int Id { get; set; }
    public int WordId { get; set; }
    public int GroupId { get; set; }
    public Words Word { get; set; }
    public Groups Group { get; set; }
}