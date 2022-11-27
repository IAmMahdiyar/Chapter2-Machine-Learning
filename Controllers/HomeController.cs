using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using site.Models;
using Microsoft.EntityFrameworkCore;

namespace site.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly Context _context = new Context();

    public IActionResult Index()
    {
        return View();
    }

    public IActionResult Recommend(int userId)
    {
        var model = CreateRecommendVm(userId);
        return View(model);
    }

    private RecommendVm CreateRecommendVm(int userId){
        return new RecommendVm{
            Predicts = _context.Predicts.Include(p => p.User).Include(p => p.Movie).Where(p => p.User.Id == userId)
            .Where(p => p.DoRecommend == true)
            .ToList(),
            
            User = _context.Users.Find(userId)
        };
    }
}
