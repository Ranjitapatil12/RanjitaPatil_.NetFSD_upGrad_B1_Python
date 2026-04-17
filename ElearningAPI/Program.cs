using ElearningAPI;
using ElearningAPI.Data;
using ElearningAPI.Services;
using ElearningAPI.Repositories;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// ✅ RUN TESTS FIRST (so output is visible)
TestRunner.RunTests();


// ✅ ADD CONTROLLERS
builder.Services.AddControllers();


// ✅ AUTOMAPPER
builder.Services.AddAutoMapper(AppDomain.CurrentDomain.GetAssemblies());


// ✅ DB CONTEXT (SQL SERVER)
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(
        builder.Configuration.GetConnectionString("DefaultConnection")
    )
);


// ✅ SERVICE LAYER
builder.Services.AddScoped<IUserService, UserService>();


// ✅ REPOSITORY LAYER
builder.Services.AddScoped<IUserRepository, UserRepository>();


// ✅ CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll",
        policy => policy.AllowAnyOrigin()
                        .AllowAnyMethod()
                        .AllowAnyHeader());
});


// ✅ SWAGGER
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();


var app = builder.Build();


// ✅ ENABLE SWAGGER
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}


// ✅ MIDDLEWARE ORDER
app.UseCors("AllowAll");

app.UseHttpsRedirection();

app.UseAuthorization();


// ✅ MAP CONTROLLERS
app.MapControllers();


// ✅ RUN APPLICATION
app.Run();