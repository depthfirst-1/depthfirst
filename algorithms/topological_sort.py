order = []

def topological_sort(graph):

    courses = list(graph.keys())

    # initialize all courses to GRAY to indicate undiscovered state
    nodes_color = {course: 'GRAY' for course in courses}
   
    for course in courses:
        # Run a DFS, only if the course is undiscovered
        if nodes_color[course] == 'GRAY':
            dfs(course, nodes_color, graph)
    
    return order


def dfs(course, nodes_color, graph):
    
    nodes_color[course] = 'ORANGE' # Mark as discovered

    for connected_course in graph[course]:
        if nodes_color[connected_course]  == 'GRAY':
            dfs(connected_course, nodes_color, graph)
        
    order.insert(0, course) 
    nodes_color[course] = 'GREEN' # Mark as explored


courses = {
    'Data Structures': ['Algorithms', 'Databases', 'Compilers'],
    'Formal Languages': ['Compilers'],
    'Computer Organization': ['Compilers'],
    'Discrete Math': ['Data Structures'],
    'Intro To Programming': ['Discrete Math'],
    'Single Variable Calculus': ['Multi Variable Calculus'],
    'Algorithms': [],
    'Databases': [],
    'Compilers': [],
    'Multi Variable Calculus': []
}

print(topological_sort(courses))
