from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class PlotTimes:
    hours_back: int = 3
    minutes_forward: int = 10
    now: datetime = datetime.utcnow()
    start_time: datetime = now - timedelta(hours=hours_back)
    end_time_time: datetime = now + timedelta(hours=minutes_forward)
    update_time: str = f'Updated:  {now.strftime(" %H:%M UTC -- %b %d, %Y")}'
    

class BuoyData:
    plot_times = PlotTimes(int(3), int(10))
    print(plot_times.minutes_forward)
    
    
if __name__ == "__main__":
    BuoyData()