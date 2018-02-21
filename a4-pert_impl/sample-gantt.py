import datetime
import gantt

gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family="Verdana")

sample_date = datetime.date(2018,2,10)

t1 = gantt.Task(name="task1", start=sample_date, duration=5)
t2 = gantt.Task(name="task2", start=sample_date, duration=3, depends_of=[t1])
t3 = gantt.Task(name="task3", start=sample_date, duration=4, depends_of=[t1])
t4 = gantt.Task(name="task4", start=sample_date, duration=6, depends_of=[t3])
t5 = gantt.Task(name="task5", start=sample_date, duration=4, depends_of=[t2,t3])
t6 = gantt.Task(name="task6", start=sample_date, duration=1, depends_of=[t4])
t7 = gantt.Task(name="task7", start=sample_date, duration=5, depends_of=[t4,t5,t6])

project = gantt.Project(name="SampleProject")
project.add_task(t1)
project.add_task(t2)
project.add_task(t3)
project.add_task(t4)
project.add_task(t5)
project.add_task(t6)
project.add_task(t7)

project.make_svg_for_tasks(filename="SampleProject.svg", today=datetime.date(2018,2,1))
