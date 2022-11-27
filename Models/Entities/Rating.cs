class Rating : BaseEntity<int>
{
    public Movie? Movie;
    public User? User;
    public double? RatingNumber { get; set; }
}