# Task Prioritization and Scheduling Tool  
Efficiently manage tasks and optimize your schedule using a **Greedy Algorithm** and an intuitive GUI.

---

## Features  
- 📝 **Task Prioritization**: Calculates a priority score based on urgency, difficulty, and duration.  
- 🎨 **Interactive GUI**: Add tasks and view the schedule seamlessly.  
- ⏱️ **Realistic Scheduling**: Limits daily tasks to 12 hours for practical management.  

---

## How It Works  
1. **Input Tasks**:  
   Enter task details including:
   - Name
   - Estimated duration (hours)
   - Difficulty (1-10)
   - Deadline (`YYYY-MM-DD`)  

2. **Prioritization**:  
   Tasks are sorted by:
   - Deadline urgency.
   - Estimated duration and difficulty.  

3. **Schedule Output**:  
   Tasks are scheduled sequentially, with a daily cap of 12 hours.

---

## File Structure  
- `task.py`: Defines the `Task` class and calculates priority scores.  
- `PrioritySchedule.py`: Implements the greedy scheduling algorithm.  
- `gui.py`: Provides the graphical user interface.

---

## Getting Started  
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-prioritization-scheduler.git
cd task-prioritization-scheduler
python3 gui.py
