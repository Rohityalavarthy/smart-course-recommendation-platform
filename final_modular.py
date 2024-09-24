import pandas as pd
import numpy as np
import json
import csv
import networkx as nx

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def read_csv(file_path):
    return pd.read_csv(file_path)

def write_csv(data, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(data)

def get_courses_data(json_file_path, csv_file_path):
    json_data = read_json(json_file_path)
    courses = [course for sublist in json_data.values() for course in sublist]
    write_csv(courses, csv_file_path)

def load_student_courses(data_file_path):
    data = read_csv(data_file_path)
    student_courses = {}
    for _, row in data.iterrows():
        student_id = row['student_id']
        course_id = row['course_id']
        course_grade = row['course_grade']
        if student_id not in student_courses:
            student_courses[student_id] = []
        student_courses[student_id].append((course_id, course_grade))
    return student_courses

def predict_gpa(similarities, this_student, i=25):
    cgpa_data = read_csv('CGPA.csv').to_records(index=False)
    gpas = [cgpa_data[int(student_id[0])][1] for student_id in similarities[:i]]
    return sum(gpas) / len(gpas)

def calculate_similarity(courses1, courses2):
    courses1_set = set(courses1)
    courses2_set = set(courses2)
    jaccard_similarity = len(courses1_set & courses2_set) / len(courses1_set | courses2_set)
    weighted_jaccard_similarity = 0
    print(courses2)
    for course_id1, grade1 in list(courses1.values())[0]:
        for course_id2, grade2 in courses2:
            if course_id1 == course_id2 and grade1 == grade2:
                weighted_jaccard_similarity += grade1 * grade2
    return jaccard_similarity + weighted_jaccard_similarity

def recommend_courses(student_id, train_students, student_courses, cdcs, msc=""):
    similarities = []
    for other_student_id, other_student_courses in train_students.items():
          similarity = calculate_similarity(student_courses, other_student_courses)
          similarities.append((other_student_id, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    predicted_gpa_value = predict_gpa(similarities, student_courses[student_id])
    with open('public/output_2.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([predicted_gpa_value])
    
    recommended_courses = []
    for student_id, sim in similarities[:25]:
        recommended_courses.extend([course[0] for course in train_students[student_id]])
    
    filtered_courses = filter_courses(recommended_courses, cdcs, msc)
    return filtered_courses

def filter_courses(course_list, cdcs, msc=""):
    be_index = cdcs.index(be)
    final_courses = []
    for course, count in course_list:
        if msc != "":
            be_index = cdcs.index(msc)
        if course not in columns_as_lists[be_index] and course + "\n" not in columns_as_lists[be_index]:
            final_courses.append((course, count))
    return final_courses

def main():
    be = "B.E Electrical & Electronic"
    msc = ""
    selected_course = "CINEMATIC ADAPTATION"
    json_file_path = 'data.json'
    csv_file_path = 'g.csv'
    cdcs_file_path = "C:\\Users\\11110\\OneDrive\\Desktop\\CDCs.csv"

    get_courses_data(json_file_path, csv_file_path)
    test_data = read_csv(csv_file_path)
    test_data = test_data[['subject', 'courseGrade']]

    cdcs = ["B.E Chemical", "B.E Civil", "B.E Computer Science", "B.E Electrical & Electronic", "B.E Electronics & Communication", "B.E Electronics & Instrumentation", "B.E Mechanical", "B.Pharm", "M.Sc. Biological Sciences", "M.Sc. Chemistry", "M. Sc. Economics", "M.Sc. Mathematics", "M. Sc. Physics"]
    columns_as_lists = read_csv(cdcs_file_path).values.T.tolist()

    student_courses = load_student_courses('Grade.csv')
    student_courses[1112] = [(row['subject'], row['courseGrade']) for _, row in test_data.iterrows()]

    train_students = {student_id: courses for student_id, courses in student_courses.items() if student_id != 1112}
    test_students = {1112: student_courses[1112]}

    recommended_courses = recommend_courses(1112, train_students, test_students, cdcs, msc)
    write_csv(recommended_courses, 'public/output.csv')

    directed_graph = {}
    for index, row in pd.read_csv("Grade_Student.csv", encoding='latin-1').iterrows():
        if row['student_id'] in directed_graph:
            directed_graph[row['student_id']].append((row['subject'], row['courseGrade']))
        else:
            directed_graph[row['student_id']] = [(row['subject'], row['courseGrade'])]

    G = nx.DiGraph()
    for student in directed_graph.keys():
        G.add_node(student)
    for student, courses in directed_graph.items():
        for course, weight in courses:
            G.add_edge(course, student, weight=weight)

    pagerank_scores = nx.pagerank(G)
    student_input = [row['subject'] for _, row in test_data.iterrows()]
    available_courses = [course for course in pagerank_scores.keys() if course not in student_input]
    recommended_courses_pagerank = sorted(available_courses, key=lambda x: pagerank_scores[x], reverse=True)[:40]
    write_csv(recommended_courses_pagerank, 'public/output_3.csv')

    students = pd.read_csv("GradeDataWithBranch.csv")
    studs = {}
    for index, row in students.iterrows():
        if msc == "":
            if row['branch1'] == be and pd.isna(row['branch2']):
                studs.setdefault(row['student_id'], []).append(row['course_id'])
        else:
            if row['branch1'] == be and row['branch2'] == msc:
                studs.setdefault(row['student_id'], []).append(row['course_id'])

    all_courses = []
    for student in studs:
        if selected_course in studs[student]:
            all_courses.extend(studs[student])

    final = sorted([(x, all_courses.count(x)) for x in set(all_courses)], key=lambda x: x[1], reverse=True)
    final = filter_courses(final, cdcs, msc)
    write_csv(final, 'public/output-4.csv')

    print('Output Updated')

if __name__ == "__main__":
    main()
