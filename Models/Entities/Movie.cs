class Movie : BaseEntity<int>{
    public string? Title { get; set; }
    public string? Genres { get; set; }
    public ICollection<Predict>? Predicts { get; set; }
    public ICollection<Rating>? Ratings { get; set; }
}