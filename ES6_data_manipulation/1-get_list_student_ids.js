function getListStudentsids() {
    const students = getListStudents();
    return students.map((student) => student.id);
}

export default getListStudentsids;