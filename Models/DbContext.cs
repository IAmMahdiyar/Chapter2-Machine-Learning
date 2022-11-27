using Microsoft.EntityFrameworkCore;

class Context : DbContext{
    public string DbPath { get; }
    public Context()
    {
        var folder = Environment.SpecialFolder.LocalApplicationData;
        var path = Environment.GetFolderPath(folder);
        DbPath = System.IO.Directory.GetCurrentDirectory() + @"/database.db"; 
    }
    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseSqlite($"Data Source={DbPath}");

    public virtual DbSet<Movie> Movies { get; set; }
    public virtual DbSet<User> Users { get; set; }
    public virtual DbSet<Predict> Predicts { get; set; }
    public virtual DbSet<Rating> Ratings { get; set; }
}