import utils.clock as clock
import utils.weather as weather

print(clock.getTime()+ " " + clock.getMonthAndDate())
print(weather.getFormattedWeather(weather.getWeather()))