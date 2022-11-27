class Predict : BaseEntity<int>{
    public Movie? Movie { get; set; }
    public User? User {get; set;}
    public bool DoRecommend { get; set; }
}