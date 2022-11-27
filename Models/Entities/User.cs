class User : BaseEntity<int>{
    public string? Name { get; set; }
    public ICollection<Predict>? Predicts { get; set; }
    public ICollection<Rating>? Ratings { get; set; }
}