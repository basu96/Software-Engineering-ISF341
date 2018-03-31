import datetime
import gantt
import networkx as nx
import matplotlib.pyplot as plt
"""
    Input format:
    <task_id>, <task_name>, <dependencies>, <duration>, <percent_completed>
"""

INPUT_FILENAME = "gantt_chart.csv"
GANTT_FILENAME = "gantt.svg"
PERT_FILENAME = "pert.png"
CRITICAL_NODES_FILENAME = "critical_nodes.csv"
PROJECT_NAME = ""
START_DATE = datetime.date(2018,5,20)
gantt.define_font_attributes(fill='black', stroke='black', stroke_width=1, font_family="Verdana")

def make_gantt_chart(list_of_tasks):
    # print(list_of_tasks)
    # Create gantt.Task objects to be sent to project
    gantt_tasks = []
    for task in list_of_tasks:

        dependencies = []
        for gtask in gantt_tasks:
            if(gtask.name in task['depends_of']):
                dependencies.append(gtask)

        t = gantt.Task(
            name = task['name'],
            start = task['start'],
            duration = task['duration'],
            depends_of = dependencies,
            percent_done = task['percent_done'],
        )
        gantt_tasks.append(t)

    # Add task to project
    project = gantt.Project(name=PROJECT_NAME)
    for task in gantt_tasks:
        project.add_task(task)

    project.make_svg_for_tasks(filename=GANTT_FILENAME)

def make_PERT_chart(list_of_tasks):

    # for task in list_of_tasks:
    #     print(task)

    # Dependencies in the format (from,to) : from must be completed before to begins
    dependencies = []
    for task in list_of_tasks:
        for depends in task['depends_of']:
            dependencies.append((depends,task['name']))

    critical_nodes_file = open(CRITICAL_NODES_FILENAME)
    test_critical_nodes = critical_nodes_file.read().split(',')
    # test_critical_nodes = ['b','c','f','h']

    G = nx.DiGraph()
    for task in list_of_tasks:
        G.add_node(task['name'])

    for dep in dependencies:
        # G.add_edges_from(dependencies)
        if(dep[0] in test_critical_nodes and dep[1] in test_critical_nodes):
            G.add_edge(dep[0],dep[1],color='r',weight=4)
        else:
            G.add_edge(dep[0],dep[1],color='b',weight=1)

    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    weights = [G[u][v]['weight'] for u,v in edges]

    print("nodes\t", G.nodes)
    print("edges\t",G.edges)
    print(list(G.adj['a']))

    color_map = []
    for node in G:
        if node in test_critical_nodes:
            color_map.append('blue')
        else:
            color_map.append('green')
    # nx.draw(G,node_color = color_map,with_labels = True)
    # plt.show()

    nx.draw_circular(
        G,
        with_labels=True,
        font_weight='bold',
        # node_size=1000,
        node_color = color_map,
        edges=edges,
        edge_color=colors,
        width=weights,
    )
    plt.savefig(PERT_FILENAME)

###############################################################################


input_file = open(INPUT_FILENAME)
content = input_file.read()
records = content.split('\n')[1:]

# Create task objects
list_of_tasks = []
for rec in records:

    if(rec == ''):
        break

    values = rec.split(',')[:-1]

    task_args = {}
    task_args['id'] = values[0]
    task_args['name'] = values[1]
    task_args['start'] = START_DATE
    task_args['duration'] = int(values[3])

    dependencies = []
    temps = values[2].split(' ')
    for task in list_of_tasks:
        # print("task", task)
        if(task['id'] in temps):
            dependencies.append(task['name'])

    # if(not values[2] == ''):
    #     task_args['depends_of'] = list(map(int,values[2].split(' ')))
    # else:
    #     task_args['depends_of'] = []

    task_args['depends_of'] = dependencies

    perc = values[4]
    if(perc == '' or perc == 'null'):
        task_args['percent_done'] = 0
    else:
        task_args['percent_done'] = int(perc)
    list_of_tasks.append(task_args)


make_gantt_chart(list_of_tasks)
# for task in list_of_tasks:
#     print(task)
make_PERT_chart(list_of_tasks)
